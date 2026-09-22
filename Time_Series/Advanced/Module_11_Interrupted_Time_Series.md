# Module 11: Interrupted Time Series Done Properly

> **Developed by Yin Zhang, PhD**, Assistant Professor, Department of Mathematics and Statistics, Washington State University

**The question this module answers:** *Did something change when the policy took effect, and how much of that answer is the design rather than the data?*

---

## The Question

An interrupted time series asks whether something changed when a policy took effect. It is the most widely used design in public safety evaluation and the easiest one to run badly.

This module separates a **level change** from a **slope change** and shows why that separation is harder than it looks, runs the **parallel trends** check that decides whether the design is usable at all, and is honest about what a single agency can establish.

## Model and Assumptions

> log(mu) = log(arrests) + intercept + b1·time + seasonal + b2·phase + b3·post + b4·(time since post)
>
> **b3** is the level change. **b4** is the slope change.

Almost every published interrupted time series splits the data at one date. This programme had **three** periods: before, a four month phase in from July 2023, and the settled period from November. Folding the phase in months into "before" says the programme did nothing while it was being introduced; folding them into "after" says it had full effect from day one.

| Assumption | Diagnostic | Consequence of failing |
|---|---|---|
| The counterfactual is the extrapolated pre trend | is there a comparison group instead | the secular trend becomes the effect |
| Treated and comparison groups were moving alike | pre period trend test, and a plot | the estimate carries someone else's trend |
| The intervention date is right | phase in modelled separately | the effect is diluted across the transition |
| The level and slope terms are separately identified | correlation between the step and the trend | the two trade off and neither means anything |
| Residuals are not autocorrelated | Ljung Box | the interval is wrong, in either direction |

## Estimation

```python
poisson("n_uof ~ C(agency_id) + C(year_month) + treated:phase + treated:post", clean)
```

## Worked Example

![Two panels. The left shows Stonewick's use of force rate with the pre period trend extrapolated across the intervention, the phase in months shaded, and the note that the level term here is minus 3.0 percent with an interval from minus 13.4 to plus 8.7. The right compares two controlled specifications across the settled window: a sloped path running from minus 4 to minus 21 percent and a flat line at minus 12.6, which cross at the window's midpoint where the sloped path averages minus 12.7](Figures/fig_a11_its.png)

### A single agency, done correctly, and still not enough

Stonewick, with a trend, a season, a phase in term and a level term:

| Specification | Level change | 95 percent interval |
|---|---|---|
| Level change only | −3.0% | [−13.4, +8.7] |
| Level and slope | +2.4% | [−10.0, +16.6] |

Nothing here is wrong, and the interval is **22 percentage points wide**. That is the correct result, not a failure, and the reason is in the design matrix:

| Quantity | Value |
|---|---|
| Correlation between the level indicator and the trend | **0.821** |
| Standard error on the level term | 0.0578 |
| Standard error on the trend | 0.0125 |

The step sits in the last third of the series, so a downward step and a steeper slope explain the same data and the model splits the difference. **This is not fixed by a better estimator.** It is fixed by a comparison group, which pins the trend down from agencies the programme did not touch.

### Parallel trends: the check that decides everything

| Pre programme trend | Estimate | 95 percent interval |
|---|---|---|
| A007 alone | **−11.96% a year** | [−15.43, −8.36] |
| The other treated agencies | −5.17% a year | [−7.04, −3.26] |
| The comparison agencies | −4.46% a year | [−6.13, −2.77] |

A007 was falling at twice everyone else's rate **four years before the training existed**. The formal interaction test:

| | Difference in pre trends | p |
|---|---|---|
| A007 excluded | −0.70% a year | 0.603 |
| A007 included | −2.16% a year | **0.087** |

Note that carefully. With A007 in, the group level test returns p = 0.087 and **passes at the conventional threshold**, while the violation is glaring the moment A007 is looked at on its own. **A test that passes is not evidence that trends are parallel; with a handful of agencies it is mostly evidence that the test is underpowered.** Plot the pre period and look at every agency.

### The controlled version, and the central result

| Specification | Phase in | Level change | Slope change | AIC |
|---|---|---|---|---|
| Level and slope | −9.4% | **−3.4%** [−13.8, +8.3] | **−7.6% a year** [−14.3, −0.4] | **4741.5** |
| Level change only | −9.4% | **−12.6%** [−17.9, −6.9] | | 4743.7 |

The truth is a **pure 12 percent level drop with no slope change**. The level only model is right. The model with a slope term reports a modest immediate drop and a continuing improvement whose interval **excludes zero**, and **AIC prefers it by 2.2 points.**

Anyone reporting the second specification would write that the programme produced a small initial effect that keeps growing. That sentence is entirely an artefact.

| Years since fully in place | What the sloped model says |
|---|---|
| 0.08 | −4.0% |
| 1.08 | −11.3% |
| 2.08 | −18.0% |
| **Average over the window** | **−12.7%** |

