---
title: "Baryon painting"
excerpt: "Emulating intracluster gas in gravity-only simulations"
collection: research
---

I am leading a program dedicated to the creation of tSZ sky maps from $$N-$$body simulations.
Cosmological simulations can be broadly separated into two categories.
On one hand, hydrodynamic simulations jointly model many different components of the Universe, including stellar matter, gas, and dark matter.
On the other hand, gravity-only simulations only consider the gravitational interaction between particles, effectively simulating dark matter-only universes.
The obvious advantage of hydrodynamic simulations is that they can make predictions for observables tied to baryonic physics (such as the tSZ effect).
Their main downside is that they represent tremendous computational challenges: they are vastly more expensive to run than gravity-only simulations and require extremely accurate empirical models to include sub-resolution physical processes.
As a result, gravity-only simulations are useful datasets, that can be post-processed to include baryonic observables at a fraction of the cost of hydrodynamic simulations.

I am working on post-processing models to paint cluster gas properties on dark matter-only halos, with the ultimate goal of creating maps of the tSZ effect from gravity-only simulations.
This will enable the generation of tSZ effect sky maps mimicking current (SPT, ACT, or *Planck*) and future (Simons Observatory, CMB-S4) millimeter surveys, in order to validate cosmological analyses and to study the different systematics that can affect them.
The group I joined at Argonne National Laboratory has developed the HACC software[^1], and uses it to generate some of the state-of-the-art gravity-only and hydrodynamic simulations in the field.
These are already widely used for studies at visible and infrared wavelengths, for example in preparation for the LSST survey.
This work will thus enable multi-wavelength analyses of cluster catalogs, and the characterization of systematics in cosmological analyses of cluster surveys.

# Optimization and quality assessment of a painting algorithm

**Associated publication:** [Kéruzoré, F. et al. (2022),OJAp 6, 43.](https://ui.adsabs.harvard.edu/abs/2023OJAp....6E..43K/abstract)

As the first part of this work, I implemented a widely adopted baryon model to paint baryon properties on HACC gravity-only simulations.
I used the Borg Cube, a pair of two cosmological simulations evolved from the same initial conditions; one as a gravity-only simulation, and one including hydrodynamics[^2].
This combination allowed me not only to implement the baryon model, but also to assess its ability to make accurate and precise predictions of ICM thermodynamics, by comparing these predictions to the actual gas properties for the same halos in the hydrodynamic simulation.
As a result, I was able to optimize the model by finding the parameters providing the best agreement between gas properties as predicted from the gravity-only simulation and as observed in the hydrodynamic version.
The procedure required reading large volumes of data and was run using supercomputers at the Argonne Leadership Computing Facility (ALCF).
The resulting predictions of gas density and pressure are accurate to the few-percent level for a redshift range $$z \in [0, 2]$$.
In addition, I also compared the mass-tSZ observable scaling relation reconstructed from the two simulations and showed that the relation reconstructed for the gravity-only simulation was compatible with that observed in the hydrodynamic simulation, with only a few percent additional scatter.
This highlights the power of baryon painting methods as a viable, cheaper surrogate to hydrodynamic simulations to create synthetic datasets to calibrate cluster cosmology using the tSZ effect.

# The `picasso` gas model

Cool stuff incoming!

[^1]: Habib, S. et al. (2016), New Astronomy, 42, 49; Frontiere, N. et al. (2022), ApJS 264(2), 34
[^2]: Emberson, J. D. et al. (2019), ApJ, 877, 85
