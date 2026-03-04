---
title: "panco2: Pressure Profile Fitting"
excerpt: "~1000× speedup of a Bayesian inference pipeline through algorithm redesign; adopted as the NIKA2 collaboration's standard analysis tool"
collection: research
permalink: /research/panco2/
date: 2023-01-01
themes: [gastrophysics, software]
header:
  teaser: banner_panco2.png
---

**Associated publications:** [Kéruzoré, F. et al. (2023), OJAp, 6, 9.](https://ui.adsabs.harvard.edu/abs/2023OJAp....6E...9K/abstract), [Kéruzoré, F. et al. (2020), mm Universe @ NIKA2](https://ui.adsabs.harvard.edu/abs/2022EPJWC.25700024K/abstract)

The NIKA2 collaboration's original pipeline for measuring gas pressure profiles from telescope maps took **several days of compute time per cluster** - fine for a handful of targets, but completely impractical for systematic studies or large samples.
I identified the bottlenecks, redesigned the core algorithms, and rewrote the pipeline from scratch in optimized Python, reducing runtime to **a few minutes** - a speedup of roughly **three orders of magnitude**.

The new tool, `panco2`, uses a forward-modeling approach: it generates a synthetic observation by convolving a parametric pressure profile model with the instrument's beam and noise properties, then compares this to the real data via MCMC.
This design makes it straightforward to handle instrumental artifacts, account for filtering effects, and propagate all uncertainties correctly through to the final profile estimate.

Beyond raw speed, I invested heavily in software quality: `panco2` was validated against a hierarchy of increasingly realistic simulations (idealized spherical clusters → realistic hydrodynamic simulations), adopted as the official SZ analysis pipeline of the NIKA2 collaboration, and generalized to work with data from any millimeter-wave instrument (*Planck*, SPT, NIKA2, and others).

**Github:** [fkeruzore/panco2](https://github.com/fkeruzore/panco2)
**Documentation:** [panco2.readthedocs.io](https://panco2.readthedocs.io)
