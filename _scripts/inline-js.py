#!/usr/bin/env python3
"""
Post-render script: inline local JavaScript into HTML pages.

Corporate proxies/firewalls sometimes block .js file requests while
allowing .html and .css.  Inlining the JS directly into each HTML page
bypasses the block without needing Pandoc's embed-resources (which
warns about cross-linked HTML pages in a Quarto book).
"""

import os
import re
from pathlib import Path


# ---------------------------------------------------------------------------
# ES-module bundling helpers
# ---------------------------------------------------------------------------

def find_exports(js_content):
    """Return a list of names exported from an ES module source."""
    exports = []
    for m in re.finditer(
        r"export\s+(?:async\s+)?(?:function|const|let|var)\s+(\w+)",
        js_content,
    ):
        exports.append(m.group(1))
    return exports


def bundle_module(main_js_path):
    """Bundle an ES module *and* its local relative imports into one script."""
    content = main_js_path.read_text(encoding="utf-8")
    base_dir = main_js_path.parent

    bundled_parts = []

    # Match:  import * as X from './path.js'   or   import X from './path.js'
    import_re = re.compile(
        r"""import\s+(?:\*\s+as\s+(\w+)|(\w+))\s+from\s+['"](\.[^'"]+)['"];?"""
    )

    for m in import_re.finditer(content):
        namespace = m.group(1) or m.group(2)
        import_path = m.group(3)
        dep_path = (base_dir / import_path).resolve()
        if not dep_path.exists():
            continue

        dep_src = dep_path.read_text(encoding="utf-8")
        exports = find_exports(dep_src)

        # Strip 'export' keyword so the declarations become local
        dep_src = re.sub(r"export\s+(async\s+)?function\s+", r"\1function ", dep_src)
        dep_src = re.sub(r"export\s+(const|let|var)\s+", r"\1 ", dep_src)

        # Escape </script> inside JS to avoid breaking the HTML
        dep_src = dep_src.replace("</script>", "<\\/script>")

        if exports:
            return_obj = ", ".join(exports)
            bundled_parts.append(
                f"const {namespace} = (function() {{\n"
                f"{dep_src}\n"
                f"return {{ {return_obj} }};\n"
                f"}})();"
            )
        else:
            bundled_parts.append(dep_src)

    # Remove the original import lines from the main module
    content = import_re.sub("", content)

    # Escape </script>
    content = content.replace("</script>", "<\\/script>")

    return "\n".join(bundled_parts) + "\n" + content


# ---------------------------------------------------------------------------
# HTML processing
# ---------------------------------------------------------------------------

SCRIPT_TAG_RE = re.compile(
    r"<script\b([^>]*?)\bsrc=[\"']([^\"']+)[\"']([^>]*)>\s*</script>",
    re.IGNORECASE,
)


def inline_js_in_html(html_path):
    """Replace local <script src="…"> tags with inline <script> blocks."""
    text = html_path.read_text(encoding="utf-8")

    def _replace(match):
        pre_attrs = match.group(1)
        src = match.group(2)
        post_attrs = match.group(3)
        full_tag = match.group(0)

        # Skip external URLs
        if src.startswith(("http://", "https://", "//", "data:")):
            return full_tag

        # Resolve path relative to the HTML file
        js_path = (html_path.parent / src).resolve()
        if not js_path.exists():
            print(f"  [skip] {src} — file not found")
            return full_tag

        all_attrs = pre_attrs + post_attrs
        is_module = 'type="module"' in all_attrs or "type='module'" in all_attrs

        if is_module:
            js_body = bundle_module(js_path)
            return f"<script>\n{js_body}\n</script>"
        else:
            js_body = js_path.read_text(encoding="utf-8")
            js_body = js_body.replace("</script>", "<\\/script>")

            # Preserve a non-module type attribute if present
            type_m = re.search(r'type="([^"]*)"', all_attrs)
            type_attr = ""
            if type_m and type_m.group(1) != "module":
                type_attr = f' type="{type_m.group(1)}"'

            return f"<script{type_attr}>\n{js_body}\n</script>"

    new_text = SCRIPT_TAG_RE.sub(_replace, text)

    if new_text != text:
        html_path.write_text(new_text, encoding="utf-8")
        return True
    return False


# ---------------------------------------------------------------------------
# Entry point (called by Quarto as a post-render script)
# ---------------------------------------------------------------------------

def main():
    output_dir = Path(os.environ.get("QUARTO_PROJECT_OUTPUT_DIR", "docs"))
    html_files = sorted(output_dir.rglob("*.html"))

    if not html_files:
        print("inline-js: no HTML files found.")
        return

    print(f"inline-js: processing {len(html_files)} HTML file(s) …")
    count = 0
    for f in html_files:
        if inline_js_in_html(f):
            print(f"  + {f.relative_to(output_dir)}")
            count += 1

    print(f"inline-js: inlined JS in {count} file(s).")


if __name__ == "__main__":
    main()
