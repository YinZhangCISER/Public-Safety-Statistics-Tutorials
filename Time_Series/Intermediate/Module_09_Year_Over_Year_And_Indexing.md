# Module 9: Year over Year, Rolling Totals and Indexing

> **Developed by Yin Zhang, PhD**, Assistant Professor, Department of Mathematics and Statistics, Washington State University

**The question this module answers:** *A monthly report has to say something about last month. Which comparison belongs in it?*

---

## The Question

[Module 7](Module_07_Seasonal_Adjustment.md) removed the season by estimating factors and dividing them out. That is powerful and it has a cost: the factors are estimated, so they get revised.

Three other presentations need no estimation at all. They suit different documents, and choosing badly is how a report ends up saying something it did not mean.

## The Idea in Plain Language

| Presentation | What it does | What it costs |
|---|---|---|
| **Year over year** | compares each month to the same month a year earlier | noisy, because it uses two single months |
| **Rolling twelve month total** | adds the last twelve months, so the season cancels by construction | slow, because an event stays in the window for a year |
| **Index to a base period** | sets a base period to 100 and reads everything as a percentage of it | says nothing about level, only about movement |

None of them needs a model, and none of them will ever be revised.

## The Method

```python
yoy      = 100 * (s / s.shift(12) - 1)
rolling  = s.rolling(12).sum()
indexed  = 100 * s / s.loc["2019"].mean()
```

The rolling total is the one worth dwelling on. Every twelve month window contains exactly one of each calendar month, so the seasonal contribution is identical in every window and cannot move the line. That is a stronger guarantee than seasonal adjustment offers, and it needs no estimation.

## Worked Example

Grandview Police Department.

![Three panels. The first shows the monthly count in grey with a much steadier rolling twelve month average in blue. The second shows year over year percentage change as bars above and below zero. The third indexes four agencies of very different sizes to their own 2019 average, putting them all on one readable axis](Figures/fig_m09_presentations.png)

### How steady each one is

| | Variability |
|---|---|
| Raw monthly count | **29.3** percent of its own mean |
| Rolling twelve month total | **8.0** percent of its own mean |
| Month on month change | standard deviation **28.6** percentage points |
| Year over year change | standard deviation **22.6** percentage points |

Year over year is calmer than month on month, but not by much, because both are built from individual months. The rolling total is in a different class.

### The rolling total as a headline

| Twelve months ending December | 2019 | 2020 | 2021 | 2022 | 2023 | 2024 | 2025 |
|---|---|---|---|---|---|---|---|
| **Incidents** | 1,405 | 1,274 | 1,224 | 1,254 | 1,136 | 1,131 | 1,058 |

Seven numbers, a clear direction, nothing to argue about. This is why the rolling twelve month total is the usual headline figure in an annual report, and why it is a poor choice for detecting anything: an event enters the window and stays for a year.

### Indexing puts different sizes on one chart

An eight officer department and a 902 officer department cannot share an axis measured in incidents. They can share one measured in percent of their own 2019.

Read across such a chart and you are comparing **how far each agency has moved from its own starting point**, not how they compare in level. Two warnings follow: the base period must be an ordinary one, and an agency at 70 on the index may still have a higher rate than one at 110.

## Do It Yourself

> 📓 **Notebook:** [Module_09_Year_Over_Year_And_Indexing.ipynb](Notebooks/Module_09_Year_Over_Year_And_Indexing.ipynb)
> [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/OWNER/REPO/blob/main/Time_Series/Intermediate/Notebooks/Module_09_Year_Over_Year_And_Indexing.ipynb)
> About 15 minutes.

The notebook builds all three, compares their variability, and ends with an exercise finding months where year over year and the rolling total point in opposite directions.

## Pitfalls

| What goes wrong | What it looks like | What to do |
|---|---|---|
| Saying "incidents are up" without naming the comparison | two people reading the same report disagree | always name the comparison and the period |
| Using a rolling total to detect a change | the line moves a year after the event | use a control chart, [Module 8](Module_08_Rolling_Statistics_And_Control_Limits.md) |
| Indexing to an unusual base year | every later figure measured against an outlier | pick an ordinary base and say which it is |
| Reading an index as a level | an agency at 70 assumed to be safer than one at 110 | an index measures movement, never level |
| Year over year against a month that contained an event | a meaningless percentage | check the base month before dividing |
| A rolling total with months missing from the window | a total silently short by one month | repair the calendar first, [Module 2](Module_02_Building_An_Honest_Calendar.md) |

## Check Your Understanding

<details>
<summary><b>1.</b> Why does the rolling twelve month total remove the season without estimating anything?</summary>

Because every window of twelve consecutive months contains exactly one January, one February and so on. The seasonal contribution to the total is therefore the same in every window, and sliding the window forward by one month cannot change it. Seasonal adjustment achieves the same thing by estimating factors, which is more flexible and introduces something that can be revised. The rolling total's guarantee is arithmetic rather than statistical.
</details>

<details>
<summary><b>2.</b> A report shows year over year up 4 percent and the rolling twelve month total down. Is one of them wrong?</summary>

No. They are different comparisons. Year over year compares one month to one month. The rolling total compares a twelve month window to the window one month earlier, which differs only by dropping the oldest month and adding the newest. If the month that dropped out was higher than the month that came in, the rolling total falls even while this month beats the same month last year. Both are true, which is exactly why a report must name the comparison rather than saying "incidents are up".
</details>

<details>
<summary><b>3.</b> When would indexing mislead?</summary>

Whenever the reader takes it as a statement about level. An agency that has cut its rate from very high to merely high will show a low index and still be among the worst performers. Indexing answers "how much has this agency changed", and it must be published alongside the level, or next to a peer comparison, if the reader needs to know where the agency actually stands.
</details>

## Key Takeaway

Use year over year for a monthly line, a rolling twelve month total for an annual headline, and an index when agencies of different sizes share a chart. Name the comparison every time.

---

| | |
|---|---|
| **Previous** | [Module 8: Rolling Statistics and Control Limits](Module_08_Rolling_Statistics_And_Control_Limits.md) |
| **Next** | [Module 10: Reading ACF and PACF as Pictures](Module_10_Reading_Autocorrelation.md) |
| **Builds on** | [Beginner Topic 18](../Beginner/Topic_18_Year_Over_Year_Comparison.md), [Module 7](Module_07_Seasonal_Adjustment.md) |
| **Used again in** | [Module 13](Module_13_Baseline_Forecasts.md), [Module 16](Module_16_Did_Something_Change.md) |

*This module is part of a series developed for the Washington Data Exchange for Public Safety (WADEPS) through the Center for Interdisciplinary Statistical Education and Research (CISER) at Washington State University. Version 1.0, September 2026. Questions, errors, or suggestions: yin.zhang@wsu.edu*

*All examples use synthetic data created for teaching. They do not represent any real jurisdiction, agency, officer, or incident. See [Data/DATA_DICTIONARY.md](../../Data/DATA_DICTIONARY.md).*
