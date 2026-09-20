# Topic 13: Smoothing and Moving Averages

> **Prepared by Yin Zhang**, Center for Interdisciplinary Statistical Education and Research (CISER), Washington State University

**The question this module answers:** *The monthly line jumps around so much that every meeting argues about the last point. Is there a way to see past it?*

---

## The Core Concept

**Smoothing** replaces each point with an average of itself and its neighbours. The result is a second line, drawn over the first, that moves more slowly.

The most common version is the **moving average**. A three month moving average for June is the average of April, May and June. For July it is May, June and July. The window slides along, one month at a time, which is where the name comes from.

Nothing is deleted. The original values stay on the chart. Smoothing adds a line, it does not replace one.

## Why It Matters

Raw monthly numbers move for two reasons at once: because something changed, and because months are short and events are countable. A reader cannot see which is which, so every meeting relitigates the most recent point.

A smoothed line separates those. Because noise is as likely to be high as low, averaging several months together mostly cancels it out, while a real change survives because it is present in every month of the window.

The window length decides what survives:

- **Three months** removes most of the month to month noise and keeps the seasonal shape.
- **Twelve months** removes the seasonal shape entirely, because every window contains exactly one of each month. What is left is the trend.

## The Example

**Removing noise: Lakeshore County, 2023, with a three month moving average.**

| Month | Jan | Feb | Mar | Apr | May | Jun | Jul | Aug | Sep | Oct | Nov | Dec |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| **Reported** | 8 | 7 | 9 | 13 | 10 | 14 | 13 | 8 | 7 | **14** | **4** | 5 |
| **Three month average** | | | 8.0 | 9.7 | 10.7 | 12.3 | 12.3 | 11.7 | 9.3 | 9.7 | 8.3 | 7.7 |

In the raw row, October to November is 14 down to 4, a fall of 71 percent. In the smoothed row the same two months read 9.7 and 8.3, a fall of 14 percent. [Topic 10](Topic_10_Noise_And_Irregular_Fluctuations.md) argued from the whole year that this drop was noise. The moving average shows it directly.

Notice also that the first two cells are empty. A three month average cannot be computed until three months exist.

**Removing the season: Grandview, twelve month moving average.**

![Two panels. The left panel shows Lakeshore County's 2023 raw monthly counts in grey with a three month moving average drawn over it in blue, which flattens the October to November drop. The right panel shows Grandview's full monthly series in grey with a twelve month moving average in blue, a smooth line that falls steadily and shows no summer peaks at all](Figures/fig_13_smoothing.png)

The grey line on the right is the raw series, with its July spike every year. The blue line is the twelve month average, and it has no spikes at all, because every window it computes contains one July and one January. What remains is the seven year decline, visible without having to squint past the seasonal pattern.

## What To Watch For

- **A moving average lags.** It is an average of the past, so it turns after the raw series does. A twelve month average will not fully reflect a change until twelve months after the change. If the question is "has something just happened", a smoothed line is the wrong tool.
- **The last points are unreliable.** Near the end of the series the window may be incomplete, or may include provisional months. Many charts simply stop the smoothed line early, and that is the honest choice.
- **Missing months break it.** Prairie County has no data for March, April and May 2022, so no three month average can be computed for any window containing them. Software that silently skips the gap and averages February with June produces a number that is not a three month average of anything. See [Topic 6](Topic_06_Missing_Time_Points_And_Reporting_Gaps.md).
- **Choose the window to match the question, then say which you used.** "Incidents are down" means something different with a three month window than with a twelve month one.
- **Smoothing hides genuine spikes too.** Cedar Falls in June 2021 is a real event that a moving average will flatten into something unremarkable. Always show the raw line as well.

## 💡 The Insight

A raw line answers "what was last month". A smoothed line answers "where is this going". Put both on the chart and the reader stops confusing the two.

## Check Your Understanding

<details>
<summary><b>1.</b> Lakeshore's three month average for December is 7.7, computed from October, November and December. Verify it.</summary>

The three values are 14, 4 and 5. Their sum is 23, and 23 divided by 3 is 7.67, which rounds to 7.7. Note that October's 14 is still in the window and is still pulling the average up, which is why a smoothed line takes time to respond. By January, October will have dropped out.
</details>

<details>
<summary><b>2.</b> Why does a twelve month moving average remove seasonality, while a three month one does not?</summary>

Because every twelve month window contains exactly one of each calendar month, so the same seasonal contribution is in every window, and moving the window along cannot change it. A three month window contains only three months, so a window covering June, July and August is made of high months while one covering December, January and February is made of low months. The seasonal pattern is still there, just softened.
</details>

<details>
<summary><b>3.</b> A program launched in September. In December, a twelve month moving average shows almost no change. Has the program failed?</summary>

The chart cannot say. Only three of the twelve months in that window are after the launch, so even a large effect would move the average by about a quarter of its true size. A twelve month average in December is mostly describing the year before the program. Either wait, or use a shorter window, or compare against agencies that did not adopt the program. [Topic 15](Topic_15_Lagged_Effects.md) and [Topic 14](Topic_14_Comparing_Multiple_Time_Series.md) take up both routes.
</details>

## Key Takeaway

Draw the smoothed line over the raw one, never instead of it, and say how long the window is. Then remember that the smoothed line is always looking slightly backwards.

---

| | |
|---|---|
| **Previous** | [Topic 12: Short Term Fluctuation and Long Term Change](Topic_12_Short_Vs_Long_Term_Change.md) |
| **Next** | [Topic 14: Comparing Multiple Time Series](Topic_14_Comparing_Multiple_Time_Series.md) |
| **Builds on** | [Topic 10: Noise and Irregular Fluctuation](Topic_10_Noise_And_Irregular_Fluctuations.md), [Topic 6: Missing Time Points and Reporting Gaps](Topic_06_Missing_Time_Points_And_Reporting_Gaps.md) |
| **Used again in** | [Topic 17: Stationarity](Topic_17_Stationarity.md), [Topic 20: How to Read a Time Series Chart](Topic_20_How_To_Read_A_Chart_Checklist.md) |

*Prepared by Yin Zhang, Center for Interdisciplinary Statistical Education and Research (CISER), Washington State University. Version 1.0, September 2026. Questions, errors, or suggestions: yin.zhang@wsu.edu*

*All examples use synthetic data created for teaching. They do not represent any real jurisdiction, agency, officer, or incident. See [Data/DATA_DICTIONARY.md](../../Data/DATA_DICTIONARY.md).*
