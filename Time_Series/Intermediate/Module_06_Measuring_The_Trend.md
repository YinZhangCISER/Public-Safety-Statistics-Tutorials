# Module 6: Measuring the Trend

> **Developed by Yin Zhang, PhD**, Assistant Professor, Department of Mathematics and Statistics, Washington State University

**The question this module answers:** *How much is this agency changing per year, and how sure can anyone be about that number?*

---

## The Question

Beginner [Topic 7](../Beginner/Topic_07_Trend.md) said to look at several years before judging a direction. This module puts a number on the direction.

The number is the easy part. The interval around it is the part that gets left out, and leaving it out is how "down 5 percent a year" comes to be quoted as though it were measured rather than estimated.

## The Idea in Plain Language

Fit a straight line to the **logarithm** of the series. The slope of that line is a constant **percentage** change per period, which is what people mean by a trend in public safety data. A line fitted to the raw series is a constant number of incidents per period, which is almost never what they mean.

Then report the confidence interval, because the slope is estimated from noisy data and the interval says how much the data actually pinned it down.

## The Method

```python
fit = smf.ols("np.log(rate) ~ t", data=whole_years).fit()
per_year = lambda b: 100 * (np.exp(12 * b) - 1)
low, high = fit.conf_int().loc["t"]
```

The slope comes out per month, so multiply by 12 and convert back from logs. Three refinements matter:

**Use whole calendar years, or add month effects.** A window that starts in January and ends in June is unbalanced across the seasonal cycle, and the imbalance leaks into the slope. Either trim to whole years or put `+ C(month)` in the formula.

**Month effects also narrow the interval.** Seasonal swing that the model does not explain is counted as error, which inflates the standard error of the slope for no reason.

**Check that nothing happened during the window.** One line assumes one story.

## Worked Example

Ashfell Police Department, use of force per 100 arrests, whole years 2019 to 2025. The dataset was built with a decline of about **4.9 percent a year**.

