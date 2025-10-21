---
title: "panco2: Pressure Profile Fitting"
excerpt: "Fast, open-source Python library for measuring ICM pressure profiles from tSZ maps"
collection: research
permalink: /research/panco2/
date: 2023-01-01
themes: [gastrophysics, software]
header:
  teaser: picasso_header.png
---

**Associated publications:** [Kéruzoré, F. et al. (2023), OJAp, 6, 9.](https://ui.adsabs.harvard.edu/abs/2023OJAp....6E...9K/abstract), [Kéruzoré, F. et al. (2020), mm Universe @ NIKA2](https://ui.adsabs.harvard.edu/abs/2022EPJWC.25700024K/abstract)

The progression of NIKA2 observations on clusters within the LPSZ sample highlighted the necessity for standardized cluster sample analyses.
These analyses serve several purposes.
First, they enable initial estimates for the main LPSZ scientific products from a subset of clusters.
They are also needed to evaluate data quality and conduct systematic studies, examining the impact of analysis choices on final results.
However, the time constraints imposed by the NIKA2 SZ pipeline for analyzing individual cluster thermodynamic properties limited the possibility of running these analyses.
In response, I undertook a complete rewrite of the pipeline, accelerating it using optimized Python code and efficient numerical libraries.
This development significantly reduced computation time, from several days down to a few minutes, enabling both standardized analyses on cluster samples and systematic studies on the impact of tSZ signal modeling choices.
The new software, named `panco2`, underwent extensive validation tests using various numerical simulations.
These tests, based on idealized spherical clusters to realistic hydrodynamic simulations, ensured the software's reliability.
The results were published and detailed in an internal note to the NIKA2 collaboration, leading to `panco2` becoming the new SZ analysis pipeline of the NIKA2 collaboration.

`panco2` has been in use since 2021, contributing to several published works.
Recognizing its potential interest for the wider scientific community, I adapted the code to be easily usable on any millimeter-wave dataset, offering flexibility and compatibility with various studies.
To assess the code's accuracy, I implemented a validation procedure based on the analysis of simulated maps.
This involved synthetic cluster maps mimicking observations from instruments like *Planck*, SPT, and NIKA2.
The pressure profiles reconstructed with `panco2` consistently showed excellent agreement with the real profiles, validating the accuracy of the adjustments made.
This updated version of `panco2` is now a Python library, publicly available at [fkeruzore/panco2](https://github.com/fkeruzore/panco2), accompanied by a comprehensive [documentation](https://panco2.readthedocs.io/en/latest/).

**Github:** [fkeruzore/panco2](https://github.com/fkeruzore/panco2)
**Documentation:** [panco2.readthedocs.io](https://panco2.readthedocs.io)
