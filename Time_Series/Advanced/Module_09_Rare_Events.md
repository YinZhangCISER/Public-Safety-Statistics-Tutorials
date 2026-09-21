# Module 9: Rare Events, Zero Inflation and When to Aggregate Up

> **Developed by Yin Zhang, PhD**, Assistant Professor, Department of Mathematics and Statistics, Washington State University

**The question this module answers:** *Half the months are zero. Is that zero inflation, and if not, what is the actual problem?*

---

## The Question

Orrindale Police Department has eight sworn officers and averages under one use of force incident a month. Forty three percent of its months are zero.

The reflex is to reach for a zero inflated model. This module checks whether that reflex is right, finds that it is not, and then takes up the problem that actually exists at an agency this size, which turns out not to be a modelling problem at all.

Small agencies are not a corner case in WADEPS. Most of Washington's three hundred agencies are closer to Orrindale than to Seattle, and most published comparisons quietly assume otherwise.

## Model and Assumptions

A zero inflated model is a mixture:

> with probability p, the month is **structurally** incapable of producing an incident
>
> with probability 1 − p, the month produces a Poisson count, which may itself be zero

**The first line is a claim about the world.** It needs a mechanism: a facility closed, a programme not yet running, a category not collected. It is not something a histogram can establish.

| Assumption | Diagnostic | Consequence of failing |
|---|---|---|
| There is a structural zero mechanism | name it, in words, before fitting | a spurious inflation probability and an uninterpretable model |
| Excess zeros exist at all | observed zero share against the Poisson prediction | fitting a parameter that is not identified |
| The upper tail is not also heavy | variance to mean ratio | zero inflation treats one tail and leaves the other |
| The series carries enough information | the smallest detectable effect | a confident report of no change, from a series that could not have shown one |

## Estimation

```python
print(f"observed {100*(y==0).mean():.1f}%   a Poisson with this mean gives {100*np.exp(-y.mean()):.1f}%")
```

That line, run before anything is fitted, resolves most cases.

## Worked Example

