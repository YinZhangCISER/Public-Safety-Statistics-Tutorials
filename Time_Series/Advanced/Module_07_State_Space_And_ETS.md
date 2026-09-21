# Module 7: State Space, Unobserved Components and ETS

> **Developed by Yin Zhang, PhD**, Assistant Professor, Department of Mathematics and Statistics, Washington State University

**The question this module answers:** *An agency never submitted three months. Which models can still be fitted, and which ones fail without saying so?*

---

## The Question

Prairie County stopped reporting in March 2022 and resumed in June. Intermediate [Module 2](../Intermediate/Module_02_Building_An_Honest_Calendar.md) said to leave those months missing rather than filling them with zero, and that was the right advice.

It also makes the series unusable by most of the methods in this series. This module is about the family that can cope, and about how the others fail, which is more interesting than it sounds because **two of them fail without saying so**.

## Model and Assumptions

A state space model separates what it believes about the world from what it observed:

> **state equation:** the level, the slope and the season evolve from one month to the next
>
> **observation equation:** what was reported is the state plus measurement noise

The **Kalman filter** carries the state forward month by month and updates it whenever an observation arrives. When a month is missing there is no update: the filter propagates the state, widens its uncertainty, and continues. Nothing is imputed and nothing special is required.

SARIMA, ETS and unobserved components are all writable in this form. In statsmodels, `SARIMAX` and `UnobservedComponents` use the filter; `ExponentialSmoothing` and `STL` do not.

| Assumption | Diagnostic | Consequence of failing |
|---|---|---|
| The gap is unrelated to the outcome | why did reporting stop | a gap caused by the events themselves biases everything |
| The chosen components exist | estimated state variances | a component pinned at zero is deterministic, not absent |
| Observation noise is roughly Gaussian on the modelled scale | residual plot | intervals are wrong for small counts |
| The calendar is complete | `index.freq` is not None | see section on the shortcut below |

## Estimation

```python
uc = UnobservedComponents(lp, level="local linear trend", seasonal=12).fit(disp=False)
```

## Worked Example

Prairie County, log use of force counts, three months missing in 2022.

