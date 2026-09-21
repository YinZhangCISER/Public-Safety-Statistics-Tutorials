# Module 2: Incident Counts Are Not Gaussian

> **Developed by Yin Zhang, PhD**, Assistant Professor, Department of Mathematics and Statistics, Washington State University

**The question this module answers:** *Ordinary regression on a monthly count runs without complaint. What exactly is it getting wrong, and how much does it cost?*

---

## The Question

Every model in the Intermediate series treated a monthly count, or a rate built from one, as a continuous quantity with constant spread. That is the software default and it is wrong in three specific ways for public safety data.

The three failures are not equally serious, and the most expensive one is the least visible.

## Model and Assumptions

| Ordinary regression assumes | Counts do this instead | Diagnostic | Consequence of ignoring it |
|---|---|---|---|
| the outcome is continuous and unbounded | a count is a non negative integer | plot the prediction intervals | impossible intervals, most obvious at small agencies |
| the spread is constant | the variance of a count grows with its mean | residual variance by fitted value | intervals too wide where the level is low, too narrow where it is high |
| errors are normal | a count averaging 0.8 a month is nothing like normal | the residual histogram | tests and intervals resting on the wrong distribution |

The replacement is a **generalised linear model for counts**. Poisson regression assumes the variance equals the mean. Negative binomial adds one parameter for extra spread.

Exposure goes in as an **offset**: a term whose coefficient is fixed at 1.

> log(expected count) = log(exposure) + intercept + trend + month effects

Fixing the coefficient at 1 says that an agency with twice the arrests is expected to have twice the incidents, all else equal, which is exactly what a rate means. The difference from modelling the rate directly is that the outcome stays a count, so the variance assumption stays right.

## Estimation

```python
poisson = smf.glm("n_uof ~ t + C(mon)", data=g, family=sm.families.Poisson(),
                  offset=np.log(g["n_arrests"])).fit()
```

Because the model is on the log scale, the coefficient on `t` is already a proportional change. Multiply by 12 and exponentiate for a yearly percentage.

## Worked Example

![Three panels. The first plots each agency's variance divided by its mean twice, once raw and once after fitting a model, showing the raw figure far above one for large agencies and the model based figure close to one for nearly all. The second shows Orrindale's lower prediction bounds, with the ordinary regression bound below zero for every month and the Poisson bound never below zero. The third compares the Poisson and negative binomial trend intervals for Ashfell against the true value](Figures/fig_a02_counts.png)

### Measure dispersion with a model, not with a ratio

The tempting check is variance divided by mean, looking for 1. Do not use it. That ratio is inflated by every bit of trend and season in the series, and the inflation grows with agency size because larger agencies have more visible structure.

| Agency | Mean a month | Raw variance over mean | **Dispersion after a model** |
|---|---|---|---|
| Orrindale | 0.8 | 0.96 | 0.94 |
| Dunmoor Tribal | 0.8 | 0.89 | 0.92 |
| Kelsmoor | 2.8 | 1.37 | 1.32 |
| Millgate | 7.6 | 1.45 | 1.16 |
| Havenbrook | 12.4 | 1.44 | 0.94 |
| Summit County | 22.8 | **3.42** | **1.12** |
| Tarnbridge | 28.2 | 2.84 | 1.38 |
| Stonewick | 58.8 | **4.34** | **1.04** |
| **Ashfell** | 101.0 | **8.46** | **1.76** |

Raw, Ashfell looks eight times overdispersed. After a model with a trend and month terms it is **1.76**. Stonewick goes from 4.34 to 1.04. **Most of the apparent overdispersion was the seasonal pattern and the trend.**

Several agencies come out slightly below 1, which is sampling noise in the estimate rather than genuine underdispersion.

**Dispersion is a property of a model's residuals, not of a series.** A reported dispersion figure is meaningless without the model it came from.

### Poisson against negative binomial

Ashfell, with arrests as exposure:

| Model | Trend | 95 percent interval | Width | Deviance over df |
|---|---|---|---|---|
| Poisson | **−5.32%** a year | −6.32 to −4.30 | **2.02** | 1.78 |
| Negative binomial | **−5.35%** a year | −6.57 to −4.11 | **2.46** | 1.23 |

**The estimate barely moves. The interval widens by about a fifth.**

That is the whole of it. Overdispersion does not bias the slope; it makes you more confident than you are entitled to be. A Poisson model fitted to overdispersed counts reports intervals that are too narrow and p values that are too small, and **nothing in its output looks wrong**. The deviance over degrees of freedom column is the quick check: around 1 means Poisson is adequate, and 1.78 says it is not.

### Where the Gaussian assumption fails visibly

At a large agency the wrong model gives slightly wrong intervals. At a small one it gives impossible ones.

Orrindale has eight officers and averages 0.8 incidents a month.

| | Months with a negative lower bound |
|---|---|
| Ordinary regression, 95 percent prediction intervals | **84 of 84** |
| Poisson with exposure | **0 of 84** |

