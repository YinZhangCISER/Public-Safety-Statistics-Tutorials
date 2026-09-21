# Module 3: Model Selection, Diagnostics and Honest Uncertainty

> **Developed by Yin Zhang, PhD**, Assistant Professor, Department of Mathematics and Statistics, Washington State University

**The question this module answers:** *Which model, is it finished, and how wrong could it be?*

---

## The Question

Three questions, in the order they have to be answered. Most analyses do the first, skip the second, and assert the third.

**Which model?** Information criteria narrow the field, and they rank rather than certify.

**Is it finished?** Diagnostics decide. A model that fails them is not a model whose coefficients you may quote.

**How wrong could it be?** A point forecast is worthless without a distribution, and a distribution is worthless until someone checks it.

## Model and Assumptions

The vehicle is a seasonal ARIMA on the log of Ashfell's monthly counts, but the procedure is the same for anything.

| Assumption | Diagnostic | What failing means |
|---|---|---|
| The residuals carry no structure | Ljung Box on the residuals | the model is missing a term; fix the model |
| The residuals are roughly normal | Jarque Bera, and a quantile plot | intervals and p values rest on the wrong shape |
| The variance is constant | Ljung Box on squared residuals | intervals too narrow in volatile stretches |
| No single point dominates | the largest standardised residual | one month is driving the fit |
| The forecast distribution is calibrated | coverage over many origins | the interval does not mean what it says |

The last row is the one nothing else checks, and it is the subject of half this module.

## Estimation

```python
fit = SARIMAX(train, order=(0, 1, 1), seasonal_order=(0, 1, 1, 12)).fit(disp=False)
res = fit.resid[13:]          # drop the differencing burn in
```

Dropping the burn in matters. The first observations of a differenced seasonal model have nothing to be predicted from, and leaving them in makes every diagnostic look worse than it is.

## Worked Example

![Six panels. The top row shows AIC and BIC for seven candidate orders with both agreeing on the winner, the residual autocorrelations all inside the noise band, and a quantile plot lying close to the line. The bottom row shows the forecast with its simulated interval, a calibration plot of nominal against observed coverage sitting above the diagonal, and a bar chart of where outcomes fell in the forecast distribution](Figures/fig_a03_diagnostics.png)

### Selection

Seven candidate orders. **AIC and BIC both pick the airline model**, one first difference and one seasonal difference, with a moving average term at each. Agreement between the two is worth reporting: it means the choice does not depend on how hard you penalise complexity.

**What information criteria cannot do.** They compare models fitted to the same data on the same scale. An AIC from a model on logs cannot be compared against one on counts, and two models with different differencing orders are not comparable unless the effective sample is the same. They also say nothing about whether the winner is any good.

### Diagnostics

| Check | p value | Verdict |
|---|---|---|
| Structure left in the residuals, Ljung Box at lag 12 | **0.78** | pass |
| Residuals not normal, Jarque Bera | **0.70** | pass |
| Changing variance, Ljung Box on squared residuals | **0.82** | pass |
| Largest standardised residual | **2.57** | nothing extreme |

All four pass, so this model has nothing obvious left in it.

**Passing the battery is not a guarantee.** Intermediate [Module 10](../Intermediate/Module_10_Reading_Autocorrelation.md) showed a case where Ljung Box is entirely silent about an enormous outlier, because an outlier is not a correlation. Each test looks for one thing.

### A distribution, not a forecast

| | Mean interval width |
|---|---|
| Analytic, from the fitted model | 64.9 incidents |
| Simulated from the fitted model | 64.7 incidents |

Essentially identical, which is the expected result for a well specified model with Gaussian errors, and worth confirming rather than assuming.

**What simulation does buy is the back transform.** The model works on logs and people want counts.

| Month | Exp of the mean of logs | Mean of the simulated counts | Difference |
|---|---|---|---|
| 1 | 66.2 | 67.6 | **+2.1%** |
| 6 | 116.7 | 119.2 | +2.1% |
| 12 | 66.0 | 67.1 | +1.7% |

Exponentiating the forecast of the logs gives the **median** count. The **mean** is about two percent higher. Small, and it is the difference between "a typical month" and "how many in total to expect", which are different questions a chief may ask in the same meeting. Exponentiating the interval endpoints is fine, because quantiles survive a monotone transform. Exponentiating the point forecast and calling it the expected count is not.

### Is the distribution any good?

Twelve months cannot distinguish 95 percent coverage from 100 percent. Score at five origins and pool, giving 60 forecast months.

| Nominal coverage | Observed |
|---|---|
| 50% | **45.0%** |
| 80% | **86.7%** |
| 95% | **98.3%** |

**The intervals are wider than they claim** at the levels anyone reports, which is the opposite of the usual warning and the same shape of surprise as Intermediate Module 10's robust standard errors. The 50 percent interval is slightly narrow, so the miscalibration is not a simple scaling.

Where the outcomes actually fell in the forecast distribution:

| | Observed | A calibrated forecast gives |
|---|---|---|
| below the 10th percentile | **7%** | 10% |
| in the middle 80 percent | **87%** | 80% |
| above the 90th percentile | **7%** | 10% |

Too few in the tails, consistently. **This is a finding you can only get by checking.** Nothing in the model output hints at it.

### Scoring the whole distribution

