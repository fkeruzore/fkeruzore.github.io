---
title: "halox: Dark matter halos in JAX"
excerpt: "JAX-powered Python library for differentiable dark matter halo property and mass function calculations."
collection: research
permalink: /research/halox/
date: 2025-10-01
themes: [simulations, software, aiml]
header:
  teaser: picasso_header.png
---

In cosmology and astrophysics, modeling dark matter halos is central to understanding the large-scale structure of the Universe and its formation. This has motivated the development of many toolkits focused on halo modeling, such as, e.g., [halofit](https://github.com/robsmith155/halofit), [halotools](https://github.com/astropy/halotools), [colossus](https://bdiemer.bitbucket.io/colossus/), or [pyCCL](https://github.com/LSSTDESC/CCL). Recently, the AI-driven advent of novel computational frameworks such as [JAX](https://github.com/google/jax), have led to the development of differentiable and hardware-accelerated software to simulate and model physical processes. The increasing complexity of cosmological data and astrophysical models has motivated the wide adoption of this framework in cosmology, where JAX-powered software has been published to address a wide variety of scientific goals, including modeling fundamental cosmological quantities, with, e.g., [JAX-cosmo](https://github.com/DifferentiableUniverseInitiative/jax_cosmo);  or modeling various physical properties of dark matter halos, such as mass acretion history [Diffmah](https://github.com/ArgonneCPAC/diffmah), galaxy star formation history [Diffstar](https://github.com/ArgonneCPAC/diffstar), gas-halo connection [picasso](https://github.com/fkeruzore/picasso).

I developped the halox library, which offers a JAX implementation of some widely used properties that, while existing in other libraries focused on halo modeling, do not currently have a publicly available, differentiable and GPU-accelerated implementation, namely:

* Radial profiles of dark matter halos following a Navarro-Frenk-White (NFW) distribution;
* The halo mass function, quantifying the abundance of dark matter halos in mass and redshift, including its dependence on cosmological parameters;
* The halo bias.

The use of JAX as a backend allows these functions to be compiled and GPU-accelerated, enabling high-performance computations; and automatically differentiable, enabling their efficient use in gradient-based workflows, such as sensitivity analyses, Hamiltonian Monte-Carlo sampling for Bayesian inference, or machine learning-based methods.

All functions available in halox are validated against existing, non-JAX-based software. Cosmology calculations are validated against [Astropy](https://github.com/astropy/astropy) for varying cosmological parameters and redshifts. Other quantities are validated against [colossus](https://bdiemer.bitbucket.io/colossus/) for varying halo masses, redshifts, critical overdensities, and cosmological parameters. These tests are included in an automatic CI/CD pipeline on the GitHub repository, and presented graphically in the online documentation.
