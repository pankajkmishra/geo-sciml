---
number-sections: false
title-block-banner: false
---

# Preface {.unnumbered}

<style>
h1.title,
#title-block-header,
#preface > h1 {
  display: none !important; 
} 
</style>


Welcome to **Geoscientific Machine Learning**!

This book is for geoscience students, researchers, and practitioners who want to get started with scientific machine learning (SciML), where machine learning models are trained using domain knowledge about the problem, most often the physics and numerical structure behind it. It is also for machine learning practitioners who are building new methods and want to apply them to geoscientific problems, a domain with some of the most diverse and challenging datasets in science.

This is a living book hosted at [www.geo-sciml.com](https://www.geo-sciml.com). The website contains the book source code, and whenever the text or code changes, a new version of the site is rendered and published. Code outputs such as figures, tables, and results are updated as well, and the downloadable PDF is regenerated so it matches the latest version. The full website source can also be downloaded and run locally, for example in VS Code.

Machine learning and AI are evolving rapidly, and it is difficult to estimate how geoscience research and applications will change over the coming years. For that reason, this book is written as a live project rather than a conventional one-time publication. The content will evolve over time, tracking current research questions while keeping a forward-looking view. At the same time, stable and citable checkpoints matter, so PDF snapshots of the book will be published on arXiv, with a permanent archive of the corresponding source code for each snapshot on Zenodo.

The programming language used throughout is Julia [@bezanson2017julia]. The first part of the book introduces the computational setup and teaches enough Julia to reproduce the results and continue learning with confidence. No prior programming experience is required. The book then covers the core ideas of machine learning and deep learning that underpin modern models, before moving into Scientific machine learning methods and geoscience-focused applications. The emphasis is on methods designed for systems governed by differential equations and physical structure, including physics-informed approaches and operator learning. The goal is to connect data-driven models with scientific reasoning in a way that is practical for real geoscientific problems.

If you find this book useful, please consider citing the current web edition as:


Mishra, P. K. (2026). *Geoscientific Machine Learning* [Online book]. https://geo-sciml.com


```bibtex
@book{mishra2026geosciml,
  title={Geoscientific Machine Learning},
  author={Pankaj K Mishra},
  url={https://geo-sciml.com},
  year={2026},
  note={Web edition}
}
```