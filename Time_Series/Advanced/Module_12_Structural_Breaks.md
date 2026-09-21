# Module 12: Structural Breaks and Changepoints

> **Developed by Yin Zhang, PhD**, Assistant Professor, Department of Mathematics and Statistics, Washington State University

**The question this module answers:** *Did something change on a date nobody announced, and how is that tested without finding a break in every series?*

---

## The Question

[Module 11](Module_11_Interrupted_Time_Series.md) asked whether something changed on a date you were given. This module asks the harder question.

It happens constantly in public safety data. A records system is replaced, a category is redefined, a reporting requirement changes, a unit is disbanded. None of it appears in a data dictionary, and all of it breaks a trend.

The module also covers the mistake that searching for a date makes almost inevitable, and the arithmetic that fixes it.

## Model and Assumptions

> log(calls) = intercept + b1·time + seasonal + **b2·1[month ≥ k]**
>
> fitted at every candidate k, taking the largest test statistic

The first and last 15 percent of the series are excluded, because a break in the first few months is indistinguishable from a different intercept.

| Assumption | Diagnostic | Consequence of failing |
|---|---|---|
| The break is a level shift, not something else | inspect the series | a slope difference or an outlier reported as a break |
| The date was not chosen by looking | where did the date come from | the p value is wrong by an order of magnitude |
| The critical value accounts for the search | Andrews values, not chi square | see below |
| There is one break, not several | scan the subsamples too | a middling statistic at neither true date |
| The series has enough signal | width of the plausible date set | a confident date that is a coin flip |

## Estimation

```python
for k in range(int(0.15 * n), int(0.85 * n)):
    d = (np.arange(n) >= k).astype(float)
    r = sm.OLS(y, np.column_stack([X, d])).fit()
```

## Worked Example

Havenbrook changed how it classified calls in January 2023. Nobody records that anywhere in the data.

