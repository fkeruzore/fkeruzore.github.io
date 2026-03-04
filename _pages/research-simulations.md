---
layout: research-theme
title: "Simulations"
permalink: /research/simulations/
author_profile: true
theme_id: simulations
---

A central challenge in data-driven science is that the most accurate forward models are often too expensive to run at the scale required for statistical inference.
In cosmology, this tension is acute: the most realistic simulations of the Universe (full hydrodynamic runs modeling dark matter, gas, stars, and feedback) cost millions of CPU-hours each, yet constraining cosmological parameters requires exploring a large model space.

My work on simulations addresses this through **surrogate modeling** - training fast, data-driven models on expensive simulations and using them in place of the full simulator downstream.
I work on *baryon painting*: methods that take cheap "dark matter-only" simulations as input and predict the gas properties that a full hydrodynamic run would have produced, at a tiny fraction of the cost.
These surrogate outputs can then be used to generate realistic synthetic observations, enabling large-scale validation studies and systematic analyses that would be impossible with the original simulations.

The observables I target are the thermal Sunyaev-Zeldovich (tSZ) effect and X-ray emission of galaxy clusters, which I use to produce synthetic sky maps for current surveys (SPT, ACT, *Planck*) and next-generation experiments (Simons Observatory, CMB-S4).
