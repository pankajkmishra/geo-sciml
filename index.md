---
title: "Geoscientific Machine Learning"
number-sections: false
title-block-banner: false
---

<style>
.title {
  display: none !important;
}
.quarto-title-meta,
.quarto-title-authors,
.quarto-title-author {
  display: none !important;
}
</style>



Welcome to **Geoscientific Machine Learning**.

::: {.callout-note}
## Free living book
This book is free to read. Between stable releases, chapters and code may change as the book evolves.
:::

If you’re reading this, you probably already have some familiarity with geoscience. You’re used to thinking in terms of physical processes, models, scales, and uncertainty. When it comes to computation, though, you may have mostly worked through existing tools: running models, adjusting parameters, or modifying scripts written by someone else. That’s a common place to be, and it works, until you want to change the model itself or test an idea that doesn’t fit into the existing workflow.

You might also be here because you keep hearing about AI and machine learning and you’re not sure what to make of it. Is it actually useful for your research, or is it just hype? Will it help you work faster, or will it send you down a rabbit hole? Can it help you do things you thought were out of reach before, or is it mostly a waste of time?

Before you decide, it’s worth trying it in a way that respects how geoscience works. That’s what this book is about.

By **scientific machine learning**, we mean instead of training a model only on data and hoping it behaves, you guide the learning with what you already know: physical laws, conservation principles, symmetries, and numerical structure. The goal is not just to fit observations, but to produce models that behave sensibly when you change conditions or run them for longer times. By **geoscientific machine learning**, we mean applying scientific machine learning to geoscience problems. That means combining geoscience domain knowledge with learning methods so the models respect physics, scale relationships, and observational constraints. 

If you don’t yet have a favorite programming language, or you’re still deciding what’s worth learning, here’s the important part: the exact language matters less than having *one*. You need a way to talk to computers clearly, so they can help you turn ideas into experiments and hypotheses into something you can test. 


In this book we’ll choose **Julia**. If you spend time with it, you’ll see why—especially once you start doing more demanding computation. We’ll begin slowly and keep things practical, using Julia to express ideas you already know. Machine learning comes later where it connects naturally geoscience practices.

If you’re new to programming, expect some friction at first (we'll try to minimise that). That’s normal. The payoff is that you gain more control over your models and more confidence in the results they produce.



::: {.callout-note}
## This book is under construction
Some sections are incomplete. If there’s something you’d like to see included, open an issue and let me know what you’re working on.
:::

