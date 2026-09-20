# Topic 11: Outliers and Spikes

> **Prepared by Yin Zhang**, Center for Interdisciplinary Statistical Education and Research (CISER), Washington State University

**The question this module answers:** *One extraordinary week pushed a department's yearly average up by 40 percent. Which number should be reported?*

---

## The Core Concept

An **outlier** is a value so far outside a series' normal range that it almost certainly reflects one specific event rather than a change in the underlying situation.

An outlier is not the same as noise. Noise is small and constant and has no cause worth naming. An outlier is large, usually rare, and can usually be traced to something that actually happened on a known date.

## Why It Matters

Averages are not robust. A single extreme value can pull a yearly average a long way, and the average carries that distortion into every table, every comparison, and every trend line it appears in.

This leads to two opposite failures, and both are common:

- **Leaving it in without saying so.** The agency appears to have had a bad year. Comparisons against other agencies and against its own other years become meaningless.
- **Quietly removing it.** Now the numbers look better, and the reader has no way to know that a real week in which real force was used has been deleted from the record.

Neither is honest. The answer is to do both, visibly.

## The Example

Cedar Falls Police Department, 2021:

| Month | Jan | Feb | Mar | Apr | May | Jun | Jul | Aug | Sep | Oct | Nov | Dec |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| **Incidents** | 27 | 28 | 17 | 26 | 34 | **176** | 45 | 37 | 43 | 27 | 21 | 35 |

Every other month in the year sits between 17 and 45. June recorded 176, nearly six times the typical month of 31. A week of civil unrest is documented for that month.

![Two panels. The left panel shows Cedar Falls monthly counts for 2021, flat between 17 and 45 except for June at 176, which is marked in orange against a dashed line at the typical month of 31. The right panel shows the agency's average monthly incidents for each year from 2019 to 2025, computed twice, with and without June 2021. The two bars are identical in every year except 2021, where they read 43.0 and 30.9](Figures/fig_11_outliers.png)

**With June included,** Cedar Falls averaged 43.0 incidents a month in 2021. **With June set aside,** it averaged 30.9.

Now look at the agency's other years:

| Year | 2019 | 2020 | 2021 | 2022 | 2023 | 2024 | 2025 |
|---|---|---|---|---|---|---|---|
| **Average a month, June 2021 included** | 31.7 | 33.1 | **43.0** | 28.7 | 28.6 | 23.6 | 21.0 |
| **Average a month, June 2021 set aside** | 31.7 | 33.1 | **30.9** | 28.7 | 28.6 | 23.6 | 21.0 |

The two rows are identical everywhere except one cell. With that one month in, 2021 looks like a year in which Cedar Falls suddenly got much worse and then recovered. With it set aside, 2021 fits smoothly into a steady multi year decline. **The second story is the true one about how Cedar Falls operates. The first is the true one about what happened in Cedar Falls in 2021.** Both are facts and they answer different questions.

## What To Watch For

- **Report both numbers.** "43.0 incidents a month, or 30.9 excluding the civil unrest in June" takes one extra clause and removes all the ambiguity.
- **Never remove a point silently.** If a value is excluded, say which one, say why, and say what the number would have been with it in.
- **Use the median as a cross check.** The median of Cedar Falls in 2021 is 31, essentially unchanged by June, because the middle value does not care how extreme the extreme is. A large gap between the mean and the median is a reliable signal that an outlier is present.
- **Ask the three way question.** When a spike appears: is this the new normal, which would be a trend; does it happen every year at this time, which would be seasonality; or was it one event, which would be an outlier. See [Topic 7](Topic_07_Trend.md) and [Topic 8](Topic_08_Seasonality.md).
- **A spike can also be a data problem.** A batch of backlogged records entered in one month produces exactly this shape with nothing having happened at all. [Topic 19](Topic_19_Data_Quality_And_Pitfalls.md).

## 💡 The Insight

An outlier is not a number to be deleted or defended. It is a separate fact, and it deserves its own sentence rather than being folded into an average.

## Check Your Understanding

<details>
<summary><b>1.</b> A news report says Cedar Falls use of force rose 30 percent in 2021 compared to 2020. Is that accurate?</summary>

Arithmetically yes: 33.1 to 43.0 is a rise of about 30 percent. As a description of the agency it is badly misleading, because the entire rise and more is one documented week of civil unrest. Excluding that month, 2021 is 30.9, which is *lower* than 2020. An honest account gives both figures and names the event.
</details>

<details>
<summary><b>2.</b> Cedar Falls in 2021 had a mean of 43.0 and a median of 31. What does the gap between those two numbers tell you before you have looked at any chart?</summary>

That at least one value is far above the rest. The mean is pulled by every value in proportion to its size, so one very large number moves it a long way. The median only depends on the middle of the sorted list, so an extreme value moves it barely at all. Whenever the mean sits well above the median, look for a spike. This works as a screening check across hundreds of agencies at once.
</details>

<details>
<summary><b>3.</b> Should June 2021 be excluded when fitting a long term trend for Cedar Falls?</summary>

Usually yes, and it must be stated. The purpose of a trend is to describe the underlying direction, and a single week of civil unrest is not part of that direction. But the exclusion belongs in the notes, along with the trend computed both ways if the two differ much. If a reader can only see one version, they cannot judge whether the choice changed the conclusion.
</details>

## Key Takeaway

Find the spikes before computing any average. Then report the number with the spike, the number without it, and the name of the event that caused it.

---

| | |
|---|---|
| **Previous** | [Topic 10: Noise and Irregular Fluctuation](Topic_10_Noise_And_Irregular_Fluctuations.md) |
| **Next** | [Topic 12: Short Term Fluctuation and Long Term Change](Topic_12_Short_Vs_Long_Term_Change.md) |
| **Builds on** | [Topic 10: Noise and Irregular Fluctuation](Topic_10_Noise_And_Irregular_Fluctuations.md) |
| **Used again in** | [Topic 14: Comparing Multiple Time Series](Topic_14_Comparing_Multiple_Time_Series.md), [Topic 19: Data Quality and Common Pitfalls](Topic_19_Data_Quality_And_Pitfalls.md) |

*Prepared by Yin Zhang, Center for Interdisciplinary Statistical Education and Research (CISER), Washington State University. Version 1.0, September 2026. Questions, errors, or suggestions: yin.zhang@wsu.edu*

*All examples use synthetic data created for teaching. They do not represent any real jurisdiction, agency, officer, or incident. See [Data/DATA_DICTIONARY.md](../../Data/DATA_DICTIONARY.md).*