![Two panels. The left panel shows Ashfell's monthly rate in grey with a fitted exponential trend line in orange running from about 2.9 down to about 2.0. The right panel is a coefficient plot: four windows, each with a point estimate and a horizontal confidence interval, against a dashed vertical line marking the true trend](Figures/fig_m06_measuring_the_trend.png)

| Window | Estimate | 95 percent interval | Width |
|---|---|---|---|
| 2024 and 2025 only | −0.50% | −14.61 to +15.94 | **30.6** |
| 2021 through 2023 | −5.89% | −14.06 to +3.06 | 17.1 |
| 2019 through 2025 | −5.06% | −7.24 to −2.83 | 4.4 |
| 2019 through 2025, with month effects | −5.36% | −6.78 to −3.91 | **2.9** |

Every interval covers the truth. What differs is how much each one says.

**Two years of monthly data is compatible with almost anything.** The 2024 and 2025 window returns an estimate of −0.50 percent with an interval spanning a 15 percent annual improvement and a 16 percent annual deterioration. That is not a less accurate answer. It is an answer with no content.

**Seven years with month effects narrows the interval to under three points.** Adding the month terms barely moves the estimate and cuts the interval by a third, because the seasonal swing stops being counted as error.

**Even then, the honest statement is a range.** "Ashfell's rate is falling by about 5 percent a year, somewhere between 4 and 7" is what the data supports. "Falling 5.06 percent a year" is not.

### One slope assumes one story

Stonewick adopted the de escalation training in July 2023. Fitting a single line across the whole period produces a number that describes neither half of it:

| Fit | Estimate | 95 percent interval | Months |
|---|---|---|---|
| One line across everything | −6.65% | −8.58 to −4.68 | 84 |
| Before July 2023 | −5.45% | −9.54 to −1.16 | 54 |
| After July 2023 | −7.58% | −15.17 to +0.69 | 30 |

The single line is an average of two different periods, weighted by how many months fall in each. Before fitting any trend, ask whether something happened during the window. Fitting the right number of lines, and testing where they should break, is [Module 16](Module_16_Did_Something_Change.md) and Advanced Module 11.

## Do It Yourself

> 📓 **Notebook:** [Module_06_Measuring_The_Trend.ipynb](Notebooks/Module_06_Measuring_The_Trend.ipynb)
> [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/OWNER/REPO/blob/main/Time_Series/Intermediate/Notebooks/Module_06_Measuring_The_Trend.ipynb)
> About 20 minutes.

The notebook fits the log linear model, builds the window comparison, contrasts the regression with a simple compound growth rate, splits Stonewick at the programme date, and ends with an exercise recovering Summit County's built in decline of 12.2 percent a year.

## Pitfalls

| What goes wrong | What it looks like | What to do |
|---|---|---|
| Fitting on the raw scale | a trend in incidents per month that makes no sense across agency sizes | fit on `np.log` |
| Reporting the point estimate alone | false precision that survives into policy documents | always publish the interval |
| A window that is not whole years | the season leaks into the slope | trim to whole years, or add `C(month)` |
| A window under three years | an interval so wide it excludes nothing | say the period is too short rather than quoting the number |
| An intervention inside the window | one slope averaging two regimes | split, or model the break |
| Comparing slopes across agencies without intervals | ranking agencies on differences that are all noise | overlay the intervals before claiming a difference |
| First to last year growth rate as the only measure | two numbers standing in for eighty four | fine for communicating, not for deciding |

## Check Your Understanding

<details>
<summary><b>1.</b> An agency reports its use of force rate fell 12 percent a year over the last two years. What should be asked before that appears in a report?</summary>

The confidence interval. Two years of monthly data from a single agency typically supports an interval 20 to 30 points wide, so a point estimate of −12 percent is often compatible with everything from a large improvement to a modest deterioration. Ask for the interval and the number of months. If the interval crosses zero, the honest statement is that the period is too short to establish a direction.
</details>

<details>
<summary><b>2.</b> Why does adding a term for each calendar month narrow the interval without changing the estimate much?</summary>

Because the seasonal swing is predictable variation that the simpler model has no way to account for, so it lands in the residuals and inflates the standard error. Removing it shrinks the residuals and therefore the interval. The slope barely moves because the seasonal pattern is roughly balanced across a window of whole years, so it was not biasing the estimate, only obscuring it.
</details>

<details>
<summary><b>3.</b> Stonewick's single line says −6.65 percent a year with an interval that excludes zero. Is that a valid description of the agency?</summary>

It is a valid description of the seven year window and a poor description of the agency, because the programme launched in the middle of it. The number is a weighted average of a pre programme decline of about 5.5 percent and a post programme decline of about 7.6 percent. Quoting −6.65 percent implies a steady process that never existed. Report the two periods, or model the break explicitly.
</details>

## Key Takeaway

Fit on the log scale, use whole years or month effects, and never publish the slope without the interval. If the interval is wider than the effect anyone cares about, say the window is too short.

---

| | |
|---|---|
| **Previous** | [Module 5: Decomposition](Module_05_Decomposition.md) |
| **Next** | [Module 7: Seasonal Adjustment](Module_07_Seasonal_Adjustment.md) |
| **Builds on** | [Beginner Topic 7](../Beginner/Topic_07_Trend.md), [Module 5](Module_05_Decomposition.md) |
| **Used again in** | [Module 16](Module_16_Did_Something_Change.md), and throughout the Advanced series |

*This module is part of a series developed for the Washington Data Exchange for Public Safety (WADEPS) through the Center for Interdisciplinary Statistical Education and Research (CISER) at Washington State University. Version 1.0, September 2026. Questions, errors, or suggestions: yin.zhang@wsu.edu*

*All examples use synthetic data created for teaching. They do not represent any real jurisdiction, agency, officer, or incident. See [Data/DATA_DICTIONARY.md](../../Data/DATA_DICTIONARY.md).*
