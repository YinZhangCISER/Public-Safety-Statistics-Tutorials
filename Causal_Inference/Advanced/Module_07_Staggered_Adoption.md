# Module 7: Staggered Adoption and the Negative Weights Problem

> **Developed by Yin Zhang, PhD**, Assistant Professor, Department of Mathematics and Statistics, Washington State University

**The question this module answers:** *When units adopt at different times, two way fixed effects can return a number outside the range of every unit's true effect. How much of that is the negative weights, and how much is something else?*

---

## The Question

With staggered adoption, two way fixed effects uses **already treated units as controls for later adopters**. Those comparisons are contaminated.

The program in this dataset arrived everywhere at once, so this module simulates staggered adoption and measures the damage. **Two separate problems turn out to be involved, and they can be separated.**

## Estimand and Assumptions

Two counterfactual baselines are built from the same data, neither containing any program:

| Baseline | Construction |
|---|---|
| **mu0** | the planted effect divided back out, keeping the panel's own agency trends |
| **mu0par** | fitted agency and month effects only, **parallel by construction** |

Four adoption waves, one a year, with early adopters receiving larger effects, which is the case that breaks the estimator hardest and is not an unusual pattern.

| Agency | Adopts | Treated months | True effect |
|---|---|---|---|
| Stonewick | 2021-01 | 64 | 25% |
| Tarnbridge | 2022-01 | 52 | 18% |
| Millgate | 2023-01 | 40 | 10% |
| Pinecrest | 2024-01 | 28 | 5% |

The treated month weighted average of those is **−16.72 percent**.

## Estimation

```python
smf.glm("y ~ C(agency_id)+C(year_month)+D", d,
        family=sm.families.Poisson(), offset=d["lo"]).fit()
```

## Worked Example

![A bar chart of the bias of two way fixed effects in four simulated cases. With the panel's own trends, constant effects give minus 3.73 and heterogeneous effects minus 7.06. With trends forced parallel, constant effects give plus 0.23 and heterogeneous effects minus 3.79](Figures/fig_a07_staggered.png)

| | Trends as they are in this panel | Trends forced parallel |
|---|---|---|
| **Constant 12 percent effects** | bias **−3.73** | bias **+0.23** |
| **Heterogeneous by wave** | bias **−7.06** | bias **−3.79** |

**The bottom right cell is the textbook case and it is unbiased**, which validates the simulation.

**Parallel trends with heterogeneity leaves −3.79 points.** That is the negative weights problem: with staggered timing, some of the two by two comparisons inside the estimator use already treated units as controls, and those enter with the wrong sign when effects differ across cohorts.

**The panel's own trends with constant effects leaves −3.73 points.** That is not the negative weights problem at all. It is ordinary non parallel trends, which staggered timing amplifies because each cohort's treatment indicator correlates with time differently.

**The two are roughly additive**, giving −7.06 when both are present.

That decomposition matters because the two have different remedies, and a heterogeneity robust estimator fixes only one of them.

## Recovering the Planted Answer

The generator gives a single adoption date and a homogeneous effect, so the real study sits in neither of the damaged cells. **This module exists to establish what would have happened had the rollout been staggered**, which is how most real programs arrive, and the answer is that the estimator's bias would have been between 3.7 and 7.1 points with no warning in the output.

## Diagnostics

| Check | Acceptable |
|---|---|
| Are adoption dates staggered | if yes, TWFE needs justification |
| Goodman Bacon decomposition | the share of weight on already treated comparisons |
| A heterogeneity robust estimator | reported alongside, not instead |
| Never treated controls only | as a robustness check |
| Cohort specific pre trends | the other half of the problem |

## What To Do About It

| Remedy | What it fixes |
|---|---|
| Report the Goodman Bacon decomposition | shows which comparisons carry weight |
| Callaway and Sant'Anna, or Sun and Abraham | the negative weights |
| Restrict to never treated controls | removes the forbidden comparisons, costs precision |
| Allow cohort specific trends | the non parallel trends half, costs precision |

**The first row matters most and is the cheapest.** A decomposition showing 90 percent of the weight on clean never treated comparisons is a different situation from one where half the weight sits on already treated controls.

## Do It Yourself

> 📓 **Notebook:** [Module_07_Staggered_Adoption.ipynb](Notebooks/Module_07_Staggered_Adoption.ipynb)
> [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/YinZhangCISER/Public-Safety-Statistics-Tutorials/blob/main/Causal_Inference/Advanced/Notebooks/Module_07_Staggered_Adoption.ipynb)
> About 35 minutes.

The exercise estimates each cohort against never treated agencies only, which is the logic of the modern estimators in one cell.

## When Not To Use This

| Situation | Reach for |
|---|---|
| A single adoption date | plain TWFE is fine; this module does not apply |
| Staggered adoption, homogeneous effects, parallel trends | plain TWFE is unbiased, and say why you believe all three |
| Staggered adoption, anything else | a cohort aware estimator, and report both |
| Treatment that turns off again | this module's remedies do not cover it |

## Reporting the Result

> Adoption in this study occurred on a single date, so the two way fixed effects estimator does not face the negative weights problem. A simulation on the same panel establishes what a staggered rollout would have cost: with effects constant across cohorts and trends forced parallel the estimator is unbiased, with heterogeneous effects across cohorts it is biased by 3.8 percentage points, with the panel's own non parallel trends and constant effects by 3.7, and with both by 7.1. Had adoption been staggered, a cohort aware estimator would have been used and the Goodman Bacon decomposition reported.

## Further Reading

- Goodman Bacon, A. (2021). Difference in differences with variation in treatment timing. *Journal of Econometrics*, 225.
- Callaway, B. and Sant'Anna, P. H. C. (2021). Difference in differences with multiple time periods. *Journal of Econometrics*, 225.
- Sun, L. and Abraham, S. (2021). Estimating dynamic treatment effects in event studies with heterogeneous treatment effects. *Journal of Econometrics*, 225.
- de Chaisemartin, C. and D'Haultfoeuille, X. (2020). Two way fixed effects estimators with heterogeneous treatment effects. *American Economic Review*, 110.

---

| | |
|---|---|
| **Previous** | [Module 6: Event Studies and Pre Trend Testing](Module_06_Event_Studies_And_Pre_Trend_Testing.md) |
| **Next** | [Module 8: Synthetic Control](Module_08_Synthetic_Control.md) |
| **Builds on** | [Module 5](Module_05_Two_Way_Fixed_Effects.md), [Module 6](Module_06_Event_Studies_And_Pre_Trend_Testing.md) |
| **Used again in** | [Module 15](Module_15_Heterogeneous_Effects.md), [Module 16](Module_16_The_Causal_Claim.md) |

*This module is part of a series developed for the Washington Data Exchange for Public Safety (WADEPS) through the Center for Interdisciplinary Statistical Education and Research (CISER) at Washington State University. Version 1.0, September 2026. Questions, errors, or suggestions: yin.zhang@wsu.edu*

*All examples use synthetic data created for teaching. They do not represent any real jurisdiction, agency, officer, or incident. See [Data/DATA_DICTIONARY.md](../../Data/DATA_DICTIONARY.md).*
