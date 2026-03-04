---
title: "picasso: Advanced Gas Model"
excerpt: "ML surrogate model (conditional neural network in JAX) replacing expensive physics simulations; deployed on multi-node, multi-GPU HPC systems"
collection: research
permalink: /research/picasso/
date: 2024-01-01
themes: [simulations, software, aiml]
header:
  teaser: picasso_header.png
---

**Github:** [fkeruzore/picasso](https://github.com/fkeruzore/picasso)
**Documentation:** [picasso-cosmo.readthedocs.io](https://picasso-cosmo.readthedocs.io)

`picasso` is a **ML-powered simulation surrogate** that generates realistic intracluster gas distributions for dark matter-only cosmological simulations, enabling synthetic observations of galaxy clusters at a fraction of the cost of full hydrodynamic runs.

## The Problem

Modern cosmological surveys like the South Pole Telescope (SPT) and the Simons Observatory (SO) observe thousands of galaxy clusters through the tSZ effect, where hot intracluster gas distorts the cosmic microwave background. To interpret these observations and extract cosmological constraints, we need theoretical predictions from simulations. However, hydrodynamical simulations that model gas physics are computationally expensive, limiting the volume and resolution we can achieve. Dark matter-only simulations are orders of magnitude faster, but lack the gas physics needed to predict tSZ observables - so there is a direct tradeoff between realism and scale.

## The Approach

`picasso` resolves this tradeoff by training a **conditional neural network** on paired data from gravity-only and hydrodynamic simulations, learning the mapping from dark matter halo properties to realistic 3D gas pressure and density fields.
Once trained, the model acts as a fast emulator: given a new gravity-only simulation (cheap to run), it predicts gas properties that a full hydrodynamic run (expensive) would have produced.

Key properties of the model:

- **Speed**: Generate tSZ maps from large simulation volumes orders of magnitude faster than full hydro simulations
- **Physical accuracy**: Reproduce baryonic physics - AGN feedback, gas cooling, stellar winds - learned from state-of-the-art hydrodynamic runs
- **Differentiable**: Implemented end-to-end in [JAX](https://github.com/google/jax), enabling gradient-based inference and sensitivity analysis
- **Scalable**: Deployed on multi-node, multi-GPU HPC systems at the [Argonne Leadership Computing Facility (ALCF)](https://www.alcf.anl.gov/)
- **Flexible**: Easily retrained on simulations with different feedback prescriptions, enabling systematic studies of astrophysical uncertainty

## Applications

`picasso` is being used to generate mock tSZ sky maps for SPT survey forecasts and calibration, study observational systematics at scales unreachable by hydrodynamic simulations, test cluster-finding algorithms and mass calibration methods, and explore degeneracies between cosmological and astrophysical parameters.

The software is actively developed and maintained as an open-source tool, with comprehensive documentation and example workflows.

