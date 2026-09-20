# Topic 4: Time Units, Frequency, and Aggregation

> **Level:** Beginner | **Reading time:** about 5 minutes
> **Prepared by Yin Zhang**, Center for Interdisciplinary Statistical Education and Research (CISER), Washington State University

**The question this module answers:** *Should I be looking at this daily, monthly, or yearly? Does it matter?*

---

## The Core Concept

**Frequency** is how often you record a value: daily, weekly, monthly, quarterly, yearly.

**Aggregation** is rolling smaller units up into bigger ones. Thirty one daily counts add up to one July. Twelve monthly counts add up to one year.

Every dataset can be shown at several frequencies, and they are all the same underlying data. They do not all tell you the same thing.

## Why It Matters

Choosing a frequency is choosing what you are able to see.

**Too fine and everything is noise.** Daily counts for a single agency bounce between two and ten for reasons that are nothing more than chance. Yesterday was quiet, today was not, and neither fact means anything.

**Too coarse and everything disappears.** Yearly totals are so smooth that a three month crisis inside the year leaves no mark at all.

The frequency is not a technical detail chosen by whoever built the report. It decides which questions the report is capable of answering.

## The Example

The same Grandview Police Department data, at three frequencies.

**Daily, July 2023:**

| Day | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | ... | 29 | 30 | 31 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| **Incidents** | 3 | 2 | 7 | 8 | 8 | 4 | 3 | 9 | 4 | 2 | ... | 6 | 6 | 4 |

**Monthly, 2023:**

| Month | Jan | Feb | Mar | Apr | May | Jun | Jul | Aug | Sep | Oct | Nov | Dec |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| **Incidents** | 50 | 64 | 86 | 108 | 85 | 128 | 157 | 144 | 89 | 84 | 63 | 78 |

**Yearly, 2019 through 2025:**

| Year | 2019 | 2020 | 2021 | 2022 | 2023 | 2024 | 2025 |
|---|---|---|---|---|---|---|---|
| **Incidents** | 1,405 | 1,274 | 1,224 | 1,254 | 1,136 | 1,131 | 1,058 |

![Three panels of the same agency's data. The left panel shows daily counts for July 2023 as a jagged line between two and ten with no discernible pattern. The middle panel shows monthly counts for 2023 as a clear rise to a July peak and a fall back. The right panel shows yearly totals from 2019 to 2025 as bars declining gently from 1,405 to 1,058](Figures/fig_04_three_frequencies.png)

**Daily** is unreadable. The 16th had ten incidents and the 10th had two. That is a factor of five between two days in the same month, and there is no lesson in it. Anyone who staffs on the basis of this chart is reacting to coin flips.

**Monthly** shows the shape: a low winter, a climb into summer, a July peak, a return. This is the frequency that supports decisions about training calendars and seasonal staffing.

**Yearly** shows something the monthly view cannot: a steady decline across seven years, from 1,405 down to 1,058. It also completely hides July. At this frequency there is no such thing as a summer.

None of the three is wrong. They answer different questions.

## What To Watch For

- **Match the frequency to the question.** Planning next summer's staffing is a monthly question. Judging a seven year reform is a yearly question. Neither is answerable at the other frequency.
- **Never compare across frequencies.** "We had ten incidents on Saturday, against a monthly average of 95" is a meaningless sentence. Compare days to days and months to months.
- **Smaller units mean bigger swings, always.** A quiet day is normal. A quiet year is not. The smaller the time unit, the larger the share of what you see that is pure chance.
- **Monthly is usually the right default for public safety data.** It is short enough to catch a policy taking effect and long enough to average out the noise.

## 💡 The Insight

Changing the frequency does not change the data. It changes which patterns are visible and which are mathematically impossible to see.

## Check Your Understanding

<details>
<summary><b>1.</b> A new patrol strategy launches in March and is dropped in May after a bad April. Which frequency would have been needed to evaluate it fairly, and which frequency would hide it completely?</summary>

Monthly at minimum, and weekly would be better given how short the window is. A yearly view cannot see a two month program at all. It would appear only as a slightly different annual total, indistinguishable from chance. Note also that two months is probably too short to judge any strategy, for the reason covered in [Topic 15](Topic_15_Lagged_Effects.md).
</details>

<details>
<summary><b>2.</b> Grandview averaged about 5 incidents a day in July 2023. On the 16th there were 10. Is that a crisis day?</summary>

Almost certainly not. Daily counts for this agency run anywhere from 2 to 10 across an ordinary month. Ten is the high end of normal, not a departure from it. The way to check is to ask how often days like it occur, not how far it sits above the average. [Topic 10](Topic_10_Noise_And_Irregular_Fluctuations.md) and [Topic 11](Topic_11_Outliers_And_Spikes.md) take this up.
</details>

<details>
<summary><b>3.</b> Why can a yearly view show the seven year decline when the monthly view of a single year cannot?</summary>

Because within one year the seasonal swing, from 50 up to 157, is far larger than the year to year decline, which is about 5 percent annually. The big pattern drowns out the small one. Aggregating to years removes the seasonal swing entirely, which leaves the slow decline visible. Every frequency suppresses some patterns in order to reveal others.
</details>

## Key Takeaway

Decide what question you are asking, then pick the frequency that can answer it. For most public safety work, that is monthly.

---

| | |
|---|---|
| **Previous** | [Topic 3: Visualizing a Time Series](Topic_03_Visualizing_A_Time_Series.md) |
| **Next** | [Topic 5: Counts and Rates](Topic_05_Counts_And_Rates.md) |
| **Builds on** | [Topic 1: What Is a Time Series?](Topic_01_What_Is_A_Time_Series.md) |
| **Used again in** | [Topic 10: Noise and Irregular Fluctuations](Topic_10_Noise_And_Irregular_Fluctuations.md), [Topic 19: Data Quality and Common Pitfalls](Topic_19_Data_Quality_And_Pitfalls.md) |

*Prepared by Yin Zhang, Center for Interdisciplinary Statistical Education and Research (CISER), Washington State University. Version 1.0, September 2026. Questions, errors, or suggestions: yin.zhang@wsu.edu*

*All examples use synthetic data created for teaching. They do not represent any real jurisdiction, agency, officer, or incident. See [Data/DATA_DICTIONARY.md](../../Data/DATA_DICTIONARY.md).*