Every single one. The lowest bound is **−1.55**, and a typical interval reads **[−1.48, 2.41]** for a quantity that cannot be negative.

Note what does **not** go wrong: the fitted values stay positive. The failure is in the intervals, which is the part people are least likely to plot and most likely to quote.

The constant variance assumption fails too, in the direction a count model predicts:

| Ordinary regression residual variance | |
|---|---|
| where the fitted value is low | **0.38** |
| where the fitted value is high | **1.02** |

## Recovering the Planted Answer

The dataset built Ashfell with a decline of **4.88 percent a year**. Poisson gives −5.32 and negative binomial −5.35, both intervals covering the truth. Ordinary regression on the rate gives an equivalent of −5.46 percent.

**All three recover the slope.** The choice of model is not about the point estimate; it is about everything else the model is asked to produce.

## Diagnostics

| Check | What to look at | Acceptable |
|---|---|---|
| Overdispersion | deviance over degrees of freedom, or Pearson dispersion | close to 1 for Poisson, otherwise use negative binomial |
| Impossible predictions | the lower bound of the prediction interval | never below zero for a count |
| Non constant spread | residual variance in the low and high halves of the fitted values | roughly equal after the right model |
| Excess zeros | share of zero months against what the model predicts | see [Module 9](Module_09_Rare_Events.md) |
| Exposure correctly specified | the offset coefficient, if you free it, should be near 1 | far from 1 means the exposure is wrong |

## Do It Yourself

> 📓 **Notebook:** [Module_02_Counts_Are_Not_Gaussian.ipynb](Notebooks/Module_02_Counts_Are_Not_Gaussian.ipynb)
> [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/OWNER/REPO/blob/main/Time_Series/Advanced/Notebooks/Module_02_Counts_Are_Not_Gaussian.ipynb)
> About 25 minutes.

The notebook builds the dispersion table, fits all three models, reproduces the Orrindale interval failure, and ends with an exercise comparing this module's dispersion estimate against the one Intermediate Module 8 obtained by a different route.

## When Not To Use This

| Situation | Reach for |
|---|---|
| The quantity is genuinely continuous, such as response time in minutes | ordinary regression, which is correct there |
| Half the months are zero | zero inflated or hurdle models, [Module 9](Module_09_Rare_Events.md) |
| You need the autocorrelation modelled as well | [Module 6](Module_06_Regression_With_ARMA_Errors.md), or a count model with lagged terms |
| Many agencies at once | [Module 10](Module_10_Panel_And_Hierarchical.md) |
| Only the point estimate is wanted, and the series is large | the difference is small, and you should say so |

That last row is the honest caveat. For Ashfell the Poisson and negative binomial slopes agree to two decimal places. **If all you report is the slope, the choice hardly matters. The moment you report an interval, a p value, or a prediction, it does.**

## Reporting the Result

> Monthly use of force counts were modelled with a negative binomial regression, with the log of arrests as an offset and indicator terms for calendar month. Ashfell's rate fell by 5.35 percent a year over 2019 to 2025, 95 percent interval 4.11 to 6.57 percent. A Poisson model gives the same point estimate with an interval a fifth narrower; its deviance over degrees of freedom of 1.78 indicates the extra spread that the negative binomial accounts for.

## Further Reading

- Cameron, A. C. and Trivedi, P. K. *Regression Analysis of Count Data*, on Poisson, negative binomial, and the diagnostics for choosing between them.
- Hilbe, J. M. *Negative Binomial Regression*, on overdispersion in practice.
- Hyndman, R. J. and Athanasopoulos, G. *Forecasting: Principles and Practice*, on why count data needs a different treatment from continuous series.

---

| | |
|---|---|
| **Previous** | [Module 1: Stationarity Tested, Not Eyeballed](Module_01_Stationarity_Tested.md) |
| **Next** | [Module 3: Model Selection, Diagnostics and Honest Uncertainty](Module_03_Model_Selection_And_Uncertainty.md) |
| **Builds on** | [Intermediate Module 3](../Intermediate/Module_03_Choosing_A_Denominator.md), [Intermediate Module 4](../Intermediate/Module_04_Why_Small_Agencies_Look_Volatile.md), [Intermediate Module 8](../Intermediate/Module_08_Rolling_Statistics_And_Control_Limits.md) |
| **Used again in** | [Module 8](Module_08_Count_Regression_With_Harmonics.md), [Module 9](Module_09_Rare_Events.md), [Module 10](Module_10_Panel_And_Hierarchical.md) |

*This module is part of a series developed for the Washington Data Exchange for Public Safety (WADEPS) through the Center for Interdisciplinary Statistical Education and Research (CISER) at Washington State University. Version 1.0, September 2026. Questions, errors, or suggestions: yin.zhang@wsu.edu*

*All examples use synthetic data created for teaching. They do not represent any real jurisdiction, agency, officer, or incident. See [Data/DATA_DICTIONARY.md](../../Data/DATA_DICTIONARY.md).*
