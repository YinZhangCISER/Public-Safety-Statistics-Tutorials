# Module 2: Building an Honest Calendar

> **Developed by Yin Zhang, PhD**, Assistant Professor, Department of Mathematics and Statistics, Washington State University

**The question this module answers:** *A group by returned 50 months when the calendar has 90. Where did the other 40 go, and what should replace them?*

---

## The Question

A group by only creates rows for things that happened. A month in which nothing happened produces no row, so it disappears from the series entirely, and every average taken afterwards is an average over the busy months only.

That error is invisible. The series looks complete, the chart has a line on it, and the mean is wrong by a large margin.

Worse, a month that disappeared because nothing happened looks identical to a month that disappeared because the agency never submitted anything. The first is a zero. The second is unknown. They must not be treated the same way, and the incident file alone cannot tell them apart.

## The Idea in Plain Language

Three states, not two:

| State | Meaning | How to store it |
|---|---|---|
| **A number** | the agency reported and this is what happened | the number |
| **Zero** | the agency reported and nothing happened | `0` |
| **Missing** | the agency did not report | `NaN`, never `0` |

The fix has two steps. **Reindex** to the full calendar so every month exists as a row. Then decide, month by month, whether the newly created rows are zeros or unknowns, which requires knowing when each agency was reporting.

## The Method

```python
calendar = pd.period_range("2019-01", "2026-06", freq="M").astype(str)
counts = events.groupby("year_month").size()

reported = pd.Index(calendar).isin(roster["year_month"])
series = counts.reindex(calendar).fillna(0).where(reported)
```

In words: lay out every month; drop the counts into place; turn the holes into zeros; then put the holes back wherever the agency was not reporting.

The `roster` is the part people forget. It is any source that records which periods an agency submitted at all, whether or not anything happened. In this dataset `agency_monthly.csv` serves that role, because it has one row per agency per reported month regardless of the count. In a real extract it may be a submission log, a compliance report, or an email to the agency.

Finally, drop the periods that are still being entered.

## Worked Example

**Orrindale Police Department** has eight sworn officers. Grouping its incident records returns **50 months**. The calendar has **90**.

| | Months | Mean incidents |
|---|---|---|
| What the group by returned | 50 | **1.42** |
| The full calendar, zeros included | 90 | **0.79** |

The naive mean is **80 percent too high**, because it averages over the busy months and silently discards forty quiet ones. For a small agency this is the single largest source of error in any summary statistic.

![Two panels. The left panel shows Orrindale with two lines: the grouped event file, which has 50 points and never touches zero, and the same data reindexed to the calendar, which has 90 points and drops to zero repeatedly. The right panel shows Prairie County with green dots marking reported zeros and an orange band marking the three months that were never submitted](Figures/fig_m02_honest_calendar.png)

**Prairie County Sheriff's Office** shows why `fillna(0)` is not a default. Eleven of its months are absent from the incident file. Only **three** of those are the records system migration in the spring of 2022. The other **eight** are months in which the agency reported and recorded no use of force.

Three ways of handling it give three different answers:

| Approach | Mean incidents a month | What it gets wrong |
|---|---|---|
| Drop the absent months | 3.08 | discards eight real zeros, so the mean is too high |
| Fill everything with zero | 2.70 | invents three quiet months, so the mean is too low |
| **Zeros as zero, gaps as missing** | **2.84** | correct |

The right answer required a source outside the incident file. No amount of care with the incident file alone would have produced it.

**The most recent months are also not final.** In this dataset May and June 2026 carry a `provisional` flag and run at roughly three quarters and one half of a normal month. Nothing happened; the records are still being entered. Exclude them from anything you fit and mark them on anything you plot.

## Do It Yourself

> 📓 **Notebook:** [Module_02_Building_An_Honest_Calendar.ipynb](Notebooks/Module_02_Building_An_Honest_Calendar.ipynb)
> [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/OWNER/REPO/blob/main/Time_Series/Intermediate/Notebooks/Module_02_Building_An_Honest_Calendar.ipynb)
> Opens in Google Colab, runs top to bottom, about 15 minutes.

The notebook works both agencies through, builds the comparison table above, and ends with a reusable `monthly_series` function that handles zeros, gaps and provisional months in one call. Use it at the top of every later module.

## Pitfalls

| What goes wrong | What it looks like | What to do |
|---|---|---|
| Never reindexing | the series is shorter than the calendar; means are too high | `reindex` to `pd.period_range(...)` |
| `fillna(0)` everywhere | quiet months invented where the agency was absent | fill only where the roster says the agency reported |
| Treating a gap as an outlier | a "sharp drop to zero" that never happened | check the roster before explaining any zero |
| Interpolating across a gap without saying so | a smooth line through a period nobody has data for | leave it missing, or label the estimate everywhere |
| Leaving provisional months in a trend fit | the trend bends downward at the right hand edge | drop them, then refit |
| Averaging across agencies with different coverage | agencies with gaps contribute fewer months and get silently down weighted | count the months per agency and report it |

## Check Your Understanding

<details>
<summary><b>1.</b> Why is the naive mean for Orrindale too high rather than too low?</summary>

Because the months that disappear are exactly the quiet ones. A month with zero incidents produces no rows, so the group by has nothing to make a row from. The months that survive are the ones where something happened, which are by definition the busier months. Averaging over only those overstates the typical month. The smaller the agency, the more of its months vanish and the worse the error gets.
</details>

<details>
<summary><b>2.</b> An agency's file has no rows for August. What do you need in order to know whether August is a zero or a gap?</summary>

A source that records whether the agency submitted anything in August, independent of whether anything happened. The incident file cannot answer this, because an incident file only contains incidents and the absence of a record is not evidence. In this dataset the monthly roster answers it. In practice, ask the agency or check the submission log, and if neither exists, report August as unknown rather than guessing.
</details>

<details>
<summary><b>3.</b> Prairie County's 2022 rate per 100 arrests is computed from nine months of data. Is the rate wrong?</summary>

The rate is fine, because incidents and arrests are both missing the same three months, so the ratio is unaffected. The annual **count** is not fine: comparing a nine month total to another agency's twelve month total understates Prairie County by about a quarter before anything real happens. Rates tolerate coverage gaps; counts do not. [Module 3](Module_03_Choosing_A_Denominator.md) returns to this.
</details>

## Key Takeaway

Reindex to a full calendar before doing anything else, fill only the months the agency actually reported, and drop the months that are still being entered.

---

| | |
|---|---|
| **Previous** | [Module 1: From Incident Records to a Time Series](Module_01_From_Incident_Records_To_A_Time_Series.md) |
| **Next** | [Module 3: Choosing a Denominator](Module_03_Choosing_A_Denominator.md) |
| **Builds on** | [Beginner Topic 6](../Beginner/Topic_06_Missing_Time_Points_And_Reporting_Gaps.md), [Beginner Topic 19](../Beginner/Topic_19_Data_Quality_And_Pitfalls.md) |
| **Used again in** | every module that follows |

*This module is part of a series developed for the Washington Data Exchange for Public Safety (WADEPS) through the Center for Interdisciplinary Statistical Education and Research (CISER) at Washington State University. Version 1.0, September 2026. Questions, errors, or suggestions: yin.zhang@wsu.edu*

*All examples use synthetic data created for teaching. They do not represent any real jurisdiction, agency, officer, or incident. See [Data/DATA_DICTIONARY.md](../../Data/DATA_DICTIONARY.md).*
