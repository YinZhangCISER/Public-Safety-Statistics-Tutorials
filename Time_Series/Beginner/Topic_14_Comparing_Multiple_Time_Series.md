# Topic 14: Comparing Multiple Time Series

> **Prepared by Yin Zhang**, Center for Interdisciplinary Statistical Education and Research (CISER), Washington State University

**The question this module answers:** *One agency had a terrible month. Was it something that agency did, or something that happened to everyone?*

---

## The Core Concept

A single series can tell you that something changed. It can never tell you **why**, because there is nothing to compare against.

Adding other agencies over the same months supplies the missing piece. If they all moved together, the cause is something they share: the weather, a state law, a holiday, a region wide event. If one moved and the others did not, the cause is local to that one.

The other agencies act as a **comparison group**. They show what a normal version of those same months looked like.

## Why It Matters

Without a comparison group, every change gets attributed to whatever the agency in question happened to be doing. A new commander arrived, a new tactic was tried, a new policy took effect, and the numbers moved. It is very hard to resist joining those facts together.

A comparison group breaks the habit, in both directions. It stops an agency being blamed for a statewide heat wave, and it stops an agency taking credit for a statewide decline.

This is the beginner form of an idea that the rest of this repository is built on. It is the whole basis of the [Causal Inference series](../../Causal_Inference/).

## The Example

Cedar Falls recorded 176 use of force incidents in June 2021, against a typical month of 31. Was June 2021 a difficult month everywhere?

Agencies differ enormously in size, so raw counts cannot be compared directly. Each agency below is measured **against its own typical month in 2021**, so a value of 1.0 means an entirely ordinary month for that agency.

![Two panels. The left panel shows three agencies through 2021, each divided by its own typical month, with Cedar Falls spiking to 5.7 in June while Grandview and Lakeshore County stay between 0.6 and 1.7 all year. The right panel shows all twelve agencies ranked by their June 2021 value, with Cedar Falls at 5.7 far ahead and every other agency between 0.0 and 2.0](Figures/fig_14_comparison_group.png)

| Agency | June 2021, as times its own typical month |
|---|---|
| **Cedar Falls** | **5.7** |
| Northgate | 2.0 |
| Harbor Point | 1.8 |
| Grandview | 1.6 |
| Riverbend | 1.5 |
| Prairie County | 1.2 |
| Pinecrest State University | 1.0 |
| Lakeshore County | 1.0 |
| Summit County | 1.0 |
| Millgate | 0.9 |
| Two Rivers Tribal | 0.0 |
| Elkhorn | 0.0 |

Eleven agencies had a June somewhere between an unusually quiet one and a mildly busy one. The values above 1.0 are mostly [seasonality](Topic_08_Seasonality.md), since June is a summer month everywhere. The two zeros are small agencies that happened to record nothing, which is [noise](Topic_10_Noise_And_Irregular_Fluctuations.md), not an achievement.

Cedar Falls is at 5.7. Nothing else is close.

**That single comparison answers the question.** June 2021 was not a hard month across the state. Whatever happened, happened in Cedar Falls. No further investigation of weather, state policy, or regional conditions is needed, and an investigation of Cedar Falls is warranted. Without the other eleven agencies, neither of those conclusions would have been available.

## What To Watch For

- **Put the agencies on comparable footing first.** Raw counts compare size, not behaviour. Use rates, or index each agency to its own normal as above. See [Topic 5](Topic_05_Counts_And_Rates.md).
- **Choose comparison agencies that actually resemble the one in question.** A campus force is not a fair comparison for a county sheriff. This is precisely the problem the WADEPS peer group work exists to solve, and the Intermediate series takes it up in detail.
- **Three or four lines is the limit on one chart.** Beyond that use a ranked bar chart, as in the right panel above, or separate panels. See [Topic 3](Topic_03_Visualizing_A_Time_Series.md).
- **Moving together does not prove a shared cause.** It makes a local explanation much less likely, which is usually the decision you need, but two agencies can move together by chance, especially small ones.
- **A comparison group is only useful over the same months.** Comparing this agency's summer to another agency's winter proves nothing.

## 💡 The Insight

A comparison group turns "our numbers changed" into "our numbers changed and nobody else's did", which is a completely different sentence and the only one worth acting on.

## Check Your Understanding

<details>
<summary><b>1.</b> Suppose every agency in the table had come in between 4 and 6 times its own typical June. What would that tell you about Cedar Falls?</summary>

That Cedar Falls needed no special explanation at all. A statewide spike of that size points to something shared: a regional event, a change in state reporting rules, a widespread disturbance. The investigation would move from Cedar Falls to the thing all twelve agencies had in common. The same Cedar Falls number means opposite things depending on what the others did.
</details>

<details>
<summary><b>2.</b> Northgate came in at 2.0, double its typical June. Should that be investigated too?</summary>

Probably not on its own. Northgate is a 31 officer department whose typical month is around 2 or 3 incidents, so doubling means going from roughly 2 to roughly 5. That is well inside ordinary variation for numbers that small, and June is a summer month. Compare it to Cedar Falls, where 5.7 times a typical month means going from about 31 to 176. The multiple is only half the story; the size of the base is the other half.
</details>

<details>
<summary><b>3.</b> A state report shows use of force falling at one agency over three years and credits the agency's new training program. What single addition would make that claim much stronger or much weaker?</summary>

The same three years for agencies that did not adopt the program. If they were flat and the trained agency fell, the claim gains real support. If they fell by the same amount, the decline was statewide and the program has no case. In this dataset every agency is declining at about 5 percent a year, so any agency can show a fall over three years without doing anything at all. [Topic 15](Topic_15_Lagged_Effects.md) works through exactly this comparison.
</details>

## Key Takeaway

Never interpret one agency's change alone. Put comparable agencies on the same months and ask whether they moved too. That one step decides whether the explanation is local or shared.

---

| | |
|---|---|
| **Previous** | [Topic 13: Smoothing and Moving Averages](Topic_13_Smoothing_And_Moving_Averages.md) |
| **Next** | [Topic 15: Lagged Effects](Topic_15_Lagged_Effects.md) |
| **Builds on** | [Topic 2: Time Series and Cross Sectional Data](Topic_02_Time_Series_And_Cross_Sectional_Data.md), [Topic 5: Counts and Rates](Topic_05_Counts_And_Rates.md), [Topic 11: Outliers and Spikes](Topic_11_Outliers_And_Spikes.md) |
| **Used again in** | [Topic 15: Lagged Effects](Topic_15_Lagged_Effects.md), [Topic 20: How to Read a Time Series Chart](Topic_20_How_To_Read_A_Chart_Checklist.md) |

*Prepared by Yin Zhang, Center for Interdisciplinary Statistical Education and Research (CISER), Washington State University. Version 1.0, September 2026. Questions, errors, or suggestions: yin.zhang@wsu.edu*

*All examples use synthetic data created for teaching. They do not represent any real jurisdiction, agency, officer, or incident. See [Data/DATA_DICTIONARY.md](../../Data/DATA_DICTIONARY.md).*
