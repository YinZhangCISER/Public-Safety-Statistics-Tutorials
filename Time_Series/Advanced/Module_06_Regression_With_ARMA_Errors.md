# Module 6: Regression with ARMA Errors

> **Developed by Yin Zhang, PhD**, Assistant Professor, Department of Mathematics and Statistics, Washington State University

**The question this module answers:** *How does a policy indicator, or any other explanatory variable, go into a time series model without the autocorrelation ruining the answer?*

---

## The Question

Everything so far has modelled a series using only its own past. This module adds explanatory variables: exposure, an external driver, a policy indicator.

That last one is why the module exists. A policy indicator in a regression is the simplest form of an intervention estimate and the direct precursor to [Module 11](Module_11_Interrupted_Time_Series.md). It is also where ordinary regression does its most expensive damage, and the damage is not the one people expect.

## Model and Assumptions

> log(incidents) = intercept + b1 · log(arrests) + b2 · programme + error
>
> and the error follows an ARMA process rather than being assumed independent

The coefficients mean what they would in ordinary regression. **b2** is the proportional change associated with the programme. **b1** is the elasticity with respect to arrests and should come out near 1: one percent more arrests, one percent more incidents.

| Assumption | Diagnostic | Consequence of failing |
|---|---|---|
| The error structure is modelled | Ljung Box on the residuals | the interval is wrong, often by a factor of two |
| The seasonal pattern is in the model | Ljung Box at lag 24 | the season leaks into the coefficients |
| The regressors are not themselves affected by the outcome | domain knowledge, not a test | the coefficient is not interpretable at all |
| Exposure behaves proportionally | is the estimated coefficient near 1 | the denominator is not doing what a rate assumes |

**The third row has no diagnostic and is the most important.** No amount of error modelling makes a coefficient causal.

## Estimation

```python
arma = SARIMAX(y, exog=X, order=(0, 0, 1), seasonal_order=(0, 1, 1, 12)).fit(disp=False)
```

## Worked Example

Stonewick, which adopted the de escalation training. The programme indicator switches on in November 2023, the month it was fully in place.

![Three panels. The first shows the residual autocorrelations from ordinary least squares, with several bars well outside the noise band. The second shows the same for a regression with ARMA errors, all inside. The third compares the two estimated programme effects against the true value, with the ordinary least squares estimate at roughly twice the truth and a much narrower interval](Figures/fig_a06_arma_errors.png)

| Model | Programme effect | 95 percent interval | Exposure coefficient |
|---|---|---|---|
| Ordinary least squares | **−23.6%** | [−30.6, −16.0] | **+1.51** |
| Seasonal MA errors | −10.1% | [−22.8, +4.8] | +0.89 |
| MA(1) and seasonal MA errors | **−10.4%** | [−23.1, +4.5] | **+0.93** |
| **The truth built into the data** | **−12.0%** | | **1.00** |

### Two separate failures, and the second is the serious one

**The interval is wrong.** OLS residuals have a Ljung Box p value of **0.0000**; the ARMA error model's is **0.6433**. Intermediate [Module 10](../Intermediate/Module_10_Reading_Autocorrelation.md) explained the mechanism. Here it produces an interval roughly half the width it should be.

**The point estimate is also wrong**, by about a factor of two. OLS has no seasonal term, so the seasonal pattern has nowhere to go but into the regressors, and the programme indicator absorbs part of it. **Modelling the error structure is not only about the standard errors when the missing structure is seasonal.**

### The free diagnostic nobody reads

Look at the exposure coefficient. Theory says it should be near 1.

**OLS returns 1.51**, which would mean a one percent rise in arrests brings a one and a half percent rise in incidents, and its interval [1.06, 1.97] excludes the value theory predicts. The ARMA error models return 0.89 and 0.93, and the second one's interval [0.55, 1.32] contains 1.

**A coefficient with a known expected value is the cheapest diagnostic in the model**, and it flagged this before any residual plot was drawn. Most analyses report the policy coefficient and discard the control.

### Exposure as a regressor or as an offset

[Module 2](Module_02_Counts_Are_Not_Gaussian.md) fixed the exposure coefficient at 1 as an offset. Here it is estimated freely and the interval contains 1, so fixing it costs nothing and buys a degree of freedom.

**The rule: leave it free first and look.** If the interval contains 1, fix it and say you checked. If it does not, the denominator is not behaving proportionally and that needs explaining before any rate is published.

