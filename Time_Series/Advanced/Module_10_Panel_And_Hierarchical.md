# Module 10: Panel and Hierarchical Time Series

> **Developed by Yin Zhang, PhD**, Assistant Professor, Department of Mathematics and Statistics, Washington State University

**The question this module answers:** *How do you estimate one effect from three hundred agencies at once, and keep the published numbers adding up?*

---

## The Question

Every module so far has fitted one series at a time. A public safety dataset is not one series. WADEPS holds roughly three hundred agencies, each with its own level, its own reporting habits, and the same statewide conditions acting on all of them.

Two things become possible once the series are modelled together. A common effect can be estimated far more precisely than any single agency can manage, and a set of published numbers can be kept internally consistent.

## Model and Assumptions

> log(mu) = log(arrests) + agency effect + month effect + b·intervention

**`C(agency_id)`** gives every agency its own baseline rate. **`C(year_month)`** gives every month its own level, shared across agencies, which absorbs the statewide trend and the season without assuming a shape for either.

| Assumption | Diagnostic | Consequence of failing |
|---|---|---|
| Agencies differ in level, not in slope | pre period trend comparison | the intervention coefficient absorbs a private trend |
| Common shocks hit all agencies alike | month effects present and estimated | the trend leaks into the treatment indicator |
| The treatment date is right | phase in and settled periods modelled separately | the effect is diluted across the transition |
| Errors are not correlated within agency | clustered standard errors, with enough clusters | intervals too narrow |
| The parts of a hierarchy are consistent | do the forecast components sum to the total | a published table that contradicts itself |

## Estimation

```python
smf.glm("n_uof ~ C(agency_id) + C(year_month) + settled + phasein",
        data, family=sm.families.Poisson(), offset=data["lo"]).fit()
```

## Worked Example

The de escalation training, adopted by five agencies in July 2023 and fully in place from November. The true effect built into the data is a **12 percent reduction**.

