# Module 5: SARIMA and Seasonal Orders

> **Developed by Yin Zhang, PhD**, Assistant Professor, Department of Mathematics and Statistics, Washington State University

**The question this module answers:** *How is a July peak modelled rather than removed, and how many seasonal terms does it take?*

---

## The Question

[Module 4](Module_04_ARIMA_End_To_End.md) showed a non seasonal model failing on a seasonal series, and no amount of extra autoregressive terms rescuing it. The repair is a second set of orders operating at the seasonal lag.

Beginner [Topic 8](../Beginner/Topic_08_Seasonality.md) and Intermediate [Module 7](../Intermediate/Module_07_Seasonal_Adjustment.md) both removed the season before doing anything else. This module **models** it, which keeps the seasonal uncertainty inside the forecast where it belongs.

## Model and Assumptions

A SARIMA carries two sets of the same three numbers.

| | Non seasonal | Seasonal |
|---|---|---|
| written | (p, d, q) | (P, D, Q) at period m |
| the lag they act on | 1, 2, 3 months | m, 2m, 3m months |
| what d or D differences against | last month | **the same month last year** |

For monthly data m is 12. So `(0,1,1)(0,1,1)12` means: difference against last month, difference against last year, one moving average term at lag 1 and one at lag 12. It is common enough to have a name, the **airline model**.

| Assumption | Diagnostic | Consequence of failing |
|---|---|---|
| The seasonal period is right | the ACF at lags m, 2m | a seasonal term fitted to nothing |
| One seasonal difference is enough | variance after D = 1 and D = 2, [Module 1](Module_01_Stationarity_Tested.md) | over differencing |
| The seasonal orders are large enough | Ljung Box **at lag 24**, not only 12 | seasonal structure left over |
| The seasonal pattern is worth modelling at all | seasonal strength, Intermediate [Module 5](../Intermediate/Module_05_Decomposition.md) | parameters spent on noise |

That last row is the one people skip, and the exercise in this module is about what it costs.

## Estimation

```python
fit = SARIMAX(train, order=(0, 1, 1), seasonal_order=(0, 1, 1, 12)).fit(disp=False)
```

**Check Ljung Box at lag 24 as well as 12.** A seasonal deficiency shows up at the seasonal lags, and a test that stops at 12 can miss it entirely.

## Worked Example

![Three panels. The first shows the ACF and PACF of Ashfell after one seasonal difference, with dashed lines marking lags 12 and 24 and both functions still active at 12. The second ranks six seasonal orders by AIC, marking the ones that fail the diagnostic. The third compares the AIC of the manually identified model against the one auto_arima selected](Figures/fig_a05_sarima.png)

### Identify the seasonal orders the same way

Ashfell, after one seasonal difference. The noise band is ±0.25.

| Lag | ACF | PACF |
|---|---|---|
| 1 | −0.02 | −0.02 |
| 2 | −0.22 | −0.23 |
| 11 | −0.09 | −0.02 |
| **12** | **−0.29** | **−0.37** |
| 13 | +0.01 | −0.10 |
| 24 | −0.17 | −0.31 |

Something is still present at lag 12 in both functions, so one seasonal difference has not finished the job and a seasonal term is needed. The ACF and PACF are close in size there, which does not settle whether it should be a seasonal moving average or a seasonal autoregressive term, so fit both.

### Fit the candidates

| Order | AIC | BIC | Ljung Box at 24 | Parameters |
|---|---|---|---|---|
| **(0,1,1)(0,1,1)12** | **−12.2** | **−6.8** | **0.864** | **3** |
| (1,1,1)(0,1,1)12 | −10.3 | −3.1 | 0.867 | 4 |
| (0,1,1)(1,1,1)12 | −9.8 | −2.6 | 0.088 | 4 |
| (0,1,1)(1,1,0)12 | −2.8 | 2.7 | **0.048** | 3 |
| (0,1,1)(0,1,2)12 | −2.5 | 3.5 | 0.052 | 4 |
| (0,1,1)(2,1,0)12 | −2.0 | 4.3 | 0.768 | 4 |

The airline model wins on AIC, on BIC, on the diagnostic and on parsimony at once. That does not always happen, and when it does it is worth saying, because nothing about the choice is then a judgment call.

Note the fourth row. **A model can have a respectable AIC and still fail the diagnostic**, which is why both columns are in the table.

### Automatic selection is not the end of the story

| | AIC |
|---|---|
| Chosen by reading the ACF and PACF | **−12.2** |
| Chosen by `auto_arima` | **−8.5** |

