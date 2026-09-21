# Topic 11: Why the Worst Performers Always Improve

> **Developed by Yin Zhang, PhD**, Assistant Professor, Department of Mathematics and Statistics, Washington State University

**The question this module answers:** *Why does anything measured at its worst tend to get better, even when nothing is done about it?*

---

## The Core Concept

Any measured number has two parts: the real underlying level, and whatever happened to be going on that month.

An agency that comes out worst in a given year is usually somewhat worse than average **and** had a bad year. Next year the real part is still there, but the bad luck is replaced by fresh luck, which is average. So the number comes down.

Nothing improved. Only the luck was re drawn. This is **regression to the mean**, and it happens to every extreme measurement, always, with no exceptions and no cause needed.

## Why It Matters

Programs are given to whoever looks worst. That is sensible policy and it is a measurement trap, because the worst performers were going to improve anyway.

**The improvement is guaranteed before the program starts.** Any before and after comparison at those agencies will show a decline that the program did not produce.

## The Example

Take the seven agencies that **never took any training**. Nothing was done to any of them. Sort them by where they started and see where they ended up.

![Two panels. The left connects each of the seven untrained agencies from its 2019 to mid 2020 rate to its 2022 to mid 2023 rate. The three that started highest are orange and come down steeply; the three that started lowest are blue and two of them rise. The right panel shows the average change for each trio as bars: minus 12.0 percent for those that started highest and plus 6.8 percent for those that started lowest](Figures/fig_11_regression_to_mean.png)

| Among agencies that received nothing | Average change |
|---|---|
| The three that started **highest** | **−12.0%** |
| The three that started **lowest** | **+6.8%** |
| **The gap** | **19 points** |

Read that again. **Nineteen percentage points separate the worst performers from the best, and no program exists anywhere in this picture.** If you had given the three worst agencies a program and evaluated it before and after, you would have reported a 12 percent reduction, and you would have been reporting arithmetic.

Twelve percent is also, by coincidence, exactly the size of the real training effect in this dataset. A method that produces the right answer for the wrong reason is not a method.

## What To Watch For

- **It is strongest where measurement is noisiest.** The agencies at the bottom of this chart are also the smallest ones, which is not a separate explanation; it is the mechanism. Small agencies produce more extreme readings, so they regress further.
- **It applies to good news too.** An agency celebrated as a model after an exceptional year will look worse next year without anything going wrong.
- **One year is not enough to identify the worst performer.** Use several years, or the ranking is mostly luck.
- **A comparison group fixes it, if chosen the same way.** If the comparison agencies were also selected for being at an extreme, the regression happens in both groups and subtracts out. If not, it does not. See [Topic 13](Topic_13_Picking_The_Winners.md).

## 💡 The Insight

Anything picked for being extreme will look better next time. Getting worse is what "extreme" means, and getting better is what happens next.

## Check Your Understanding

<details>
<summary><b>1.</b> A state gives a grant to the ten agencies with the highest use of force rates. A year later their average rate has fallen 15 percent. What can be concluded?</summary>

Almost nothing, without a comparison. A fall was guaranteed by the selection rule before any money was spent. To learn anything about the grant you need agencies that were also at the top of the ranking and did **not** get it, so that the regression happens in both groups and cancels.
</details>

<details>
<summary><b>2.</b> Why does this bias not appear when a program is given out at random?</summary>

Because a random group contains agencies from everywhere in the distribution, high, low and middling. The ones that happened to have a bad year regress down, the ones that had a good year regress up, and on average the two cancel. Regression to the mean is not caused by randomness; it is caused by **selecting on** the noisy measurement.
</details>

<details>
<summary><b>3.</b> How could an agency be identified as genuinely high without falling into this trap?</summary>

Use several years of data rather than one, which averages out the year to year luck and leaves more of the real level. Report an interval rather than a rank. And compare against agencies of similar size, because a small agency at the top of a ranking is far more likely to be there by accident than a large one.
</details>

## Key Takeaway

Whenever a group was chosen for being at an extreme, expect improvement with no cause, and find a comparison group that was chosen the same way.

---

| | |
|---|---|
| **Previous** | [Topic 10: When the Comparison Group Moves Too](Topic_10_When_The_Comparison_Group_Moves_Too.md) |
| **Next** | [Topic 12: Who Chose to Participate?](Topic_12_Who_Chose_To_Participate.md) |
| **Builds on** | [Topic 4](Topic_04_Before_And_After_Is_Not_Enough.md), [Topic 5](Topic_05_Things_Were_Already_Changing.md) |
| **Used again in** | [Topic 13](Topic_13_Picking_The_Winners.md), [Topic 19](Topic_19_Reading_A_Causal_Claim.md) |

*This module is part of a series developed for the Washington Data Exchange for Public Safety (WADEPS) through the Center for Interdisciplinary Statistical Education and Research (CISER) at Washington State University. Version 1.0, September 2026. Questions, errors, or suggestions: yin.zhang@wsu.edu*

*All examples use synthetic data created for teaching. They do not represent any real jurisdiction, agency, officer, or incident. See [Data/DATA_DICTIONARY.md](../../Data/DATA_DICTIONARY.md).*
