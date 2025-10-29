---
title: "picasso: Advanced Gas Model"
excerpt: "Next-generation baryon painting model for creating tSZ sky maps from cosmological simulations"
collection: research
permalink: /research/picasso/
date: 2024-01-01
themes: [simulations, software, aiml]
header:
  teaser: picasso_header.png
---

**Github:** [fkeruzore/picasso](https://github.com/fkeruzore/picasso)
**Documentation:** [picasso-cosmo.readthedocs.io](https://picasso-cosmo.readthedocs.io)

`picasso` is a machine learning-powered baryon painting model that efficiently generates realistic intracluster gas distributions on dark matter-only cosmological simulations. This tool addresses one of the key computational challenges in modern cosmology: predicting the thermal Sunyaev-Zeldovich (tSZ) effect observable in large-scale structure simulations without the prohibitive cost of full hydrodynamical simulations.

## The Problem

Modern cosmological surveys like the South Pole Telescope (SPT) and the Simons Observatory (SO) observe thousands of galaxy clusters through the tSZ effect, where hot intracluster gas distorts the cosmic microwave background. To interpret these observations and extract cosmological constraints, we need theoretical predictions from simulations. However, hydrodynamical simulations that model gas physics are computationally expensive, limiting the volume and resolution we can achieve. Dark matter-only simulations are much faster but lack the gas physics needed to predict tSZ observables.

## The Solution

`picasso` uses machine learning to "paint" realistic gas distributions onto dark matter halos from gravity-only simulations. The model is trained on hydrodynamical simulations to learn the complex relationships between dark matter structure and gas properties. Once trained, it can rapidly generate gas distributions on large volumes of dark matter-only simulations, providing the speed of gravity-only runs with the physical richness of hydro simulations.

The key innovation is using a conditional neural network architecture that takes dark matter halo properties as input and outputs realistic 3D pressure and density fields for the intracluster medium. This allows for:

- **Computational efficiency**: Generate tSZ maps from large simulation volumes orders of magnitude faster than running full hydro simulations
- **Physical realism**: Capture complex baryonic physics including feedback, cooling, and gas dynamics learned from state-of-the-art hydro simulations
- **Flexibility**: Easily explore different astrophysical scenarios by training on simulations with varying feedback prescriptions
- **Integration**: Seamlessly interface with existing simulation and analysis pipelines through standard data formats

## Applications

`picasso` is being used to:

- Generate mock tSZ sky maps for SPT survey forecasts and calibration
- Study systematic effects in cluster cosmology from survey selection and measurement biases
- Explore degeneracies between cosmological parameters and astrophysical uncertainties
- Test cluster-finding algorithms and mass calibration methods on realistic simulated data

The software is actively developed and maintained as an open-source tool for the cosmology community, with comprehensive documentation and example workflows.

## Technical Details

The model is implemented in JAX for GPU acceleration and automatic differentiation, making it both fast and easy to integrate into gradient-based inference frameworks.

