# Topic 16: Autocorrelation, the Memory of Data

> **Developed by Yin Zhang, PhD**, Assistant Professor, Department of Mathematics and Statistics, Washington State University

**The question this module answers:** *What is the best guess for next month, before knowing anything about next month?*

---

## The Core Concept

**Autocorrelation** means a value is related to its own earlier values. In plain language, the data has **memory**.

The reason is not mysterious. The conditions that produced this month's number do not disappear on the first of next month. The same staffing, the same neighbourhoods, the same policies, the same weather, mostly the same people. A month is a boundary on a calendar, not in the world.

## Why It Matters

Memory sets expectations, and expectations are what make a number surprising or not.

If a series has strong memory, next month will be close to this month. So a number that is far from this month is genuinely unusual and worth attention, while a number close to it is exactly what should have happened.

Memory also explains why large changes are hard. A series with strong memory resists being moved. One announcement, one meeting, one memo will not shift it, because next month is mostly determined by conditions that are already in place. Changing the trajectory takes sustained force, which is the same lesson [Topic 15](Topic_15_Lagged_Effects.md) reached from a different direction.

## The Example

**Neighbouring months are close.** Grandview Police Department, 2023:

| Month | Jan | Feb | Mar | Apr | May | Jun | Jul | Aug | Sep | Oct | Nov | Dec |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| **Incidents** | 50 | 64 | 86 | 108 | 85 | 128 | 157 | 144 | 89 | 84 | 63 | 78 |

Step from one month to the next and the average distance is **24 incidents**. Pick any two months of the year at random and the average distance is **38**. Neighbours are closer than strangers. That gap is the memory.

![Three panels. The left panel shows Grandview's 2023 line with each step between neighbouring months highlighted. The middle panel is a scatter plot with each month's count on the horizontal axis and the following month's count on the vertical axis, for Grandview, where the dots rise together in a band. The right panel is the same scatter for Elkhorn, where the dots form a shapeless cloud](Figures/fig_16_autocorrelation.png)

**The scatter plots make it visible.** Each dot is one pair of neighbouring months: this month across the bottom, the month after up the side.

For **Grandview**, the dots rise together. A month around 60 is followed by a month around 60 to 90. A month around 150 is followed by a month around 120 to 160. Knowing where you are on the bottom axis narrows down where you will land on the side axis. That is memory.

For **Elkhorn**, the eight officer department, the same picture is a shapeless cloud. Knowing this month was 2 tells you essentially nothing about next month.

**Memory grows with size.** Across the dataset, the bigger agencies have strong memory and the smallest have almost none. This is not because big agencies are more stable places. It is because their counts are large enough for underlying conditions to show through the randomness, while in a department averaging under one incident a month, chance is nearly the whole story. See [Topic 10](Topic_10_Noise_And_Irregular_Fluctuations.md).

## What To Watch For

- **Strong memory makes a simple forecast surprisingly good.** For a large agency, "about the same as this month, adjusted for the season" is hard to beat without a formal model.
- **Memory raises the bar for what counts as news.** If neighbouring months are normally within 24 of each other, a move of 20 is unremarkable and a move of 70 is not.
- **Memory is not causation.** This month does not cause next month. Both are produced by conditions that persist across both. The persistence is the real thing; the correlation is its shadow.
- **Do not confuse memory with a trend.** A series can have strong memory and no trend at all, simply drifting slowly around a fixed level.
- **Seasonality contributes to memory.** Part of the reason June and July resemble each other is that both are summer months. Memory and season are entangled, and separating them is a job for the Intermediate series.

## 💡 The Insight

Ask what next month will be, and for a large agency the honest answer is usually "close to this one". That is not a failure of imagination. It is what the data is telling you.

## Check Your Understanding

<details>
<summary><b>1.</b> Grandview's neighbouring months are 24 apart on average and any two months of the year are 38 apart. Why does that difference demonstrate memory?</summary>

If a month's value were unrelated to the one before it, neighbouring pairs would be no closer than randomly chosen pairs, and the two numbers would be about the same. They are not: neighbours are about a third closer. Something links a month to the one beside it. That link is what autocorrelation names.
</details>

<details>
<summary><b>2.</b> Elkhorn's scatter is a cloud. Does that mean Elkhorn is more volatile than Grandview in a way that should concern anyone?</summary>

No. It means Elkhorn's counts are so small that randomness swamps everything else. Grandview's 100 incidents a month reflect conditions across a large department; Elkhorn's 0 or 2 reflect whether a handful of events happened to fall inside a particular month. The cloud is a statement about sample size, not about how the department operates.
</details>

<details>
<summary><b>3.</b> A commander wants next month's number to be 40 percent lower than this month's. Given what memory implies, what should be expected?</summary>

That it will not happen from a single intervention, and that if it does happen it was probably not the intervention. Strong memory means next month is largely set by conditions already in place. A 40 percent drop in one month at a large agency would be far outside the usual step size, which makes noise, a data problem, or a reporting change the more likely explanations. Real change of that size appears gradually, across many months.
</details>

## Key Takeaway

For a large agency, expect next month to resemble this month. Judge every new number against that expectation rather than against zero.

---

| | |
|---|---|
| **Previous** | [Topic 15: Lagged Effects](Topic_15_Lagged_Effects.md) |
| **Next** | [Topic 17: Stationarity, the Stable Baseline](Topic_17_Stationarity.md) |
| **Builds on** | [Topic 10: Noise and Irregular Fluctuation](Topic_10_Noise_And_Irregular_Fluctuations.md), [Topic 15: Lagged Effects](Topic_15_Lagged_Effects.md) |
| **Used again in** | [Topic 17: Stationarity](Topic_17_Stationarity.md) |

*This module is part of a series developed for the Washington Data Exchange for Public Safety (WADEPS) through the Center for Interdisciplinary Statistical Education and Research (CISER) at Washington State University. Version 1.0, September 2026. Questions, errors, or suggestions: yin.zhang@wsu.edu*

*All examples use synthetic data created for teaching. They do not represent any real jurisdiction, agency, officer, or incident. See [Data/DATA_DICTIONARY.md](../../Data/DATA_DICTIONARY.md).*
