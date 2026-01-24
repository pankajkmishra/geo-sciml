# Geoscientific Machine Learning

This is a book for doing geoscience with scientific machine learning with examples in Julia.
You can read the book online or download the PDF version. If you want to render this book locally, here is how you do this: 



## Prerequisites

- [Julia](https://julialang.org/downloads/) (v1.12+)
- [Quarto](https://quarto.org/docs/get-started/) CLI
- [Conda](https://docs.conda.io/en/latest/miniconda.html) (optional, for environment management)

## Clone the Repository

```bash
git clone https://github.com/pankajkmishra/geo-sciml.git
cd geo-sciml
```

## Setup Julia Environment

```bash
julia -e 'using Pkg; Pkg.activate("."); Pkg.instantiate(); Pkg.precompile()'
```

This installs all Julia dependencies listed in `Project.toml`.

## Render Locally

### Preview (with live reload)

```bash
quarto preview
```

Opens in browser at `http://localhost:4916/` (port may vary).

### Render HTML

```bash
quarto render
```

Output is generated in `docs/` folder.

## Deploy to GitHub Pages

This book is deployed locally (no GitHub Actions). After rendering:

```bash
quarto render
git add .
git commit -m "Build book"
git push
```

GitHub Pages is configured to serve from the `docs/` folder on the `main` branch.

## Generate PDF

```bash
quarto render --to pdf
```

The PDF will be available at `_site/geo-sciml.pdf`.

### PDF Requirements

For PDF generation, you need LaTeX. Install TinyTeX via Quarto:

```bash
quarto install tinytex
```

## Project Structure

```
geo-sciml/
├── _quarto.yml          # Book configuration
├── index.md             # Home page
├── styles.css           # Custom styling
├── Project.toml         # Julia dependencies
├── chapters/
│   ├── 01-getting-started-julia.qmd
│   └── 02-placeholder.qmd
└── _site/               # Generated output (gitignored)
```

## GitHub Pages Deployment

The book auto-deploys via GitHub Actions on push to `main`. 

To enable:
1. Go to **Settings → Pages**
2. Set **Source** to **GitHub Actions**

Live site: https://pankajkmishra.github.io/geo-sciml/

PDF: https://pankajkmishra.github.io/geo-sciml/geo-sciml.pdf

## Proxy Configuration (if needed)

If behind a corporate proxy:

```powershell
$env:HTTP_PROXY = "http://your-proxy:8080"
$env:HTTPS_PROXY = "http://your-proxy:8080"
```

For Julia packages, set these before running `Pkg.add()`.

## License

MIT 
