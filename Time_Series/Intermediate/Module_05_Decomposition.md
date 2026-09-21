# Module 5: Decomposition into Trend, Season and Remainder

> **Developed by Yin Zhang, PhD**, Assistant Professor, Department of Mathematics and Statistics, Washington State University

**The question this module answers:** *A series contains a trend and a season at the same time. How do I get them out as separate numbers?*

---

## The Question

Beginner [Topic 7](../Beginner/Topic_07_Trend.md) and [Topic 8](../Beginner/Topic_08_Seasonality.md) argued that a public safety series carries a long run direction and a repeating annual shape simultaneously, and that confusing them causes most misreadings.

Decomposition does that separation arithmetically and hands back three series you can chart, measure and model independently. It is the operation that makes Modules 6, 7 and 8 possible.

## The Idea in Plain Language

Every value is treated as the product of three things:

**observed = trend × season × remainder**

- **Trend** is the level, once the calendar and the noise are gone.
- **Season** is the repeating shape, expressed as a multiplier. A factor of 1.45 means the calendar alone puts that month 45 percent above the level.
- **Remainder** is whatever the first two do not explain. It should look like noise around 1.0.

Multiplying rather than adding is almost always right for counts. A department running at 100 a month and one at 10 do not both get 40 extra incidents in July; both run about 40 percent high. Multiplying also keeps the pieces from implying negative counts.

## The Method

Taking logs turns multiplication into addition, so a multiplicative decomposition is an additive one on the log scale:

```python
from statsmodels.tsa.seasonal import STL

stl = STL(np.log(series), period=12, robust=True).fit()
trend, season, remainder = np.exp(stl.trend), np.exp(stl.seasonal), np.exp(stl.resid)
```

STL, which stands for seasonal and trend decomposition using loess, is the sensible default over the older `seasonal_decompose`. It lets the seasonal shape drift slowly across years rather than forcing one fixed shape, and `robust=True` stops a single extraordinary month from bending the trend around it.

Four things it needs from you:

| Requirement | Why | What happens otherwise |
|---|---|---|
| A complete series, no gaps | loess cannot span a hole | an error, or silently wrong output |
| At least two full cycles, preferably four | the seasonal shape is averaged across years | unstable, meaningless factors |
| `robust=True` when outliers exist | one month otherwise bends the trend | a bump in the trend around the event |
| Provisional months removed | the final points drag the trend | a downturn that is not real |

## Worked Example

Ashfell Police Department, 88 finished months.

![Four stacked panels on the left showing the observed series, the trend falling from about 119 to about 90, the repeating seasonal factor, and the remainder scattered around 1.0. A panel on the right compares the seasonal factor of counts, arrests and the rate, showing counts and arrests peaking in August while the rate peaks in July](Figures/fig_m05_decomposition.png)

**The trend** falls from about **119** incidents a month in early 2019 to about **90** by 2026. **The season** runs from roughly 0.71 in February to 1.45 in August. **The remainder** puts 56 percent of months within 10 percent of what the trend and season predicted, and shows no obvious pattern, which is what it should do.

### Which series you decompose changes the answer

| Seasonal factor | Jan | Feb | Mar | Apr | May | Jun | Jul | Aug | Sep | Oct | Nov | Dec | Peak |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Counts | 0.78 | 0.71 | 0.86 | 0.94 | 1.10 | 1.30 | 1.44 | **1.45** | 1.11 | 0.99 | 0.86 | 0.80 | August |
| Arrests | 0.93 | 0.84 | 0.94 | 1.02 | 0.97 | 1.09 | 1.09 | **1.18** | 1.09 | 0.99 | 0.98 | 0.95 | August |
| Rate per 100 arrests | 0.80 | 0.81 | 0.87 | 0.98 | 1.15 | 1.11 | **1.34** | 1.27 | 1.07 | 0.99 | 0.92 | 0.88 | July |

Ashfell's **counts** peak in August. Its **rate** peaks in July. Both are correct, because a count carries two seasonal patterns at once: the rate has one and the denominator has another, and the count is the product.

So the choice is the same one [Module 3](Module_03_Choosing_A_Denominator.md) made. If the question is about **officer behaviour**, decompose the rate. If it is about **workload**, decompose the count. Reporting a seasonal pattern without saying which series it came from is not enough.

### Checking against the answer key

