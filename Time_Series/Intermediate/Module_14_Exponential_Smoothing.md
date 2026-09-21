# Module 14: Exponential Smoothing in Plain Language

> **Developed by Yin Zhang, PhD**, Assistant Professor, Department of Mathematics and Statistics, Washington State University

**The question this module answers:** *What is the simplest thing that is actually a model, and does it beat the baseline?*

---

## The Question

[Module 13](Module_13_Baseline_Forecasts.md) set the bar at 15.6 incidents a month for Grandview. This module clears it with the simplest method that deserves to be called a model, and one that can still be explained in a meeting.

## The Idea in Plain Language

Keep a running estimate of three things and update all three every month, weighting recent observations more than old ones.

| What it tracks | Parameter | What the parameter decides |
|---|---|---|
| **Level**, where the series is now | alpha | how fast the model accepts that the level has moved |
| **Trend**, how fast it is moving | beta | how fast it accepts a change in direction |
| **Season**, what each month does | gamma | how fast it accepts a change in the seasonal shape |

Each runs from 0 to 1. Near 0 the model is stubborn and ignores new data. Near 1 it is jumpy and chases every month.

## The Method

```python
hw = ExponentialSmoothing(train, trend="add", seasonal="add",
                          seasonal_periods=12,
                          initialization_method="estimated").fit()
pred = hw.forecast(12)
```

Then **look at the parameters it chose**. They are the most informative output the model produces, and almost nobody reads them.

## Worked Example

Grandview, trained through December 2024, forecasting 2025.

![Two panels. The left panel shows the series with the Holt Winters forecast, its interval, and the seasonal naive baseline for comparison. The right panel shows a series that steps from 50 to 80, with three smoothing curves at alpha 0.1, 0.35 and 0.8 responding at very different speeds](Figures/fig_m14_exponential_smoothing.png)

### It clears the bar

| Method | Average error, 2025 |
|---|---|
| **Holt Winters** | **9.6** |
| Same month last year | 15.9 |

A **40 percent** improvement over the free answer. That is the sort of margin that justifies maintaining a model.

### The parameters are the finding

Fitted on Grandview, the optimiser chose

> alpha **0.000**, beta **0.000**, gamma **0.000**

All three at zero, and that is a result rather than a failure. A smoothing parameter of zero means the model looked at the data and concluded that recent months carry **no extra information** about the level, the trend or the seasonal shape. Everything is estimated once, from the whole training period, and never revised. In effect it has fitted a straight trend with a fixed set of monthly factors.

For Grandview that is believable: the level drifts smoothly and the seasonal pattern is stable, so a month that came in high is noise rather than news.

**It also explains the improvement.** Seasonal naive estimates the seasonal pattern from **one** year. This model estimates it from **six**. The gain comes from using more data, not from being adaptive.

A series whose level genuinely shifts would produce a large alpha instead. The parameters are the first place to look when a forecast behaves unexpectedly.

### Additive or multiplicative

| Variant | Average error |
|---|---|
| Additive trend, additive season | 9.60 |
| Additive trend, multiplicative season | 9.77 |
| No trend, additive season | 9.84 |

Within a fifth of an incident of each other here, so the choice barely matters for this agency. Do not read that as general: it holds because Grandview's level fell only about a quarter over the training period. Fit both and compare, every time. Taking logs first is a third option, and it keeps the forecast from going negative, which matters for small agencies.

### The interval, and whether it holds

The interval is built from the spread of the model's own one step errors on the training data, so it assumes the estimated parameters are correct. It is a **lower bound** on the real uncertainty.

Checked against 2025, **11 of 12** months fell inside the nominal 95 percent interval. Close to advertised, slightly under, which is the usual direction.

## Do It Yourself

> 📓 **Notebook:** [Module_14_Exponential_Smoothing.ipynb](Notebooks/Module_14_Exponential_Smoothing.ipynb)
> [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/OWNER/REPO/blob/main/Time_Series/Intermediate/Notebooks/Module_14_Exponential_Smoothing.ipynb)
> About 20 minutes.

The notebook fits the model, reads out the parameters, compares three variants, checks interval coverage, and ends with an exercise on what the Cedar Falls unrest month does to the estimated June seasonal component.

## Pitfalls

| What goes wrong | What it looks like | What to do |
|---|---|---|
| Never reading the parameters | a model whose behaviour nobody can explain | print alpha, beta and gamma and interpret them |
| Additive season on a series whose level moved a lot | the seasonal swing too small at one end | fit multiplicative too, or take logs |
| Fewer than four years of data | an unstable seasonal estimate | it needs several full cycles |
| Negative forecasts | a small agency predicted to record fewer than zero | fit on logs, or use a count model |
| Trusting the interval | coverage well under nominal, discovered too late | check it, as in [Module 15](Module_15_Measuring_Forecast_Error.md) |
| Forecasting across a known intervention | the model predicts a world that no longer exists | stop the forecast at the intervention, or model it |
| Letting an outlier into the seasonal estimate | one event baked into every future July | handle documented events first |

## Check Your Understanding

<details>
<summary><b>1.</b> The fitted alpha is 0. Has the model failed to converge?</summary>

No. Zero is a legitimate estimate and it carries information: the data says that a high month is not evidence the level has moved, so the model should not chase it. The estimate is then made once from the whole training period. You should be suspicious in the other direction: an alpha near 1 means the model is essentially repeating the last observation, and at that point the seasonal naive baseline is doing the same job for free.
</details>

<details>
<summary><b>2.</b> Holt Winters beats seasonal naive by 40 percent even though its smoothing parameters are all zero, so it never adapts. Where does the improvement come from?</summary>

From using more data. Seasonal naive estimates each month's level from a single observation, last year's same month, so it inherits that one month's noise. Holt Winters with gamma at zero estimates each month's factor from all six years of training data, which averages the noise away. The improvement is a sample size effect, not an adaptivity effect, and recognising that tells you it will shrink if the seasonal pattern ever starts genuinely changing.
</details>

<details>
<summary><b>3.</b> Why is the interval called a lower bound on the uncertainty?</summary>

Because it is computed from the residuals of a fitted model while treating the fitted parameters as though they were known exactly. In reality alpha, beta, gamma and the initial states were all estimated from the same data, and each carries its own uncertainty that the interval ignores. It also assumes the future behaves like the training period. Real coverage is therefore usually a little below nominal, which is what the 11 of 12 result shows, and the fix is to measure coverage rather than to assume it.
</details>

## Key Takeaway

Fit the simplest model that is a model, check it against the baseline on data it has not seen, and read the parameters it chose. They usually say more than the forecast does.

---

| | |
|---|---|
| **Previous** | [Module 13: Baseline Forecasts You Must Beat](Module_13_Baseline_Forecasts.md) |
| **Next** | [Module 15: How Wrong Is the Forecast?](Module_15_Measuring_Forecast_Error.md) |
| **Builds on** | [Module 5](Module_05_Decomposition.md), [Module 13](Module_13_Baseline_Forecasts.md) |
| **Used again in** | [Module 16](Module_16_Did_Something_Change.md), and Advanced Module 7 |

*This module is part of a series developed for the Washington Data Exchange for Public Safety (WADEPS) through the Center for Interdisciplinary Statistical Education and Research (CISER) at Washington State University. Version 1.0, September 2026. Questions, errors, or suggestions: yin.zhang@wsu.edu*

*All examples use synthetic data created for teaching. They do not represent any real jurisdiction, agency, officer, or incident. See [Data/DATA_DICTIONARY.md](../../Data/DATA_DICTIONARY.md).*
