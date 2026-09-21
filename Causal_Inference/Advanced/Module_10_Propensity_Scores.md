# Module 10: Propensity Scores and the Overlap Assumption

> **Developed by Yin Zhang, PhD**, Assistant Professor, Department of Mathematics and Statistics, Washington State University

**The question this module answers:** *A propensity score fitted here separates the groups perfectly. What does that mean, and is it about this program?*

---

## The Question

It has **two independent causes** and only one of them is about the program. Distinguishing them is the module.

## Estimand and Assumptions

Matching, weighting and stratifying on a propensity score all rest on **overlap**, sometimes called positivity: for every covariate value, both treated and untreated units must be possible.

| Assumption | Diagnostic |
|---|---|
| Overlap | the range each group covers, variable by variable |
| Unconfoundedness given the covariates | not testable |
| The score is correctly specified | balance after weighting, which is weak evidence |

## Estimation

```python
sm.Logit(X["treated"], sm.add_constant(X[cols])).fit()
```

## Worked Example

![Two panels. The left shows propensity scores under one, two and four covariates: the groups mix at one covariate and separate completely at four, with pseudo R squared rising from 0.09 to 1.00. The right plots each agency's pre program use of force rate by treatment status, showing the treated group from 3.12 to 4.02 and the controls from 2.09 to 3.20 with a single crossing](Figures/fig_a10_propensity.png)

| Covariates in the score | Pseudo R² | Lowest treated score | Highest control score |
|---|---|---|---|
| One | 0.085 | 0.330 | 0.725 |
| Two | 0.509 | 0.325 | 0.770 |
| **Four** | **1.000** | **1.000** | **0.000** |

**None of those four is the variable selection was based on.**

### Cause one: twelve units

**Four columns of pure noise separate these groups perfectly in 6 percent of 200 draws.** Perfect separation at this sample size is partly a small sample artefact and is not evidence about the assignment mechanism.

That matters, because the usual response is to drop covariates until the logit converges. Doing so produces a score that looks usable and was chosen for its convergence rather than its content.

### Cause two: the selection rule

| Variable | The groups overlap over |
|---|---|
| Sworn officers | 41% of the combined range |
| Violent crime rate | 34% |
| **Use of force rate before the program** | **4%** |

The covariates overlap substantially. The outcome's own history does not, and the entire overlap is one agency: **Havenbrook at 3.200, just above Summit County at 3.118.**

So there is exactly one control agency available to match four of the five treated ones, and it cannot be used four times.

**This is not a failure of the estimator. It is the selection rule**, which took four of the top five agencies by baseline rate.

## Recovering the Planted Answer

**It cannot be recovered by this method**, and the reason is the planted selection rule rather than anything about the estimator. Trimming to common support leaves two agencies: Summit County, which is the pre trend violator excluded from the main analysis, and Havenbrook, which reclassified its call categories in 2023.

## Diagnostics

| Check | Acceptable |
|---|---|
| Overlap in the variable selection was based on | before fitting any score |
| Units surviving a trim to common support | enough to estimate anything |
| Separation tested against noise covariates | at small n, to see how much is mechanical |
| Balance after weighting | necessary, and far from sufficient |
| The covariates the score omits | named, especially the selection variable |

## Do It Yourself

> 📓 **Notebook:** [Module_10_Propensity_Scores.ipynb](Notebooks/Module_10_Propensity_Scores.ipynb)
> [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/OWNER/REPO/blob/main/Causal_Inference/Advanced/Notebooks/Module_10_Propensity_Scores.ipynb)
> About 30 minutes.

The exercise trims to common support and finds two agencies left, one of them the agency the main analysis excluded.

## When Not To Use This

| Response | Verdict here |
|---|---|
| Trim to common support | leaves one control agency; not usable |
| Drop the outcome history from the score | estimates a score that omits the selection rule |
| Fewer covariates so the logit converges | fits, and does not address the overlap |
| Report the lack of overlap and change the estimand | **this is the answer** |
| **Difference in differences instead** | **does not require overlap in levels, only parallel trends** |

**Difference in differences is the right tool here precisely because it does not need overlap in the level.** It needs the groups to move together, which is a different and weaker requirement.

## Reporting the Result

> Propensity score methods were considered and are not used. The five treated agencies were selected on their pre program use of force rate, and the two groups overlap over 4 percent of the combined range of that variable: one control agency lies above the lowest treated one. Trimming to the region of common support leaves two agencies. A propensity score fitted on four other covariates separates the groups perfectly, but a simulation shows that four columns of random noise do the same in 6 percent of draws at this sample size, so the separation is not by itself informative about assignment. Difference in differences is used instead because it requires the groups to move in parallel rather than to overlap in level.

## Further Reading

- Rosenbaum, P. R. and Rubin, D. B. (1983). The central role of the propensity score in observational studies for causal effects. *Biometrika*, 70.
- King, G. and Nielsen, R. (2019). Why propensity scores should not be used for matching. *Political Analysis*, 27.
- Crump, R. K., Hotz, V. J., Imbens, G. W. and Mitnik, O. A. (2009). Dealing with limited overlap in estimation of average treatment effects. *Biometrika*, 96.

---

| | |
|---|---|
| **Previous** | [Module 9: Honest Inference with Few Clusters](Module_09_Honest_Inference_With_Few_Clusters.md) |
| **Next** | [Module 11: Instrumental Variables](Module_11_Instrumental_Variables.md) |
| **Builds on** | [Module 3](Module_03_Identification_Before_Estimation.md), [Module 4](Module_04_Selection_Mechanisms.md) |
| **Used again in** | [Module 14](Module_14_Sensitivity_And_Partial_Identification.md), [Module 16](Module_16_The_Causal_Claim.md) |

*This module is part of a series developed for the Washington Data Exchange for Public Safety (WADEPS) through the Center for Interdisciplinary Statistical Education and Research (CISER) at Washington State University. Version 1.0, September 2026. Questions, errors, or suggestions: yin.zhang@wsu.edu*

*All examples use synthetic data created for teaching. They do not represent any real jurisdiction, agency, officer, or incident. See [Data/DATA_DICTIONARY.md](../../Data/DATA_DICTIONARY.md).*
