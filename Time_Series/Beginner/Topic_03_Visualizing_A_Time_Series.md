# Topic 3: Visualizing a Time Series

> **Developed by Yin Zhang, PhD**, Assistant Professor, Department of Mathematics and Statistics, Washington State University

**The question this module answers:** *A chart makes a department's numbers look alarming. Is the alarm in the data, or in the chart?*

---

## The Core Concept

For data over time, the **line plot** is the right picture. A line connects each point to the one before it, which is exactly the relationship that matters: what came next.

Your eye is far better at reading a shape than a row of numbers. A line plot hands the pattern over in about a second. A table of the same twelve numbers takes a minute and you will still miss things.

## Why It Matters

The same twelve numbers can be drawn to look like a steady year or like a catastrophe. Nothing has to be falsified. Two choices do all the work: where the vertical axis starts, and how many lines are on the page.

People present charts to get decisions. If you cannot spot these two moves, you can be walked to a conclusion the data does not support.

## The Example

Grandview Police Department, 2023, drawn three times.

| Month | Jan | Feb | Mar | Apr | May | Jun | Jul | Aug | Sep | Oct | Nov | Dec |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| **Incidents** | 50 | 64 | 86 | 108 | 85 | 128 | 157 | 144 | 89 | 84 | 63 | 78 |

![Three panels of the same 2023 data. The left panel is a line plot with the vertical axis starting at zero. The middle panel is the identical data with the axis starting at 45, which makes January appear near zero and July appear as a cliff. The right panel overlays six different agencies, producing a tangle of lines that cannot be read](Figures/fig_03_reading_a_line_plot.png)

**Left, drawn honestly.** The axis starts at zero. July is about three times January, and the picture shows it as about three times.

**Middle, the axis cut off.** Identical numbers. The axis now starts at 45, so January sits on the floor and July towers over it. The rise looks like a collapse of control. Nothing was falsified and the impression is wrong.

**Right, too many lines.** Six agencies at once. Every line is drawn correctly. Try to answer one question about any single agency from this panel. You cannot, and neither can the person you are presenting to.

## What To Watch For

- **Read the vertical axis before the line.** If it does not start at zero, there may be a good reason, and you still need to know before you react.
- **Bars are for categories, lines are for time.** A bar chart of twelve months invites you to compare July against March as two separate things. A line shows the path between them, which is the point.
- **Three or four lines is the limit.** Beyond that, split into separate small charts. Six panels a reader can follow beats one panel nobody can.
- **A gap in a line is a fact.** If a line runs straight through a period with no data points, someone drew a guess. See [Topic 6](Topic_06_Missing_Time_Points_And_Reporting_Gaps.md).

## 💡 The Insight

Every chart is an argument. The axis and the number of lines are where the argument is made, and both are set before you ever see the data.

## Check Your Understanding

<details>
<summary><b>1.</b> A slide shows monthly complaints rising from 41 to 46 over a year, and the line climbs steeply across the whole slide. What should you check first?</summary>

Where the vertical axis starts. A change from 41 to 46 is about 12 percent. If the axis runs from 40 to 47, that small change fills the entire height of the slide and looks like a crisis. Ask for the chart redrawn from zero, then decide whether 12 percent is worth acting on.
</details>

<details>
<summary><b>2.</b> Why is a bar chart a poor choice for twelve months of incident counts?</summary>

Bars are built for comparing separate categories, like four agency types. They put a visual wall between each pair of adjacent values, which is precisely the wrong signal for months, since the whole point is that July follows June. A line makes the flow visible. A bar chart makes you reconstruct it.
</details>

<details>
<summary><b>3.</b> A report has to show trends for eight precincts. What should it do?</summary>

Not eight lines on one chart. Either eight small panels side by side sharing one vertical axis, so the shapes can be compared at a glance, or just the two or three precincts the decision actually concerns, with the rest summarized as a single average line for context.
</details>

## Key Takeaway

Plot the data before you analyze it, start the axis at zero unless you can say why not, and keep it to three or four lines.

---

| | |
|---|---|
| **Previous** | [Topic 2: Time Series and Cross Sectional Data](Topic_02_Time_Series_And_Cross_Sectional_Data.md) |
| **Next** | [Topic 4: Time Units, Frequency, and Aggregation](Topic_04_Time_Units_Frequency_And_Aggregation.md) |
| **Used again in** | [Topic 14: Comparing Multiple Time Series](Topic_14_Comparing_Multiple_Time_Series.md), [Topic 20: How to Read a Time Series Chart](Topic_20_How_To_Read_A_Chart_Checklist.md) |

*This module is part of a series developed for the Washington Data Exchange for Public Safety (WADEPS) through the Center for Interdisciplinary Statistical Education and Research (CISER) at Washington State University. Version 1.0, September 2026. Questions, errors, or suggestions: yin.zhang@wsu.edu*

*All examples use synthetic data created for teaching. They do not represent any real jurisdiction, agency, officer, or incident. See [Data/DATA_DICTIONARY.md](../../Data/DATA_DICTIONARY.md).*
