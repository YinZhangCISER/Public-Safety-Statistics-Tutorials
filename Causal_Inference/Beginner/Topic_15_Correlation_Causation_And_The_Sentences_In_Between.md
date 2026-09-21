# Topic 15: Correlation, Causation, and the Sentences In Between

> **Developed by Yin Zhang, PhD**, Assistant Professor, Department of Mathematics and Statistics, Washington State University

**The question this module answers:** *"Correlation is not causation" is true and useless. What are you allowed to say?*

---

## The Core Concept

Everyone knows the slogan. Almost nobody knows what to do after saying it, so in practice the conversation goes straight from "correlation is not causation" to reporting the correlation as though it were.

There are sentences in between, and they form a ladder. Each rung says more than the one below and requires more to support it.

| The sentence | What it needs |
|---|---|
| The rate fell at these agencies | records |
| It fell more than at other agencies | records from other agencies |
| It fell more than at other agencies that were moving the same way before | records, plus a pre period check |
| The program caused the fall | all of the above, plus an argument that nothing else differed |
| The program will cause the same fall elsewhere | all of the above, plus a reason to think other places are like these |

Most reports climb one or two rungs and write the fourth sentence.

## Why It Matters

The top rung is the one funders act on, and it is the one that needs the most support. A report that stops honestly at rung three is more useful than one that asserts rung five, because the reader can tell what has been established.

## The Example

Every diagram below produces exactly the same observation: agencies that took the training had their use of force fall.

![Three panels, each with a box labelled took the training and a box labelled use of force fell. In the first, an arrow runs directly between them, labelled the effect. In the second, a third box, everything was already falling statewide, has arrows into both, and the direct arrow is dashed. In the third the third box reads their rate was the highest in the state, again with arrows into both](Figures/fig_15_three_structures.png)

**All three are consistent with the data.** They are not consistent with each other.

The first says the training worked. The second says a statewide decline lowered the rate at every agency, and the trained ones were simply among them. The third says the agencies were picked for having high rates, and high rates come down on their own.

The observed association does not distinguish them. What distinguishes them is the evidence assembled in Topics 5 through 14: what happened to untrained agencies, whether the groups were moving together before, and how the recipients were chosen.

## What To Watch For

- **Name the rung.** Write the sentence you are entitled to, rather than the strongest one that is not obviously false.
- **The word "linked" is a rung two word being used at rung four.** So are "associated with," "followed by," and "coincided with." They are honest words, and readers routinely read them as causal.
- **Generalisation is its own rung.** An effect measured at five agencies in one state is not automatically an effect at three hundred. That last rung is skipped almost universally.
- **Going down a rung is not a defeat.** "We found the rate fell 12 percent more than at comparable agencies that were moving the same way before" is a strong, defensible, useful sentence.

## 💡 The Insight

The question is never whether correlation equals causation. It is which rung of the ladder your evidence reaches, and whether your sentence is standing on that rung.

## Check Your Understanding

<details>
<summary><b>1.</b> Which rung does this reach: "Agencies with de escalation training have lower use of force rates than agencies without it"?</summary>

Rung two at best, and possibly lower. It compares levels rather than changes, so it does not even establish that anything fell. In this dataset the sentence would be false in the other direction: the trained agencies started with **higher** rates than the untrained ones, because that is how they were chosen. A level comparison between groups that were selected differently says almost nothing.
</details>

<details>
<summary><b>2.</b> Rewrite "the training cut use of force by 12 percent" to sit honestly at rung three.</summary>

"Use of force at the trained agencies fell 12 percent more than at comparison agencies that had been moving at the same rate before the program began." Longer, and every clause is doing work: it names the comparison, it names the check that was run, and it says "fell more than" rather than "cut." A reader who wants the causal claim can weigh the remaining gap themselves.
</details>

<details>
<summary><b>3.</b> What would it take to reach the fifth rung, that the program would work elsewhere?</summary>

An argument that the agencies studied resemble the agencies you want to apply it to, in the respects that matter. Here that argument would be weak: the five trained agencies were the highest use of force agencies in the state, and a program that helps at the extreme may do nothing in the middle. Reaching rung five usually requires several studies in different settings, not a better analysis of one.
</details>

## Key Takeaway

Decide which rung your evidence reaches, write that sentence, and resist the one above it.

---

| | |
|---|---|
| **Previous** | [Topic 14: Confounding, the Third Thing](Topic_14_Confounding.md) |
| **Next** | [Topic 16: Randomness Solves a Problem You Cannot Otherwise Solve](Topic_16_Randomness_Solves_A_Problem.md) |
| **Builds on** | [Topic 2](Topic_02_The_Question_Behind_Every_Policy_Question.md), [Topic 14](Topic_14_Confounding.md) |
| **Used again in** | [Topic 19](Topic_19_Reading_A_Causal_Claim.md), [Topic 20](Topic_20_Questions_To_Ask.md) |

*This module is part of a series developed for the Washington Data Exchange for Public Safety (WADEPS) through the Center for Interdisciplinary Statistical Education and Research (CISER) at Washington State University. Version 1.0, September 2026. Questions, errors, or suggestions: yin.zhang@wsu.edu*

*All examples use synthetic data created for teaching. They do not represent any real jurisdiction, agency, officer, or incident. See [Data/DATA_DICTIONARY.md](../../Data/DATA_DICTIONARY.md).*
