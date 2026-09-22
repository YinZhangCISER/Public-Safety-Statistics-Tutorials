# Module 8: Poisson and Negative Binomial Regression with Harmonic Seasonality

> **Developed by Yin Zhang, PhD**, Assistant Professor, Department of Mathematics and Statistics, Washington State University

**The question this module answers:** *What is the right default model for a monthly incident count, and when does overdispersion actually mean what it appears to mean?*

---

## The Question

[Module 2](Module_02_Counts_Are_Not_Gaussian.md) argued that monthly incident counts are counts. This module is the working version of that argument: a count regression with a trend, a season and an exposure offset, which is the right default for almost every monthly series in a public safety dataset.

It also settles a question that costs people a great deal of time. **Overdispersion is usually a diagnosis about the mean, not about the distribution.** Before reaching for a negative binomial, check whether the Poisson looks overdispersed only because something is missing from the right hand side.

## Model and Assumptions

> incidents ~ Poisson(mu), with log(mu) = log(arrests) + intercept + b·time + seasonal terms

The offset fixes the exposure coefficient at 1, so the model is about the rate per arrest. The seasonal terms are a **sine and cosine pair at the annual frequency**, not eleven monthly dummies.

| Assumption | Diagnostic | Consequence of failing |
|---|---|---|
| The mean structure is complete | Pearson residuals grouped by calendar month | apparent overdispersion, biased coefficients |
| Variance equals the mean | Pearson dispersion near 1 | intervals too narrow |
| Exposure enters proportionally | estimate it freely once and check it covers 1 | the rate is not a rate |
| Observations are independent given the model | Ljung Box on the residuals | see [Module 6](Module_06_Regression_With_ARMA_Errors.md) |
| The seasonal shape is smooth | compare harmonics against dummies | a rougher fit and eleven parameters spent |

## Estimation

```python
X = pd.concat([pd.DataFrame({"t": years}), harmonics(month, K=1)], axis=1)
m = sm.GLM(y, sm.add_constant(X), family=sm.families.Poisson(), offset=np.log(arrests)).fit()
```

## Worked Example

Stonewick, 88 months, averaging 57.6 incidents a month.

![Three panels. The first is a bar chart of Pearson dispersion for five model designs, falling from 2.19 with a trend alone to about 1.09 as soon as one harmonic is added. The second plots AIC against the number of parameters, with one harmonic lowest and eleven monthly dummies slightly worse on nine more parameters. The third overlays the planted seasonal shape with the shapes recovered by one harmonic and by eleven dummies, which agree](Figures/fig_a08_count_regression.png)

### Step one: fit a trend and look at where the residuals are

A Poisson with only a trend gives a **Pearson dispersion of 2.19**. The textbook signal is to switch to a negative binomial. Do not switch yet. Group the Pearson residuals by calendar month first:

| Month | J | F | M | A | M | J | J | A | S | O | N | D |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Mean residual | −1.79 | −1.20 | −0.76 | +0.16 | −0.36 | +2.07 | +1.47 | +1.18 | +0.62 | +0.23 | −0.53 | −0.97 |

These are not scattered. They are negative in winter and positive in summer. **That is not what a dispersion problem looks like. It is what a missing seasonal term looks like.**

### Step two: add the season, two parameters at a time

| Design | Parameters | AIC | Pearson dispersion |
|---|---|---|---|
| Trend only | 2 | 709.4 | **2.19** |
| **+ 1 harmonic** | **4** | **615.3** | **1.09** |
| + 2 harmonics | 6 | 618.9 | 1.11 |
| + 3 harmonics | 8 | 618.6 | 1.09 |
| + 11 monthly dummies | 13 | 618.8 | 1.03 |

Two extra parameters took the dispersion from 2.19 to 1.09 and the AIC down by 94 points. **The apparent overdispersion was the July peak**, sitting in the residuals because nothing in the model accounted for it.

Eleven monthly dummies cost nine more parameters and score slightly worse. Monthly public safety seasonality is smooth: July resembles June and August, and a model that knows this estimates it with two numbers instead of eleven.

### Step three: check whether the negative binomial still has work to do

| Model, one harmonic | AIC |
|---|---|
| Poisson | **615.3** |
| Negative binomial, best alpha 0.005 | 616.9 |

The best negative binomial sits at the smallest alpha on the grid and does not improve on the Poisson. **Once the mean is right, there is nothing left for the extra variance parameter to do.**

### Three diagnoses, three fixes

| What the residuals look like | Diagnosis | Fix |
|---|---|---|
| Patterned by calendar month | a missing seasonal term | add harmonics |
| One enormous residual | an event | model it or exclude it, and document either |
| Too big everywhere, no pattern, no culprit | genuine overdispersion | negative binomial |

