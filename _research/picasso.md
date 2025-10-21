---
title: "picasso: Advanced Gas Model"
excerpt: "Next-generation baryon painting model for creating tSZ sky maps from cosmological simulations"
collection: research
permalink: /research/picasso/
date: 2024-01-01
themes: [simulations, software]
tags: [simulations, baryon painting, HACC, tSZ, software]
header:
  teaser: picasso_header.png
---

I am leading a program dedicated to the creation of tSZ sky maps from $$N$$-body simulations.
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

## The `picasso` gas model

![picasso banner](/images/picasso_header.png "picasso")

Cool stuff incoming!

[^1]: Habib, S. et al. (2016), New Astronomy, 42, 49; Frontiere, N. et al. (2022), ApJS 264(2), 34
