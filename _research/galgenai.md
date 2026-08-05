---
title: "GalGenAI: Guided Astronomical Image Generation"
excerpt: "Deep generative models (VAE, flow-matching) for guided astronomical image generation; in development"
collection: research
permalink: /research/galgenai/
date: 2025-06-01
themes: [simulations, aiml]
---

**Github:** [fkeruzore/GalGenAI](https://github.com/ArgonneCPAC/GalGenAI)

`GalGenAI` is an active project, in which we are building deep generative models for conditional astronomical image generation.
The generation is conditioned on physical properties, guiding the generated images toward specified characteristics to produce a realistic population from a catalog.
This makes the models useful for producing targeted synthetic datasets: generating populations with prescribed physical properties for training and testing downstream analysis pipelines, or probing how physical parameters shape observable morphology.

We are focusing on two model classes: variational autoencoders, and conditional flow-matching.
Models are implemented in [PyTorch](https://docs.pytorch.org/docs/index.html) -

