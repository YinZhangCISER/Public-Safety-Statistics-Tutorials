# Topic 5: Things Were Already Changing

> **Developed by Yin Zhang, PhD**, Assistant Professor, Department of Mathematics and Statistics, Washington State University

**The question this module answers:** *How much of the improvement after a program would have arrived without it?*

---

## The Core Concept

Public safety numbers are not still. They drift, for reasons nobody in any single agency controls: changes in law, in policy, in training standards, in what gets recorded, in what the public expects, in the economy, in who lives where.

A program arrives in the middle of that drift. **Anything measured against the agency's own past gets the drift added to it.**

## Why It Matters

The drift is not small. In this dataset it is large enough to account for most of what a before and after comparison reports, and it is invisible unless you deliberately go and look at agencies that did nothing.

The general lesson is more important than the number: **before crediting a program, find out what was happening to everybody else.**

## The Example

Here is the change in use of force rate for all twelve agencies, measured from 2019 to 2022. **This is entirely before the training program existed.** It began in July 2023.

![A horizontal bar chart of the change in use of force rate from 2019 to 2022 for twelve agencies, sorted from the largest fall to the largest rise. Ten of the twelve bars point left, indicating a decline. The five agencies that later took the training are coloured blue and the seven that never did are grey, and both colours appear throughout the ranking](Figures/fig_05_already_changing.png)

**Ten of the twelve agencies were already falling**, several of them steeply, years before any training existed. Summit County had already fallen 35.7 percent. Stonewick, one of the agencies that later took the training, had already fallen 18.7 percent.

Now put that next to [Topic 4](Topic_04_Before_And_After_Is_Not_Enough.md). Over the actual study period, the seven agencies that **never took the training** saw their rate fall from 2.67 to 2.15, a decline of **19.5 percent**.

| | Change in the use of force rate |
|---|---|
| The trained agencies, before against after | −33.1% |
| The agencies that never took the training | **−19.5%** |
| What is left over | about −13% |

The agencies that did nothing got most of the way to the trained agencies' result by doing nothing.

## What To Watch For

- **The drift is usually in the helpful direction.** Most public safety indicators have been declining for years. That means most before and after evaluations overstate their programs.
- **Two colours, one ranking.** In the chart, agencies that later took the training and agencies that never did are mixed together throughout. Before the program, nothing distinguished them in how fast they were changing.
- **The drift can reverse.** If the statewide number rises during your study, a before and after comparison will understate a program that worked, or make a working program look harmful. The direction of the error follows the drift.
- **"Compared to last year" inherits all of this.** A year is long enough for the drift to matter.

## 💡 The Insight

Most of what happens after a program starts is the same thing that was already happening. Find out how much before you claim the rest.

## Check Your Understanding

<details>
<summary><b>1.</b> Two of the twelve agencies rose rather than fell over the period before the program. Does that undermine the point?</summary>

No, and it adds one. Both of them, Orrindale and Kelsmoor, are among the smallest agencies in the dataset. Orrindale averages under one use of force incident a month, so its percentage change is mostly noise rather than drift. Small agencies swing in both directions for no reason at all, which is a separate problem taken up in [Topic 11](Topic_11_Why_The_Worst_Performers_Always_Improve.md).
</details>

<details>
<summary><b>2.</b> If everyone is falling anyway, how can a program ever be shown to work?</summary>

By falling **faster** than the agencies that did not take it. That is the entire idea, and it is where the next three topics go. The statewide drift is not an obstacle to measurement; it is something you subtract, once you have someone to measure it from.
</details>

<details>
<summary><b>3.</b> An agency has no comparison group available. What should it report?</summary>

The before and after number, labelled as such, plus whatever statewide or regional figure exists for the same period, even if it is imperfect. A sentence like "the rate here fell 33 percent while the statewide rate fell 20 percent" is far more informative than the first half alone, and it costs one phone call.
</details>

## Key Takeaway

Look up what happened to agencies that did not take the program, over exactly the same months, before you write down what your program did.

---

| | |
|---|---|
| **Previous** | [Topic 4: Before and After Is Not Enough](Topic_04_Before_And_After_Is_Not_Enough.md) |
| **Next** | [Topic 6: Comparing Yourself to Someone Else](Topic_06_Comparing_Yourself_To_Someone_Else.md) |
| **Builds on** | [Topic 4](Topic_04_Before_And_After_Is_Not_Enough.md) |
| **Used again in** | [Topic 8](Topic_08_Two_Differences_Are_Better_Than_One.md), [Topic 14](Topic_14_Confounding.md) |

*This module is part of a series developed for the Washington Data Exchange for Public Safety (WADEPS) through the Center for Interdisciplinary Statistical Education and Research (CISER) at Washington State University. Version 1.0, September 2026. Questions, errors, or suggestions: yin.zhang@wsu.edu*

*All examples use synthetic data created for teaching. They do not represent any real jurisdiction, agency, officer, or incident. See [Data/DATA_DICTIONARY.md](../../Data/DATA_DICTIONARY.md).*
