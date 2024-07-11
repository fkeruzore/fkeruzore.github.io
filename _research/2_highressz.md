---
title: "Gastrophysics"
excerpt: "Measuring ICM thermodynamics from tSZ (and sometimes X-ray) observations"
collection: research
---

The cosmological exploitation of tSZ surveys relies on the knowledge of several properties of galaxy clusters.
On one hand, the knowledge of the mean pressure profile of the intracluster medium is necessary to build cluster catalogs from millimeter observations.
Indeed, the amplitude of the tSZ effect is directly proportional to the pressure of the intracluster medium integrated along the line of sight.
Thus, prior knowledge of this distribution may help maximize the purity and completeness of the tSZ surveys, thus improving the statistical properties of the catalogs, and thus the precision and accuracy of the cosmological parameter estimates.
On the other hand, millimeter surveys alone cannot provide individual cluster mass estimates, and rely on mass-observable scaling relations that require calibration.

My thesis work was part of the large NIKA2 SZ program (LPSZ), a follow-up of about 40 intermediate- to high-redshift galaxy clusters covering a wide mass range.
The goal of this program is to map the tSZ effect in these galaxy clusters with high angular resolution using the NIKA2 camera and to combine these observations with similar measurements in the X-ray domain to study the mean pressure profile of galaxy clusters and the mass-tSZ observable scaling relation.
I have been involved in several activities within this program, from exploiting the raw data to construct maps of the SZ effect and extracting thermodynamic properties of the clusters from these observations to studying the mass-observable scaling relation.

# Measurements of the thermodynamic properties of a distant low-mass cluster

**Associated publications:** [Kéruzoré, F. et al. (2020), A&A, 644, A93.](https://ui.adsabs.harvard.edu/abs/2020A&A...644A..93K/abstract), [Kéruzoré, F. et al. (2020), mm Universe @ NIKA2](https://ui.adsabs.harvard.edu/abs/2020EPJWC.22800012K/abstract)

I led the comprehensive analysis of the thermodynamic properties of one of the most challenging clusters within the NIKA2 LPSZ.
ACT-cl J0215.4+0030 (ACTJ0215 for short) was initially identified in the first ACT tSZ survey.
This cluster has a particularly important place within the LPSZ, as one of its lowest mass, highest redshift targets.
Such systems are particularly interesting to study: because of their shallower gravitational potential, they are more susceptible to non-gravitational processes, thus offering valuable insights into the thermodynamic properties of the intracluster medium.
However, measuring their properties is challenging, as the amplitude of the tSZ signal of a cluster is closely tied to its mass, and its spatial extension to redshift.
These systems therefore appear as dim and small in tSZ data.
Moreover, in the case of ACTJ0215, an additional difficulty came from a strong contamination of the tSZ signal by point sources.
The main bandwidth of NIKA2 for the observation of the tSZ effect is around 150 GHz; at this frequency, the tSZ effect manifests as a decrement in the surface brightness of the CMB.
Therefore, the positive flux from astrophysical sources can compensate -- partially or totally -- for the tSZ decrement in NIKA2 maps, and thus alter the reconstructed cluster properties.

The measurement and analysis of the thermodynamic properties of ACTJ0215 were, therefore, both crucial steps of the LPSZ, and required a large number of observational difficulties to be solved for the exploitation of the rest of the sample.
I carried out this analysis by first constructing the tSZ maps of this cluster from NIKA2 raw data, and then quantifying the remaining noise in the maps and the filtering undergone by the signal.
The pipeline I developed to perform this analysis is still used by the NIKA2 collaboration to reduce tSZ data.
I then used a Markov chain Monte Carlo algorithm and a forward modeling approach to fit the pressure profile of the intracluster medium on the NIKA2 data.
In this approach, I accounted for the point source contamination by jointly modeling the NIKA2 map as the sum of tSZ signal and point source emission, with source fluxes treated as parameters of the model.
This approach enables propagating the uncertainty on this contamination to the final results, by adding informative priors on the flux values, which are then marginalized over.

Combining the measured pressure profile with X-ray observations from the *XMM-Newton* satellite allowed me to characterize the cluster's thermodynamic properties.
The integration of NIKA2 and *XMM-Newton* data revealed a disturbed core, and provided precise constraints on the cluster's mass and integrated Compton parameter $$Y_{500}$$, which is a key tSZ survey observable.
These results demonstrated that the combination of NIKA2 and *XMM-Newton* observations could establish precise constraints on properties in the mass-observable scaling relation, even for complex clusters like ACTJ0215.
This is highly promising for the future results of the large NIKA2 LPSZ, indicating a potentially substantial constraining power on the final sample properties.

# Mass-observable scaling relation from the NIKA2 SZ Large Program

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

# `panco2`: pressure profile measurements from tSZ maps

**Associated publications:** [Kéruzoré, F. et al. (2023), OJAp, 6, 9.](https://ui.adsabs.harvard.edu/abs/2023OJAp....6E...9K/abstract), [Kéruzoré, F. et al. (2020), mm Universe @ NIKA2](https://ui.adsabs.harvard.edu/abs/2022EPJWC.25700024K/abstract)

The progression of NIKA2 observations on clusters within the LPSZ sample highlighted the necessity for standardized cluster sample analyses.
These analyses serve several purposes.
First, they enable initial estimates for the main LPSZ scientific products from a subset of clusters.
They are also needed  to evaluate data quality and conduct systematic studies, examining the impact of analysis choices on final results.
However, the time constraints imposed by the NIKA2 SZ pipeline for analyzing individual cluster thermodynamic properties limited the possibility of running these analyses.
In response, I undertook a complete rewrite of the pipeline, accelerating it using optimized Python code and efficient numerical libraries.
This development significantly reduced computation time, from several days down to a few minutes, enabling both standardized analyses on cluster samples and systematic studies on the impact of tSZ signal modeling choices.
The new software, named `panco2`, underwent extensive validation tests using various numerical simulations.
These tests, based on idealized spherical clusters to realistic hydrodynamic simulations, ensured the software's reliability.
The results were published and detailed in an internal note to the NIKA2 collaboration, leading to `panco2` becoming the new SZ analysis pipeline of the NIKA2 collaboration.

`panco2` has been in use since 2021, contributing to several published works.
Recognizing its potential interest for the wider scientific community, I adapted the code to be easily usable on any millimeter-wave dataset, offering flexibility and compatibility with various studies.
To assess the code's accuracy, I implemented a validation procedure based on the analysis of simulated maps.
This involved synthetic cluster maps mimicking observations from instruments like *Planck*, SPT, and NIKA2.
The pressure profiles reconstructed with `panco2` consistently showed excellent agreement with the real profiles, validating the accuracy of the adjustments made.
This updated version of `panco2` is now a Python library, publicly available at [fkeruzore/panco2](https://github.com/fkeruzore/panco2), accompanied by a comprehensive [documentation](https://panco2.readthedocs.io/en/latest/).


[^1]: Sereno, M., MNRAS 455, no. 2 (2016): 2149-2162. See also [fkeruzore/pylira](https://github/com/fkeruzore/pylira)
