# Module 6: Event Studies and Pre Trend Testing

> **Developed by Yin Zhang, PhD**, Assistant Professor, Department of Mathematics and Statistics, Washington State University

**The question this module answers:** *The event study plot is the standard credibility exhibit. What is it actually evidence of?*

---

## The Question

Less than it appears, and more than it appears, in different respects. **The individual coefficients are unreadable at this sample size. The joint test on the pre period coefficients is the usable output, and it is rarely reported.**

## Estimand and Assumptions

> one coefficient per month relative to the program's start, with the month before it as the reference
>
> **pre period coefficients estimate zero** if the parallel trends assumption holds

| Assumption | Diagnostic |
|---|---|
| Parallel trends | the joint test on the pre period coefficients |
| No anticipation | individual pre period coefficients near the start |
| Enough units per event time cell | the width of each interval |

## Estimation

```python
terms = " + ".join([f"I(trm&(ek=={j}))" for j in js])
smf.glm("n_uof ~ C(agency_id)+C(year_month)+" + terms, d, ...)
```

## Worked Example

![Two panels. The left plots one coefficient per month around the program start with very wide intervals, swinging from about 20 percent down to 16 percent up in the pre period, against a smooth orange curve showing the effect that is actually there. The right shows the share of simulations where the pre period test rejects a planted violation, 2 percent at one percent a year rising to 87 at five](Figures/fig_a06_event_study.png)

| Months since start | Estimate | 95 percent interval |
|---|---|---|
| −8 | −8.3% | [−26.6, +14.5] |
| −7 | +15.6% | [−19.4, +65.7] |
| −5 | −11.8% | [−39.2, +28.0] |
| −3 | −19.6% | [−43.3, +14.1] |
| +2 | +24.0% | [−11.5, +73.8] |
| +6 | −26.1% | [−50.1, +9.4] |

The truth for every pre period coefficient is zero, and they swing between 20 percent down and 16 percent up with intervals thirty to fifty points wide.

**Reading a story into this plot is reading noise**, and the story a reader constructs from a jagged pre period is almost always "the trends were already diverging".

### The test that is informative

| | |
|---|---|
| Joint test that all 7 pre period coefficients are zero | **chi squared 4.9 on 7 df, p = 0.678** |
| The largest individual pre period coefficient | 19.6% |

**Those two facts together are the point.** A reader who sees a 20 percent pre period swing doubts the design. A reader given the joint test sees that a set of coefficients this noisy is exactly what zero looks like at this sample size.

**Report the joint test with the plot, always.**

### What the test could have caught

| Planted violation | Found at p < 0.05 |
|---|---|
| 1 percent a year | **2%** |
| 2 percent a year | **16%** |
| 3 percent a year | 40% |
| 5 percent a year | 87% |

The violation that mattered in this dataset, the one Summit County creates at the group level, is **2.16 percent a year**. A violation that size is found one time in six.

**A passing pre trend test on eleven agencies is weak evidence.** The honest report gives the test, the interval on the trend difference, and the size of violation the test had a fair chance of detecting.

## Recovering the Planted Answer

The generator gives all agencies the same trend except Summit County, which is excluded here. The joint pre period test therefore should pass, and does, at p = 0.678. The power simulation then shows that this particular test would also have passed on a panel whose trends differed by two percentage points a year, which is the honest limit of what it establishes.

## Diagnostics

| Check | Acceptable |
|---|---|
| Joint pre period test | reported, with its degrees of freedom |
| Interval on the pre trend difference | reported alongside the p value |
| Detectable violation size | computed by simulation |
| Bin width | chosen from the number of units, not the calendar |
| Individual coefficients | not interpreted one at a time at this sample size |

## Do It Yourself

> 📓 **Notebook:** [Module_06_Event_Studies_And_Pre_Trend_Testing.ipynb](Notebooks/Module_06_Event_Studies_And_Pre_Trend_Testing.ipynb)
> [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/YinZhangCISER/Public-Safety-Statistics-Tutorials/blob/main/Causal_Inference/Advanced/Notebooks/Module_06_Event_Studies_And_Pre_Trend_Testing.ipynb)
> About 30 minutes.

The exercise bins event time into quarters and the plot becomes readable.

## When Not To Use This

| Situation | Reach for |
|---|---|
| Fewer than about twenty units | bin heavily, or report the test alone |
| Staggered adoption | [Module 7](Module_07_Staggered_Adoption.md); the plot needs a cohort aware estimator |
| The question is the response shape | Time Series Advanced [Module 13](../../Time_Series/Advanced/Module_13_Intervention_Analysis.md) |
| A bound on the violation is wanted | [Module 14](Module_14_Sensitivity_And_Partial_Identification.md), Rambachan and Roth |

## Reporting the Result

> An event study was estimated with one coefficient per month from eight months before to ten months after the program's start, relative to the month before. The seven pre program coefficients are jointly indistinguishable from zero, chi squared 4.9 on 7 degrees of freedom, p = 0.678, although individual coefficients range up to 19.6 percent in absolute value and are not individually informative at this sample size. A simulation places the smallest pre trend violation this test would detect 80 percent of the time at approximately 5 percent a year; a violation of 2 percent a year is detected 16 percent of the time. The plot is reported with the joint test and should not be read coefficient by coefficient.

## Further Reading

- Rambachan, A. and Roth, J. (2023). A more credible approach to parallel trends. *Review of Economic Studies*, 90.
- Roth, J. (2022). Pretest with caution: event study estimates after testing for parallel trends. *American Economic Review: Insights*, 4.
- Freyaldenhoven, S., Hansen, C., Pérez Pérez, J. and Shapiro, J. M. (2021). Visualization, identification, and estimation in the linear panel event study design. NBER Working Paper 29170.

---

| | |
|---|---|
| **Previous** | [Module 5: Two Way Fixed Effects Done Properly](Module_05_Two_Way_Fixed_Effects.md) |
| **Next** | [Module 7: Staggered Adoption and the Negative Weights Problem](Module_07_Staggered_Adoption.md) |
| **Builds on** | [Module 5](Module_05_Two_Way_Fixed_Effects.md), Intermediate [Module 7](../Intermediate/Module_07_Testing_Parallel_Trends.md) |
| **Used again in** | [Module 7](Module_07_Staggered_Adoption.md), [Module 14](Module_14_Sensitivity_And_Partial_Identification.md) |

*This module is part of a series developed for the Washington Data Exchange for Public Safety (WADEPS) through the Center for Interdisciplinary Statistical Education and Research (CISER) at Washington State University. Version 1.0, September 2026. Questions, errors, or suggestions: yin.zhang@wsu.edu*

*All examples use synthetic data created for teaching. They do not represent any real jurisdiction, agency, officer, or incident. See [Data/DATA_DICTIONARY.md](../../Data/DATA_DICTIONARY.md).*
