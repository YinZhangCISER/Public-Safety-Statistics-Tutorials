# Module 1: From "It Went Down" to "The Program Did It"

> **Developed by Yin Zhang, PhD**, Assistant Professor, Department of Mathematics and Statistics, Washington State University

## The Question

Three sentences about the same program, each stronger than the last. Which one do a given set of records support, and what does each additional rung cost?

## The Idea in Plain Language

A causal claim is a comparison against a world that did not happen. Each piece of evidence you add replaces a guess about that world with a measurement, and the estimate moves.

The Beginner series made that argument in words. This module computes all three sentences on the same records so the movement is visible as arithmetic.

## The Method

> **rung one** the rate after, divided by the rate before, at the agencies that took the program
>
> **rung two** that quantity, divided by the same quantity at agencies that did not
>
> **rung three** the same, restricted to agencies whose pre program trend matches the comparison group

In words: measure the change, subtract the change that happened anyway, and then drop any agency for which "happened anyway" was clearly different.

| Assumption | What it takes |
|---|---|
| Rung one: nothing else changed over four years | never true, and almost never stated |
| Rung two: both groups would have changed by the same proportion | a comparison group |
| Rung three: the same, and the pre period is consistent with it | a plot and a regression on the years before |

## Worked Example

![A horizontal bar chart of three sentences. The rate fell reports 33.1 percent and needs records only. It fell more than at other agencies reports 16.9 percent and needs records from seven more agencies. It fell more than at agencies moving the same way reports 12.5 percent and needs a pre period check. A dashed line marks the true 12 percent](Figures/fig_01_claim_ladder.png)

| Sentence | Estimate | What it takes to say it |
|---|---|---|
| The rate fell | −33.1% | records |
| It fell more than at other agencies | −16.9% | records from seven more agencies |
| **It fell more than at agencies moving the same way** | **−12.5%** | the same, plus a pre period check |
| **The truth** | **−12.0%** | |

Rung one is honest and answers a different question. Rung two divides by what the comparison agencies did, which was a 19.5 percent fall of their own.

Rung three is the same division run on four agencies instead of five. The fifth, Summit County, was falling at **12.0 percent a year before the training existed** against the comparison group's 4.5. Its own reform gets credited to the program unless it is removed.

**Nothing became more sophisticated between rung two and rung three.** The third estimate is the same arithmetic on a subset chosen by a check anyone can run.

## Do It Yourself

> 📓 **Notebook:** [Module_01_From_It_Went_Down_To_The_Program_Did_It.ipynb](Notebooks/Module_01_From_It_Went_Down_To_The_Program_Did_It.ipynb)
> [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/OWNER/REPO/blob/main/Causal_Inference/Intermediate/Notebooks/Module_01_From_It_Went_Down_To_The_Program_Did_It.ipynb)
> About 20 minutes.

- Computes all three rungs from the raw monthly files
- Prints each trained agency's pre program trend beside the comparison group's
- The exercise runs rung two against each comparison agency separately

## Pitfalls

| What goes wrong | What it looks like | What to do |
|---|---|---|
| Reporting rung one as the effect | a number two to three times too large | name the comparison in the sentence |
| Using one comparison agency | an estimate anywhere from +2 to −29 percent | pool every agency the rule admits |
| Skipping the pre period check | rung two reported as rung three | plot the years before, one line per agency |
| Choosing the comparison after seeing results | an estimate that cannot be defended | write the rule down first |
| Treating rung three as causal | a claim the design does not support | see the table of what is still unresolved |

## Check Your Understanding

<details>
<summary><b>1.</b> Rung two gives 16.9 and rung three gives 12.5. Which is closer to the truth, and does that make rung three the better method?</summary>

Rung three is closer, and the reason is not that it is a better method. It is the same method applied to agencies for which its assumption survives inspection. If Summit County's pre trend had matched the others, rung two and rung three would be the same number and both would be right. The improvement comes from the check, not from the arithmetic.
</details>

<details>
<summary><b>2.</b> A colleague says rung three is "cherry picking" because an agency was dropped. What is the answer?</summary>

The objection is legitimate in form and answerable in this case. Cherry picking means choosing based on the result; here the choice was made on the **pre program** trend, which is data the outcome cannot influence, and the reason is documented. The test of good faith is whether the rule and the exclusion would have been stated before the estimates were seen, and whether the estimate with the agency included is also reported. Both are cheap.
</details>

<details>
<summary><b>3.</b> Rung three lands at 12.5 against a truth of 12.0. Is the remaining 0.5 points meaningful?</summary>

No. It is well inside what sampling noise produces from twelve agencies over 88 months, and the interval around 12.5 runs roughly from 7 to 18. Treating 12.5 as distinguishable from 12.0 would be reading precision the data does not have. The right report gives the interval, not the third digit.
</details>

## Key Takeaway

Write the sentence you are entitled to, then compute the next rung up and see how far the number moves.

---

| | |
|---|---|
| **Next** | [Module 2: Potential Outcomes Without the Algebra](Module_02_Potential_Outcomes_Without_The_Algebra.md) |
| **Builds on** | Beginner [Topics 4](../Beginner/Topic_04_Before_And_After_Is_Not_Enough.md), [8](../Beginner/Topic_08_Two_Differences_Are_Better_Than_One.md) and [9](../Beginner/Topic_09_Were_They_Moving_Together_Before.md) |
| **Used again in** | every module in this series |

*This module is part of a series developed for the Washington Data Exchange for Public Safety (WADEPS) through the Center for Interdisciplinary Statistical Education and Research (CISER) at Washington State University. Version 1.0, September 2026. Questions, errors, or suggestions: yin.zhang@wsu.edu*

*All examples use synthetic data created for teaching. They do not represent any real jurisdiction, agency, officer, or incident. See [Data/DATA_DICTIONARY.md](../../Data/DATA_DICTIONARY.md).*
