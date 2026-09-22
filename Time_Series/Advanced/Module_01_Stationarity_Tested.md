# Module 1: Stationarity Tested, Not Eyeballed

> **Developed by Yin Zhang, PhD**, Assistant Professor, Department of Mathematics and Statistics, Washington State University

**The question this module answers:** *Is this series stable enough to model, and if not, what is the smallest transform that makes it so?*

---

## The Question

Beginner [Topic 17](../Beginner/Topic_17_Stationarity.md) asked whether a series holds still and answered by looking at it. That works for the obvious cases and fails for everything else, which is most of what you will meet.

Every model from [Module 4](Module_04_ARIMA_End_To_End.md) onward assumes stationarity somewhere. Getting the answer wrong in one direction leaves a trend in the residuals; getting it wrong in the other destroys information and inflates the variance of everything downstream.

## Model and Assumptions

A series is **weakly stationary** when its mean, its variance, and the covariance between any two points a fixed distance apart do not depend on where in time you look.

Two tests, and the essential point is that **their null hypotheses are opposite**.

| Test | Null hypothesis | A small p value is evidence |
|---|---|---|
| **ADF**, augmented Dickey Fuller | there is a unit root, so the series is **not** stationary | **for** stationarity |
| **KPSS** | the series **is** stationary | **against** stationarity |

Running only one gives half an answer, and which half depends on which test you happened to pick. Running both gives four possible verdicts, and the two that are not "stationary" or "not stationary" are the ones worth knowing about.

| | KPSS cannot reject | KPSS rejects |
|---|---|---|
| **ADF rejects** | **stationary**, model the level | **conflict**, usually a trend plus a stable part |
| **ADF cannot reject** | **inconclusive**, not enough evidence | **not stationary**, difference it |

## Estimation

```python
a_p = adfuller(s.dropna(), autolag="AIC")[1]
k_p = kpss(s.dropna(), regression="c", nlags="auto")[1]
```

**One detail that catches people.** KPSS p values come from a lookup table that stops at 0.01 and 0.10. A reported 0.010 means "0.01 or less" and 0.100 means "0.10 or more". Report them as bounds. Comparing a 0.100 against a 0.094 as though the difference meant something is a mistake the software will not stop you making.

## Worked Example

