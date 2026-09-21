# Topic 17: When You Cannot Randomize

> **Developed by Yin Zhang, PhD**, Assistant Professor, Department of Mathematics and Statistics, Washington State University

**The question this module answers:** *The program was handed out years ago and nobody tossed a coin. What is actually available?*

---

## The Core Concept

This is the normal situation. The program exists, the agencies were chosen somehow, and an answer is wanted.

The designs available form a ladder, and moving down it means **assuming less**. Each design asks you to believe something, and the whole craft is in choosing the one whose assumption you can defend and then testing that assumption as hard as you can.

## Why It Matters

The temptation is to treat these as interchangeable options and pick whichever is easiest. They are not interchangeable: on this dataset, where the answer is known, they give 33.1, 16.9 and 12.5 percent for the same program.

## The Example

![A horizontal chart of four designs. Before and after reports 33.1 percent, difference in differences 16.9, difference in differences after checking the pre period 12.5, and randomising within the eligible group is marked as not available here because the program was already given out. Beside each is the assumption it requires, and a dashed line marks the true 12 percent](Figures/fig_17_when_you_cannot_randomize.png)

| Design | It reported | It has to assume |
|---|---|---|
| Before and after | **−33.1%** | nothing else changed between the two periods |
| Difference in differences | **−16.9%** | the two groups would have moved together |
| The same, after checking the years before | **−12.5%** | the same, and the check found nothing against it |
| Randomise within the eligible group | not available here | nothing: the groups match on average by design |

Read the right hand column downward. "Nothing else changed" is a claim about the whole world over four years, and it is never true. "The two groups would have moved together" is a claim about two specific sets of agencies, which is far more modest. Adding the pre period check does not weaken the assumption further, but it gives you evidence about whether it holds.

**The estimate improves as the assumption gets smaller.** That is the pattern, and it is the reason to work down the ladder rather than stopping at the first design that produces a number.

## The other tools, named

Three more designs appear constantly in this literature. None of them applies to this dataset, and knowing why is as useful as knowing how they work.

| Design | What it needs | Why not here |
|---|---|---|
| **Matching** | agencies that resemble each other on the things that matter | the trained agencies were 43 percent higher on the outcome itself, and there is nothing to match them to |
| **Instrumental variables** | something that pushed agencies into the program but has no other route to the outcome | no such thing exists in these records |
| **Regression discontinuity** | a sharp threshold that decided who got in | the rule was close to a threshold, and close is not sharp |

The Advanced series takes all three apart in detail. For now the point is that a design is not a technique you apply; it is a claim about how the world produced your data, and the world has to cooperate.

## What To Watch For

- **Say which design and which assumption, in the report.** One sentence each.
- **Test the assumption you chose.** The pre period check in [Topic 9](Topic_09_Were_They_Moving_Together_Before.md) is the main one available, and it is free.
- **Report more than one design.** If before and after and difference in differences disagree by twenty points, the reader should see that.
- **A fancier method is not a better assumption.** Matching, weighting and machine learning all handle measured differences. None of them handles the reason an agency joined.

## 💡 The Insight

You do not choose a method. You choose which assumption you are prepared to defend, and the method follows.

## Check Your Understanding

<details>
<summary><b>1.</b> Why does adding the pre period check change the estimate from 16.9 to 12.5 without changing the assumption?</summary>

The assumption is the same in both: that the groups would have moved together. The check does not weaken it, it **tests** it, and the test found one agency for which it plainly failed. Removing that agency leaves a set of agencies for which the assumption survives scrutiny. The estimate improved because the assumption is now closer to true, not because less is being assumed.
</details>

<details>
<summary><b>2.</b> An analyst says the study used matching, and that matching is more rigorous than difference in differences. Is that right?</summary>

No, and the comparison is not on a single scale. Matching addresses differences in **measured characteristics between the groups**. Difference in differences addresses everything that changed over **time** for both groups. They solve different problems and are often used together. Neither is more rigorous in the abstract, and on this dataset matching would be actively misleading, because the characteristic that separates the groups is the outcome's own history.
</details>

<details>
<summary><b>3.</b> All three of the extra designs are unavailable here. Is this dataset unusually poor?</summary>

It is fairly typical. Instruments are rare and most claimed ones do not survive scrutiny; sharp thresholds exist but are uncommon; matching needs overlap that selected programs usually destroy. The realistic toolkit for most public safety evaluations is a comparison group, a pre period check, and an honest account of what remains unresolved. That is not a weak position, provided it is described accurately.
</details>

## Key Takeaway

Pick the design whose assumption you can state in one sentence and test with data you have, then state it and test it.

---

| | |
|---|---|
| **Previous** | [Topic 16: Randomness Solves a Problem You Cannot Otherwise Solve](Topic_16_Randomness_Solves_A_Problem.md) |
| **Next** | [Topic 18: How Long Do You Have to Wait?](Topic_18_How_Long_Do_You_Have_To_Wait.md) |
| **Builds on** | [Topic 8](Topic_08_Two_Differences_Are_Better_Than_One.md), [Topic 9](Topic_09_Were_They_Moving_Together_Before.md), [Topic 16](Topic_16_Randomness_Solves_A_Problem.md) |
| **Used again in** | [Topic 20](Topic_20_Questions_To_Ask.md) |

*This module is part of a series developed for the Washington Data Exchange for Public Safety (WADEPS) through the Center for Interdisciplinary Statistical Education and Research (CISER) at Washington State University. Version 1.0, September 2026. Questions, errors, or suggestions: yin.zhang@wsu.edu*

*All examples use synthetic data created for teaching. They do not represent any real jurisdiction, agency, officer, or incident. See [Data/DATA_DICTIONARY.md](../../Data/DATA_DICTIONARY.md).*
