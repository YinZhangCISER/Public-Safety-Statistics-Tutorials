# Module 15: How Wrong Is the Forecast?

> **Developed by Yin Zhang, PhD**, Assistant Professor, Department of Mathematics and Statistics, Washington State University

**The question this module answers:** *Which error measure, how many test periods, and does the prediction interval mean what it says?*

---

## The Question

Every forecast comes with an error number. The most widely used one is the worst choice for public safety data, most evaluations use a single test period that flatters the model, and almost nobody checks whether the prediction interval covers what it claims to.

All three are fixable and none of the fixes is difficult.

## The Idea in Plain Language

| Measure | What it is | Units | Reads well when |
|---|---|---|---|
| **MAE** | average absolute error | incidents | you want a number people understand |
| **RMSE** | square root of the average squared error | incidents | large misses matter more than small ones |
| **MAPE** | average absolute error as a percent of the actual | percent | actuals are comfortably above zero |
| **MASE** | MAE divided by what a naive forecast would get | a ratio | comparing across series of different sizes |

**Default to MAE for people and MASE for comparison.** MASE below 1 means better than the naive benchmark, above 1 means worse, and it is comparable across agencies of any size, which none of the others are.

## The Method

```python
naive_scale = np.mean(np.abs(train.values[12:] - train.values[:-12]))
mase = np.mean(np.abs(actual - pred)) / naive_scale
```

Then score at **several** origins rather than one, and check interval coverage.

## Worked Example

### Why MAPE fails on public safety data

**It cannot be computed when the actual is zero.** Orrindale's 2025 ran 0, 1, 1, 0, 0, 1, 1, 0, 3, 1, 1, 0. Five months are zero.

| Measure | Value |
|---|---|
| MAE | **0.69** |
| MASE | **0.67** |
| MAPE | **undefined** |

MAE and MASE report perfectly usable numbers. MAPE reports infinity, and software that silently drops the zero months instead reports a figure computed from whichever seven months happened not to be zero.

**It is also asymmetric.** The actual sits in the denominator, so the same absolute miss is scored differently depending on which way it went.

| Actual | Forecast | Absolute error | APE |
|---|---|---|---|
| 5 | 10 | 5 | **100%** |
| 15 | 10 | 5 | **33%** |
| 10 | 5 | 5 | 50% |
| 10 | 15 | 5 | 50% |

Every row is a miss of five incidents. A method that over forecasts quiet months is punished hardest, which is the opposite of what a public safety user usually wants: **under forecasting a busy month is the more costly error.**

### One holdout is one number

