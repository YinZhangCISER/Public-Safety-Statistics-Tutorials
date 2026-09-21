# Module 10: Reading ACF and PACF as Pictures

> **Developed by Yin Zhang, PhD**, Assistant Professor, Department of Mathematics and Statistics, Washington State University

**The question this module answers:** *How do I know whether my model has finished, and whether its confidence intervals can be believed?*

---

## The Question

Beginner [Topic 16](../Beginner/Topic_16_Autocorrelation.md) showed that a series resembles its own recent past. The autocorrelation function puts that on a chart, one bar per lag.

Drawn on a raw series it mostly tells you what you already knew. Drawn on a model's **residuals** it does two things nothing else does: it tells you whether the model has anything left to explain, and it tells you whether the confidence intervals are trustworthy.

## The Idea in Plain Language

**The ACF at lag k** is the correlation between the series and itself shifted by k periods. **The PACF at lag k** is what lag k contributes on its own, after everything reaching it through shorter lags has been removed.

Both come with a noise band, roughly ±1.96/√n. Bars inside it are indistinguishable from zero.

**Ljung Box** tests all the lags at once, so you do not have to judge twenty four bars by eye. A small p value means structure remains.

## The Method

```python
res = smf.ols("np.log(rate) ~ t + C(mon)", data=whole).fit().resid
a = acf(res, nlags=24, fft=False)
p = acorr_ljungbox(res, lags=[12], return_df=True)["lb_pvalue"].iloc[0]
```

Then the order of operations, which matters more than any of the numbers:

1. Fit the model you think is right.
2. Run the ACF and Ljung Box **on the residuals**.
3. If structure remains, **fix the model**. Missing seasonal terms is a modelling error, not a standard error problem.
4. Once the residuals are clean, check whether autocorrelation robust standard errors change anything.

## Worked Example

Grandview Police Department, use of force per 100 arrests, whole years.

### On the raw series, the ACF is the calendar

| Lag | 1 | 3 | 6 | 9 | 12 | 18 | 24 |
|---|---|---|---|---|---|---|---|
| **ACF** | +0.60 | +0.04 | **−0.54** | +0.04 | **+0.63** | −0.42 | +0.55 |

A wave with a twelve month period: strongly positive at lag 12, strongly negative at lag 6, where summer lines up against winter. That is seasonality, and an ACF on any raw seasonal series will always show it.

### On the residuals, it becomes a test of the model

![Two panels of autocorrelation bars with a shaded noise band. The left panel, from a model with a trend only, has many bars far outside the band in a wave pattern. The right panel, from a model with a trend and month terms, has all bars inside or near the band](Figures/fig_m10_autocorrelation.png)

| Model | Lags outside the band, of 24 | Ljung Box p at lag 12 |
|---|---|---|
| Trend only | many | **0.0000** |
| Trend and month terms | few | **0.2089** |

With a trend only, the residuals still contain the whole seasonal cycle and the test rejects overwhelmingly. Add month terms and it no longer rejects. **That is the model telling you it is finished**, and it is a more useful statement than any coefficient in it.

### Why this changes your conclusions

Ordinary regression assumes independent errors. If they are not, every confidence interval is wrong.

| Model, trend and month terms | Estimate | Interval | Width |
|---|---|---|---|
| Ordinary standard errors | −5.36% a year | −6.78 to −3.91 | 2.87 |
| Autocorrelation robust | −5.36% a year | −5.92 to −4.80 | **1.12** |

Two things follow, and the second contradicts advice you will often hear.

**The estimate does not move.** Autocorrelation does not bias the slope. It affects only how certain you may be about it.

**The interval here gets narrower, not wider.** The familiar warning is that autocorrelation makes ordinary standard errors too small. That warning assumes **positive** autocorrelation. These residuals are negatively correlated at most lags, and negative autocorrelation makes ordinary standard errors too **large**.

So the rule is not "autocorrelation inflates your confidence". It is **"ignoring autocorrelation gives you the wrong interval, and you have to look to find out in which direction"**.