## Recovering the Planted Answer

The dataset built a **12 percent** reduction at five agencies including Stonewick. The ARMA error models return **10.1 and 10.4 percent**, both intervals covering the truth. Ordinary least squares returns 23.6 percent with an interval that **excludes** the truth entirely.

The interval from the correct models also includes zero. That is the right answer from one agency, and it matches Intermediate [Module 16](../Intermediate/Module_16_Did_Something_Change.md): a 12 percent effect is not measurable from a single department.

## Diagnostics

| Check | Acceptable |
|---|---|
| Ljung Box on residuals at 12 and 24 | both above 0.05 |
| Exposure coefficient | interval contains 1 |
| Seasonal term present | yes, whenever the series has a season |
| The intervention date | fixed in advance, and matching when the thing was actually in place |
| Residual extremes | no standardised residual beyond about 3 |

## Do It Yourself

> 📓 **Notebook:** [Module_06_Regression_With_ARMA_Errors.ipynb](Notebooks/Module_06_Regression_With_ARMA_Errors.ipynb)
> [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/OWNER/REPO/blob/main/Time_Series/Advanced/Notebooks/Module_06_Regression_With_ARMA_Errors.ipynb)
> About 30 minutes.

The exercise repeats the comparison on Tarnbridge, where the documented unrest month has to be handled first.

## When Not To Use This

This model estimates an **association**, correctly, with an honest interval. It does not estimate an effect.

| What is missing | Why it matters | Where it is handled |
|---|---|---|
| A comparison group | anything else that changed at the same time is inside the coefficient | Intermediate [Module 12](../Intermediate/Module_12_Building_A_Peer_Benchmark_Series.md) |
| A level and slope change modelled separately | the programme may have changed the direction, not just the level | [Module 11](Module_11_Interrupted_Time_Series.md) |
| A response shape | effects phase in; a step function assumes they do not | [Module 13](Module_13_Intervention_Analysis.md) |
| More than one agency | one department cannot measure an effect this size | [Module 10](Module_10_Panel_And_Hierarchical.md) |
| An argument for why the association is causal | none of the above supplies it | the [Causal Inference series](../../Causal_Inference/) |

## Reporting the Result

> Monthly counts were modelled on the log scale with the log of arrests and an indicator for the training programme as regressors, and an MA(1) with a seasonal moving average term at lag 12 for the errors. Over the period the programme was fully in place, incidents at Stonewick ran 10.4 percent below what arrests and the seasonal pattern predict, 95 percent interval from 23.1 percent below to 4.5 percent above. The interval includes zero: a single agency does not provide enough information to establish an effect of this size. The estimated elasticity with respect to arrests was 0.93, consistent with the value of 1 that proportionality implies. An ordinary least squares fit of the same regressors returns 23.6 percent with strongly autocorrelated residuals and an implausible exposure coefficient of 1.51, and should not be used.

## Further Reading

- Hyndman, R. J. and Athanasopoulos, G. *Forecasting: Principles and Practice*, chapter on dynamic regression models. Free at otexts.com/fpp3.
- Box, G. E. P. and Tiao, G. C. (1975). Intervention analysis with applications to economic and environmental problems. *Journal of the American Statistical Association*, 70.

---

| | |
|---|---|
| **Previous** | [Module 5: SARIMA and Seasonal Orders](Module_05_SARIMA.md) |
| **Next** | [Module 7: State Space, Unobserved Components and ETS](Module_07_State_Space_And_ETS.md) |
| **Builds on** | [Module 2](Module_02_Counts_Are_Not_Gaussian.md), [Module 5](Module_05_SARIMA.md), [Intermediate Module 10](../Intermediate/Module_10_Reading_Autocorrelation.md) |
| **Used again in** | [Module 11](Module_11_Interrupted_Time_Series.md), [Module 13](Module_13_Intervention_Analysis.md) |

*This module is part of a series developed for the Washington Data Exchange for Public Safety (WADEPS) through the Center for Interdisciplinary Statistical Education and Research (CISER) at Washington State University. Version 1.0, September 2026. Questions, errors, or suggestions: yin.zhang@wsu.edu*

*All examples use synthetic data created for teaching. They do not represent any real jurisdiction, agency, officer, or incident. See [Data/DATA_DICTIONARY.md](../../Data/DATA_DICTIONARY.md).*
