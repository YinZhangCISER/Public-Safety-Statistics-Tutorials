# Module 4: ARIMA End to End on One Agency

> **Developed by Yin Zhang, PhD**, Assistant Professor, Department of Mathematics and Statistics, Washington State University

**The question this module answers:** *What does the complete workflow look like, with nothing skipped?*

---

## The Question

Four steps, in order. **Identify** the orders from the data rather than guessing. **Estimate.** **Diagnose**, and go back to step one if it fails. **Forecast**, and score against the bar from Intermediate [Module 13](../Intermediate/Module_13_Baseline_Forecasts.md).

The agency is Millgate, chosen because it has the weakest seasonal pattern in the dataset, so a non seasonal model gets a fair hearing. [Module 5](Module_05_SARIMA.md) adds the seasonal orders.

## Model and Assumptions

An **ARIMA(p, d, q)** says: difference the series `d` times, then explain what is left with `p` of its own past values and `q` of its own past errors.

| Assumption | Diagnostic | Consequence of failing |
|---|---|---|
| The differenced series is stationary | ADF and KPSS, [Module 1](Module_01_Stationarity_Tested.md) | a trend left in the residuals, or over differencing |
| `p` and `q` are large enough | Ljung Box on the residuals | structure the model never saw |
| `p` and `q` are not larger than needed | AIC and BIC against simpler orders | parameters spent on noise |
| The errors have constant variance and no extreme points | squared residuals, largest standardised residual | intervals that do not mean what they say |

## Estimation

```python
fit = SARIMAX(train, order=(0, 1, 1), seasonal_order=(0, 0, 0, 0)).fit(disp=False)
res = fit.resid[3:]
```

## Worked Example

