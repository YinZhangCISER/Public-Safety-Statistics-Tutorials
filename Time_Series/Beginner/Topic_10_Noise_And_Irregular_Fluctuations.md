# Topic 10: Noise and Irregular Fluctuation

> **Developed by Yin Zhang, PhD**, Assistant Professor, Department of Mathematics and Statistics, Washington State University

**The question this module answers:** *A department's incidents fell 71 percent in one month. What did it do right?*

---

## The Core Concept

**Noise** is the part of a series that has no explanation because there is nothing to explain. It is what is left over after trend, season and cycle have been accounted for.

Noise is not measurement error and it is not a mistake in the data. It is the ordinary result of counting events that happen to individual people on particular days. Two nearly identical months will still produce different counts, in the same way two fair coins tossed ten times will rarely give the same number of heads.

Every real series has noise in it. The skill is not removing it. The skill is recognising it, and declining to explain it.

## Why It Matters

Organisations are built to find reasons. A number moves, someone is asked why, and an answer gets produced. The answer is often invented, because the honest one, "nothing in particular", is not a comfortable thing to say in a meeting.

This has real costs. Explaining noise means:

- Credit gets assigned to whatever happened to be going on during a good month, so ineffective things get expanded.
- Blame gets assigned during a bad month, so people learn that the numbers are a threat rather than a tool.
- Attention goes to whichever unit had a random bad month instead of the unit with a genuine problem.

Saying "this is within the normal range of variation" is a professional judgment, and an analyst who cannot say it is not much use.

## The Example

Lakeshore County Sheriff's Office, 2023:

| Month | Jan | Feb | Mar | Apr | May | Jun | Jul | Aug | Sep | Oct | Nov | Dec |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| **Incidents** | 8 | 7 | 9 | 13 | 10 | 14 | 13 | 8 | 7 | **14** | **4** | 5 |

October to November is 14 down to 4. A 71 percent drop in a single month. That is the kind of number that ends up in a briefing as evidence that something worked.

![Three panels. The left panel shows Lakeshore County's 2023 monthly counts bouncing between 4 and 14 with October at 14 and November at 4 labelled. The middle panel shows the same agency's yearly rate from 2019 to 2025 hovering close to a flat average of 2.36. The right panel shows Orrindale's 2023 counts, which run between 0 and 4, with orange dots marking months that reported zero](Figures/fig_10_noise.png)

Nothing worked. Look at the whole year: the series goes 8, 7, 9, 13, 10, 14, 13, 8, 7, 14, 4, 5. It has been bouncing between roughly 4 and 14 all year with no direction whatsoever. October at 14 is the top of the ordinary range and November at 4 is the bottom of it. Landing on both in consecutive months is unremarkable.

Now widen the view. Lakeshore's use of force per 100 arrests, by year:

| Year | 2019 | 2020 | 2021 | 2022 | 2023 | 2024 | 2025 |
|---|---|---|---|---|---|---|---|
| **Per 100 arrests** | 2.84 | 2.27 | 2.43 | 2.57 | 1.93 | 2.28 | 2.20 |

Seven years, average 2.36, and the whole range is 1.93 to 2.84. There is no trend here at all. This agency has been doing the same thing, at the same level, for seven years. Every monthly movement in 2023 was noise around a line that has not moved.

**Small agencies are almost entirely noise.** Orrindale Police Department has eight officers. Its 2023: 0, 2, 1, 0, 2, 0, 4, 0, 2, 1, 1, 1. June was 0 and July was 4. Expressed as a percentage that is an infinite increase. Expressed in incidents it is four. There is no version of Orrindale's monthly numbers that can support a claim about anything.

## What To Watch For

Three questions separate noise from signal. A real change usually answers yes to all three.

1. **Is it bigger than the movement this series shows routinely?** Lakeshore routinely moves by 5 or 6 in a month. A change of 10 is notable. A change of 4 is not.
2. **Did it last?** One month is never enough. Two or three consecutive months in the same direction start to mean something.
3. **Does it line up with something real?** A documented policy, event, or change in conditions, with the timing to match. And note that a cause you found only after seeing the number is weak evidence, because something can always be found.

Also worth remembering:

- **Smaller units are noisier.** Smaller agency, shorter time period, narrower category. All three increase the share of what you see that is chance. See [Topic 4](Topic_04_Time_Units_Frequency_And_Aggregation.md).
- **Percentages exaggerate small numbers.** "Up 300 percent" can mean one incident became four.

## 💡 The Insight

The most valuable sentence an analyst can say is "this is within the normal range of variation." It is a finding, not an absence of one.

## Check Your Understanding

<details>
<summary><b>1.</b> Lakeshore went from 14 in October to 4 in November. Apply the three questions.</summary>

**Bigger than routine?** No. The year already ran from 4 to 14, so both endpoints are inside the range the agency shows normally. **Did it last?** No. December was 5, then the following year returns to the same average. **Something real?** Nothing documented. All three say noise. The correct response is no response.
</details>

<details>
<summary><b>2.</b> Orrindale reported 0 incidents in June and 4 in July 2023. A report describes this as a sharp deterioration. What is wrong?</summary>

The numbers are too small to describe anything. Orrindale averages under one incident a month, so the difference between a quiet month and a busy one is a handful of events, any of which could have fallen on either side of the month boundary. A percentage calculated from a base of zero is meaningless. For an agency this size the only honest unit of analysis is a year or several years, not a month.
</details>

<details>
<summary><b>3.</b> Why is a cause discovered after seeing the number weaker evidence than one predicted in advance?</summary>

Because something is always available. In any given month there was a staffing change, a new supervisor, a weather event, or a training session, and it is easy to attach whichever one fits the direction the number moved. If you had committed in advance to what you expected and when, the data could have proved you wrong. An explanation that cannot be wrong is not evidence. [Topic 15](Topic_15_Lagged_Effects.md) makes the same point about program evaluation.
</details>

## Key Takeaway

Do not explain every movement. Ask whether it is larger than this series normally moves, whether it lasted, and whether something real lines up. If the answer is no, say so and move on.

---

| | |
|---|---|
| **Previous** | [Topic 9: Cycles and Seasonality](Topic_09_Cycles_And_Seasonality.md) |
| **Next** | [Topic 11: Outliers and Spikes](Topic_11_Outliers_And_Spikes.md) |
| **Builds on** | [Topic 4: Time Units, Frequency, and Aggregation](Topic_04_Time_Units_Frequency_And_Aggregation.md), [Topic 7: Trend](Topic_07_Trend.md) |
| **Used again in** | [Topic 12: Short Term Fluctuation and Long Term Change](Topic_12_Short_Vs_Long_Term_Change.md), [Topic 13: Smoothing and Moving Averages](Topic_13_Smoothing_And_Moving_Averages.md) |

*This module is part of a series developed for the Washington Data Exchange for Public Safety (WADEPS) through the Center for Interdisciplinary Statistical Education and Research (CISER) at Washington State University. Version 1.0, September 2026. Questions, errors, or suggestions: yin.zhang@wsu.edu*

*All examples use synthetic data created for teaching. They do not represent any real jurisdiction, agency, officer, or incident. See [Data/DATA_DICTIONARY.md](../../Data/DATA_DICTIONARY.md).*
