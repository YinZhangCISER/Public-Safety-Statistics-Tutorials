# Time Series, Advanced Level

### Fitting a model, checking it, and knowing when not to trust it

*Prepared by Yin Zhang, Center for Interdisciplinary Statistical Education and Research (CISER), Washington State University.*

For agency data analysts, graduate students outside statistics, and early career researchers. Sixteen modules with complete Python notebooks. Notation is used freely, proofs are not. The emphasis throughout is on what a model assumes, how you check the assumption, and what it costs you when the assumption fails.

---

## Part I. Foundations for Modeling

| # | Module | The question it answers |
|---|---|---|
| 1 | Stationarity Tested, Not Eyeballed | ADF, KPSS, differencing, and what over differencing costs you |
| 2 | Incident Counts Are Not Gaussian | Poisson and negative binomial thinking, and the right way to use exposure |
| 3 | Model Selection and Diagnostic Discipline | AIC, residual checks, Ljung Box, and rolling origin backtesting |

## Part II. Core Univariate Models

| # | Module | The question it answers |
|---|---|---|
| 4 | ARIMA End to End on One Agency | The full workflow, from identification to a defensible forecast |
| 5 | SARIMA and Seasonal Orders | How to model a July peak rather than removing it |
| 6 | Regression with ARMA Errors | Adding exposure, policy indicators, and external drivers |
| 7 | State Space, Unobserved Components, and ETS | When a structural model beats ARIMA, and where Prophet fits |

## Part III. Counts, Rare Events, and Many Agencies

| # | Module | The question it answers |
|---|---|---|
| 8 | Poisson and Negative Binomial Regression with Harmonic Seasonality | The right default for monthly incident counts |
| 9 | Rare Events, Zero Inflation, and When to Aggregate Up | What to do when half the months are zero |
| 10 | Panel and Hierarchical Time Series | Two hundred agencies at once, and making the parts sum to the whole |

## Part IV. Intervention and Change

| # | Module | The question it answers |
|---|---|---|
| 11 | Interrupted Time Series Done Properly | Separating a level change from a slope change, with honest standard errors |
| 12 | Structural Breaks and Changepoints | Finding the date you were not told about |
| 13 | Intervention Analysis and Transfer Functions | Modeling the shape of a response, and the handoff to causal inference |

## Part V. Getting It Used

| # | Module | The question it answers |
|---|---|---|
| 14 | Communicating Forecast Uncertainty | Prediction intervals, fan charts, and whether yours are calibrated |
| 15 | Reproducible Analysis for Public Agencies | Structure, seeds, environments, and documentation that survives staff turnover |
| 16 | Reporting to Decision Makers | What to put in front of a chief, and what you are not entitled to claim |

---

## Recovering the planted answer

Every module that estimates something compares its estimate against the value deliberately built into the dataset, reported in [Data/GROUND_TRUTH.md](../../Data/GROUND_TRUTH.md). Where a simpler method gets the wrong answer, the wrong number is shown next to the right one.

## Software

`pandas`, `numpy`, `statsmodels`, `matplotlib`, with `pmdarima` in two modules. Everything is available in Google Colab by default. See [requirements.txt](../../requirements.txt).

---

*All examples use synthetic data created for teaching. They do not represent any real jurisdiction, agency, officer, or incident.*

*Questions, corrections, or suggestions: yin.zhang@wsu.edu*
