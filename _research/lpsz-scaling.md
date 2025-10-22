---
title: "LPSZ Mass-Observable Scaling Relation"
excerpt: "Hierarchical Bayesian modeling to constrain the mass-tSZ scaling relation from the NIKA2 SZ Large Program"
collection: research
permalink: /research/lpsz-scaling/
date: 2022-06-01
themes: [gastrophysics]
header:
  teaser: banner_scaling.png
---

**Associated publication:** [Kéruzoré, F. et al. (2022), mm Universe @ NIKA2](https://ui.adsabs.harvard.edu/abs/2022EPJWC.25700025K/abstract)

Calibrating the scaling relation between cluster mass and tSZ signal $$Y_{500}$$ is one of the main scientific goals of the NIKA2 LPSZ.
I have set up and validated a pipeline to fit this relation from the measurement of individual cluster properties from LPSZ data.
The regression of this relation is complex and involves a large number of systematic effects, such as the correlation between the measurement uncertainties, selection effects, and bias and scatter of the mass estimators used.
I proposed the use of a hierarchical Bayesian model using LIRA software[^1], allowing me to take into account a large number of systematic effects in the fitting.

I used this tool to predict the potential constraining power of the LPSZ on the scaling relation.
For this purpose, I developed a Monte Carlo procedure to simulate mock cluster samples that mimic the LPSZ.
The simulation algorithm can be summarized as follows.
First, random samples are drawn from a halo mass function, creating a cluster sample with a realistic mass-redshift distribution.
A fiducial scaling relation is then used to compute $$Y_{500}$$ values for these synthetic clusters.
Part of this sample is then randomly selected based on their tSZ signal and redshift, following the LPSZ selection function.
This produces a sample with a mass-redshift distribution identical to that of the real LPSZ sample.
Realistic errors are then added to the mass and tSZ observable values to mimic the process of thermodynamic properties measurement from NIKA2 LPSZ data.
The resulting sample is thus similar to the LPSZ sample in terms of redshift distribution, mass-observable plane coverage, and data quality, and has a known mass-observable scaling relation.

The study of the constraining power of the LPSZ consisted of a large number of repetitions of this procedure, allowing the creation of thousands of realistic samples, and then fitting the observed scaling relation on each mock.
I compared the reconstructed scaling relations with the true one -- i.e. that used to generate the samples -- and showed that there was no evidence of a significant bias on the reconstructed relation, validating the accuracy of the fitting procedure.
I was also able to assess the expected precision of the scaling relation constraints from the LPSZ and showed that given the high quality of constraints on individual cluster properties that could be obtained by combining NIKA2 and *XMM-Newton* observations, the LPSZ results would be very competitive, and could lead to precise mass calibration for tSZ-selected cluster samples.

[^1]: Sereno, M., MNRAS 455, no. 2 (2016): 2149-2162. See also [fkeruzore/pylira](https://github/com/fkeruzore/pylira)