![Three panels. The left shows Havenbrook's total calls, public order offences and Other, with the total continuing smoothly across January 2023 while the two components cross. The middle plots the Wald statistic for a break at each candidate date on a log scale, with a sharp peak at 2023-01 for public order offences and a flat line near zero for the total, against two horizontal critical value lines. The right is a histogram of the largest Wald statistic found by searching in 400 series that contain no break at all](Figures/fig_a12_breaks.png)

### With the date known, and without it

A Chow test at 2023-01 gives a shift of **+51.3 percent**, F = 254.3, p = 1.1 × 10⁻¹⁶.

A scan over all 62 candidate dates finds **2023-01**, to the month. Then the same scan on the other two series:

| Series | Best date found | Wald | Shift |
|---|---|---|---|
| Public order offences | 2023-01 | **254.3** | +51.3% |
| Other | 2023-01 | **132.1** | −27.9% |
| **All calls, the total** | 2021-08 | **2.73** | −1.9% |

Two components break hard in the same month, in opposite directions, and the total shows nothing worth a second look. **A dashboard built on totals would never have seen this.**

### The mistake that searching makes

The scan tested 62 dates and reported the largest statistic. Comparing that maximum against the critical value for a **single** test is wrong, and it is wrong by a lot. Rather than assert it, simulate: 400 series with a trend, a season, noise and **no break anywhere**.

| The largest Wald found by searching | |
|---|---|
| Median | 4.6 |
| Exceeds 3.84, the chi square 5 percent value | **62% of the time** |
| Exceeds 8.85, the Andrews 5 percent value | 9% of the time |

**Sixty two percent.** Use the ordinary critical value after searching and you will find a significant break in most series that do not have one.

The correct reference distribution is the one for the **maximum** over candidate dates, tabulated by Andrews. For one shifting parameter with 15 percent trimming:

| Level | Critical value |
|---|---|
| 10 percent | 7.12 |
| 5 percent | **8.85** |
| 1 percent | 12.35 |

The simulation clears 8.85 about 9 percent of the time rather than 5, which is worth stating plainly: with 88 months and four nuisance parameters the asymptotic value is still a little optimistic. Against Havenbrook's 254 the distinction does not matter. Against a Wald of 9 it decides the answer.

### Three things that are not breaks

A level shift model, pointed at any series, always returns a best candidate date.

| Agency | What is actually there | Best date | Wald | Apparent shift | Verdict |
|---|---|---|---|---|---|
| Tarnbridge | one extreme month, June 2021 | 2023-11 | 6.06 | −22.9% | below 8.85 |
| Summit County | a steeper trend throughout | 2020-02 | 6.45 | +27.4% | below 8.85 |
| Lakeshore County | nothing planted at all | 2024-04 | 3.54 | +29.0% | below 8.85 |

An outlier is not a break. A different slope is not a level break. A clean series still produces a best candidate, here with an apparent shift of 29 percent.

Note Tarnbridge's best candidate: **2023-11**, the month the training was fully in place. The break is real and the test cannot see it, the same conclusion [Module 6](Module_06_Regression_With_ARMA_Errors.md) reached from a different direction.

### How certain is the date itself

Inverting the likelihood gives the set of dates the data cannot rule out. For Havenbrook's public order series it is **2023-01 to 2023-01**: a single month, because a 51 percent shift in a series this regular leaves no room for doubt.

**Do not expect that.** A 10 percent break in a noisy series routinely produces a plausible set spanning a year, and reporting the argmax as "the date the policy took effect" then overstates what you know. Report the set, not just the peak.

### A practical order of operations

| Step | Why |
|---|---|
| Ask the agency first | most breaks have a documented cause and a known date |
| Plot the components, not only the total | Havenbrook |
| Fix the date from outside the data if you can | it restores the ordinary critical value |
| If you search, use the searched critical value | 8.85, not 3.84 |
| Check that it is not one outlier | Tarnbridge |
| Check that it is not a slope difference | Summit County |
| Report the plausible date range | not just the argmax |
| Then decide what to do about it | split the series, add an indicator, or drop the affected span |

**A break you can explain is a data quality note. A break you cannot explain is a reason to call whoever maintains the records system, not a finding.**

## Recovering the Planted Answer

The generator moves 30 percent of Havenbrook's Other calls into Public Order Offense from January 2023, and changes nothing else.

The scan finds 2023-01 in both affected categories and nothing in the total. The plausible date set is one month wide. The three unaffected agencies tested return no significant break, and the three planted non breaks are all correctly rejected.

## Diagnostics

| Check | Acceptable |
|---|---|
| Critical value | matched to whether the date was searched for |
| Components as well as totals | both scanned |
| One outlier removed, then rescan | the break survives |
| A slope difference allowed for | the level break survives |
| Plausible date set | reported |
| Explanation | sought from the agency before anything is published |

## Do It Yourself

> 📓 **Notebook:** [Module_12_Structural_Breaks.ipynb](Notebooks/Module_12_Structural_Breaks.ipynb)
> [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/OWNER/REPO/blob/main/Time_Series/Advanced/Notebooks/Module_12_Structural_Breaks.ipynb)
> About 35 minutes.

The exercise repeats the scan on category shares rather than counts, and finds the reason not to.

## When Not To Use This

| Situation | Reach for |
|---|---|
| The date is known and documented | [Module 11](Module_11_Interrupted_Time_Series.md), with the ordinary critical value |
| The change is gradual, not a step | [Module 13](Module_13_Intervention_Analysis.md) |
| Several breaks are plausible | Bai and Perron's sequential procedure, cited below |
| The series is short | do not scan; 88 months is already near the floor |
| The break needs to be explained, not just found | the agency's records staff |

## Reporting the Result

> Havenbrook's monthly calls for service were tested for an unannounced level shift by fitting a break at every candidate month between March 2020 and February 2025 and taking the largest Wald statistic, compared against Andrews critical values for a searched break date. Public order offences shift by 51.3 percent at January 2023, Wald 254.3 against a 1 percent critical value of 12.35, and Other shifts by 27.9 percent in the opposite direction at the same date. Total calls for service show no break, the largest candidate statistic being 2.73. The pattern is consistent with a reclassification rather than a change in underlying activity. Comparisons of Havenbrook's public order category across January 2023 compare two different definitions and should not be made without adjustment.

## Further Reading

- Andrews, D. W. K. (1993). Tests for parameter instability and structural change with unknown change point. *Econometrica*, 61. The critical values used here.
- Bai, J. and Perron, P. (2003). Computation and analysis of multiple structural change models. *Journal of Applied Econometrics*, 18.
- Zeileis, A. et al. (2003). Testing and dating of structural changes in practice. *Computational Statistics and Data Analysis*, 44.

---

| | |
|---|---|
| **Previous** | [Module 11: Interrupted Time Series Done Properly](Module_11_Interrupted_Time_Series.md) |
| **Next** | [Module 13: Intervention Analysis and Transfer Functions](Module_13_Intervention_Analysis.md) |
| **Builds on** | [Module 10](Module_10_Panel_And_Hierarchical.md), [Module 11](Module_11_Interrupted_Time_Series.md), [Beginner Topic 19](../Beginner/Topic_19_Data_Quality_And_Pitfalls.md) |
| **Used again in** | [Module 14](Module_14_Reporting_And_Reproducibility.md) |

*This module is part of a series developed for the Washington Data Exchange for Public Safety (WADEPS) through the Center for Interdisciplinary Statistical Education and Research (CISER) at Washington State University. Version 1.0, September 2026. Questions, errors, or suggestions: yin.zhang@wsu.edu*

*All examples use synthetic data created for teaching. They do not represent any real jurisdiction, agency, officer, or incident. See [Data/DATA_DICTIONARY.md](../../Data/DATA_DICTIONARY.md).*