Intermediate [Module 15](../Intermediate/Module_15_Measuring_Forecast_Error.md) scored point forecasts with MAE and MASE. Those ignore the interval: a confident wrong forecast and a vague wrong forecast score the same. **Proper scores** grade the whole distribution, and a forecast cannot improve its score by misrepresenting its own uncertainty.

| | CRPS | Pinball loss |
|---|---|---|
| SARIMA | **7.18** | **3.76** |
| Same month last year | 11.49 | 6.02 |

SARIMA wins by about a third on both. That is a stronger statement than beating the baseline on MAE, because it says the whole distribution is better, not just the central guess.

## Recovering the Planted Answer

There is no planted parameter to recover here; the thing being checked is the **procedure**. What the dataset does supply is a stable series with a known seasonal period, and the selection step recovers exactly that: both criteria choose the model with a seasonal difference and a seasonal moving average term at lag 12, which is the structure the generator produced.

## Diagnostics: what these intervals still leave out

Every interval above holds the fitted parameters fixed, as though the coefficients were known rather than estimated from 72 months.

The obvious repair is to resample the parameters and simulate again. **For ARIMA this fails naively, and it is worth knowing why before trying it.** The moving average coefficients of the airline model sit close to the invertibility boundary, so drawing them from a normal approximation puts most draws outside the region where the model is defined.

| Parameter sets drawn | Sets that are actually invertible |
|---|---|
| 600 | **8** |

An interval built from those eight would be nonsense, and nothing in the code would warn you. Doing it properly needs a residual bootstrap with care about the differencing burn in, or a model fitted in a Bayesian framework where parameter uncertainty falls out of the posterior. **Both are beyond this module.**

The honest position in the meantime: the published intervals condition on the fitted parameters and are therefore **somewhat too narrow** on that account, while the calibration check found them **somewhat too wide** overall. Those work in opposite directions, and which dominates is an empirical question that the calibration check is how you answer.

## Do It Yourself

> 📓 **Notebook:** [Module_03_Model_Selection_And_Uncertainty.ipynb](Notebooks/Module_03_Model_Selection_And_Uncertainty.ipynb)
> [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/OWNER/REPO/blob/main/Time_Series/Advanced/Notebooks/Module_03_Model_Selection_And_Uncertainty.ipynb)
> About 30 minutes.

The notebook runs the selection table, the diagnostic battery, the back transform comparison, the pooled calibration check, implements CRPS and pinball loss from scratch, and demonstrates the invertibility failure. The exercise runs the whole sequence on Stonewick.

## When Not To Use This

| Situation | Instead |
|---|---|
| The outcome is a small count | a count model, [Module 2](Module_02_Counts_Are_Not_Gaussian.md); ARIMA on logs cannot handle zeros |
| The series has a gap | ARIMA cannot; state space can, [Module 7](Module_07_State_Space_And_ETS.md) |
| An intervention falls inside the window | one model for two regimes, [Module 11](Module_11_Interrupted_Time_Series.md) |
| Fewer than four years | too little to estimate a seasonal order and check it |
| You need to explain why, not what | none of this is causal; the [Causal Inference series](../../Causal_Inference/) |

## Reporting the Result

> A seasonal ARIMA of order (0,1,1)(0,1,1) with period 12 was fitted to the log of monthly counts. AIC and BIC both selected this order among seven candidates. Residual diagnostics found no remaining autocorrelation (Ljung Box p = 0.78), no departure from normality (Jarque Bera p = 0.70) and no evidence of changing variance (p = 0.82). Forecast intervals were obtained by simulation. Over five forecast origins and 60 months, nominal 95 percent intervals covered 98.3 percent of outcomes, so the intervals reported here are slightly conservative. Intervals condition on the fitted parameters and do not include parameter uncertainty.

That last sentence is short, and it is the difference between an interval a reader can rely on and one they cannot audit.

## Further Reading

- Hyndman, R. J. and Athanasopoulos, G. *Forecasting: Principles and Practice*, on model selection, residual diagnostics, and evaluating distributional forecasts. Free at otexts.com/fpp3.
- Gneiting, T. and Raftery, A. E. (2007). Strictly proper scoring rules, prediction, and estimation. *Journal of the American Statistical Association*, 102.
- Bergmeir, C. and Benítez, J. M. (2012). On the use of cross validation for time series predictor evaluation. *Information Sciences*, 191.

---

| | |
|---|---|
| **Previous** | [Module 2: Incident Counts Are Not Gaussian](Module_02_Counts_Are_Not_Gaussian.md) |
| **Next** | Part II, beginning with [Module 4: ARIMA End to End on One Agency](Module_04_ARIMA_End_To_End.md) |
| **Builds on** | [Intermediate Module 10](../Intermediate/Module_10_Reading_Autocorrelation.md), [Intermediate Module 15](../Intermediate/Module_15_Measuring_Forecast_Error.md), [Module 1](Module_01_Stationarity_Tested.md) |
| **Used again in** | every module that follows |

*This module is part of a series developed for the Washington Data Exchange for Public Safety (WADEPS) through the Center for Interdisciplinary Statistical Education and Research (CISER) at Washington State University. Version 1.0, September 2026. Questions, errors, or suggestions: yin.zhang@wsu.edu*

*All examples use synthetic data created for teaching. They do not represent any real jurisdiction, agency, officer, or incident. See [Data/DATA_DICTIONARY.md](../../Data/DATA_DICTIONARY.md).*