![Two panels. The left panel plots average error over the following twelve months at six different training cut off dates, for Holt Winters and for the seasonal naive baseline, with the usual holdout marked as the lowest point. The right panel shows Orrindale's 2025 absolute errors alongside absolute percentage errors, five of which are marked undefined](Figures/fig_m15_measuring_error.png)

| Training ends | Months of training | Holt Winters | Same month last year |
|---|---|---|---|
| `2022-12` | 48 | **15.8** | **14.2** |
| `2023-06` | 54 | 14.1 | 17.0 |
| `2023-12` | 60 | 12.2 | 17.4 |
| `2024-06` | 66 | 11.6 | 16.5 |
| **`2024-12`** | 72 | **9.6** | 15.9 |
| `2025-04` | 76 | 12.1 | 14.9 |

Two findings, neither visible from a single split.

**The usual holdout is the most flattering one.** Ending at December 2024 gives the lowest error of all six. [Module 14](Module_14_Exponential_Smoothing.md) reported 9.6; the average across origins is **12.6**. Reporting the single figure overstates the method by a quarter.

**With four years of data the model loses to the baseline.** At the first origin Holt Winters is worse than using last year's same month. Its advantage appears only once there are five or six years to estimate the seasonal shape from. **A method is not good or bad on its own; it is good or bad given how much data you have.**

### Does the interval mean what it says?

Pooled across five origins, 95 percent intervals covered the truth in about **92 percent** of months. Close to nominal, slightly under, which is the usual direction: the interval is built from fitted residuals and treats the estimated parameters as though they were known exactly.

**Reporting an interval without ever checking its coverage is a claim nobody has tested.**

## Do It Yourself

> 📓 **Notebook:** [Module_15_Measuring_Forecast_Error.ipynb](Notebooks/Module_15_Measuring_Forecast_Error.ipynb)
> [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/OWNER/REPO/blob/main/Time_Series/Intermediate/Notebooks/Module_15_Measuring_Forecast_Error.ipynb)
> About 20 minutes.

The notebook implements all four measures, demonstrates both MAPE failures, builds the rolling origin table, checks coverage, and ends with a reusable `rolling_origin` function plus an exercise on Tarnbridge.

## Pitfalls

| What goes wrong | What it looks like | What to do |
|---|---|---|
| MAPE on count data | infinity, or a number silently computed from a subset | use MAE and MASE |
| One holdout | a flattering number that will not repeat | score at several origins, report the range |
| No baseline in the table | the reader cannot judge whether the model earned its keep | always score the baseline alongside |
| Comparing MAE across agencies | a large agency always looks worse | MASE is scale free, MAE is not |
| Assuming interval coverage | a 95 percent interval that covers 70 | measure it |
| Tuning on the test period | an error estimate that is no longer honest | hold out a period you never look at |
| Averaging errors across horizons | a one month ahead error hidden inside a twelve month average | report by horizon when the horizon matters |

## Check Your Understanding

<details>
<summary><b>1.</b> A dashboard reports MAPE by agency. The smallest agency shows the worst MAPE by a wide margin. What has happened?</summary>

Almost certainly nothing about that agency's forecastability. MAPE divides by the actual, so months with small actuals produce enormous percentages, and the smallest agency has the smallest actuals. If any month is zero the figure is undefined and has probably been dropped silently. Replace it with MASE, which divides by what a naive forecast would have achieved on that same series and is therefore comparable across sizes.
</details>

<details>
<summary><b>2.</b> Holt Winters scores 9.6 at one origin and 15.8 at another. Which number should the report give?</summary>

Both, and the range. The single best number is not a property of the method, it is a property of that starting point. An honest report gives the average across origins, here about 12.6, states the range from 9.6 to 15.8, and gives the baseline alongside at each origin. Quoting 9.6 alone is selecting the most favourable result from a set that was all computed.
</details>

<details>
<summary><b>3.</b> At 48 months of training data the model loses to the baseline, and at 72 it wins by 40 percent. What should an agency with four years of data conclude?</summary>

That it should use the baseline for now and revisit in a year or two. The result is not that Holt Winters is a poor method; it is that the method needs enough history to estimate a seasonal shape, and four years does not provide it. This is a common and underappreciated situation: the right model depends on the data available, and the honest answer for a young dataset is often the simple rule. WADEPS is itself a young dataset, which makes the point practical rather than academic.
</details>

## Key Takeaway

Use MAE for readers and MASE for comparison, never MAPE on counts. Score at several origins and report the range. Then check that your intervals cover what they claim.

---

| | |
|---|---|
| **Previous** | [Module 14: Exponential Smoothing in Plain Language](Module_14_Exponential_Smoothing.md) |
| **Next** | [Module 16: Did Something Change?](Module_16_Did_Something_Change.md) |
| **Builds on** | [Module 13](Module_13_Baseline_Forecasts.md), [Module 14](Module_14_Exponential_Smoothing.md) |
| **Used again in** | [Module 16](Module_16_Did_Something_Change.md), and Advanced Module 3 |

*This module is part of a series developed for the Washington Data Exchange for Public Safety (WADEPS) through the Center for Interdisciplinary Statistical Education and Research (CISER) at Washington State University. Version 1.0, September 2026. Questions, errors, or suggestions: yin.zhang@wsu.edu*

*All examples use synthetic data created for teaching. They do not represent any real jurisdiction, agency, officer, or incident. See [Data/DATA_DICTIONARY.md](../../Data/DATA_DICTIONARY.md).*