![Three panels. The first compares Orrindale's observed distribution of monthly counts with a plain Poisson of the same mean, and the two match closely including at zero. The second shows observed against Poisson predicted zero shares for five agencies, matching everywhere except Kelsmoor. The third plots the smallest detectable annual trend against agency size on log scales, with a horizontal line at the 4.9 percent decline that is actually present, above which sit Orrindale, Dunmoor and Kelsmoor](Figures/fig_a09_rare_events.png)

### The check that resolves it

| Incidents in a month | Observed | Poisson, mean 0.807 |
|---|---|---|
| 0 | **43.2%** | **44.6%** |
| 1 | 37.5% | 36.0% |
| 2 | 15.9% | 14.5% |
| 3 | 2.3% | 3.9% |
| 4 | 1.1% | 0.8% |

**Forty three observed against forty five predicted.** There is no excess of zeros to explain, and the variance to mean ratio is 0.94.

Fitting the zero inflated model anyway confirms it. AIC is 211.0 either way, the inflation coefficient runs off to −15.14 with a p value of 0.990, and the optimiser emits a ConvergenceWarning. **The warning is not a nuisance to be silenced. It is the answer:** the inflation probability is zero and the parameter is not identified.

Orrindale's officers were on duty in every one of those 38 months and nobody used force. That is a small Poisson mean, not a separate process.

### The problem that is actually there

A series averaging 0.8 a month carries almost no information about a trend. Every agency in this dataset is declining at **4.9 percent a year**.

| Agency | Incidents a month | Smallest detectable annual trend |
|---|---|---|
| Orrindale | 0.81 | **11.7%** |
| Dunmoor | 0.80 | **11.9%** |
| Kelsmoor | 2.78 | **6.1%** |
| Pinecrest | 3.61 | 5.3% |
| Prairie County | 2.84 | 6.1% |
| Millgate | 7.55 | 3.7% |
| Havenbrook | 12.25 | 2.9% |
| Stonewick | 57.65 | 1.3% |
| Ashfell | 99.84 | 1.0% |

Stonewick detects the decline comfortably. **Orrindale cannot distinguish anything smaller than 11.7 percent a year, so the real decline is invisible to it, and no choice of model changes that.** The information is not in the series.

This is four lines of code and the most useful number to compute before promising an agency an analysis.

### Aggregating up

| Window | Periods | Mean | Months at zero |
|---|---|---|---|
| Monthly | 88 | 0.81 | 43.2% |
| Quarterly | 30 | 2.37 | 6.7% |
| Annual | 8 | 8.88 | 0.0% |

Pooling Orrindale and Dunmoor together brings the detection threshold from 11.7 percent down to 8.2, and the real decline of 4.9 percent is still below it. **Two small agencies together are still small.** The genuine fix is [Module 10](Module_10_Panel_And_Hierarchical.md): put all twelve in one model and estimate the common structure from all of them.

### What to report for an agency this size

| Do | Do not |
|---|---|
| Report counts, and the period they cover | report a rate per 100 arrests for a single month |
| Give an interval, always | give a point estimate for a month with one incident |
| State what the series cannot detect | say "no significant change" and stop |
| Aggregate to a year, and say so | quietly change the window when the answer is inconvenient |
| Compare against a pooled peer group | rank three hundred agencies by a monthly rate |

The most important line in a small agency report is the one stating what could not have been seen. Without it, "no change was detected" reads as evidence of no change.

## Recovering the Planted Answer

The dataset deliberately includes **two agencies too small to analyse alone**, A006 and A011, so that "this agency's rate tripled" can be shown to mean "it went from one incident to three".

Both come back with 43.2 percent zeros, both match a plain Poisson at every count, and both have detection thresholds more than twice the decline that is genuinely present in their data. The planted lesson is recovered exactly: **the limitation is the agency's size, not the analyst's model.**

## Diagnostics

| Check | Acceptable |
|---|---|
| Observed zero share against the Poisson prediction | within a couple of points, or a named mechanism for the gap |
| Variance to mean ratio | near 1; well above 1 means the upper tail, not the lower |
| Inflation coefficient, if a zero inflated model is fitted | identified, with a sensible standard error |
| Smallest detectable effect | computed and reported, always |
| Aggregation window | fixed before looking at results |

## Do It Yourself

> 📓 **Notebook:** [Module_09_Rare_Events.ipynb](Notebooks/Module_09_Rare_Events.ipynb)
> [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/OWNER/REPO/blob/main/Time_Series/Advanced/Notebooks/Module_09_Rare_Events.ipynb)
> About 30 minutes.

The exercise takes Kelsmoor, the one agency here with more zeros than a Poisson predicts, and works out what the excess really is.

## When Not To Use This

| Situation | Reach for |
|---|---|
| A real structural zero mechanism exists | a zero inflated or hurdle model, and say what the mechanism is |
| Excess at both tails | a negative binomial, [Module 8](Module_08_Count_Regression_With_Harmonics.md) |
| Several small agencies with a shared question | [Module 10](Module_10_Panel_And_Hierarchical.md) |
| A rate needs a denominator the agency did not submit | Intermediate [Module 12](../Intermediate/Module_12_Building_A_Peer_Benchmark_Series.md) |
| Ranking small agencies against each other | do not; use a funnel plot, Intermediate [Module 12](../Intermediate/Module_12_Building_A_Peer_Benchmark_Series.md) |

## Reporting the Result

> Orrindale averages 0.81 use of force incidents a month, and 43.2 percent of months are zero. A Poisson distribution with this mean places 44.6 percent of its mass at zero, so the zero share is what the count distribution predicts and no zero inflation component is warranted; a zero inflated Poisson fitted for comparison does not improve AIC and its inflation parameter is not identified. Over the 88 months observed, the smallest annual trend this series could distinguish from zero is 11.7 percent. The statewide decline over the same period is approximately 4.9 percent a year, which this agency's data could not detect. No conclusion about Orrindale's trend should be drawn from its own series alone.

## Further Reading

- Cameron, A. C. and Trivedi, P. K. (2013). *Regression Analysis of Count Data*, 2nd edition. Cambridge University Press. Chapter 4 on zero inflated and hurdle models.
- Wilson, P. (2015). The misuse of the Vuong test for non nested models to test for zero inflation. *Economics Letters*, 127.
- Spiegelhalter, D. (2005). Funnel plots for comparing institutional performance. *Statistics in Medicine*, 24.

---

| | |
|---|---|
| **Previous** | [Module 8: Poisson and Negative Binomial Regression with Harmonic Seasonality](Module_08_Count_Regression_With_Harmonics.md) |
| **Next** | [Module 10: Panel and Hierarchical Time Series](Module_10_Panel_And_Hierarchical.md) |
| **Builds on** | [Module 2](Module_02_Counts_Are_Not_Gaussian.md), [Module 8](Module_08_Count_Regression_With_Harmonics.md), [Intermediate Module 4](../Intermediate/Module_04_Why_Small_Agencies_Look_Volatile.md) |
| **Used again in** | [Module 10](Module_10_Panel_And_Hierarchical.md), [Module 14](Module_14_Reporting_And_Reproducibility.md) |

*This module is part of a series developed for the Washington Data Exchange for Public Safety (WADEPS) through the Center for Interdisciplinary Statistical Education and Research (CISER) at Washington State University. Version 1.0, September 2026. Questions, errors, or suggestions: yin.zhang@wsu.edu*

*All examples use synthetic data created for teaching. They do not represent any real jurisdiction, agency, officer, or incident. See [Data/DATA_DICTIONARY.md](../../Data/DATA_DICTIONARY.md).*
