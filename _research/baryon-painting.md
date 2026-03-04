---
title: "Baryon Painting Optimization"
excerpt: "Benchmarking a physics-based simulation surrogate at scale on HPC systems, achieving few-percent accuracy as a replacement for expensive hydrodynamic runs"
collection: research
permalink: /research/baryon-painting/
date: 2022-01-01
themes: [simulations]
header:
  teaser: banner_bpbc.png
---

**Associated publication:** [Kéruzoré, F. et al. (2022), OJAp 6, 43.](https://ui.adsabs.harvard.edu/abs/2023OJAp....6E..43K/abstract)

This project established the foundation for the ML-based surrogate approach later extended in [picasso](/research/picasso/), starting from a classical, parametric baryon model and rigorously benchmarking it as a surrogate for expensive hydrodynamic simulations.

The key experimental setup was the **Borg Cube**: a matched pair of cosmological simulations run from identical initial conditions - one gravity-only (fast, cheap), one full hydrodynamics (slow, expensive, physically complete).
This paired dataset provides a ground-truth benchmark for evaluating any surrogate model: by applying the model to the gravity-only run and comparing its predictions to the hydrodynamic run *for the same halos*, we can measure the surrogate's accuracy without any confounding factors.

I implemented the baryon model on HACC gravity-only outputs and optimized its parameters against the hydrodynamic ground truth using large-scale data processed on HPC systems at the [Argonne Leadership Computing Facility (ALCF)](https://www.alcf.anl.gov/).
The resulting surrogate achieves **few-percent accuracy** on gas density and pressure predictions across a redshift range $$z \in [0, 2]$$, and reproduces the mass-tSZ scaling relation with only a small additional scatter relative to the full hydrodynamic simulation.

This validates the surrogate paradigm: gravity-only simulations, augmented with a learned or calibrated baryon model, can substitute for far more expensive hydrodynamic runs in contexts where large simulation volumes and high throughput matter more than per-object precision.

[^1]: Emberson, J. D. et al. (2019), ApJ, 877, 85
