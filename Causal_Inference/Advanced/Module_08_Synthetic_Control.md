# Module 8: Synthetic Control

> **Developed by Yin Zhang, PhD**, Assistant Professor, Department of Mathematics and Statistics, Washington State University

**The question this module answers:** *Synthetic control is the most visually persuasive method in this series. What has to be true for the picture to mean anything?*

---

## The Question

On this dataset it fails at all five treated agencies, **for a reason visible before the answer is computed.** This module is about learning to look at that reason first.

## Estimand and Assumptions

> choose weights **w** over the untreated units, non negative and summing to one, minimising the distance between the treated unit and the weighted donors **over the pre period**
>
> then read the gap between them afterwards

The convexity constraint keeps the synthetic unit interpretable and stops it extrapolating. It is also the source of the failure here.

| Assumption | Diagnostic |
|---|---|
| The treated unit lies inside the donors' range | compare pre period levels |
| The synthetic unit tracks the treated unit before | pre period fit error |
| No donor is affected by the treatment | ask |
| The pre period is long enough to identify the weights | count months against donors |

## Estimation

```python
minimize(lambda w: np.mean((Y - X @ w) ** 2), w0,
         bounds=[(0, 1)] * len(donors),
         constraints=({"type": "eq", "fun": lambda w: w.sum() - 1},))
```

## Worked Example

Seven donors, 54 pre period months. The donors span **2.06 to 3.19** on the pre period mean.

| Agency | Pre period mean | Inside the donors' range |
|---|---|---|
| Stonewick | 3.51 | **no** |
| Tarnbridge | 3.70 | **no** |
| Millgate | 3.57 | **no** |
| Summit County | 3.12 | yes |
| Pinecrest | 3.72 | **no** |

**Four of the five sit above every donor.** No convex combination can reach them, so the pre period fit is guaranteed to be poor before a single weight is estimated. That is arithmetic, not a property of the optimiser.

![Two panels. The left shows each treated agency's pre period fit error as a percentage of its own mean: 25, 30, 37, 29 and 48 percent, all far above a dashed line at 5 percent. The right shows what synthetic control reports for each: plus 11.3, plus 6.0, plus 1.1, minus 25.1 and plus 2.8 percent, against a dashed line at the true 12 percent](Figures/fig_a08_synthetic_control.png)

| Agency | Pre period fit error | What it reports | Largest weights |
|---|---|---|---|
| Stonewick | 25% | **+11.3%** | Ashfell 0.53, Havenbrook 0.47 |
| Tarnbridge | 30% | +6.0% | Havenbrook 0.63, Ashfell 0.30 |
| Millgate | 37% | +1.1% | Havenbrook 0.76, Ashfell 0.16 |
| Summit County | 29% | **−25.1%** | Ashfell 0.54, Havenbrook 0.30 |
| Pinecrest | **48%** | +2.8% | Havenbrook 0.83, Prairie 0.10 |
| **The truth** | | **−12.0%** | |

Five agencies, one true effect of 12 percent, answers from **plus 11 to minus 25**.

Every one carries a pre period fit error between 25 and 48 percent of the agency's own mean, **including Summit County, whose level was inside the donors' range**. Its 29 percent error is the second worst: the donors can reach its average and cannot follow its steeper decline. **Being inside the range is necessary, not sufficient.**

**A synthetic control whose pre period fit error is a quarter of the outcome's level has not been fitted; it has been declared.**

The one closest to the truth is Summit County, and it gets there for the wrong reason: the pre trend violation from Intermediate [Module 8](../Intermediate/Module_08_When_Parallel_Trends_Fails.md) is being read as an effect.

## Recovering the Planted Answer

**It does not.** The planted 12 percent is not recovered at any agency, and the failure is entirely predictable from the selection rule: the program went to the five agencies with the highest rates in the state, so the donor pool contains nobody comparable.

**Selection on the outcome and synthetic control are a bad combination**, and the first is routine in public safety work.

## Diagnostics

| Check | Threshold |
|---|---|
| **Is the treated unit inside the donors' range** | it must be |
| Pre period fit error relative to the outcome's level | under about 5 percent |
| Number of donors receiving weight | more than two or three |
| Placebo on each donor in turn | the treated gap should be extreme |
| Pre period length | long enough to identify the weights |

**The first is free and it settles this case.** Reporting an effect from a synthetic control without the pre period fit error is like reporting a coefficient without its standard error.

## Do It Yourself

> 📓 **Notebook:** [Module_08_Synthetic_Control.ipynb](Notebooks/Module_08_Synthetic_Control.ipynb)
> [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/YinZhangCISER/Public-Safety-Statistics-Tutorials/blob/main/Causal_Inference/Advanced/Notebooks/Module_08_Synthetic_Control.ipynb)
> About 35 minutes.

The exercise drops the convexity constraint, which improves the fit and turns the method into extrapolation.

## When Not To Use This

| Situation | Verdict |
|---|---|
| One treated unit, many donors, long pre period | its home ground |
| The treated unit sits inside the donor distribution | required |
| Donors plausibly unaffected by the treatment | required |
| Several treated units | possible, but difference in differences is usually simpler |
| **The treated unit is the largest or most extreme** | **do not**; this module is the reason |

## Reporting the Result

> Synthetic control was considered and is not reported as a primary estimate. Four of the five treated agencies have pre program use of force rates above every agency in the donor pool, so no convex combination of donors can match their level; the fifth is inside the range but its trajectory is not matched. Pre period fit errors range from 25 to 48 percent of each agency's own mean, and the resulting estimates range from a 25 percent reduction to an 11 percent increase against a design where the effect is common to all five. The diagnostic that rules the method out here is the comparison of pre period levels, which requires no fitting.

## Further Reading

- Abadie, A. (2021). Using synthetic controls: feasibility, data requirements, and methodological aspects. *Journal of Economic Literature*, 59. Section 4 is the diagnostics.
- Abadie, A., Diamond, A. and Hainmueller, J. (2010). Synthetic control methods for comparative case studies. *Journal of the American Statistical Association*, 105.
- Ferman, B., Pinto, C. and Possebom, V. (2020). Cherry picking with synthetic controls. *Journal of Policy Analysis and Management*, 39.

---

| | |
|---|---|
| **Previous** | [Module 7: Staggered Adoption and the Negative Weights Problem](Module_07_Staggered_Adoption.md) |
| **Next** | [Module 9: Honest Inference with Few Clusters](Module_09_Honest_Inference_With_Few_Clusters.md) |
| **Builds on** | [Module 4](Module_04_Selection_Mechanisms.md), Intermediate [Module 3](../Intermediate/Module_03_The_Counterfactual_You_Have_To_Construct.md) |
| **Used again in** | [Module 10](Module_10_Propensity_Scores.md), [Module 16](Module_16_The_Causal_Claim.md) |

*This module is part of a series developed for the Washington Data Exchange for Public Safety (WADEPS) through the Center for Interdisciplinary Statistical Education and Research (CISER) at Washington State University. Version 1.0, September 2026. Questions, errors, or suggestions: yin.zhang@wsu.edu*

*All examples use synthetic data created for teaching. They do not represent any real jurisdiction, agency, officer, or incident. See [Data/DATA_DICTIONARY.md](../../Data/DATA_DICTIONARY.md).*
