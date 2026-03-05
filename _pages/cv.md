---
layout: archive
title: "CV"
permalink: /cv/
author_profile: true
redirect_from:
  - /resume
---

{% include base_path %}

*Machine learning engineer with a PhD in physics, specializing in GPU-accelerated scientific ML, HPC, and distributed training. Experienced in profiling and optimizing multi-GPU and multi-node ML workloads, developing physics-informed surrogates for large-scale simulations, and validating performance on modern NVIDIA architectures using JAX and PyTorch.*

# Technical Skills

**Machine Learning:** Deep learning (JAX/Flax, PyTorch); CNNs, VAEs, fully-connected networks; Physics-informed neural networks; Differentiable programming; Generative models; Bayesian inference, MCMC, gradient-based optimization

**Programming:** Python (expert): NumPy, SciPy, Pandas, JAX ecosystem; Shell scripting; R; IDL

**Infrastructure:** GPU/HPC: MPI, OpenMP, SLURM, PBS; CI/CD (GitHub Actions); Testing (pytest); Documentation (Sphinx, ReadTheDocs); PyPI packaging (uv, Poetry)

# Open-Source Software

**[picasso](https://github.com/fkeruzore/picasso)** - Neural network for 3D field generation (JAX, Flax) - 2024

* Designed conditional neural network predicting gas pressure fields from dark matter halo properties
* Achieves **10,000× speedup** over traditional simulation methods while preserving physical accuracy
* GPU-accelerated and fully differentiable for integration into gradient-based inference pipelines
* Peer-reviewed publication; adopted by South Pole Telescope collaboration
* Documentation: [picasso-cosmo.readthedocs.io](https://picasso-cosmo.readthedocs.io)

**[halox](https://github.com/fkeruzore/halox)** - Differentiable scientific computing library (JAX) - 2025

* GPU-accelerated, auto-differentiable physics calculations for gradient-based workflows
* Validated against standard benchmarks; 100% test coverage; automated CI/CD; distributed via PyPI
* Publication: [Kéruzoré, Submitted to JOSS](https://ui.adsabs.harvard.edu/abs/2025arXiv250922478K/abstract)
* Documentation: [halox.readthedocs.io](https://halox.readthedocs.io)

**[panco2](https://github.com/fkeruzore/panco2)** - Bayesian inference pipeline (Python) - 2022

* Forward-modeling MCMC pipeline for signal extraction from noisy and filtered image data; **~1000× speedup** over prior tool
* Adopted as the official pipeline of the NIKA2 collaboration; peer-reviewed publication
* Documentation: [panco2.readthedocs.io](https://panco2.readthedocs.io)

**[GalGenAI](https://github.com/fkeruzore/GalGenAI)** - Experimental generative models for image synthesis (PyTorch) - In development

* Deep generative models (VAE + flow-matching) for conditional astronomical image generation

# Experience

## 2021 – Present: Post-doctoral Research Associate

* Argonne National Laboratory, Cosmological Physics and Advanced Computing group
* Developed neural networks generating synthetic 3D datasets from TB-scale simulations, enabling physics-informed predictions **four orders of magnitude faster** than traditional methods
* Built and shipped 3 open-source ML libraries with documentation, CI/CD, and PyPI distribution
* Leveraged DOE leadership-class supercomputers (ALCF) for large-scale, multi-node, multi-GPU inference
* Led analysis coordination for multi-institution collaboration (100+ researchers)
* Designed validation benchmarks and stress tests to evaluate generative model fidelity
* Mentored 3 junior researchers on ML projects (3–6 month appointments)
* Communicated complex ML architectures and results to diverse technical audiences at international conferences and research institutes

## 2018 – 2021: Graduate Research Associate

* Université Grenoble Alpes, Laboratoire de Physique Subatomique et Cosmologie
* Developed end-to-end data pipelines extracting weak signals from noisy observational data
* Built Monte Carlo simulation frameworks for statistical uncertainty quantification & sensitivity analysis
* Designed and deployed collaboration-wide database serving 50+ researchers
* Teaching assistant: 96 hours of instruction in physics courses

# Education

* **Ph.D. in Astrophysics**, Université Grenoble Alpes, 2021
* **M.S. in Physics**, Université de Montpellier, 2018 · *First in class*
  * Research project: Deep learning for cosmological parameter estimation from supernova data
* **B.S. in Physics & Chemistry**, Université de Bordeaux, 2016

# Professional Development

* *Intro to AI-driven Science on Supercomputers* - Argonne Leadership Computing Facility (2024)
* *Statistical Challenges in Modern Astronomy* - Penn State University (2021)

# Research Output

* <strong>{{ site.data.pub_stats.publications }}</strong> publications (8 as first-author) · <strong>{{ site.data.pub_stats.citecount }}</strong> citations · h-index: <strong>{{ site.data.pub_stats.hindex }}</strong> (*Source*: [NASA ADS](https://ui.adsabs.harvard.edu/search/filter_doctype_facet_hier_fq_doctype=AND&filter_doctype_facet_hier_fq_doctype=doctype_facet_hier%3A%220%2FArticle%22&fq=%7B!type%3Daqp%20v%3D%24fq_doctype%7D&fq_doctype=(doctype_facet_hier%3A%220%2FArticle%22)&q=%20author%3A%22keruzore%2C%20florian%22&sort=date%20desc%2C%20bibcode%20desc&p_=0)) - For the complete list, see the [Publications](https://fkeruzore.github.io/publications/) page.
* 20+ public talks - For the complete list, see the [Talks](https://fkeruzore.github.io/talks/) page.


# Leadership & Communication

* **Junior Coordinator**, Galaxy Cluster Analysis - South Pole Telescope Collaboration (2024–present)
* **Pipeline & Database Lead** - NIKA2 Collaboration (2019–2021)
* Science outreach: Argonne "Science 101" public lecture series participant
* 20+ public talks - For the complete list, see the [Talks](https://fkeruzore.github.io/talks/) page.