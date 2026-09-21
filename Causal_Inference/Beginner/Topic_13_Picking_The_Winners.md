# Topic 13: Picking the Winners Makes the Program Look Good

> **Developed by Yin Zhang, PhD**, Assistant Professor, Department of Mathematics and Statistics, Washington State University

**The question this module answers:** *What happens when the rule for choosing who gets the program is based on the very thing the program is meant to change?*

---

## The Core Concept

[Topic 11](Topic_11_Why_The_Worst_Performers_Always_Improve.md) showed that anything chosen for being extreme improves on its own. [Topic 12](Topic_12_Who_Chose_To_Participate.md) showed that the groups match on everything except the outcome's own history.

Put them together and you have the most damaging pattern in program evaluation: **the program is given to whoever scores worst on the outcome, and then evaluated on that same outcome.**

This is called **selection on the outcome**. When it happens, an apparent effect is guaranteed before the program begins, and no amount of care in the later analysis removes it.

## Why It Matters

This is not a rare mistake. It is standard practice, because it is the fair way to allocate a scarce program: give it to the agencies that need it most.

The allocation is defensible. The evaluation built on top of it is not, unless the comparison group is chosen the same way.

## The Example

Here is the rule that was actually used in this dataset, disclosed in the answer key: **the five agencies with the highest use of force rates were selected.**

| Agency | Rate before the program | Selected |
|---|---|---|
| Tarnbridge | 4.02 | **yes** |
| Pinecrest | 3.62 | **yes** |
| Millgate | 3.59 | **yes** |
| Stonewick | 3.53 | **yes** |
| Havenbrook | 3.20 | no |
| Summit County | 3.12 | **yes** |
| Ashfell | 2.67 | no |
| the five others | 2.09 to 2.59 | no |

Now the demonstration. Take the seven agencies that received **nothing at all**, pick the three that were worst, and evaluate a program that does not exist.

![A horizontal bar chart with two bars. Choosing the three worst performing untrained agencies and comparing them against the other four produces an apparent 9.2 percent reduction. Choosing the three best produces an apparent 10.5 percent increase. A dashed line at zero is labelled as the true effect of a program nobody received](Figures/fig_13_picking_winners.png)

| Which agencies were "given" the imaginary program | What a difference in differences reports |
|---|---|
| The three worst performers | **−9.2%** |
| The three best performers | **+10.5%** |
| **The truth** | **0%** |

**A program that does not exist appears to cut use of force by 9.2 percent**, three quarters of the real training effect, purely because of how the recipients were chosen. Choose the other end of the ranking and the same imaginary program appears to make things 10.5 percent worse.

This is difference in differences done correctly, with a real comparison group, on real records. The method is not at fault. The selection rule is.

## What To Watch For

- **Ask what the selection rule was.** If it mentions the outcome, or a close relative of it, the evaluation needs a comparison group chosen by the same rule.
- **"We targeted the agencies that needed it most" is a warning, not a reassurance.** It is good policy and it destroys the evaluation.
- **Thresholds are the same problem.** "All agencies above 3.0" selects on the outcome exactly as much as "the worst five" does.
- **The direction is predictable.** Selecting the worst makes the program look good. Selecting the best, as sometimes happens when a program picks agencies likely to succeed, makes it look harmful.
- **The comparison group can fix it, if it is chosen the same way.** Compare the worst five that got the program against the worst five that did not. Then the regression happens in both groups and cancels.

## 💡 The Insight

If the rule for choosing who gets a program mentions the outcome, the evaluation has an answer before it starts.

## Check Your Understanding

<details>
<summary><b>1.</b> Why does the imaginary program appear to make things worse when the best performers are chosen?</summary>

Same mechanism, opposite direction. Agencies at the bottom of a ranking are partly there because they had a good year. Next period their luck is re drawn and their numbers rise, while the agencies they are compared against come down. The gap opens in the unfavourable direction, and a difference in differences dutifully reports it as harm.
</details>

<details>
<summary><b>2.</b> The real training effect is 12 percent and the fake effect from selection is 9.2 percent. Are they simply added together?</summary>

Not exactly, but the intuition is right: the selection bias and the real effect push in the same direction and the estimate picks up both. That is why the difference in differences in [Topic 8](Topic_08_Two_Differences_Are_Better_Than_One.md) came out at 16.9 rather than 12. What made the 12.5 percent estimate in [Topic 9](Topic_09_Were_They_Moving_Together_Before.md) work was not that selection stopped mattering; it was that the remaining four trained agencies happened to be moving in step with the comparison group before the program, which is the condition that lets the bias subtract out.
</details>

<details>
<summary><b>3.</b> A state wants to allocate a program to the neediest agencies and still evaluate it properly. What should it do?</summary>

Set the eligibility rule, then randomise **within** the eligible group. Give the program to half the agencies above the threshold and put the other half on a waiting list. Both halves were selected on the outcome, so both regress equally, and the comparison between them is clean. This costs nothing except a delay for half the agencies, and it is the single most valuable thing a funder can do. See [Topic 16](Topic_16_Randomness_Solves_A_Problem.md).
</details>

## Key Takeaway

Ask how recipients were chosen before anything else. If the answer involves the outcome, the comparison group has to be chosen the same way.

---

| | |
|---|---|
| **Previous** | [Topic 12: Who Chose to Participate?](Topic_12_Who_Chose_To_Participate.md) |
| **Next** | [Topic 14: Confounding, the Third Thing](Topic_14_Confounding.md) |
| **Builds on** | [Topic 11](Topic_11_Why_The_Worst_Performers_Always_Improve.md), [Topic 12](Topic_12_Who_Chose_To_Participate.md) |
| **Used again in** | [Topic 16](Topic_16_Randomness_Solves_A_Problem.md), [Topic 19](Topic_19_Reading_A_Causal_Claim.md), [Topic 20](Topic_20_Questions_To_Ask.md) |

*This module is part of a series developed for the Washington Data Exchange for Public Safety (WADEPS) through the Center for Interdisciplinary Statistical Education and Research (CISER) at Washington State University. Version 1.0, September 2026. Questions, errors, or suggestions: yin.zhang@wsu.edu*

*All examples use synthetic data created for teaching. They do not represent any real jurisdiction, agency, officer, or incident. See [Data/DATA_DICTIONARY.md](../../Data/DATA_DICTIONARY.md).*
