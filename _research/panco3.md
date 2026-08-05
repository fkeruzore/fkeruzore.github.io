---
title: "panco3: Differentiable Bayesian Inference in JAX"
excerpt: "Differentiable, GPU-capable JAX port of panco2, using MCMC/HMC via BlackJAX; built with Claude Code"
collection: research
permalink: /research/panco3/
date: 2026-01-01
themes: [gastrophysics, software, aiml]
---

**Github:** [fkeruzore/panco2](https://github.com/fkeruzore/panco2)

`panco3` is a from-scratch [JAX](https://github.com/google/jax) port of [panco2]({{ base_path }}/research/panco2/), rebuilding the same forward-modeling approach to Bayesian pressure profile fitting as a fully differentiable, GPU-capable pipeline.

`panco2` runs on an ensemble MCMC sampler (`emcee`), which is CPU-bound and treats the forward model as a black box.
Most of the cost of `panco2` is in its forward model, which consists in straightforward tensor operations which can be accelerated using compilation and GPUs; and in sampling efficiency, which can be improved using gradient-based workflows.
`panco3` reimplements the forward model - profile parametrization, beam convolution, filtering, likelihood evaluation - end-to-end in JAX, making every step JIT-compilable, GPU-accelerated, and differentiable.
Sampling moves from ensemble MCMC to gradient-based MCMC/HMC via [BlackJAX](https://github.com/blackjax-devs/blackjax), which uses those gradients to propose more efficient moves through parameter space.

Most of the `panco3` codebase was generated with [Claude Code](https://claude.com/claude-code) as an agent-assisted development exercise, with the physics, validation, and API design directed and reviewed throughout.
`panco3` is in active development.
