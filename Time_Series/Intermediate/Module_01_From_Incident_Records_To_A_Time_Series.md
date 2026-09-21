# Module 1: From Incident Records to a Time Series

> **Developed by Yin Zhang, PhD**, Assistant Professor, Department of Mathematics and Statistics, Washington State University

**The question this module answers:** *How do I turn a file of individual incident records into a monthly series, and what am I deciding when I do?*

---

## The Question

Public safety data does not arrive as a time series. It arrives as a pile of individual records: one row per incident, in whatever order the export produced, with no time unit and no ordering.

Every chart anyone ever shows is the result of turning that pile into a series. The turning involves at least four decisions, and none of them is recoverable from the finished chart. Getting them right, and writing them down, is the first analytical task.

## The Idea in Plain Language

**Aggregation** means collapsing many rows into one number per time period.

That is all a monthly series is. Take every record whose date falls in January, count them, and that is January. Repeat for each month and you have a series.

The subtlety is that the same records support many different series. Count all incidents and you get one. Count only those involving a vehicle stop and you get another. Count distinct people rather than events and you get a third. None is more correct than the others, and a reader looking at any one of them cannot tell which choices produced it.

## The Method

For a file of incident records:

1. **Decide the unit of analysis.** One agency, a group of agencies, or the state.
2. **Decide the time key.** A column that says which period each record belongs to.
3. **Decide the grouping.** Time alone, or time crossed with a category.
4. **Decide what is being counted.** Rows, or distinct subjects, or a sum of something.

In pandas that is one line:

```python
series = records.groupby("year_month").size()
```

`groupby` splits the rows into buckets by the time key. `size()` counts the rows in each bucket. Steps 1, 3 and 4 are the filter applied before it, the columns named inside it, and the function called after it.

One practical note on the time key. The `YYYY-MM` format used throughout this dataset is **zero padded**, so `2023-07` sorts after `2023-06` as plain text. A format like `7/1/2023` does not sort correctly and will scramble the series silently. Either use a zero padded string or convert to a proper period with `pd.PeriodIndex`.

## Worked Example

The use of force file holds **22,233 records**. Filtering to Grandview Police Department in 2023 leaves **1,136**. Grouping those by month gives twelve numbers:

| Month | Jan | Feb | Mar | Apr | May | Jun | Jul | Aug | Sep | Oct | Nov | Dec |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| **Incidents** | 50 | 64 | 86 | 108 | 85 | 128 | 157 | 144 | 89 | 84 | 63 | 78 |

Those are the numbers Beginner [Topic 1](../Beginner/Topic_01_What_Is_A_Time_Series.md) opened with. They were not handed down from anywhere. They are two decisions, which agency and which time unit, applied to a file of records.

![Three panels built from the same 1,136 records. The first groups by month and gives a single line. The second groups by month and incident type and gives four lines with different shapes. The third groups by month and whether the subject was injured, as a stacked bar](Figures/fig_m01_records_into_a_series.png)

**The same records, grouped three ways.** The monthly total rises into July. Split by incident type, offences against persons drive most of the summer rise while warrant related incidents peak in May. Split by outcome, the share of incidents involving a subject injury follows its own pattern again.

Three series, one file, three different stories. The question has to come before the group by.

**Events are not people.** Across the whole file there are 22,233 records but only 19,708 distinct subjects. **2,324 subjects appear more than once**, and one appears four times. A series counting incidents and a series counting people are different series, and which one you want depends on whether the question is about police activity or about how many members of the public were involved.

## Do It Yourself

> 📓 **Notebook:** [Module_01_From_Incident_Records_To_A_Time_Series.ipynb](Notebooks/Module_01_From_Incident_Records_To_A_Time_Series.ipynb)
> [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/OWNER/REPO/blob/main/Time_Series/Intermediate/Notebooks/Module_01_From_Incident_Records_To_A_Time_Series.ipynb)
> Opens in Google Colab, runs top to bottom, about 15 minutes.

The notebook builds the twelve numbers above from the raw records, checks them against the published monthly table, then rebuilds the same records as two entirely different series. It finishes with an exercise on firearm discharges.

## Pitfalls

| What goes wrong | What it looks like | What to do |
|---|---|---|
| Date parsed as text in a non sortable format | months out of order, or a chart that zigzags backwards | use zero padded `YYYY-MM`, or `pd.PeriodIndex(..., freq="M")` |
| Months with no records vanish | the series is shorter than the calendar and every average is too high | reindex to a full calendar, which is [Module 2](Module_02_Building_An_Honest_Calendar.md) |
| Counting rows when the question is about people | the number is larger than it should be, by about 11 percent in this file | de duplicate on the subject identifier first |
| Filtering after grouping | totals that do not add up to the unfiltered series | filter first, then group |
| The grouping choice goes unrecorded | nobody can reproduce the chart, including you in six months | state the agency, the period, the filter and the count in the caption |

## Check Your Understanding

<details>
<summary><b>1.</b> Two analysts build a monthly series from the same file and get different numbers. Neither has made an error. Name three things that could differ.</summary>

The filter, the grouping and the thing being counted. One may have restricted to a single agency while the other included all twelve. One may have counted incident records while the other counted distinct subjects. One may have used the incident date while the other used the date the record was entered. All three are legitimate choices, and none of them is visible in the finished series, which is why the caption has to carry them.
</details>

<details>
<summary><b>2.</b> Why does grouping by a column of strings like `"2023-07"` work correctly here, and when would it fail?</summary>

It works because the format is zero padded and ordered from largest unit to smallest, so alphabetical order and chronological order are the same. It fails for any format that is not, such as `7/1/2023`, where `10/1/2023` sorts before `7/1/2023`. It also fails across century boundaries for two digit years. The safe habit is to convert to a period or a timestamp as soon as the data is loaded.
</details>

<details>
<summary><b>3.</b> An agency asks for "monthly use of force" and you produce a chart. What four facts belong in the caption?</summary>

Which agency and which time range; what the filter was, if any; whether the number counts incidents or people; and which date field determined the month. Without those four, the chart cannot be reproduced or compared with anyone else's, and the most common way two reports disagree is that they made different choices here and neither wrote them down.
</details>

## Key Takeaway

A time series is not in the data. It is a set of choices applied to records. Make the choices deliberately, and write them next to the chart.

---

| | |
|---|---|
| **Next** | [Module 2: Building an Honest Calendar](Module_02_Building_An_Honest_Calendar.md) |
| **Builds on** | [Beginner Topic 1](../Beginner/Topic_01_What_Is_A_Time_Series.md), [Beginner Topic 4](../Beginner/Topic_04_Time_Units_Frequency_And_Aggregation.md) |
| **Used again in** | every module that follows |

*This module is part of a series developed for the Washington Data Exchange for Public Safety (WADEPS) through the Center for Interdisciplinary Statistical Education and Research (CISER) at Washington State University. Version 1.0, September 2026. Questions, errors, or suggestions: yin.zhang@wsu.edu*

*All examples use synthetic data created for teaching. They do not represent any real jurisdiction, agency, officer, or incident. See [Data/DATA_DICTIONARY.md](../../Data/DATA_DICTIONARY.md).*
