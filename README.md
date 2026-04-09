# Geoscientific Machine Learning

This repository contains the source for the Quarto book **Geoscientific Machine Learning** by Pankaj K Mishra.

The book is written as a practical introduction to neural networks, scientific machine learning, and geoscience applications, with Julia code throughout. The public website is published at <https://geo-sciml.com>, and this repository is the source used to render the HTML site, PDF book, frozen execution outputs, and extracted chapter scripts.

## Repository structure

- `chapters/` contains the source manuscript in Quarto Markdown (`.qmd`).
- `scripts/` contains Julia scripts extracted from the chapter code blocks.
- `_freeze/` stores cached execution outputs used for stable renders.
- `docs/` contains the rendered HTML site.
- `_scripts/inline-js.py` runs after rendering to inline module scripts for broader browser compatibility.

## Build the book

The book uses Quarto with the Julia engine.

```bash
quarto render
```

This renders the website into `docs/` and regenerates the PDF output.

## Local development workflow

Work from the repository root:

```bash
cd geo-sciml
```

If you are setting up the project on a new machine, instantiate the Julia environment once before rendering:

```bash
julia --project=. -e 'using Pkg; Pkg.instantiate()'
```

For a normal local build:

```bash
quarto render
```

To preview the book locally with live rebuilds:

```bash
quarto preview
```

If old chapter names, stale pages, or outdated outputs remain in the site, do a clean rebuild by removing all generated and cached output first:

```bash
rm -rf docs .quarto _freeze
quarto render
```

On PowerShell, the equivalent command is:

```powershell
Remove-Item -Recurse -Force docs, .quarto, _freeze
quarto render
```

If you also want fresh exported Julia scripts after cleaning the render output, run:

```bash
julia scripts/00-extract_chapter_code.jl
```

## Regenerate extracted chapter scripts

```bash
julia scripts/00-extract_chapter_code.jl
```

This exports the Julia code blocks from the manuscript into standalone `.jl` files that mirror the chapter structure.

## Chapter and script workflow

The source of truth is always the Quarto manuscript in `chapters/`.

- Write prose and Julia code blocks in `chapters/*.qmd`.
- Render the book from those chapter files.
- Export standalone Julia scripts afterward with `julia scripts/00-extract_chapter_code.jl`.

The files in `scripts/` are generated artifacts. They should not be edited by hand unless you intentionally want to break the chapter-to-script sync.

A typical authoring loop is:

```bash
quarto render
julia scripts/00-extract_chapter_code.jl
```

If you want a fully clean rebuild of both the site and the exported scripts:

```bash
rm -rf docs .quarto _freeze
quarto render
julia scripts/00-extract_chapter_code.jl
```

## Reproducibility

The Julia environment is pinned through `Project.toml` and `Manifest.toml`. For stable renders, the project also uses Quarto freeze artifacts in `_freeze/` so figures, tables, and code outputs can be reproduced consistently.

## Citation

Until a frozen archival snapshot is assigned an identifier, cite the web edition:

```bibtex
@book{mishra2026geosciml,
	title={Geoscientific Machine Learning},
	author={Pankaj K Mishra},
	url={https://geo-sciml.com},
	year={2026}
}
```