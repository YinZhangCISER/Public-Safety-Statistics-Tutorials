# Topic 9: Were They Moving Together Before?

> **Developed by Yin Zhang, PhD**, Assistant Professor, Department of Mathematics and Statistics, Washington State University

**The question this module answers:** *A comparison group exists. How do you find out whether it is any good?*

---

## The Core Concept

Difference in differences assumes that without the program, the two groups would have **changed by the same amount**. Not that they would have been equal, which they never are. That they would have moved in step.

That assumption is about a world that did not happen, so it cannot be tested directly. But it has a consequence you can check: if the two groups would have moved together afterwards, they should have been moving together **before**.

Draw the years before the program and look. This one habit catches more bad evaluations than any other.

## Why It Matters

[Topic 8](Topic_08_Two_Differences_Are_Better_Than_One.md) left an unexplained gap. Difference in differences gave 16.9 percent against a true 12.0. Something was moving one group and not the other, and it was not the training.

## The Example

![Two panels. The left shows the years before the program only, with three lines: the four agencies that took the training, the seven that did not, and Summit County separately. The first two run roughly parallel while Summit County starts among the trained agencies and falls away steeply. The right panel is a bar chart of three estimates: 33.1 percent, 16.9 percent and 12.5 percent, against a dashed line at the true 12 percent](Figures/fig_09_moving_together.png)

The left panel shows **only the years before the program existed**. Two of the three lines fall at about the same pace. One does not.

Summit County starts among the trained agencies in 2019 and ends near the comparison group by mid 2023, having crossed most of the distance before the training was announced. It began its own internal reform in 2019, four years early.

| Before the program, use of force rate falling at | |
|---|---|
| The other four agencies that took the training | 5.2% a year |
| The seven that did not | 4.5% a year |
| **Summit County** | **12.0% a year** |

The first two numbers are close, which is what makes the comparison usable. The third is nothing like them.

Summit County's own reform gets credited to the training, because the reform is inside the trained group and nothing subtracts it out. Removing that agency completes the chain:

| Method | Answer |
|---|---|
| Before and after | −33.1% |
| Difference in differences | −16.9% |
| **Difference in differences, without Summit County** | **−12.5%** |
| **The truth** | **−12.0%** |

## What To Watch For

- **Look at every agency separately, not just the group average.** Summit County is invisible in the trained group's average, because three other agencies dilute it. It is obvious on its own line.
- **"The lines look parallel" is a real check, done by eye.** It does not require any calculation and it is the most valuable minute you will spend.
- **Parallel before does not guarantee parallel after.** It is evidence, not proof. Something could still have happened to one group alone in the year the program started.
- **Removing an agency must be declared.** Say which one, why, and what the estimate was with it in. Removing agencies until the answer improves is a different activity entirely.

## 💡 The Insight

The years before the program are where you find out whether the comparison is any good, and they are the years everyone skips.

## Check Your Understanding

<details>
<summary><b>1.</b> The trained and comparison groups start at very different levels, 4.0 against 3.0. Does that violate the assumption?</summary>

No. The assumption is about how the groups **move**, not where they sit. A constant gap of one point subtracts out of the comparison entirely. What would violate the assumption is a gap that was already widening or narrowing before the program, which is exactly what Summit County does.
</details>

<details>
<summary><b>2.</b> Summit County was genuinely improving faster. Is it not unfair to exclude an agency for doing well?</summary>

The exclusion is not a judgment about the agency; it is about what the data can support. Summit County is a fine agency to study and a bad one to use as evidence about the training, because its improvement has a known cause that predates the program by four years. Leaving it in does not credit Summit County with anything. It credits the **training** with Summit County's reform, at the four other agencies too.
</details>

<details>
<summary><b>3.</b> Suppose all five trained agencies had been on steeper pre program trends. What then?</summary>

Then there would be no usable estimate from this design, and the honest report says so. That is not a failure of effort, it is a finding: the agencies that adopted the program were already on a different path, so their later improvement cannot be separated from it. The remedy is a different comparison group or a different design, not a more elaborate calculation on the same data.
</details>

## Key Takeaway

Plot the years before the program, one line per agency, and look at them before computing anything.

---

| | |
|---|---|
| **Previous** | [Topic 8: Two Differences Are Better Than One](Topic_08_Two_Differences_Are_Better_Than_One.md) |
| **Next** | [Topic 10: When the Comparison Group Moves Too](Topic_10_When_The_Comparison_Group_Moves_Too.md) |
| **Builds on** | [Topic 6](Topic_06_Comparing_Yourself_To_Someone_Else.md), [Topic 8](Topic_08_Two_Differences_Are_Better_Than_One.md) |
| **Used again in** | [Topic 17](Topic_17_When_You_Cannot_Randomize.md), [Topic 19](Topic_19_Reading_A_Causal_Claim.md), [Topic 20](Topic_20_Questions_To_Ask.md) |

*This module is part of a series developed for the Washington Data Exchange for Public Safety (WADEPS) through the Center for Interdisciplinary Statistical Education and Research (CISER) at Washington State University. Version 1.0, September 2026. Questions, errors, or suggestions: yin.zhang@wsu.edu*

*All examples use synthetic data created for teaching. They do not represent any real jurisdiction, agency, officer, or incident. See [Data/DATA_DICTIONARY.md](../../Data/DATA_DICTIONARY.md).*
