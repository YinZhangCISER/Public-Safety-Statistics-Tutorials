# Module 9: Honest Inference with Few Clusters

> **Developed by Yin Zhang, PhD**, Assistant Professor, Department of Mathematics and Statistics, Washington State University

**The question this module answers:** *Every interval so far rests on asymptotics. Eleven agencies do not supply them. What should the interval be?*

---

## The Question

Four intervals can be put on the same estimate. **The one most people reach for is the least honest here**, and two of the four need no large sample theory at all.

## Estimand and Assumptions

| Method | Assumes |
|---|---|
| **Model based** | the model, and independence given it |
| **Cluster robust** | many clusters, conventionally forty or more |
| **Cluster bootstrap** | the clusters are exchangeable |
| **Randomisation inference** | the assignment could have been otherwise, over a stated set |

## Estimation

```python
.fit(cov_type="cluster", cov_kwds={"groups": d["agency_id"]})
# and: resample whole agencies with replacement, 400 times
# and: reassign the treatment label at random, 400 times
```

## Worked Example

The estimate is **−12.61 percent** from **11 agencies**.

![A chart of four 95 percent intervals for the same estimate. Model based runs from minus 17.9 to minus 6.9, cluster robust is identical, the cluster bootstrap runs from minus 20.9 to minus 8.0, and the randomisation null runs from minus 13.1 to plus 12.2 with a note that the estimate sits at p equals 0.030](Figures/fig_a09_few_clusters.png)

| Method | Interval | Width |
|---|---|---|
| Model based | [−17.9, −6.9] | 11.0 |
| Cluster robust, 11 clusters | [−17.9, −6.9] | 11.0 |
| **Cluster bootstrap** | **[−20.9, −8.0]** | **12.9** |
| Randomisation, the null | [−13.1, +12.2] | p = 0.030 |

**The model based and cluster robust intervals are identical to four decimal places, and that is the warning rather than the reassurance.**

Cluster robust standard errors are consistent as the number of clusters grows. With eleven they are known to be biased downward, and the usual guidance is that forty or more are needed. Agreeing with the model based errors does not mean both are right; it means neither correction is doing anything.

**The bootstrap interval is wider, 12.9 points against 11.0, and wider on the side that matters**, reaching 20.9 percent against 17.9. The model based interval was too narrow by about a sixth. That is not a catastrophe and it is not nothing.

**Randomisation inference asks a different question**, and for a design like this a better one: among all the ways four agencies could have been labelled treated, how unusual is the one that was? The answer is p = 0.030, and it assumes nothing about sample size.

All four agree about the conclusion, which was not guaranteed and is worth reporting as a fact.

## Recovering the Planted Answer

The planted effect is 12.0 percent and every one of the four intervals covers it. What the module establishes is not that the estimate is right, which is known, but **that the width of the reported interval depends on a choice that is usually made without comment**, and that the default choice understates it here.

## Diagnostics

| Check | Acceptable |
|---|---|
| Number of clusters | 40 or more before trusting cluster robust errors |
| At least two methods reported | and the one the conclusion rests on named |
| Bootstrap and model based compared | a large gap is a finding |
| The randomisation assignment set | stated explicitly, because it is a choice |
| Wild cluster bootstrap | the standard advice for 5 to 40 clusters |

## Do It Yourself

> 📓 **Notebook:** [Module_09_Honest_Inference_With_Few_Clusters.ipynb](Notebooks/Module_09_Honest_Inference_With_Few_Clusters.ipynb)
> [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/YinZhangCISER/Public-Safety-Statistics-Tutorials/blob/main/Causal_Inference/Advanced/Notebooks/Module_09_Honest_Inference_With_Few_Clusters.ipynb)
> About 30 minutes.

The exercise restricts the randomisation to plausible assignments and the p value moves, which is the method's central and uncomfortable feature on observational data.

## When Not To Use This

| Situation | Reach for |
|---|---|
| 40 or more clusters | cluster robust errors are fine |
| 5 to 40 clusters | the wild cluster bootstrap, Cameron Gelbach Miller |
| Fewer than 5 clusters | no method rescues this; report it as a case study |
| A genuine randomisation | randomisation inference is exact, and is the right default |
| Serial correlation within units | Bertrand Duflo Mullainathan, cited below |

## Reporting the Result

> The estimate rests on eleven agencies, which is far below the number at which cluster robust standard errors can be trusted; in this case they are numerically indistinguishable from the model based errors, which indicates that the correction is doing nothing rather than that none is needed. A cluster bootstrap over 400 resamples of whole agencies gives a 95 percent interval from 20.9 to 8.0 percent below, against 17.9 to 6.9 from the model. A randomisation test over 400 reassignments of the treatment label places the estimate at p = 0.030 against a null constructed from all assignments of four agencies out of eleven. The bootstrap interval is reported as the primary uncertainty statement.

## Further Reading

- Cameron, A. C., Gelbach, J. B. and Miller, D. L. (2008). Bootstrap based improvements for inference with clustered errors. *Review of Economics and Statistics*, 90.
- MacKinnon, J. G. and Webb, M. D. (2017). Wild bootstrap inference for wildly different cluster sizes. *Journal of Applied Econometrics*, 32.
- Bertrand, M., Duflo, E. and Mullainathan, S. (2004). How much should we trust differences in differences estimates? *Quarterly Journal of Economics*, 119.
- Young, A. (2019). Channeling Fisher: randomization tests and the statistical insignificance of seemingly significant experimental results. *Quarterly Journal of Economics*, 134.

---

| | |
|---|---|
| **Previous** | [Module 8: Synthetic Control](Module_08_Synthetic_Control.md) |
| **Next** | [Module 10: Propensity Scores and the Overlap Assumption](Module_10_Propensity_Scores.md) |
| **Builds on** | [Module 5](Module_05_Two_Way_Fixed_Effects.md), Intermediate [Module 12](../Intermediate/Module_12_Placebo_Tests.md) |
| **Used again in** | [Module 14](Module_14_Sensitivity_And_Partial_Identification.md), [Module 16](Module_16_The_Causal_Claim.md) |

*This module is part of a series developed for the Washington Data Exchange for Public Safety (WADEPS) through the Center for Interdisciplinary Statistical Education and Research (CISER) at Washington State University. Version 1.0, September 2026. Questions, errors, or suggestions: yin.zhang@wsu.edu*

*All examples use synthetic data created for teaching. They do not represent any real jurisdiction, agency, officer, or incident. See [Data/DATA_DICTIONARY.md](../../Data/DATA_DICTIONARY.md).*