**The automatic search lost, by about four AIC points.** It settled on `(1,0,1)(1,0,1,12)`, with no differencing at all.

This is not a bug. A stepwise search does not visit every combination, and its built in tests chose `d = 0` and `D = 0`, which sends it down a different branch. Nothing in the output flags that; it returns a model.

**Use automatic selection to generate candidates, then check them against what the pictures said and compare on AIC yourself.** When the two disagree, that is information.

## Recovering the Planted Answer

The dataset generates a July peak in the use of force rate with a fixed twelve month period. The identification step finds structure at exactly lag 12 and nowhere else surprising, and the selected model carries one seasonal difference and one seasonal moving average term at that lag. **The procedure recovers the period the generator used.**

## Diagnostics

| Check | Where |
|---|---|
| Structure left at the seasonal lags | Ljung Box at 24, and the ACF at 12 and 24 |
| Over differencing seasonally | variance after D = 1 against D = 2, [Module 1](Module_01_Stationarity_Tested.md) |
| Seasonal terms worth having at all | seasonal strength, and the forecast score against a non seasonal fit |
| Coefficients near the invertibility boundary | seasonal MA close to −1, which matters for [Module 3](Module_03_Model_Selection_And_Uncertainty.md) |

## Do It Yourself

> 📓 **Notebook:** [Module_05_SARIMA.ipynb](Notebooks/Module_05_SARIMA.ipynb)
> [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/YinZhangCISER/Public-Safety-Statistics-Tutorials/blob/main/Time_Series/Advanced/Notebooks/Module_05_SARIMA.ipynb)
> About 30 minutes.

The exercise runs the same comparison on Millgate, the least seasonal agency, where **AIC prefers the seasonal model by nearly thirty points and the seasonal model forecasts worse than a constant.**

## When Not To Use This

| Situation | Instead |
|---|---|
| Seasonal strength below about 0.3 | a non seasonal model; the terms will fit noise |
| Fewer than four years | too few cycles to estimate a seasonal order |
| The seasonal pattern changed part way | [Module 12](Module_12_Structural_Breaks.md), then refit |
| Small counts with zeros | [Module 9](Module_09_Rare_Events.md) |
| The season is a nuisance rather than the subject | adjust it away instead, Intermediate [Module 7](../Intermediate/Module_07_Seasonal_Adjustment.md) |

## Reporting the Result

> A seasonal ARIMA(0,1,1)(0,1,1) with period 12 was fitted to the log of monthly counts. Seasonal orders were identified from the ACF and PACF after one seasonal difference, which showed remaining structure at lag 12. Among six candidates this order had the lowest AIC and BIC, the fewest parameters, and no remaining autocorrelation at lag 24 (Ljung Box p = 0.86). An automatic stepwise search returned a different and worse fitting specification, which was not used.

That last sentence belongs in the methods note. A reader who runs `auto_arima` and gets something else should be able to see that the difference was noticed rather than missed.

## Further Reading

- Box, G. E. P., Jenkins, G. M., Reinsel, G. C. and Ljung, G. M. *Time Series Analysis: Forecasting and Control*, where the airline model comes from.
- Hyndman, R. J. and Khandakar, Y. (2008). Automatic time series forecasting: the forecast package for R. *Journal of Statistical Software*, 27, on what stepwise selection does and does not search.

---

| | |
|---|---|
| **Previous** | [Module 4: ARIMA End to End on One Agency](Module_04_ARIMA_End_To_End.md) |
| **Next** | [Module 6: Regression with ARMA Errors](Module_06_Regression_With_ARMA_Errors.md) |
| **Builds on** | [Module 4](Module_04_ARIMA_End_To_End.md), [Beginner Topic 8](../Beginner/Topic_08_Seasonality.md), [Intermediate Module 5](../Intermediate/Module_05_Decomposition.md) |
| **Used again in** | [Module 6](Module_06_Regression_With_ARMA_Errors.md), [Module 11](Module_11_Interrupted_Time_Series.md) |

*This module is part of a series developed for the Washington Data Exchange for Public Safety (WADEPS) through the Center for Interdisciplinary Statistical Education and Research (CISER) at Washington State University. Version 1.0, September 2026. Questions, errors, or suggestions: yin.zhang@wsu.edu*

*All examples use synthetic data created for teaching. They do not represent any real jurisdiction, agency, officer, or incident. See [Data/DATA_DICTIONARY.md](../../Data/DATA_DICTIONARY.md).*