![Four panels. The first shows Millgate's monthly counts. The second shows the ACF and PACF after one difference, with a single large negative spike in the ACF at lag one. The third plots AIC against forecast error for seven candidate orders, with different models winning each. The fourth shows Ljung Box p values for three models fitted to Ashfell, where both non seasonal models fall below the threshold](Figures/fig_a04_arima.png)

### Step 1: how many differences

| | ADF p | KPSS p | Verdict |
|---|---|---|---|
| level | 0.006 | 0.043 | **conflict** |
| first difference | 0.000 | 0.100 | **stationary** |

The level lands in the conflict cell from [Module 1](Module_01_Stationarity_Tested.md): ADF rejects a unit root while KPSS rejects stationarity. That usually means a trend with a stable part around it, and differencing once resolves it cleanly.

### Step 2: which orders

| Lag | ACF | PACF |
|---|---|---|
| 1 | **−0.55** | **−0.55** |
| 2 | +0.16 | −0.21 |
| 3 | −0.12 | −0.19 |
| 4 | +0.16 | +0.06 |

One large negative spike in the **ACF**, a **PACF** that decays rather than cutting off. That is the signature of a moving average term of order one, so the candidate is **ARIMA(0,1,1)**.

**This is what identification means.** The picture proposes a model. It does not prove one, which is what the next two steps are for.

### Step 3: estimate, and the finding in the last column

| Order | AIC | Ljung Box p | Forecast error, 2025 |
|---|---|---|---|
| **(0,1,1)** | **100.1** | 0.726 | 2.62 |
| (2,0,0) | 101.5 | 0.967 | 2.42 |
| **(1,0,1)** | 101.7 | 0.885 | **2.33** |
| (1,1,1) | 102.1 | 0.736 | 2.61 |
| (0,0,0) | 102.8 | 0.441 | 2.34 |
| (1,0,0) | 103.2 | 0.754 | 2.42 |
| (1,1,0) | 110.1 | 0.866 | 4.17 |

**The lowest AIC is exactly what the ACF and PACF proposed.** That agreement is the point of identification: without it, the criterion has nothing to check.

Now the last column. **The best fitting model is not the best forecasting model.** `(0,1,1)` wins on AIC and `(1,0,1)` forecasts better, and the constant only model is a hair behind that. Every one of them beats the seasonal naive baseline of **4.08**, and none beats the others by anything a person could act on, on a series averaging **7.8** incidents a month.

That is the honest conclusion for a small, weakly structured series, and it is Intermediate Module 13's lesson arriving with more machinery behind it. **AIC ranks how well a model fits the data it was fitted to. It is not a forecast score.**

### Step 4: diagnose

`(0,1,1)` passes everything: Ljung Box 0.73 at lag 12 and 0.90 at lag 24, normality 0.49, no extreme residual.

### What happens on a seasonal series

Millgate was chosen for its weak season. The same approach on Ashfell:

| Model | AIC | Ljung Box, lag 12 | lag 24 |
|---|---|---|---|
| ARIMA(1,1,1) | 15.9 | **0.0123** | **0.0003** |
| ARIMA(2,1,2) | 6.9 | **0.0006** | **0.0000** |
| SARIMA(0,1,1)(0,1,1)12 | **−12.2** | 0.7823 | 0.8639 |

Both non seasonal models fail decisively, and **the more elaborate one fails harder**. Piling on autoregressive terms cannot imitate a pattern that repeats every twelve months. That is [Module 5](Module_05_SARIMA.md).

## Recovering the Planted Answer

There is no planted ARIMA order to recover. What the dataset supplies is an agency whose seasonal strength is 0.159, the lowest of the twelve, and the workflow correctly concludes that a non seasonal model is adequate for it while the same workflow rejects one for Ashfell at 0.796. **The procedure discriminates, which is what it is for.**

## Diagnostics

| Step | Go back when |
|---|---|
| Identify differencing | the differenced series is still not stationary |
| Identify orders | nothing cuts off cleanly in either picture |
| Estimate | the optimiser does not converge |
| Diagnose | any check fails; return to step one, not to step three |
| Forecast | it does not beat the baseline on held out data |

## Do It Yourself

> 📓 **Notebook:** [Module_04_ARIMA_End_To_End.ipynb](Notebooks/Module_04_ARIMA_End_To_End.ipynb)
> [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/OWNER/REPO/blob/main/Time_Series/Advanced/Notebooks/Module_04_ARIMA_End_To_End.ipynb)
> About 30 minutes.

The exercise runs the workflow on Havenbrook, where the recipe that worked for Millgate turns out to be the wrong one.

## When Not To Use This

| Situation | Instead |
|---|---|
| A visible seasonal pattern | [Module 5](Module_05_SARIMA.md) |
| Small counts, or any zeros | [Module 2](Module_02_Counts_Are_Not_Gaussian.md) and [Module 9](Module_09_Rare_Events.md) |
| A gap in the series | [Module 7](Module_07_State_Space_And_ETS.md); ARIMA cannot |
| Explanatory variables | [Module 6](Module_06_Regression_With_ARMA_Errors.md) |
| An intervention inside the window | [Module 11](Module_11_Interrupted_Time_Series.md) |

## Reporting the Result

> Millgate's monthly counts were modelled on the log scale. ADF and KPSS disagreed on the level and agreed on the first difference, so one difference was taken. The differenced ACF showed a single spike at lag 1 with a decaying PACF, indicating a first order moving average, and ARIMA(0,1,1) had the lowest AIC of seven candidates. Residual diagnostics passed. Its 2025 forecast error of 2.62 incidents a month compares with 4.08 for a seasonal naive baseline, though three other specifications forecast marginally better, so the choice among them is not material.

## Further Reading

- Box, G. E. P., Jenkins, G. M., Reinsel, G. C. and Ljung, G. M. *Time Series Analysis: Forecasting and Control*, the original identify, estimate, diagnose cycle.
- Hyndman, R. J. and Athanasopoulos, G. *Forecasting: Principles and Practice*, on reading ACF and PACF. Free at otexts.com/fpp3.

---

| | |
|---|---|
| **Previous** | [Module 3: Model Selection, Diagnostics and Honest Uncertainty](Module_03_Model_Selection_And_Uncertainty.md) |
| **Next** | [Module 5: SARIMA and Seasonal Orders](Module_05_SARIMA.md) |
| **Builds on** | [Module 1](Module_01_Stationarity_Tested.md), [Module 3](Module_03_Model_Selection_And_Uncertainty.md), [Intermediate Module 13](../Intermediate/Module_13_Baseline_Forecasts.md) |
| **Used again in** | [Module 5](Module_05_SARIMA.md), [Module 6](Module_06_Regression_With_ARMA_Errors.md), [Module 11](Module_11_Interrupted_Time_Series.md) |

*This module is part of a series developed for the Washington Data Exchange for Public Safety (WADEPS) through the Center for Interdisciplinary Statistical Education and Research (CISER) at Washington State University. Version 1.0, September 2026. Questions, errors, or suggestions: yin.zhang@wsu.edu*

*All examples use synthetic data created for teaching. They do not represent any real jurisdiction, agency, officer, or incident. See [Data/DATA_DICTIONARY.md](../../Data/DATA_DICTIONARY.md).*