Tarnbridge shows the second case. Its Pearson dispersion is **5.92**, and the largest Pearson residual is **19.1**, in June 2021. Drop that one month and the dispersion is **1.41**. A residual of 19 is not overdispersion; it is one extraordinary month with a name and a date.

Ashfell shows the third. Its dispersion falls from 4.45 to 1.73 when the season enters and then stops: no number of harmonics moves it, the largest residual is only 2.6, and a negative binomial improves AIC from 718.4 to 704.9. A large agency aggregates many neighbourhoods and shifts, and its month to month variation really is wider than a Poisson allows.

## Recovering the Planted Answer

The generator gave the use of force rate a seasonal factor of amplitude **0.20 on the log scale**, peaking in **July**.

| Quantity | Recovered | Planted |
|---|---|---|
| Amplitude | **0.197** | 0.200 |
| Peak month | **7** | 7 |
| Peak above trough | 48 percent | |

Two parameters.

## Diagnostics

| Check | Acceptable |
|---|---|
| Pearson dispersion | near 1, after the mean structure is complete |
| Residuals grouped by calendar month | no pattern left |
| Largest standardised residual | below about 3, or a named explanation |
| AIC against added harmonics | flat after the first pair, for monthly data |
| Exposure, estimated freely once | interval contains 1 |

## Do It Yourself

> 📓 **Notebook:** [Module_08_Count_Regression_With_Harmonics.ipynb](Notebooks/Module_08_Count_Regression_With_Harmonics.ipynb)
> [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/YinZhangCISER/Public-Safety-Statistics-Tutorials/blob/main/Time_Series/Advanced/Notebooks/Module_08_Count_Regression_With_Harmonics.ipynb)
> About 35 minutes.

The exercise runs the same comparison at Ashfell, where the third diagnosis turns out to be the right one.

## When Not To Use This

| Situation | Reach for |
|---|---|
| Half the months are zero | [Module 9](Module_09_Rare_Events.md), and check for real zero inflation first |
| Residuals still autocorrelated after the season is in | [Module 6](Module_06_Regression_With_ARMA_Errors.md) |
| Many agencies at once | [Module 10](Module_10_Panel_And_Hierarchical.md) |
| A seasonal pattern that shifts over the years | a state space seasonal, [Module 7](Module_07_State_Space_And_ETS.md) |
| An intervention with a known date | [Module 11](Module_11_Interrupted_Time_Series.md) |

## Reporting the Result

> Monthly use of force counts were modelled with a Poisson regression, using the log of arrests as an offset, a linear time term, and one pair of harmonic terms at the annual frequency. The seasonal pattern peaks in July at 21.7 percent above the annual average and troughs in January at 17.8 percent below. Pearson dispersion for this model is 1.09; with the seasonal terms omitted it is 2.19, so the excess dispersion reported by a trend only model is attributable to unmodelled seasonality rather than to the count distribution. Eleven monthly indicators recover the same seasonal shape with nine additional parameters and a marginally worse AIC, and a negative binomial specification does not improve on the Poisson.

## Further Reading

- Cameron, A. C. and Trivedi, P. K. (2013). *Regression Analysis of Count Data*, 2nd edition. Cambridge University Press. Chapters 3 and 5.
- Hyndman, R. J. and Athanasopoulos, G. *Forecasting: Principles and Practice*, section on Fourier terms in dynamic regression. Free at otexts.com/fpp3.
- Brandt, P. T. and Williams, J. T. (2001). A linear Poisson autoregressive model. *Political Analysis*, 9.

---

| | |
|---|---|
| **Previous** | [Module 7: State Space, Unobserved Components and ETS](Module_07_State_Space_And_ETS.md) |
| **Next** | [Module 9: Rare Events, Zero Inflation and When to Aggregate Up](Module_09_Rare_Events.md) |
| **Builds on** | [Module 2](Module_02_Counts_Are_Not_Gaussian.md), [Intermediate Module 8](../Intermediate/Module_08_Rolling_Statistics_And_Control_Limits.md) |
| **Used again in** | [Module 9](Module_09_Rare_Events.md), [Module 10](Module_10_Panel_And_Hierarchical.md), [Module 11](Module_11_Interrupted_Time_Series.md) |

*This module is part of a series developed for the Washington Data Exchange for Public Safety (WADEPS) through the Center for Interdisciplinary Statistical Education and Research (CISER) at Washington State University. Version 1.0, September 2026. Questions, errors, or suggestions: yin.zhang@wsu.edu*

*All examples use synthetic data created for teaching. They do not represent any real jurisdiction, agency, officer, or incident. See [Data/DATA_DICTIONARY.md](../../Data/DATA_DICTIONARY.md).*
