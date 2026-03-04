---
layout: research-theme
title: "Intracluster Gas Physics"
permalink: /research/gastrophysics/
author_profile: true
theme_id: gastrophysics
---

Translating telescope observations into cosmological constraints requires solving a chain of non-trivial inference problems.
Each galaxy cluster is an extended source with a complex 3D gas distribution; we observe it projected on the sky, mixed with noise, filtered by the instrument response, and potentially contaminated by other astrophysical signals.
Extracting reliable measurements from this data - and propagating all sources of uncertainty through to final constraints - demands careful **forward modeling**, **Bayesian parameter estimation**, and a thorough understanding of systematic effects.

My PhD work was part of the [NIKA2 SZ Large Program (LPSZ)](http://lpsc.in2p3.fr/nika2lpsz/), a survey of ~40 galaxy clusters with the NIKA2 camera, a state-of-the-art millimeter-wave instrument at the IRAM 30m telescope.
I led the end-to-end analysis of individual clusters: from raw time-ordered detector data to calibrated sky maps, and from maps to inferred thermodynamic profiles using MCMC.
I also developed a **hierarchical Bayesian framework** used to combine individual cluster measurements into population-level scaling relations, with full propagation of measurement uncertainties, selection effects, and mass estimation biases.

*Technical methods: MCMC (Metropolis-Hastings and gradient-free samplers), forward modeling with instrument transfer functions, joint multi-wavelength modeling (millimeter + X-ray), hierarchical Bayesian regression, Monte Carlo forecasting.*