![Two panels. The left is a forest plot of the estimated effect at four agencies separately and then pooled: the four separate estimates span eleven percentage points with wide intervals, while the pooled estimate sits on the true value with a much narrower interval. The right compares four model specifications, showing the estimate landing on the truth only when both agency and month fixed effects are present, and reporting each specification's phase in coefficient underneath](Figures/fig_a10_panel.png)

### One agency at a time throws information away

| Agency | Estimate | 95 percent interval |
|---|---|---|
| Stonewick | −9.3% | [−15.8, −2.4] |
| Tarnbridge | −17.2% | [−25.1, −8.5] |
| Millgate | −15.4% | [−29.2, +0.9] |
| Pinecrest | −20.6% | [−38.5, +2.3] |
| **All four pooled** | **−12.6%** | **[−17.9, −6.9]** |

Four estimates of one number, spanning eleven percentage points, from agencies where the planted effect is **identical**. The entire spread is noise. Pooled, the estimate lands within 0.6 points of the truth with an interval narrower than any of the four.

### What each set of fixed effects is doing

| Specification | Settled effect | Interval | Phase in | Dispersion |
|---|---|---|---|---|
| Neither set of fixed effects | −8.8% | [−12.7, −4.8] | **+15.2%** | 2.25 |
| Agency effects only | **−29.5%** | [−32.9, −26.1] | −11.0% | 1.74 |
| **Agency and month effects** | **−12.6%** | [−17.9, −6.9] | −9.4% | 1.12 |
| Agency and month, A007 left in | −17.0% | [−21.8, −11.8] | −10.5% | 1.17 |

Read the table from the right.

**The phase in column is the tell.** The first specification reports that the programme *raised* the use of force rate by 15.2 percent during the months it was being introduced, and then cut it. That is not a finding, it is a symptom. With no month effects the common secular decline has nowhere to go, and the two programme indicators absorb pieces of it in opposite directions.

This is the same lesson as the exposure coefficient in [Module 6](Module_06_Regression_With_ARMA_Errors.md): **the coefficient you were not interested in is the one that tells you the model is wrong.**

Now read the settled column. **Agency effects alone give 29.5 percent, more than twice the truth and worse than using no fixed effects at all.** Removing level differences without removing the common time path leaves the settled indicator standing in for four years of statewide decline. Half a job is worse than none.

### Partial pooling, and a result worth reading carefully

| Quantity | Value |
|---|---|
| Spread of the four separate estimates | 0.00309 |
| Spread expected from sampling noise alone | 0.00725 |
| What is left for real differences between agencies | **0.00000** |

The four estimates vary **less** than pure noise would predict, so the between agency variance is estimated at zero and every agency shrinks all the way to the common value of −12.6 percent.

That is the correct answer here: the effect really was identical at all five agencies. But note what the procedure did not do. **It did not prove the effects are the same.** It reported that four noisy estimates give no evidence they differ, and with four agencies only a very large difference would have been visible. Full shrinkage is not homogeneity established.

### Standard errors in a panel

| Standard errors | se | Interval |
|---|---|---|
| Model based | 0.0321 | [−17.9, −6.9] |
| Clustered by agency | 0.0320 | [−17.9, −6.9] |

They agree to four decimal places, which is worth understanding rather than celebrating. The month fixed effects have already absorbed the shocks common to all agencies, which is the main thing clustering protects against.

**Note the cluster count: eleven.** That is far below the forty or so at which cluster robust standard errors become reliable, and with a handful of clusters they are known to be too small. Nothing turns on it here, but in a study with a dozen agencies clustering is not the safeguard it is usually taken for.

### Making the parts sum to the whole

Agencies are one hierarchy. Incident categories are another: eight types that add up to total calls for service. Forecast the pieces independently and they do not add up.

| | First forecast month |
|---|---|
| Forecast of the total | 21,588 calls |
| The eight parts added up | 21,659 calls |
| Disagreement | **71 calls** |

Across twelve months the gap averages 0.85 percent and reaches 2.23. Nobody chose this. Eight sensible forecasts and one sensible forecast of their total simply do not agree, and a reader with a calculator will find it.

**Reconciliation** adjusts every forecast by the smallest amount that makes them coherent.

| Approach | MAE on the total | Mean MAE across the eight parts |
|---|---|---|
| Top down, forecast the total | **291.3** | |
| Bottom up, add the eight parts | 346.7 | 132.7 |
| Reconciled | 291.8 | **132.5** |

**Reconciliation bought coherence, not accuracy.** That is the honest result and it is the usual one on data like this. Coherence is still worth having: it is a requirement of any published table, and it is free.

### The reason to model the hierarchy, not just the total

Havenbrook changed how it classified calls in January 2023.

| Incident type | Before 2023 | From 2023 | Change |
|---|---|---|---|
| Civil Caretaking | 912 | 970 | +6.4% |
| Offense Against Person | 271 | 283 | +4.3% |
| **Other** | 1,115 | 823 | **−26.2%** |
| Pedestrian Stop | 121 | 127 | +4.6% |
| Property Offense | 447 | 483 | +8.2% |
| **Public Order Offense** | 635 | 1,018 | **+60.2%** |
| Vehicle Stop | 866 | 924 | +6.7% |
| Warrant | 85 | 91 | +6.8% |
| **TOTAL** | **4,452** | **4,718** | **+6.0%** |

The total grew 6.0 percent, unremarkable next to the 4 to 8 percent most categories grew. **Nothing in the aggregate suggests anything happened.** Inside it, one category rose 60 percent and another fell 26. It is a reclassification, and it is invisible in the series most dashboards display.

## Recovering the Planted Answer

The dataset's answer key states that a difference in differences estimate **recovers the 12 percent when A007 is excluded**, and that keeping A007 in biases the estimate away from the truth.

Both hold. The correct specification returns **−12.6 percent** with an interval covering the truth; keeping A007 moves it to −17.0 percent with an interval that excludes 12.

A007's reason is visible in the pre period: it was already declining at **11.96 percent a year** against 5.17 for the other treated agencies and 4.46 for the controls, and its interval does not come close to overlapping. **No amount of fixed effects fixes this.** Agency effects remove level differences, month effects remove common time movements, and neither removes an agency specific slope.

## Diagnostics

| Check | Acceptable |
|---|---|
| Month fixed effects present | always, in a panel with a common trend |
| Every coefficient, including the ones you did not want | none of them implausible |
| Pre period trends, treated against control | overlapping intervals |
| Number of clusters, if clustering | forty or more, or say why you clustered anyway |
| Hierarchy components | sum to the total, exactly |
| Dispersion after fixed effects | near 1, or a stated reason |

## Do It Yourself

> 📓 **Notebook:** [Module_10_Panel_And_Hierarchical.ipynb](Notebooks/Module_10_Panel_And_Hierarchical.ipynb)
> [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/YinZhangCISER/Public-Safety-Statistics-Tutorials/blob/main/Time_Series/Advanced/Notebooks/Module_10_Panel_And_Hierarchical.ipynb)
> About 40 minutes.

The exercise finds out why A007 has to come out, by comparing pre programme trends.

## When Not To Use This

This module estimates a **well specified association across agencies**. It still is not a causal estimate.

| What is missing | Where it is handled |
|---|---|
| A level change separated from a slope change | [Module 11](Module_11_Interrupted_Time_Series.md) |
| A break whose date nobody told you | [Module 12](Module_12_Structural_Breaks.md) |
| The shape of a response over time | [Module 13](Module_13_Intervention_Analysis.md) |
| An argument that the comparison agencies are a valid counterfactual | the [Causal Inference series](../../Causal_Inference/) |
| Agencies that select into treatment on the outcome | the [Causal Inference series](../../Causal_Inference/) |

## Reporting the Result

> Monthly use of force counts for eleven agencies over 88 months were modelled with a Poisson regression including agency and calendar month fixed effects, the log of arrests as an offset, and separate indicators for the programme's phase in and settled periods. One agency was excluded for a pre programme trend that differs significantly from the comparison group, and one documented month of civil unrest was excluded. Over the settled period the treated agencies' use of force rate ran 12.6 percent below the comparison agencies, 95 percent interval from 17.9 to 6.9 percent below. Estimates from each treated agency separately range from 9.3 to 20.6 percent and are consistent with a single common effect; the between agency variance is estimated at zero. Cluster robust standard errors by agency are indistinguishable from the model based errors, though with eleven clusters they would not be reliable if they differed.

## Further Reading

- Angrist, J. D. and Pischke, J. S. (2009). *Mostly Harmless Econometrics*. Princeton University Press. Chapter 5 on panel data and chapter 8 on clustering.
- Cameron, A. C. and Miller, D. L. (2015). A practitioner's guide to cluster robust inference. *Journal of Human Resources*, 50.
- Gelman, A. and Hill, J. (2007). *Data Analysis Using Regression and Multilevel Hierarchical Models*. Cambridge University Press. Chapters 12 and 13.
- Wickramasuriya, S. L., Athanasopoulos, G. and Hyndman, R. J. (2019). Optimal forecast reconciliation for hierarchical and grouped time series. *Journal of the American Statistical Association*, 114.

---

| | |
|---|---|
| **Previous** | [Module 9: Rare Events, Zero Inflation and When to Aggregate Up](Module_09_Rare_Events.md) |
| **Next** | [Module 11: Interrupted Time Series Done Properly](Module_11_Interrupted_Time_Series.md) |
| **Builds on** | [Module 8](Module_08_Count_Regression_With_Harmonics.md), [Module 9](Module_09_Rare_Events.md), [Intermediate Module 12](../Intermediate/Module_12_Building_A_Peer_Benchmark_Series.md) |
| **Used again in** | [Module 11](Module_11_Interrupted_Time_Series.md), [Module 12](Module_12_Structural_Breaks.md), [Module 13](Module_13_Intervention_Analysis.md) |

*This module is part of a series developed for the Washington Data Exchange for Public Safety (WADEPS) through the Center for Interdisciplinary Statistical Education and Research (CISER) at Washington State University. Version 1.0, September 2026. Questions, errors, or suggestions: yin.zhang@wsu.edu*

*All examples use synthetic data created for teaching. They do not represent any real jurisdiction, agency, officer, or incident. See [Data/DATA_DICTIONARY.md](../../Data/DATA_DICTIONARY.md).*
