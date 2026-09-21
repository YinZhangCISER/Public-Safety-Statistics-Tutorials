# Topic 18: Year over Year Comparison

> **Developed by Yin Zhang, PhD**, Assistant Professor, Department of Mathematics and Statistics, Washington State University

**The question this module answers:** *June is up 51 percent on May. Is the department in trouble?*

---

## The Core Concept

**Year over year** means comparing a period to the same period one year earlier. June 2023 against June 2022, not June 2023 against May 2023.

The reason is simple. Both Junes share the same weather, the same daylight, the same school calendar, the same holidays. Everything seasonal is the same on both sides, so it cancels, and what is left is the part that is actually about the agency.

Comparing to last month leaves all of that in.

## Why It Matters

Month over month is the comparison that appears by default in almost every dashboard, because it is the easiest one to compute. It is also the one most likely to be wrong, because in public safety data the seasonal swing is usually larger than anything real.

The consequence is a monthly cycle of false alarms in spring and false congratulations in autumn, repeating every year, in every agency, forever.

Year over year answers the question a chief, a mayor, or a resident actually has: **are things better than they were a year ago?**

## The Example

Ashfell Police Department, 2022 against 2023:

| Month | Jan | Feb | Mar | Apr | May | Jun | Jul | Aug | Sep | Oct | Nov | Dec |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| **2022** | 78 | 78 | 103 | 104 | 89 | 124 | 156 | 149 | 131 | 90 | 91 | 61 |
| **2023** | 50 | 64 | 86 | 108 | 85 | 128 | 157 | 144 | 89 | 84 | 63 | 78 |
| **Against last month** | | +28% | +34% | +26% | −21% | **+51%** | +23% | −8% | −38% | −6% | −25% | +24% |
| **Against the same month last year** | −36% | −18% | −16% | +4% | −5% | **+3%** | +1% | −3% | −32% | −7% | −31% | +28% |

![Two panels. The left panel plots Ashfell's 2022 and 2023 monthly counts on the same axes, showing two lines with almost identical shape, with 2023 sitting slightly lower for most of the year. The right panel shows, for each month of 2023, two bars: the change against the previous month and the change against the same month a year earlier](Figures/fig_18_year_over_year.png)

**June is the clearest case.** Against May, June is **up 51 percent**, which reads as an emergency. Against June of the previous year, it is **up 3 percent**, which is no change at all. The 51 percent is the arrival of summer. It happened in 2022 as well, and it will happen again.

**February and March are the reverse.** Month over month says up 28 and up 34 percent. Year over year says down 18 and down 16 percent. Read one way the agency looks like it is deteriorating fast; read the other way it is having a considerably better winter than the winter before. The second reading is the correct one.

**Look at the left panel.** The two lines have nearly the same shape, because the shape is the calendar and the calendar does not change. The useful information is the vertical gap between them, and that is exactly what year over year measures.

## What To Watch For

- **Year over year does not remove the trend, and should not.** Ashfell is improving, so most months come out negative. That is the finding.
- **A single year over year figure can still be noise.** September 2023 is down 32 percent and December is up 28 percent. Those are two months in a small window. [Topic 10](Topic_10_Noise_And_Irregular_Fluctuations.md) still applies.
- **It needs the base month to be normal.** Comparing to a month that contained a one off event produces a meaningless percentage. Tarnbridge in June 2022 would look like a triumph against June 2021 purely because of the civil unrest. See [Topic 11](Topic_11_Outliers_And_Spikes.md).
- **Watch for changes between the two years.** A new records system, a new boundary, a reclassification: any of these can make the two periods incomparable no matter how well the months line up. See [Topic 19](Topic_19_Data_Quality_And_Pitfalls.md).
- **The most recent month may be provisional.** Comparing an incomplete month to a complete one guarantees a false improvement.

## 💡 The Insight

Month over month measures the calendar. Year over year measures the agency. Only one of those is anybody's responsibility.

## Check Your Understanding

<details>
<summary><b>1.</b> Ashfell's June 2023 was up 51 percent on May and up 3 percent on June 2022. Which number belongs in the monthly report, and what should it say?</summary>

Both, with the year over year figure leading. Something like: "June recorded 128 incidents, in line with last June's 124. The rise from May is the usual seasonal increase." Suppressing the 51 percent is not the answer, because someone will compute it anyway. Putting it next to the 3 percent explains it before it can be misread.
</details>

<details>
<summary><b>2.</b> Every month from January to March 2023 is up sharply on the previous month and down sharply on the same month a year earlier. How can both be true?</summary>

Because they measure different things. Incidents always climb from January into spring, so each month beats the one before it. At the same time every one of those months came in below its counterpart in 2022, because the agency is running at a lower level than it was a year ago. The series is rising through the year and sitting lower than last year, simultaneously. There is no contradiction, only two different comparisons.
</details>

<details>
<summary><b>3.</b> An agency changed its incident classification in January. Is a year over year comparison for February reliable?</summary>

No. Year over year controls for the season, not for changes in how the data is produced. February this year is being counted under one set of rules and February last year under another, so any difference mixes real change with the reclassification. The comparison has to wait until a full year has passed under the new rules, or be restricted to categories the change did not touch.
</details>

## Key Takeaway

Put the year over year column in every monthly report, next to the month over month one. Whenever they disagree, the year over year column is the one about the agency.

---

| | |
|---|---|
| **Previous** | [Topic 17: Stationarity, the Stable Baseline](Topic_17_Stationarity.md) |
| **Next** | [Topic 19: Data Quality and Common Pitfalls](Topic_19_Data_Quality_And_Pitfalls.md) |
| **Builds on** | [Topic 8: Seasonality](Topic_08_Seasonality.md), [Topic 12: Short Term Fluctuation and Long Term Change](Topic_12_Short_Vs_Long_Term_Change.md) |
| **Used again in** | [Topic 20: How to Read a Time Series Chart](Topic_20_How_To_Read_A_Chart_Checklist.md) |

*This module is part of a series developed for the Washington Data Exchange for Public Safety (WADEPS) through the Center for Interdisciplinary Statistical Education and Research (CISER) at Washington State University. Version 1.0, September 2026. Questions, errors, or suggestions: yin.zhang@wsu.edu*

*All examples use synthetic data created for teaching. They do not represent any real jurisdiction, agency, officer, or incident. See [Data/DATA_DICTIONARY.md](../../Data/DATA_DICTIONARY.md).*
