# Topic 16: Randomness Solves a Problem You Cannot Otherwise Solve

> **Developed by Yin Zhang, PhD**, Assistant Professor, Department of Mathematics and Statistics, Washington State University

**The question this module answers:** *Why is a coin toss considered the gold standard, when it seems like the least informed way to make a decision?*

---

## The Core Concept

Every problem in this series comes from the same place: **the agencies that got the program differ from the ones that did not, in ways that also affect the outcome.**

Randomisation removes that at a stroke. If a coin decides who gets the program, then the two groups differ only by chance, on **everything at once**: things you measured, things you did not, and things nobody has thought of.

That last part is what nothing else can do. A statistical adjustment has to name and measure a confounder. A coin toss handles the ones nobody named.

## Why It Matters

Randomising is not usually available to an analyst, because the program has already been given out by the time anyone asks for an evaluation. Understanding it is still worth a topic, for two reasons.

It is the standard everything else is measured against: every other design is an attempt to approximate what a coin toss would have given. And **it is sometimes available and not used**, because nobody asked early enough.

## The Example

Five of twelve agencies were chosen. Here is what the choice looked like against four thousand alternative ways of choosing five agencies at random.

![A histogram of four thousand random draws of five agencies from twelve, showing the ratio of the chosen agencies' baseline use of force rate to the rest. The distribution centres on 1.0 and most of it lies between 0.8 and 1.25. A vertical orange line far out in the right tail at 1.43 marks how the five agencies were actually chosen, and a label notes that 0.2 percent of random draws reach that far](Figures/fig_16_randomness.png)

| | Ratio of baseline rates, chosen against the rest |
|---|---|
| Random assignment, middle 90 percent of draws | 0.81 to 1.24 |
| Random assignment, median | 1.00 |
| **How the five were actually chosen** | **1.43** |

Only **8 of 4000** random draws produce an imbalance as large as the real one. Randomisation would almost certainly not have produced these five agencies, which is another way of saying they were not chosen at random.

### The honest complication

Randomisation does not **guarantee** balance. Look at the spread: only 29 percent of the random draws land within 5 percent of perfectly balanced, and some are as lopsided as 0.7 or 1.3.

With twelve agencies, a single coin toss can easily produce two groups that differ. What randomisation guarantees is that the differences are **accidental rather than systematic**, so they shrink as the number of units grows, and so the uncertainty calculations are honest about them. It is a promise about the procedure, not about any one result.

## What To Watch For

- **Randomise late, not never.** Programs are often rolled out in waves for budget reasons. Choosing which agencies go in wave one **by lottery** costs nothing and produces a clean comparison.
- **A waiting list is a comparison group.** Half the eligible agencies now, half in a year. Everyone gets it, and the evaluation works.
- **Randomise within the eligible group.** [Topic 13](Topic_13_Picking_The_Winners.md) showed that targeting the neediest destroys the evaluation. Randomising among the neediest fixes it and keeps the targeting.
- **Check the balance anyway, and report it.** Randomisation does not excuse you from showing the two groups' characteristics side by side.
- **Randomisation can fail in practice.** Agencies drop out, refuse, or adopt the program anyway. A randomised design still needs the checks in [Topic 10](Topic_10_When_The_Comparison_Group_Moves_Too.md).

## 💡 The Insight

A coin toss is not a way of avoiding a decision. It is the only method that balances the things nobody thought to measure.

## Check Your Understanding

<details>
<summary><b>1.</b> A director objects that randomising is unfair, because some agencies that need the program would not get it. What is the answer?</summary>

Two answers, and both are honest. When a program is rationed anyway, someone is not getting it regardless, and a lottery is a defensible way to decide who; the alternative is usually whoever asked first or knew someone. And a waiting list design gives it to everyone, just in a randomised order, which costs a delay rather than an exclusion. The genuinely unfair outcome is spending several years on a program nobody can evaluate.
</details>

<details>
<summary><b>2.</b> If randomisation does not guarantee balance, why is it better than deliberately matching the two groups?</summary>

Matching can only balance what is measured. Randomisation balances everything in expectation, including the reason a chief wanted the program, which no dataset holds. It also makes the uncertainty calculation meaningful: the confidence interval accounts for exactly the accidental imbalance the coin toss can produce. With a matched design there is no such guarantee, because the unmatched differences are unknown in both size and direction.
</details>

<details>
<summary><b>3.</b> Here the imbalance was 1.43, reached by 0.2 percent of random draws. Does that prove the selection was not random?</summary>

It is strong evidence and not proof, and the distinction matters. Unlikely things happen: 8 draws out of 4000 did reach it. What settles the question is not the number but the documentation, and here the answer key states the rule outright. This is the general lesson: the way to find out how a program was allocated is to ask, not to infer it from a balance table.
</details>

## Key Takeaway

If a program has not been allocated yet, ask whether the first wave can be chosen by lottery. It is the cheapest improvement available to any evaluation.

---

| | |
|---|---|
| **Previous** | [Topic 15: Correlation, Causation, and the Sentences In Between](Topic_15_Correlation_Causation_And_The_Sentences_In_Between.md) |
| **Next** | [Topic 17: When You Cannot Randomize](Topic_17_When_You_Cannot_Randomize.md) |
| **Builds on** | [Topic 12](Topic_12_Who_Chose_To_Participate.md), [Topic 13](Topic_13_Picking_The_Winners.md), [Topic 14](Topic_14_Confounding.md) |
| **Used again in** | [Topic 17](Topic_17_When_You_Cannot_Randomize.md), [Topic 20](Topic_20_Questions_To_Ask.md) |

*This module is part of a series developed for the Washington Data Exchange for Public Safety (WADEPS) through the Center for Interdisciplinary Statistical Education and Research (CISER) at Washington State University. Version 1.0, September 2026. Questions, errors, or suggestions: yin.zhang@wsu.edu*

*All examples use synthetic data created for teaching. They do not represent any real jurisdiction, agency, officer, or incident. See [Data/DATA_DICTIONARY.md](../../Data/DATA_DICTIONARY.md).*
