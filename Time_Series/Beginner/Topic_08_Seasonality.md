# Topic 8: Seasonality

> **Prepared by Yin Zhang**, Center for Interdisciplinary Statistical Education and Research (CISER), Washington State University

**The question this module answers:** *Incidents are up sharply again this summer. Is that a crisis, or is that just summer?*

---

## The Core Concept

**Seasonality** is a pattern that repeats on a fixed schedule: the same months every year, or the same days every week.

The word to hold onto is **predictable**. A seasonal pattern is not a surprise. It happened last year, it happened the year before, and you can say in advance roughly when it will happen again.

## Why It Matters

Every summer, incident numbers rise. Every summer, that rise is discovered as though it were new.

Reacting to a seasonal increase as though it were a crisis wastes money, exhausts staff, and burns credibility. Worse, it hides the thing worth knowing. If July is always 25 percent above average, then the useful question is not "is July higher than June". It is **"is this July higher than a July should be"**.

Seasonality also cuts the other way. A drop in November is not an achievement. If a program launches in September and the numbers fall by December, the calendar would have done that anyway.

## The Example

**Pooling every agency across every year**, here is what each month looks like relative to the annual average:

| Month | Jan | Feb | Mar | Apr | May | Jun | Jul | Aug | Sep | Oct | Nov | Dec |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| **Share of average** | 0.82 | 0.81 | 0.89 | 0.95 | 1.06 | 1.25 | **1.26** | 1.19 | 1.06 | 0.97 | 0.87 | 0.85 |

July runs about 26 percent above the annual average. February runs about 19 percent below it. So a July that is 50 percent higher than the preceding February is a completely ordinary July.

**Is it reliable?** Grandview Police Department, January against July, every year:

| Year | 2019 | 2020 | 2021 | 2022 | 2023 | 2024 | 2025 |
|---|---|---|---|---|---|---|---|
| **January** | 90 | 78 | 93 | 78 | 50 | 82 | 64 |
| **July** | 167 | 132 | 120 | 156 | 157 | 109 | 141 |

July is higher in **seven years out of seven**. That is what predictable means. It is not a claim that July is always the single highest month, and it is not a claim about the size of the gap. It is a claim that the direction is dependable enough to plan around.

![Three panels. The left panel shows every agency pooled, with each month as a share of the annual average, June and July highlighted at about 1.25. The middle panel shows Grandview's January and July side by side for each of seven years, with July higher in all seven. The right panel shows the campus agency Pinecrest, whose calls peak in September and October and collapse in June and July](Figures/fig_08_seasonality.png)

**Not every agency has the same season.** Pinecrest State University Police serves a campus, and its calendar is the academic year, not the weather:

| Month | Jan | Feb | Mar | Apr | May | Jun | Jul | Aug | Sep | Oct | Nov | Dec |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| **Share of average** | 1.12 | 1.16 | 1.07 | 1.06 | 0.71 | 0.54 | 0.56 | 0.90 | **1.45** | 1.37 | 1.14 | 0.92 |

Pinecrest peaks in September when students return and falls by nearly half in June when the campus empties. Applying the statewide summer pattern to Pinecrest would get the direction exactly backwards.

## What To Watch For

- **Compare like months.** July against July, not July against June. That is the whole idea behind [Topic 18](Topic_18_Year_Over_Year_Comparison.md).
- **You need several years to establish a season.** One July that was high is not seasonality. Three or four are.
- **Seasonality is specific to the agency.** A campus, a tourist town, a farming county and a dense city will not share a calendar. Do not import a pattern from elsewhere.
- **Do not credit the calendar to a program.** Something launched in August that shows a drop by November has to beat what November does on its own.

## 💡 The Insight

Seasonality turns a recurring surprise into a schedule. Once you know July runs 26 percent high, July stops being an emergency and becomes a staffing plan.

## Check Your Understanding

<details>
<summary><b>1.</b> A department's incidents rise 45 percent between February and July. Is anything unusual happening?</summary>

Probably not. The pooled pattern has February at 0.81 and July at 1.26 of the annual average, which is a rise of about 56 percent from ordinary seasonality alone. A 45 percent rise is actually a little *less* than a normal year. The comparison worth making is against previous Julys, not against this February.
</details>

<details>
<summary><b>2.</b> Grandview recorded 109 incidents in July 2024, its lowest July in the seven years. Its January 2024 was 82. Is 2024 a good year or a bad one?</summary>

A good one, and the two numbers say so in different ways. Against its own January, July 2024 looks like the usual summer rise. Against the other six Julys, which run from 120 to 167, it is the lowest by a clear margin. Comparing like months is what reveals that. Comparing July to January only tells you that summer happened.
</details>

<details>
<summary><b>3.</b> A statewide report recommends that every agency add summer patrol staff in June. Which agency in this dataset should ignore that advice, and why?</summary>

Pinecrest State University Police. June is its quietest month, at 0.54 of its annual average, because the students are gone. Its busy period is September and October. A statewide seasonal rule applied without checking would send Pinecrest extra staff at precisely the moment it needs fewest.
</details>

## Key Takeaway

Before calling a summer rise a problem, check what the last three summers did. The question is never "higher than last month". It is "higher than usual for this month".

---

| | |
|---|---|
| **Previous** | [Topic 7: Trend, the Long Term Direction](Topic_07_Trend.md) |
| **Next** | [Topic 9: Cycles and Seasonality](Topic_09_Cycles_And_Seasonality.md) |
| **Builds on** | [Topic 4: Time Units, Frequency, and Aggregation](Topic_04_Time_Units_Frequency_And_Aggregation.md), [Topic 7: Trend](Topic_07_Trend.md) |
| **Used again in** | [Topic 17: Stationarity](Topic_17_Stationarity.md), [Topic 18: Year over Year Comparison](Topic_18_Year_Over_Year_Comparison.md) |

*Prepared by Yin Zhang, Center for Interdisciplinary Statistical Education and Research (CISER), Washington State University. Version 1.0, September 2026. Questions, errors, or suggestions: yin.zhang@wsu.edu*

*All examples use synthetic data created for teaching. They do not represent any real jurisdiction, agency, officer, or incident. See [Data/DATA_DICTIONARY.md](../../Data/DATA_DICTIONARY.md).*
