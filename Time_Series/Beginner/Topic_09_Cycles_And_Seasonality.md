# Topic 9: Cycles and Seasonality

> **Developed by Yin Zhang, PhD**, Assistant Professor, Department of Mathematics and Statistics, Washington State University

**The question this module answers:** *People say crime runs in cycles. Is a summer peak a cycle?*

---

## The Core Concept

No. A summer peak is seasonality. The two words get used interchangeably and they describe different things.

**Seasonality** repeats on a **fixed** schedule. Twelve months, or seven days. You know the length in advance and you know which part of the calendar it lands on.

**A cycle** is a slow swing with **no fixed length**. It might run three years or ten. It is driven by broad forces such as an economic downturn, a demographic shift, a wave of reform, or a change in state law, and nobody can tell you in advance when it will turn.

| | Seasonality | Cycle |
|---|---|---|
| Length | Fixed, usually twelve months | Variable, often three to ten years |
| Timing | Known in advance | Not known in advance |
| Cause | Weather, daylight, school calendar, holidays | Economy, policy era, demographics, social change |
| What it is good for | Scheduling and staffing | Long range budgeting and strategy |
| How many observations to see it | Three or four years | Fifteen years or more |

That last row is the practical problem. Confirming a cycle needs several full swings, which means decades of comparable data. Most public safety datasets, including WADEPS, are nowhere near that old.

## Why It Matters

Calling something a cycle sounds more sophisticated than calling it a trend, and it carries a hidden claim: **that it will come back around**. If a decline is cyclical, doing nothing is defensible, because it will reverse on its own eventually. If a decline is a trend caused by sustained effort, then stopping the effort stops the decline.

That is a budget argument, and it gets made with the word "cycle" all the time on the strength of five or six years of data that cannot possibly support it.

## The Example

![Two panels. The left panel shows Grandview's full monthly series from 2019 to 2026, with a sharp peak every twelve months and a heavy orange line tracing the slowly falling yearly average. The right panel is a labelled illustration, not real data, showing a smooth wave taking about five years to complete one swing](Figures/fig_09_cycles_and_seasonality.png)

**Left: what is actually in this dataset.** Grandview Police Department, every month from 2019 to 2026. Two patterns are stacked on top of each other:

- **A spike every twelve months.** Each one is July. Fixed length, known timing. That is seasonality.
- **A level that drifts downward.** The yearly average falls from about 117 incidents a month in 2019 to about 88 in 2025.

That downward drift is a **trend**, not a cycle. It goes one direction for seven straight years and never turns. Nothing in this data tells you it will ever come back up, and nothing tells you it will not.

**Right: what a cycle would look like.** This panel is an illustration, drawn to show the shape, and it is not from the dataset. One full swing takes close to five years, the turning points do not line up with any month of the calendar, and the next turn cannot be read off a calendar.

To tell the left pattern from the right one you would need to watch Grandview until roughly 2040.

## What To Watch For

- **Seven years of decline is a trend until proven otherwise.** Calling it the downswing of a cycle is a prediction, not a description, and it needs evidence beyond the data showing the decline.
- **Seasonality and a trend coexist happily.** Grandview has both at once. Every July is above its neighbours, and every July is lower than the July before it. Neither cancels the other.
- **Ask what would drive the cycle.** A real cycle has a mechanism: an economic cycle, a policy era, a generational shift. "It goes up and down" is not a mechanism.
- **Match the tool to the horizon.** Use the seasonal pattern for next quarter's staffing. Use the multi year direction for the next budget cycle. Neither answers the other's question.

## 💡 The Insight

Seasonality tells you what to expect next month. A trend tells you where the last few years have been heading. A cycle claims to tell you when things will turn around, and that claim needs far more data than most agencies have.

## Check Your Understanding

<details>
<summary><b>1.</b> Grandview's July counts run 167, 132, 120, 156, 157, 109, 141 across seven years. Is the up and down movement in those numbers a cycle?</summary>

No. Those are seven annual observations of the same month, and they bounce with no fixed period and no consistent direction. That is noise around a slowly falling level, which is [Topic 10](Topic_10_Noise_And_Irregular_Fluctuations.md). A cycle would show several consecutive years up, then several consecutive years down, and would do it more than once. These do neither.
</details>

<details>
<summary><b>2.</b> An analyst says a county's rate has been in a downswing since 2019 and will naturally turn back up around 2027. What is wrong with that statement?</summary>

The word "naturally" is doing work the data cannot support. To claim a turning point in 2027 you would need to have observed previous complete swings and measured their length. With seven years of data there has been no complete swing to measure. The statement is a forecast dressed as an observation, and it would justify cutting a program that may be the actual reason for the decline.
</details>

<details>
<summary><b>3.</b> Both a seasonal pattern and a cyclical pattern can make this year's number lower than last year's. How would you tell which one you are looking at?</summary>

Check whether the low point lands on the same part of the calendar every time. Seasonality does: Grandview's low is January or February every single year. A cycle does not, because it is not tied to the calendar at all. If you can predict the timing from the month, it is seasonality. If the timing moves around across years, you are looking at something else, and you need many more years before naming it.
</details>

## Key Takeaway

A repeating annual peak is seasonality. A steady multi year direction is a trend. Reserve the word cycle for a swing you have watched turn around more than once, and be suspicious when it is used to argue that nothing needs doing.

---

| | |
|---|---|
| **Previous** | [Topic 8: Seasonality](Topic_08_Seasonality.md) |
| **Next** | [Topic 10: Noise and Irregular Fluctuation](Topic_10_Noise_And_Irregular_Fluctuations.md) |
| **Builds on** | [Topic 7: Trend](Topic_07_Trend.md), [Topic 8: Seasonality](Topic_08_Seasonality.md) |
| **Used again in** | [Topic 12: Short Term Fluctuation and Long Term Change](Topic_12_Short_Vs_Long_Term_Change.md), [Topic 17: Stationarity](Topic_17_Stationarity.md) |

*This module is part of a series developed for the Washington Data Exchange for Public Safety (WADEPS) through the Center for Interdisciplinary Statistical Education and Research (CISER) at Washington State University. Version 1.0, September 2026. Questions, errors, or suggestions: yin.zhang@wsu.edu*

*All examples use synthetic data created for teaching. They do not represent any real jurisdiction, agency, officer, or incident. See [Data/DATA_DICTIONARY.md](../../Data/DATA_DICTIONARY.md).*
