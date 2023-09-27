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
    * Thermodynamic properties of simulated clusters
    * Baryon pasting: emulation of thermodynamic properties of simulated clusters
    * Millimeter-wave sky maps from cosmological simulations
    * Multi-wavelength studies of galaxy cluster samples
    * Supervision of a post-bachelor internship (6 months)

* 2018 - 2021: Ph.D Student
  * Université Grenoble Alpes, Laboratoire de Physique Subatomique et Cosmologie
  * Supervisor: Pr. Frédéric Mayet
  * Research activities:
    * Observations at the IRAM 30-m telescope
    * Analysis of NIKA2 raw data
    * Analysis of the thermodynamic properties of the intracluster medium
    * Mass-observable scaling relations

# Education

* Ph.D in Cosmology, Université Grenoble Alpes, 2021
* Master's degree in Cosmology and Particle Physics, Université de Montpellier, 2018
* Bachelor's degree in Physics and Chemistry, Université de Bordeaux, 2016

# Skills

* Galaxy cluster science
  * Cluster cosmology
  * Sunyaev-Zeldovich effect
  * X-ray emission
  * Intracluster medium thermodynamics
  * Mass-observable, Observable-observable scaling relations
  * Clusters in N-body simulations
* Data analysis
  * Bayesian inference
  * Monte Carlo Markov Chain sampling
  * Regression
  * Hierarchical models
* Programming
  * Python (scipy, astropy, emcee, pymc3)
  * IDL, R
  * Shell, LaTeX
  * Version control (git, svn)
  * Code Documentation (Sphinx),
  * Parallel computing (multithreading, MPI)

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
  
# Service

* Developper and maintainer of `panco2`, a Python library to extract pressure measurements from millimeter-wave maps of galaxy clusters [https://github.com/fkeruzore/panco2](fkeruzore/panco2)
* Responsible of the NIKA2 collaboration SZ pipeline from 2019 to 2021
* Responsible of the NIKA2 collaboration SZ database from 2019 to 2021

# Talks

  <ul>{% for post in site.talks reversed %}
    {% include archive-single-talk-cv.html %}
  {% endfor %}</ul>
  
# Publications

<strong>{{ site.data.pub_stats.publications }}</strong> publications; <strong>{{ site.data.pub_stats.citecount }}</strong> citations; h-index: <strong>{{ site.data.pub_stats.hindex }}</strong> (*Source*: [NASA ADS](https://ui.adsabs.harvard.edu/search/filter_doctype_facet_hier_fq_doctype=AND&filter_doctype_facet_hier_fq_doctype=doctype_facet_hier%3A%220%2FArticle%22&fq=%7B!type%3Daqp%20v%3D%24fq_doctype%7D&fq_doctype=(doctype_facet_hier%3A%220%2FArticle%22)&q=%20author%3A%22keruzore%2C%20florian%22&sort=date%20desc%2C%20bibcode%20desc&p_=0))

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
