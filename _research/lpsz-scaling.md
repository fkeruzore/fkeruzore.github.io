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

One of the central challenges in cluster cosmology is **mass calibration**: individual cluster masses cannot be measured directly, but must be inferred from observable proxies (in this case, the tSZ signal $$Y_{500}$$) via a scaling relation.
Fitting this relation is statistically non-trivial - the data contain correlated measurement uncertainties, a non-trivial selection function that biases the observed sample, and scatter in the mass estimators themselves.
Naive regression approaches give biased results; a proper treatment requires a model that accounts for all of these effects simultaneously.

I designed and validated a **hierarchical Bayesian regression pipeline** for this problem, using the LIRA framework[^1].
The hierarchical structure allows the model to share information across the cluster sample while correctly propagating individual measurement uncertainties into the population-level inference - analogous to multilevel models used in clinical trials or recommendation systems.

To validate the pipeline and forecast its constraining power, I built a **Monte Carlo simulation framework** that generates thousands of realistic synthetic cluster samples: drawing halos from a mass function, assigning tSZ observables via a fiducial scaling relation, applying the survey's selection function, and adding realistic noise.
Running the inference pipeline on each synthetic sample and comparing the recovered relation to the known true one confirmed the procedure was unbiased and allowed me to characterize the expected precision of the final LPSZ results.

[^1]: Sereno, M., MNRAS 455, no. 2 (2016): 2149-2162. See also [fkeruzore/pylira](https://github/com/fkeruzore/pylira)

[^1]: Sereno, M., MNRAS 455, no. 2 (2016): 2149-2162. See also [fkeruzore/pylira](https://github/com/fkeruzore/pylira)