The dataset was built with a July peak in the use of force rate, amplitude 0.20. See [Data/GROUND_TRUTH.md](../../Data/GROUND_TRUTH.md). STL recovers **July** as the peak and an amplitude of **0.27**. The month is exactly right; the amplitude is in the right neighbourhood and slightly overstated, which is what one agency's seven years supports.

## Do It Yourself

> 📓 **Notebook:** [Module_05_Decomposition.ipynb](Notebooks/Module_05_Decomposition.ipynb)
> [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/OWNER/REPO/blob/main/Time_Series/Intermediate/Notebooks/Module_05_Decomposition.ipynb)
> About 20 minutes.

The notebook compares additive with multiplicative, runs STL, verifies that the three pieces multiply back to the original, builds the comparison table above, and ends with an exercise on what happens to Tarnbridge when `robust=True` is switched off.

## Pitfalls

| What goes wrong | What it looks like | What to do |
|---|---|---|
| Additive model on counts | seasonal effect of a fixed size across a changing level | use logs, which makes it multiplicative |
| `robust=False` with an outlier present | the trend rises and falls around a one off event | `robust=True`, and find the outliers first |
| Fewer than three years | seasonal factors that change completely when a year is added | do not publish a seasonal pattern from two years |
| Gaps in the series | an error, or a silent failure | repair the calendar first, [Module 2](Module_02_Building_An_Honest_Calendar.md) |
| Provisional months included | a trend that turns down at the right hand edge | drop them before fitting |
| Reporting the seasonal pattern of a count as if it were behaviour | a July claim from an August peak | say which series was decomposed |
| Reading the last trend point as final | it moves when next month arrives | treat the end of the trend as provisional |

## Check Your Understanding

<details>
<summary><b>1.</b> Why does Ashfell's count peak in August while its rate peaks in July?</summary>

Because the count is the rate multiplied by the number of arrests, and both have their own seasonal shape. The rate is highest in July at 1.34. Arrests are highest in August at 1.18. Multiplying the two pushes the product's peak into August. Neither series is wrong; they answer different questions, and a report that says "use of force peaks in August" is describing workload while one that says "July" is describing how contacts are handled.
</details>

<details>
<summary><b>2.</b> The remainder for one agency shows a clear run of values above 1.0 for eight consecutive months. What does that tell you?</summary>

That the decomposition has missed something. The remainder is supposed to be what is left after the systematic parts are removed, so a sustained run in it means there is structure the trend and season did not capture: a level shift, a policy change, or a data problem starting on a particular date. Eight months in the same direction is far too long to be chance. Treat it as a finding and go looking for the cause, rather than as a residual to ignore.
</details>

<details>
<summary><b>3.</b> An agency has three years of data. Is that enough to publish a seasonal pattern?</summary>

Barely, and with a caveat attached. Each month's factor is effectively an average of three observations, so a single unusual July moves the July factor a long way. Publish it with the number of years stated, show the year to year spread rather than only the average, and re estimate when the fourth year arrives. Two years is not enough for anything.
</details>

## Key Takeaway

Split the series before analysing it, use STL on logs with `robust=True`, and say which series you decomposed, because the count and the rate do not have the same season.

---

| | |
|---|---|
| **Previous** | [Module 4: Why Small Agencies Look Volatile](Module_04_Why_Small_Agencies_Look_Volatile.md) |
| **Next** | [Module 6: Measuring the Trend](Module_06_Measuring_The_Trend.md) |
| **Builds on** | [Beginner Topic 7](../Beginner/Topic_07_Trend.md), [Beginner Topic 8](../Beginner/Topic_08_Seasonality.md), [Module 2](Module_02_Building_An_Honest_Calendar.md) |
| **Used again in** | [Module 7](Module_07_Seasonal_Adjustment.md), [Module 8](Module_08_Rolling_Statistics_And_Control_Limits.md) |

*This module is part of a series developed for the Washington Data Exchange for Public Safety (WADEPS) through the Center for Interdisciplinary Statistical Education and Research (CISER) at Washington State University. Version 1.0, September 2026. Questions, errors, or suggestions: yin.zhang@wsu.edu*

*All examples use synthetic data created for teaching. They do not represent any real jurisdiction, agency, officer, or incident. See [Data/DATA_DICTIONARY.md](../../Data/DATA_DICTIONARY.md).*
