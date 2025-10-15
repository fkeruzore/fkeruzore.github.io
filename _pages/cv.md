---
layout: archive
title: "CV"
permalink: /cv/
author_profile: true
redirect_from:
  - /resume
---

{% include base_path %}

# Research positions

* 2021 - present: Postdoctoral Scholar
  * Argonne National Laboratory, High Energy Physics division
  * Supervisor: Dr. Lindsey Bleem
  * Research activities:
    * Physics-informed AI/ML emulation of thermodynamic properties of simulated galaxy clusters
    * Millimeter-wave sky maps from cosmological simulations
    * Multi-wavelength studies of galaxy cluster samples
    * Supervision of two post-bachelor internships (6 months to 1 year)
    * Junior coordinator of galaxy cluster-related analyses in the SPT-3G collaboration

* 2018 - 2021: Ph.D Student
  * Université Grenoble Alpes, Laboratoire de Physique Subatomique et Cosmologie
  * Supervisor: Pr. Frédéric Mayet
  * Research activities:
    * Observations at the IRAM 30-m telescope
    * Analysis of NIKA2 raw data
    * Analysis of the thermodynamic properties of the intracluster medium
    * Mass-observable scaling relations
    * Responsible of the NIKA2 collaboration SZ pipeline and SZ database

# Education

* Ph.D in Cosmology, Université Grenoble Alpes, 2021
* Master's degree in Cosmology and Particle Physics, Université de Montpellier, 2018
* Bachelor's degree in Physics and Chemistry, Université de Bordeaux, 2016

# Skills

* Programming
  * Python (scipy, astropy, emcee, pymc3)
  * JAX ecosystem (Differentiable and GPU-enabled Python)
  * IDL, R, Shell scripting, LaTeX
  * Parallel computing (multithreading, MPI)
  * Version control (git, svn), Documentation (Sphinx),

* Data analysis
  * AI/ML: Artificial neural networks (design, training, and application)
  * Statistical modelling: Hierarchical models, Forward modelling
  * Inference: Bayesian analysis, Monte Carlo Markov chains, Gradient descent regression
  * Pipeline design and use of supercomputers to handle large datasets

# Public scientific software

* [fkeruzore/picasso](https://github.com/fkeruzore/picasso): Painting intracluster gas on gravity-only simulations
  * Gas model combining a parameterized physical model and neural network predictions
  * Implemented using JAX and flax, with fully GPU-friendly and differentiable predictions
  * Documentation: [picasso-cosmo.readthedocs.io](https://picasso-cosmo.readthedocs.io)
  * Publication: [Kéruzoré et al., The Open Journal of Astrophysics 7, 116 (2024)](https://ui.adsabs.harvard.edu/link_gateway/2024OJAp....7E.116K/doi:10.33232/001c.127486)

* [fkeruzore/panco2](https://github.com/fkeruzore/panco2): Pressure profile measurements from SZ galaxy cluster maps
  * Forward modeling MCMC analysis, enabling taking into account mm-wave systematics
  * Tested on simulated Planck, SPT, NIKA2 maps; can be used with any mm-wave data
  * Documentation: [panco2.readthedocs.io](https://panco2.readthedocs.io)
  * Publication: [Kéruzoré et al., The Open Journal of Astrophysics 6, 9 (2023)](https://ui.adsabs.harvard.edu/link_gateway/2023OJAp....6E...9K/doi:10.21105/astro.2212.01439)

# Collaborations

* Member of the Dark Energy Science Collaboration (DESC) since 2022
* Member of the CMB-S4 collaboration since 2022
* Member of the South Pole Telescope (SPT) collaboration since 2022
* Member of the Galaxy Clusters working group of the SPT collaboration since 2021
* Member of the CHEX-MATE collaboration since 2019
* Member of the NIKA2 collaboration since 2018 (Core team member since 2019)

# Teaching

2018-2021: 98 hours of teaching at Université Grenoble Alpes
* Electromagnetism
  * 1st year biology & chemistry students
  * Tutorials (online & in-person), labs (in-person)
  * 56 hours
* Applied thermodynamics
  * 3rd year physics students
  * Tutorials (online & in-person)
  * 30 hours
* Nuclear physics
  * 5th year radioprotection students
  * Labs (in-person)
  * 12 hours

# Service and responsibilities

* Junior coordinator of galaxy cluster-related analyses in the SPT-3G collaboration since 2024
* PI of a joint SPT-eROSITA project studying the statistical relations between multi-wavelength galaxy cluster observables since 2022
* Responsible of the NIKA2 collaboration SZ pipeline from 2019 to 2021
* Responsible of the NIKA2 collaboration SZ database from 2019 to 2021

# Talks

  <ul>{% for post in site.talks reversed %}
    {% include archive-single-talk-cv.html %}
  {% endfor %}</ul>

# Publications

<strong>{{ site.data.pub_stats.publications }}</strong> publications; <strong>{{ site.data.pub_stats.citecount }}</strong> citations; h-index: <strong>{{ site.data.pub_stats.hindex }}</strong> (*Source*: [NASA ADS](https://ui.adsabs.harvard.edu/search/filter_doctype_facet_hier_fq_doctype=AND&filter_doctype_facet_hier_fq_doctype=doctype_facet_hier%3A%220%2FArticle%22&fq=%7B!type%3Daqp%20v%3D%24fq_doctype%7D&fq_doctype=(doctype_facet_hier%3A%220%2FArticle%22)&q=%20author%3A%22keruzore%2C%20florian%22&sort=date%20desc%2C%20bibcode%20desc&p_=0))

<div class="publications-compact" markdown="1">

## Journal Articles

  <ul>{% for post in site.publications reversed %}
    {% if post.category == "fa_papers" %}
      {% include publication-cv.html %}
    {% endif %}
  {% endfor %}</ul>

  <ul>{% for post in site.publications reversed %}
    {% if post.category == "co_papers" %}
      {% include publication-cv.html %}
    {% endif %}
  {% endfor %}</ul>

## Conference Proceedings

  <ul>{% for post in site.publications reversed %}
    {% if post.category == "fa_procs" %}
      {% include publication-cv.html %}
    {% endif %}
  {% endfor %}</ul>

  Plus <strong>{{ site.data.pub_stats.co_procs }}</strong> conference proceedings as a co-author -- see the dedicated [Publications page](https://fkeruzore.github.io/publications/) for the complete list.

## PhD Thesis

  <ul>{% for post in site.publications reversed %}
    {% if post.category == "thesis" %}
      {% include publication-cv.html %}
    {% endif %}
  {% endfor %}</ul>

</div>
