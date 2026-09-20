# Topic 7: Trend, the Long Term Direction

> **Prepared by Yin Zhang**, Center for Interdisciplinary Statistical Education and Research (CISER), Washington State University

**The question this module answers:** *June was the worst month of the year for this department. Is the department getting worse?*

---

## The Core Concept

The **trend** is the long run direction of a series once the month to month movement is set aside. Up, down, or flat.

A trend is not what happened last month. It is what has been happening across years. Those two things frequently point in opposite directions, and only one of them should drive a decision about strategy.

## Why It Matters

A bad month is visible, immediate, and easy to build a story around. It arrives in a weekly report, gets raised in a meeting, and reaches a newspaper.

A trend is none of those things. Nobody notices a five percent annual improvement. It never produces a headline in any single month.

So the pressure runs entirely one way. Programs get cancelled, staff get reassigned, and policies get reversed on the strength of one bad month inside a multi year improvement. The improvement gets thrown away because it was never as loud as the setback.

The only defence is to place every month in the context of the years around it, every time, before anyone reacts.

## The Example

Riverbend Police Department.

**One year on its own, 2023:**

| Month | Jan | Feb | Mar | Apr | May | Jun | Jul | Aug | Sep | Oct | Nov | Dec |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| **Incidents** | 41 | 50 | 64 | 62 | 54 | **79** | 55 | 62 | 68 | 52 | 52 | 48 |

June's 79 is the highest month of the year, and almost double January. On its own it reads as a department losing control.

**The same agency over seven years,** measured as use of force per 100 arrests so that changes in activity are already accounted for:

| Year | 2019 | 2020 | 2021 | 2022 | 2023 | 2024 | 2025 |
|---|---|---|---|---|---|---|---|
| **Per 100 arrests** | 4.02 | 3.68 | 3.40 | 3.29 | 2.96 | 2.77 | 2.56 |

![Two panels. The left panel shows Riverbend's twelve monthly counts for 2023, with June circled at 79 as the highest month of the year. The right panel shows the same agency's use of force per 100 arrests from 2019 to 2025, falling in a near straight line from 4.02 to 2.56](Figures/fig_07_trend.png)

The rate has fallen **every single year for six years**, from 4.02 to 2.56. That is a reduction of 36 percent, and there is not one year in which it reversed.

June 2023 sits inside that. It is a high month in a year that was better than the one before it and worse than the one after it. Nothing about June 2023 interrupted the direction of travel, and a decision to abandon whatever Riverbend has been doing since 2019 would have been a decision to abandon the best sustained improvement in the dataset.

## What To Watch For

- **Two points do not make a trend.** Any two numbers form a line. You need several years before the direction is more than an accident of which two you picked.
- **Say what the trend is a trend in.** A falling rate with rising counts, or the reverse, is entirely possible. See [Topic 5](Topic_05_Counts_And_Rates.md).
- **A trend is not a promise.** "Down 36 percent over six years" describes the past. It does not guarantee next year, and it certainly does not guarantee next month.
- **Watch for the start date.** A trend measured from an unusually bad year will always look like an improvement. Ask why the series begins where it begins.

## 💡 The Insight

One month tells you what happened. Several years tell you what is happening. Only the second one should be allowed to change a strategy.

## Check Your Understanding

<details>
<summary><b>1.</b> Riverbend's June 2023 was 92 percent above its January. Does that show the agency deteriorating during 2023?</summary>

No, for two separate reasons. First, June is a summer month, and summer runs well above winter at almost every agency in the dataset, which is [Topic 8](Topic_08_Seasonality.md). Second, the full year ended at 48 in December, lower than it began. Within year movement and the multi year direction are different questions, and the January to June comparison answers neither of them cleanly.
</details>

<details>
<summary><b>2.</b> Which is stronger evidence that something is working: one month that is 40 percent better than the month before, or six consecutive years of about 6 percent improvement?</summary>

The six years, and it is not close. A single month 40 percent below the one before it happens regularly by chance, especially in a small agency. Six consecutive annual improvements in the same direction is a pattern that chance produces very rarely. Size is not the same as strength. Persistence is what makes evidence strong.
</details>

<details>
<summary><b>3.</b> A report says an agency's incidents fell from 2024 to 2025 and calls this a downward trend. What would you want before accepting the word trend?</summary>

More years. Two points always make a line, and that line always points somewhere. Ask for 2019 onward. If the series has been bouncing between the same two levels for six years, then 2024 to 2025 is noise with a label attached, which is [Topic 10](Topic_10_Noise_And_Irregular_Fluctuations.md).
</details>

## Key Takeaway

Before reacting to a bad month, put it next to the same month in the last three years. If the direction across years is good, the month is news, not evidence.

---

| | |
|---|---|
| **Previous** | [Topic 6: Missing Time Points and Reporting Gaps](Topic_06_Missing_Time_Points_And_Reporting_Gaps.md) |
| **Next** | [Topic 8: Seasonality](Topic_08_Seasonality.md) |
| **Builds on** | [Topic 1: What Is a Time Series?](Topic_01_What_Is_A_Time_Series.md), [Topic 5: Counts and Rates](Topic_05_Counts_And_Rates.md) |
| **Used again in** | [Topic 12: Short Term Fluctuation and Long Term Change](Topic_12_Short_Vs_Long_Term_Change.md), [Topic 17: Stationarity](Topic_17_Stationarity.md) |

*Prepared by Yin Zhang, Center for Interdisciplinary Statistical Education and Research (CISER), Washington State University. Version 1.0, September 2026. Questions, errors, or suggestions: yin.zhang@wsu.edu*

*All examples use synthetic data created for teaching. They do not represent any real jurisdiction, agency, officer, or incident. See [Data/DATA_DICTIONARY.md](../../Data/DATA_DICTIONARY.md).*
