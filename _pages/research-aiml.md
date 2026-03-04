---
layout: research-theme
title: "AI/ML"
permalink: /research/aiml/
author_profile: true
theme_id: aiml
---

A recurring bottleneck in cosmology is the cost of forward models: running a full physics simulation to produce a single prediction can take thousands of CPU-hours, making likelihood-based inference or large parameter sweeps prohibitively expensive.
Machine learning offers an alternative - not by replacing the physics, but by learning fast, accurate surrogates that can be queried millions of times where the original simulator cannot.

My ML work focuses on building and deploying these surrogates for cosmological observables, with an emphasis on **physical realism**, **uncertainty quantification**, and **computational scalability**.
I implement models in [JAX](https://github.com/google/jax) and deploy them on multi-node, multi-GPU clusters at the [Argonne Leadership Computing Facility (ALCF)](https://www.alcf.anl.gov/), taking advantage of JAX's native support for hardware acceleration and distributed computation.
The resulting models are automatically differentiable end-to-end, which makes them natural building blocks for gradient-based Bayesian inference (e.g., Hamiltonian Monte Carlo) and for integration into larger differentiable pipelines.

These projects center on emulating the thermal Sunyaev-Zeldovich (tSZ) signal of galaxy clusters from dark matter-only simulations, enabling the generation of realistic synthetic sky maps and the study of observational systematics at scales that full hydrodynamic simulations cannot reach.