![Two panels. The left shows Prairie County's reported counts with the three month gap shaded, and a state space fit running straight through it with the three estimated months marked. The right is a bar chart of the percentage of months for which each of three methods produced a usable fitted value: state space 100 percent, Holt Winters 44 percent, STL 0 percent, with the last two labelled as failing silently](Figures/fig_a07_state_space.png)

### The same series, three methods, no errors raised

| Method | Months with a usable fitted value | Forecast |
|---|---|---|
| State space (SARIMAX) | **100%** | usable |
| Holt Winters | **44%** | **every value missing** |
| STL | **0%** | not applicable |

**None of the three raised an error.** Holt Winters returned a ConvergenceWarning, which is the warning you get for something else entirely, and then returned a forecast of six missing values. In a pipeline that writes to a dashboard, that is a blank chart nobody can explain, and the cause is three months three years earlier.

The filter's estimates for the unreported months are **1.40, 0.73 and 0.97** incidents, against an agency average of 2.84. They are estimates, not data. They belong in a model and they do not belong in a table of what happened.

### The tempting shortcut

The obvious alternative is to delete the three months and carry on. After `dropna()`:

- the index frequency becomes `None`
- **the month after February 2022 is June 2022**

Every lag in the model is wrong from that point forward, the seasonal period no longer lines up with the calendar, and nothing warns you. **Deleting is worse than leaving the gap**, because leaving the gap at least gives the honest methods a chance to handle it.

### Unobserved components: the same machinery, readable parts

A SARIMA describes a series through its correlations. An unobserved components model describes it as a sum of pieces you can name and plot. Same filter, same tolerance of gaps, interpretable output.

For Prairie County:

| Component | Estimated shock variance | Reading |
|---|---|---|
| Level | 0.00000 | fixed |
| Slope | 0.00000 | fixed |
| Seasonal | 0.00000 | fixed |
| Irregular | 0.39509 | everything else |

**Every state variance is pinned at zero.** The model is saying that in a series averaging under three incidents a month, nothing time varying can be detected: a deterministic line plus a deterministic season plus noise fits as well as anything that moves. AIC is 175.9 against the SARIMA's 173.9, which is a tie.

That is a real finding, not a failure. It is also invisible in a SARIMA, which would fit the same series and report coefficients without ever saying that the level is not moving.

**Use unobserved components when someone will ask what the model thinks the trend is.** Use SARIMA when forecast accuracy is the only deliverable.

### Where Prophet fits

Prophet is widely used and worth a paragraph rather than a section. It fits a piecewise linear trend with automatically placed changepoints plus seasonal terms, and its appeal is that it produces a plausible chart with no decisions.

| Consideration | For this kind of data |
|---|---|
| Automatic changepoints | it will place breaks where none occurred, which matters when the question **is** whether a break occurred |
| Built for high frequency business data | monthly police counts have neither the volume nor the granularity |
| Handles gaps and outliers by default | convenient, and it hides exactly the data problems Beginner [Topic 19](../Beginner/Topic_19_Data_Quality_And_Pitfalls.md) says to look for |
| Maintenance | development has been largely dormant for several years |

A reasonable default is not to use it here. If it is used, fix the changepoints by hand and report where they were placed.

## Recovering the Planted Answer

The dataset removed Prairie County's March, April and May 2022 on purpose, and nothing else about the agency was changed. Everything in this module follows from those three months: **44 percent and 0 percent usable output from two standard methods, and a silent all missing forecast, out of a three month reporting gap in a 88 month series.**

## Diagnostics

| Check | Acceptable |
|---|---|
| Fitted values | count the missing ones before reading any result |
| Forecast | check it is not all missing before it reaches a chart |
| `index.freq` | never None |
| State variances | a zero means deterministic, and should be said out loud |
| Gap mechanism | documented, and argued to be unrelated to the outcome |

## Do It Yourself

> 📓 **Notebook:** [Module_07_State_Space_And_ETS.ipynb](Notebooks/Module_07_State_Space_And_ETS.ipynb)
> [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/OWNER/REPO/blob/main/Time_Series/Advanced/Notebooks/Module_07_State_Space_And_ETS.ipynb)
> About 30 minutes.

The exercise confirms that the gap is the whole cause by filling it and refitting, and then argues against doing that.

## When Not To Use This

| Situation | Reach for |
|---|---|
| Small counts with many zeros | a count model, [Module 9](Module_09_Rare_Events.md) |
| Many agencies at once | [Module 10](Module_10_Panel_And_Hierarchical.md) |
| An intervention with a known date | [Module 11](Module_11_Interrupted_Time_Series.md) |
| A gap caused by the events being measured | no model fixes this; report the gap |
| A chart with no decisions in it | reconsider; that is the appeal that causes the trouble |

## Reporting the Result

> Prairie County did not report from March to May 2022. The series was modelled in state space form, which handles unobserved months through the Kalman filter without imputation; the filter's estimates for the three months are 1.4, 0.7 and 1.0 incidents and are identified as estimates wherever they appear. An unobserved components decomposition places all state shock variances at zero, indicating that in a series averaging 2.8 incidents a month no time varying level, slope or seasonal movement is detectable. Exponential smoothing and STL were also fitted and are reported here only to note that both returned output for this series without error while producing no usable values across 56 and 100 percent of months respectively.

## Further Reading

- Durbin, J. and Koopman, S. J. (2012). *Time Series Analysis by State Space Methods*, 2nd edition. Oxford University Press. Chapters 2 and 4.
- Harvey, A. C. (1989). *Forecasting, Structural Time Series Models and the Kalman Filter*. Cambridge University Press.
- Hyndman, R. J. and Athanasopoulos, G. *Forecasting: Principles and Practice*, chapters on exponential smoothing and state space. Free at otexts.com/fpp3.

---

| | |
|---|---|
| **Previous** | [Module 6: Regression with ARMA Errors](Module_06_Regression_With_ARMA_Errors.md) |
| **Next** | [Module 8: Poisson and Negative Binomial Regression with Harmonic Seasonality](Module_08_Count_Regression_With_Harmonics.md) |
| **Builds on** | [Module 5](Module_05_SARIMA.md), [Intermediate Module 2](../Intermediate/Module_02_Building_An_Honest_Calendar.md) |
| **Used again in** | [Module 11](Module_11_Interrupted_Time_Series.md), [Module 12](Module_12_Structural_Breaks.md) |

*This module is part of a series developed for the Washington Data Exchange for Public Safety (WADEPS) through the Center for Interdisciplinary Statistical Education and Research (CISER) at Washington State University. Version 1.0, September 2026. Questions, errors, or suggestions: yin.zhang@wsu.edu*

*All examples use synthetic data created for teaching. They do not represent any real jurisdiction, agency, officer, or incident. See [Data/DATA_DICTIONARY.md](../../Data/DATA_DICTIONARY.md).*
