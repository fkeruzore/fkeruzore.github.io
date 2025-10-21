---
layout: research-theme
title: "Simulations"
permalink: /research/simulations/
author_profile: true
theme_id: simulations
---

Cosmological simulations are powerful tools for understanding cluster formation and evolution, and for generating synthetic datasets to validate observational analyses.
I am working on baryon painting methods to efficiently emulate intracluster gas properties in gravity-only simulations.

Cosmological simulations can be broadly separated into two categories.
On one hand, hydrodynamic simulations jointly model many different components of the Universe, including stellar matter, gas, and dark matter.
On the other hand, gravity-only simulations only consider the gravitational interaction between particles, effectively simulating dark matter-only universes.
The obvious advantage of hydrodynamic simulations is that they can make predictions for observables tied to baryonic physics (such as the tSZ effect).
Their main downside is that they represent tremendous computational challenges: they are vastly more expensive to run than gravity-only simulations and require extremely accurate empirical models to include sub-resolution physical processes.

As a result, gravity-only simulations are useful datasets that can be post-processed to include baryonic observables at a fraction of the cost of hydrodynamic simulations.
This enables the generation of tSZ effect sky maps mimicking current (SPT, ACT, or *Planck*) and future (Simons Observatory, CMB-S4) millimeter surveys, in order to validate cosmological analyses and to study the different systematics that can affect them.