![Six panels. The top row shows Lakeshore County's rate bouncing around a flat level, Summit County's rate falling steadily, and Ashfell's counts. Below them a two by two grid names the four verdicts the pair of tests can give, and two bar charts show what happens to the variance and the lag one autocorrelation as a series is differenced more and more](Figures/fig_a01_stationarity.png)

| Series | ADF p | KPSS p | Verdict |
|---|---|---|---|
| Lakeshore County, rate | 0.000 | 0.100 | **stationary** |
| Summit County, rate | 0.895 | 0.010 | **not stationary** |
| Ashfell, rate | 0.633 | 0.010 | **not stationary** |
| **Ashfell, counts** | **0.554** | **0.094** | **inconclusive** |

Three of the four verdicts appear in one table.

**Lakeshore County is stationary**, which is what Beginner Topic 17 claimed from the chart alone. **Summit County is not**, which is what the dataset built into it: a decline of about 12 percent a year.

**Ashfell's counts are inconclusive.** Neither test rejects. That is a real answer and it is not the same as stationary: it says there is not enough evidence to decide.

### The count and the rate disagree, for a reason you already know

Ashfell's **rate** tests as not stationary while its **counts** are inconclusive. Nothing is inconsistent. Intermediate [Module 3](../Intermediate/Module_03_Choosing_A_Denominator.md) established that a rate's trend is the count's trend minus the denominator's:

| Ashfell, 2019 to 2025 | Trend per year |
|---|---|
| incident counts | −3.77% |
| arrests | **+1.33%** |
| rate per 100 arrests | −5.06% |

Growing arrests partly offset the falling incidents, so the count carries a weaker trend than the rate and the tests can see it less clearly. **Test the series you intend to model.** The verdict belongs to the series, not to the agency.

## Recovering the Planted Answer

The dataset gives every agency a decline of about 4.9 percent a year except Summit County at 12.2 percent, and gives Lakeshore no distinguishing feature. See [Data/GROUND_TRUTH.md](../../Data/GROUND_TRUTH.md).

The tests recover exactly that ordering: Summit County is decisively non stationary, Lakeshore is decisively stationary, and Ashfell sits between them, non stationary on the rate and undecided on the count. **A test that could not separate those three would not be worth running.**

## Diagnostics: differencing, and going too far

Differencing removes a trend. Doing it more than necessary has a signature: it **increases the variance** of what is left and drives the lag one autocorrelation toward **minus one half**.

Summit County, log rate:

| Transform | Observations left | Variance | Lag one autocorrelation |
|---|---|---|---|
| level | 88 | 0.195 | +0.65 |
| first difference | 87 | **0.138** | −0.47 |
| **twice differenced** | 86 | **0.410** | **−0.68** |
| **seasonal difference** | 76 | **0.115** | **−0.03** |
| first and seasonal | 75 | 0.235 | −0.59 |

One difference brings the variance down, which is the point. **Two push it back above the level's own variance**, which is worse than doing nothing.

The last two rows are the finding. **A seasonal difference on its own gives the lowest variance of any transform and a lag one autocorrelation of −0.03**, about as close to white noise as this series gets. Adding a first difference on top takes the variance back up to 0.235. For this series the combination that most software applies by default is over differencing.

After the right transform, both tests agree:

| Series | ADF p | KPSS p | Verdict |
|---|---|---|---|
| Summit County, log rate, differenced once | 0.000 | 0.100 | stationary |
| Ashfell, log rate, differenced once | 0.000 | 0.100 | stationary |

## Do It Yourself

> 📓 **Notebook:** [Module_01_Stationarity_Tested.ipynb](Notebooks/Module_01_Stationarity_Tested.ipynb)
> [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/YinZhangCISER/Public-Safety-Statistics-Tutorials/blob/main/Time_Series/Advanced/Notebooks/Module_01_Stationarity_Tested.ipynb)
> About 25 minutes.

The notebook builds a reusable `stationarity` function returning both p values and the verdict, reproduces both tables, and ends with an exercise on whether the Tarnbridge unrest month changes the answer.

## When Not To Use This

| Situation | Why the tests mislead |
|---|---|
| Fewer than about five years of monthly data | both tests are weak; **inconclusive** will be common and is the honest answer |
| A level shift in the middle of the series | a structural break looks like a unit root; use [Module 12](Module_12_Structural_Breaks.md) first |
| Strong seasonality not yet removed | the tests are confused by it; take a seasonal difference or deseasonalise |
| Choosing between transforms | the tests diagnose, they do not choose; compare variance and autocorrelation |
| You need to know whether there is an outlier | a different question entirely, and these tests are silent on it |

## Reporting the Result

> Summit County's use of force rate is not stationary over 2019 to 2026. The augmented Dickey Fuller test does not reject a unit root (p = 0.90) and KPSS rejects stationarity (p ≤ 0.01). A seasonal difference of the log rate is stationary on both tests and leaves the lowest residual variance of the transforms considered; a first difference in addition to it over differences the series. Analyses below therefore use a single seasonal difference.

The caveats that travel with it: the tests are weak in a series this short, they cannot distinguish a unit root from a structural break, and passing them says nothing about outliers or changing variance.

## Further Reading

- Hyndman, R. J. and Athanasopoulos, G. *Forecasting: Principles and Practice*, chapter on stationarity and differencing. Free at otexts.com/fpp3.
- Kwiatkowski, D., Phillips, P. C. B., Schmidt, P. and Shin, Y. (1992). Testing the null hypothesis of stationarity against the alternative of a unit root. *Journal of Econometrics*, 54.
- Box, G. E. P., Jenkins, G. M., Reinsel, G. C. and Ljung, G. M. *Time Series Analysis: Forecasting and Control*, on the cost of over differencing.

---

| | |
|---|---|
| **Next** | [Module 2: Incident Counts Are Not Gaussian](Module_02_Counts_Are_Not_Gaussian.md) |
| **Builds on** | [Beginner Topic 17](../Beginner/Topic_17_Stationarity.md), [Intermediate Module 3](../Intermediate/Module_03_Choosing_A_Denominator.md), [Intermediate Module 5](../Intermediate/Module_05_Decomposition.md) |
| **Used again in** | [Module 4](Module_04_ARIMA_End_To_End.md), [Module 5](Module_05_SARIMA.md), [Module 11](Module_11_Interrupted_Time_Series.md) |

*This module is part of a series developed for the Washington Data Exchange for Public Safety (WADEPS) through the Center for Interdisciplinary Statistical Education and Research (CISER) at Washington State University. Version 1.0, September 2026. Questions, errors, or suggestions: yin.zhang@wsu.edu*

*All examples use synthetic data created for teaching. They do not represent any real jurisdiction, agency, officer, or incident. See [Data/DATA_DICTIONARY.md](../../Data/DATA_DICTIONARY.md).*