The two specifications disagree at every single month and agree on the average. **The average effect over a stated window is identified. The decomposition into a level and a slope is not.**

### Autocorrelation robust standard errors

| Standard errors | Estimate | Interval | se |
|---|---|---|---|
| Classical | −2.5% | [−13.7, +10.2] | 0.0615 |
| Newey West, 12 lags | −2.5% | [−11.3, +7.2] | **0.0483** |

The robust interval is **narrower**. Ljung Box on the residuals gives p = 0.272: once the seasonal terms are in the model there is no autocorrelation left to correct, so the robust estimator is just a different finite sample estimate of the same quantity.

**Robust standard errors are not a safety margin.** Use them when the diagnostic says so, and report the diagnostic either way.

## Recovering the Planted Answer

The truth is a 12 percent level reduction with no slope change, at five agencies, from November 2023, with one of the five on a pre existing trend of its own.

The correct specification returns **−12.6 percent** [−17.9, −6.9]. The pre trend test identifies A007 when A007 is examined individually. The slope term, added to a model where no slope exists, produces a statistically significant slope.

## Diagnostics

| Check | Acceptable |
|---|---|
| Intervention date | fixed before any estimate is seen |
| Transition period | modelled separately, not folded into either side |
| Pre period trends | tested as a group **and** plotted agency by agency |
| Level and slope terms | if they disagree about shape while agreeing on the average, report the average |
| Correlation between the step and the trend | if above about 0.7, say the decomposition is not identified |
| Ljung Box on residuals | reported, whether or not robust errors are used |

## Do It Yourself

> 📓 **Notebook:** [Module_11_Interrupted_Time_Series.ipynb](Notebooks/Module_11_Interrupted_Time_Series.ipynb)
> [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/YinZhangCISER/Public-Safety-Statistics-Tutorials/blob/main/Time_Series/Advanced/Notebooks/Module_11_Interrupted_Time_Series.ipynb)
> About 40 minutes.

The exercise varies the intervention date and the length of the follow up, and finds that only one of the two changes the answer.

## When Not To Use This

| Situation | Reach for |
|---|---|
| Nobody told you the date | [Module 12](Module_12_Structural_Breaks.md) |
| The response shape is the question | [Module 13](Module_13_Intervention_Analysis.md) |
| One agency, small effect | do not; the design cannot resolve it |
| No comparison group is available | say so, and report the estimate as descriptive |
| The comparison agencies were also affected | Intermediate [Module 12](../Intermediate/Module_12_Building_A_Peer_Benchmark_Series.md), and the [Causal Inference series](../../Causal_Inference/) |

## Reporting the Result

> Use of force was modelled as monthly counts with the log of arrests as an offset, agency and calendar month fixed effects, and separate indicators for the programme's four month phase in and its settled period from November 2023. Over the settled period, rates at the treated agencies ran 12.6 percent below the comparison agencies, 95 percent interval from 17.9 to 6.9 percent below. One agency was excluded because its pre programme trend, a decline of 12.0 percent a year against 4 to 5 percent elsewhere, is inconsistent with the comparison group. A specification adding a post intervention slope term fits marginally better by AIC and attributes the change to a smaller level shift plus a continuing 7.6 percent annual improvement; the two specifications agree on the average effect over the window and cannot be distinguished by these data, so the average is reported and no claim is made about the shape of the response.

## Further Reading

- Bernal, J. L., Cummins, S. and Gasparrini, A. (2017). Interrupted time series regression for the evaluation of public health interventions. *International Journal of Epidemiology*, 46.
- Bhaskaran, K. et al. (2013). Time series regression studies in environmental epidemiology. *International Journal of Epidemiology*, 42.
- Angrist, J. D. and Pischke, J. S. (2009). *Mostly Harmless Econometrics*. Princeton University Press. Chapter 5.

---

| | |
|---|---|
| **Previous** | [Module 10: Panel and Hierarchical Time Series](Module_10_Panel_And_Hierarchical.md) |
| **Next** | [Module 12: Structural Breaks and Changepoints](Module_12_Structural_Breaks.md) |
| **Builds on** | [Module 6](Module_06_Regression_With_ARMA_Errors.md), [Module 10](Module_10_Panel_And_Hierarchical.md), [Intermediate Module 16](../Intermediate/Module_16_Did_Something_Change.md) |
| **Used again in** | [Module 13](Module_13_Intervention_Analysis.md), [Module 14](Module_14_Reporting_And_Reproducibility.md) |

*This module is part of a series developed for the Washington Data Exchange for Public Safety (WADEPS) through the Center for Interdisciplinary Statistical Education and Research (CISER) at Washington State University. Version 1.0, September 2026. Questions, errors, or suggestions: yin.zhang@wsu.edu*

*All examples use synthetic data created for teaching. They do not represent any real jurisdiction, agency, officer, or incident. See [Data/DATA_DICTIONARY.md](../../Data/DATA_DICTIONARY.md).*
