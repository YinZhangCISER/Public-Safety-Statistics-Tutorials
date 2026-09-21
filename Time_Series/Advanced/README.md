# Time Series, Advanced Level

### Fitting a model, checking it, and knowing when not to trust it

*Developed by Yin Zhang, PhD, Assistant Professor, Data Analytics Program, Department of Mathematics and Statistics, Washington State University, for the Washington Data Exchange for Public Safety (WADEPS) through the Center for Interdisciplinary Statistical Education and Research (CISER).*

For agency data analysts, graduate students outside statistics, and early career researchers. Fourteen modules with complete Python notebooks.

Notation is used freely, proofs are not. The emphasis throughout is on **what a model assumes, how you check the assumption, and what it costs you when the assumption fails.**

> **Publication status:** Parts I, II and III, Modules 1 through 10, are published. Modules 11 through 14 are in development and their titles below are not yet links.

---

## Part I. Foundations for Modeling

Three habits that every later module depends on.

| # | Module | The question it answers |
|---|---|---|
| 1 | [Stationarity Tested, Not Eyeballed](Module_01_Stationarity_Tested.md) | ADF, KPSS, differencing, and what over differencing costs you |
| 2 | [Incident Counts Are Not Gaussian](Module_02_Counts_Are_Not_Gaussian.md) | Poisson and negative binomial thinking, and the right way to use exposure |
| 3 | [Model Selection, Diagnostics and Honest Uncertainty](Module_03_Model_Selection_And_Uncertainty.md) | AIC, residual checks, rolling origin backtesting, simulation based intervals, and whether a forecast distribution is any good |

## Part II. Core Univariate Models

| # | Module | The question it answers |
|---|---|---|
| 4 | [ARIMA End to End on One Agency](Module_04_ARIMA_End_To_End.md) | The full workflow, from identification to a defensible forecast |
| 5 | [SARIMA and Seasonal Orders](Module_05_SARIMA.md) | How to model a July peak rather than removing it |
| 6 | [Regression with ARMA Errors](Module_06_Regression_With_ARMA_Errors.md) | Adding exposure, policy indicators, and external drivers |
| 7 | [State Space, Unobserved Components, and ETS](Module_07_State_Space_And_ETS.md) | Handling a reporting gap that ARIMA cannot, and where Prophet fits |

## Part III. Counts, Rare Events, and Many Agencies

| # | Module | The question it answers |
|---|---|---|
| 8 | [Poisson and Negative Binomial Regression with Harmonic Seasonality](Module_08_Count_Regression_With_Harmonics.md) | The right default for monthly incident counts |
| 9 | [Rare Events, Zero Inflation, and When to Aggregate Up](Module_09_Rare_Events.md) | What to do when half the months are zero |
| 10 | [Panel and Hierarchical Time Series](Module_10_Panel_And_Hierarchical.md) | Two hundred agencies at once, and making the parts sum to the whole |

## Part IV. Intervention and Change

| # | Module | The question it answers |
|---|---|---|
| 11 | Interrupted Time Series Done Properly | Separating a level change from a slope change, with honest standard errors |
| 12 | Structural Breaks and Changepoints | Finding the date you were not told about |
| 13 | Intervention Analysis and Transfer Functions | Modeling the shape of a response, and the handoff to causal inference |

## Closing

| # | Module | The question it answers |
|---|---|---|
| 14 | Reporting, and Work That Outlives You | What to put in front of a chief, what you are not entitled to claim, and how to leave an analysis someone else can rerun |

---

## What the earlier levels have already promised this one

Thirteen of these fourteen modules are named somewhere in the Beginner or Intermediate series, or in the dataset's answer key, as the place a question gets taken up properly. A few examples:

| Promised by | To | About |
|---|---|---|
| [Intermediate Module 8](../Intermediate/Module_08_Rolling_Statistics_And_Control_Limits.md) | Module 2 | why counts are overdispersed, and what to do about it |
| [Intermediate Module 10](../Intermediate/Module_10_Reading_Autocorrelation.md) | Modules 3, 4, 11 | fitting the structure the residuals still contain |
| [Intermediate Module 12](../Intermediate/Module_12_Building_A_Peer_Benchmark_Series.md) | Module 10 | many agencies at once, properly |
| [Intermediate Module 16](../Intermediate/Module_16_Did_Something_Change.md) | Modules 11, 13 | estimating an intervention effect with a model |
| [Data/GROUND_TRUTH.md](../../Data/GROUND_TRUTH.md) | Modules 1, 2, 3, 5, 8, 9, 10, 11, 12, 13 | every pattern deliberately built into the dataset |

## Recovering the planted answer

Every module that estimates something compares its estimate against the value deliberately built into the dataset, reported in [Data/GROUND_TRUTH.md](../../Data/GROUND_TRUTH.md). Where a simpler method gets the wrong answer, the wrong number is shown next to the right one.

## Software

`pandas`, `numpy`, `statsmodels`, `matplotlib`, `scikit-learn`, with `pmdarima` in two modules. Everything is available in Google Colab by default. See [requirements.txt](../../requirements.txt).

---

*All examples use synthetic data created for teaching. They do not represent any real jurisdiction, agency, officer, or incident. See [Data/DATA_DICTIONARY.md](../../Data/DATA_DICTIONARY.md).*

*Questions, corrections, or suggestions: yin.zhang@wsu.edu*