## Do It Yourself

> 📓 **Notebook:** [Module_10_Reading_Autocorrelation.ipynb](Notebooks/Module_10_Reading_Autocorrelation.ipynb)
> [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/OWNER/REPO/blob/main/Time_Series/Intermediate/Notebooks/Module_10_Reading_Autocorrelation.ipynb)
> About 20 minutes.

The notebook builds both ACFs, runs Ljung Box, compares ordinary against robust standard errors, and ends with an exercise on Cedar Falls that shows an autocorrelation test and an outlier check finding completely different things.

## Pitfalls

| What goes wrong | What it looks like | What to do |
|---|---|---|
| Reading the ACF of a raw seasonal series | a dramatic wave that says only "there is a season" | run it on residuals |
| Patching standard errors instead of fixing the model | robust errors applied to a model missing month terms | add the terms first |
| Assuming autocorrelation always widens intervals | a robust interval that comes out narrower and gets discarded | look at the sign of the autocorrelation |
| Eyeballing twenty four bars | one bar outside the band treated as a finding | use Ljung Box, which tests them jointly |
| Expecting Ljung Box to catch an outlier | a model passing the test with one enormous residual | run an outlier check as well |
| Too few observations | a noise band so wide nothing is ever outside it | at least four or five years of monthly data |

## Check Your Understanding

<details>
<summary><b>1.</b> A model's residual ACF has a large positive bar at lag 12 and nothing else outside the band. What is missing?</summary>

A seasonal term. A spike at exactly the seasonal period means the model has not accounted for the annual pattern, so each month's residual resembles the same month a year earlier. The fix is to add month terms, or a seasonal component, and refit. Applying robust standard errors instead would leave a predictable pattern in the residuals and would not improve the estimate at all.
</details>

<details>
<summary><b>2.</b> Ordinary and robust standard errors give almost identical intervals. What does that tell you?</summary>

That the residuals are close to independent, so the ordinary assumption is doing no harm. It is a reassuring result and worth reporting, because a reader cannot tell the difference from the coefficient table alone. It does not mean the model is correct in other respects: the residuals could still contain an outlier, a level shift, or heteroskedasticity, none of which this comparison examines.
</details>

<details>
<summary><b>3.</b> Why is it wrong to fix autocorrelated residuals with robust standard errors when the cause is a missing seasonal term?</summary>

Because the two problems are different. Robust standard errors assume the model captures the systematic part correctly and only the error structure is misspecified. A missing seasonal term means the systematic part is wrong: the model is attributing predictable, explainable variation to error. Robust errors will widen or narrow the interval around an estimate that is still being asked to absorb a pattern it should have modelled. Fix the model first; then, and only then, ask about the errors.
</details>

## Key Takeaway

Run the ACF on residuals, not on the series. If Ljung Box rejects, fix the model. Only once the residuals are clean is it worth asking whether the standard errors need adjusting, and then look at the direction rather than assuming it.

---

| | |
|---|---|
| **Previous** | [Module 9: Year over Year, Rolling Totals and Indexing](Module_09_Year_Over_Year_And_Indexing.md) |
| **Next** | [Module 11: Lead and Lag Between Two Series](Module_11_Lead_And_Lag.md) |
| **Builds on** | [Beginner Topic 16](../Beginner/Topic_16_Autocorrelation.md), [Module 6](Module_06_Measuring_The_Trend.md) |
| **Used again in** | [Module 11](Module_11_Lead_And_Lag.md), and Advanced Modules 3, 4 and 11 |

*This module is part of a series developed for the Washington Data Exchange for Public Safety (WADEPS) through the Center for Interdisciplinary Statistical Education and Research (CISER) at Washington State University. Version 1.0, September 2026. Questions, errors, or suggestions: yin.zhang@wsu.edu*

*All examples use synthetic data created for teaching. They do not represent any real jurisdiction, agency, officer, or incident. See [Data/DATA_DICTIONARY.md](../../Data/DATA_DICTIONARY.md).*
