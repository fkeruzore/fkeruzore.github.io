---
title: "Baryon Painting Optimization"
excerpt: "Optimizing and validating baryon models to paint ICM properties on gravity-only simulations"
collection: research
permalink: /research/baryon-painting/
date: 2022-01-01
themes: [simulations]
tags: [simulations, baryon painting, HACC, tSZ]
header:
  teaser: picasso_header.png
---

**Associated publication:** [Kéruzoré, F. et al. (2022), OJAp 6, 43.](https://ui.adsabs.harvard.edu/abs/2023OJAp....6E..43K/abstract)

As the first part of this work, I implemented a widely adopted baryon model to paint baryon properties on HACC gravity-only simulations.
I used the Borg Cube, a pair of two cosmological simulations evolved from the same initial conditions; one as a gravity-only simulation, and one including hydrodynamics[^1].
This combination allowed me not only to implement the baryon model, but also to assess its ability to make accurate and precise predictions of ICM thermodynamics, by comparing these predictions to the actual gas properties for the same halos in the hydrodynamic simulation.
As a result, I was able to optimize the model by finding the parameters providing the best agreement between gas properties as predicted from the gravity-only simulation and as observed in the hydrodynamic version.
The procedure required reading large volumes of data and was run using supercomputers at the Argonne Leadership Computing Facility (ALCF).
The resulting predictions of gas density and pressure are accurate to the few-percent level for a redshift range $$z \in [0, 2]$$.
In addition, I also compared the mass-tSZ observable scaling relation reconstructed from the two simulations and showed that the relation reconstructed for the gravity-only simulation was compatible with that observed in the hydrodynamic simulation, with only a few percent additional scatter.
This highlights the power of baryon painting methods as a viable, cheaper surrogate to hydrodynamic simulations to create synthetic datasets to calibrate cluster cosmology using the tSZ effect.

[^1]: Emberson, J. D. et al. (2019), ApJ, 877, 85
