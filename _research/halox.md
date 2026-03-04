---
title: "halox: Dark matter halos in JAX"
excerpt: "JAX-powered Python library for differentiable dark matter halo property and mass function calculations."
collection: research
permalink: /research/halox/
date: 2025-10-01
themes: [simulations, software, aiml]
header:
  teaser: halox_logo.png
---

The cosmology ecosystem has excellent tools for halo modeling ([colossus](https://bdiemer.bitbucket.io/colossus/), [pyCCL](https://github.com/LSSTDESC/CCL), [halotools](https://github.com/astropy/halotools)), but almost none of them are **differentiable** or **GPU-accelerated**.
This matters increasingly as the field moves toward gradient-based inference methods (Hamiltonian Monte Carlo, variational inference) and ML-integrated pipelines - workflows where you need to compute gradients through your physical model, and where GPU throughput is the main bottleneck.

`halox` fills this gap: it is a [JAX](https://github.com/google/jax)-native library implementing the core quantities needed for halo-based cosmology, making them JIT-compilable, GPU-accelerated, and fully differentiable out of the box:

- **NFW radial profiles** - density and enclosed mass for Navarro-Frenk-White dark matter halos
- **Halo mass function** - the abundance of halos as a function of mass, redshift, and cosmological parameters
- **Halo bias** - the clustering bias between halos and the underlying dark matter field

Because `halox` functions are written in JAX, they compose naturally with the rest of the JAX ecosystem: they can be vmapped over batches of halos or cosmologies, JIT-compiled for GPU, and differentiated with `jax.grad` - making them drop-in components for HMC samplers, ML training loops, or sensitivity analyses.

All implementations are validated against established reference libraries ([Astropy](https://github.com/astropy/astropy), [colossus](https://bdiemer.bitbucket.io/colossus/)) across wide ranges of halo masses, redshifts, and cosmological parameters. These tests run automatically on every commit via a CI/CD pipeline, with results visualized in the online documentation.

**Github:** [fkeruzore/halox](https://github.com/fkeruzore/halox)
**Documentation:** [halox.readthedocs.io](https://halox.readthedocs.io)
