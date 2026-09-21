# Topic 2: The Question Behind Every Policy Question

> **Developed by Yin Zhang, PhD**, Assistant Professor, Department of Mathematics and Statistics, Washington State University

**The question this module answers:** *Different people keep asking different questions about the same program. Which one is the causal question?*

---

## The Core Concept

Around any program there are four questions that get mixed together. Only one of them is causal, and it is usually the one nobody states.

| The question | What answers it |
|---|---|
| **What happened?** | the records |
| **Is it unusual?** | a comparison against other places or other years |
| **Did the program do it?** | a comparison against what would have happened without the program |
| **Should it keep being funded?** | the answer above, plus cost, plus values |

The third question is the causal one. The first two can be answered from data alone. The fourth cannot be answered by anyone's data, because it involves what a community wants.

## Why It Matters

Meetings go badly when people answer different questions and think they are disagreeing.

An analyst reports the first question honestly: the rate fell 33 percent. A council member hears the third: the program cut use of force by a third. A journalist writes the fourth: a program that cuts use of force by a third should be funded everywhere.

Nobody lied. The claim grew one step at each handoff, and by the end it is carrying weight that the original measurement cannot hold.

## The Example

Take the same four agencies from [Topic 1](Topic_01_What_Does_Caused_Mean.md). The solid line is the record. The two dashed lines are two different guesses about the world without the training.

![A line chart of the use of force rate with the recorded line continuing after the training date, and two dashed lines projecting forward from that date: one flat and one declining. The area between the recorded line and the flat dashed line is shaded, and a label notes that the gap is the effect and depends entirely on which dashed line is right](Figures/fig_02_the_question.png)

If the flat dashed line is right, the training produced a large effect. If the declining one is right, the training produced a much smaller one. **The solid line is identical in both cases.**

That is the whole difficulty of causal inference in one picture. The answer does not depend on how carefully you measure what happened. It depends on which dashed line you can defend.

## What To Watch For

- **Ask which question is being answered.** "The rate fell 33 percent" answers the first. If somebody responds "so the program works," a question has been swapped.
- **The causal question always contains a hidden word.** Instead of a program, a comparison. Instead of a change, a difference from something else.
- **The fourth question is not statistical.** A program with a small real effect may still be worth funding, and one with a large effect may not be. That decision is not the analyst's to make, and pretending the numbers make it is its own failure.

## 💡 The Insight

Every causal question is a comparison between the world that happened and a world that did not. The work is in defending your description of the second one.

## Check Your Understanding

<details>
<summary><b>1.</b> Which question does this answer: "Our use of force rate is the third highest of the twelve agencies in the region"?</summary>

The second, is it unusual. It compares this agency against other places at the same time, which is a real and useful comparison. It says nothing about why the rate is high, and nothing about whether any program changed it. A high rate could reflect what officers do, or what they face, or how the agency records things.
</details>

<details>
<summary><b>2.</b> A grant application says "this program reduced use of force by 33 percent in participating agencies." Rewrite it so it only claims what a before and after comparison supports.</summary>

"Use of force in participating agencies fell 33 percent between the period before the program and the period after it was fully in place." The change is that the sentence no longer names the program as the cause. It also invites the obvious next question, which is what happened at agencies that did not participate, and that question is the beginning of an actual answer.
</details>

## Key Takeaway

Write down which of the four questions you are answering before you compute anything, and use that sentence in the report.

---

| | |
|---|---|
| **Previous** | [Topic 1: What Does "Caused" Mean?](Topic_01_What_Does_Caused_Mean.md) |
| **Next** | [Topic 3: The World You Cannot See](Topic_03_The_World_You_Cannot_See.md) |
| **Builds on** | [Topic 1](Topic_01_What_Does_Caused_Mean.md) |
| **Used again in** | [Topic 15](Topic_15_Correlation_Causation_And_The_Sentences_In_Between.md), [Topic 20](Topic_20_Questions_To_Ask.md) |

*This module is part of a series developed for the Washington Data Exchange for Public Safety (WADEPS) through the Center for Interdisciplinary Statistical Education and Research (CISER) at Washington State University. Version 1.0, September 2026. Questions, errors, or suggestions: yin.zhang@wsu.edu*

*All examples use synthetic data created for teaching. They do not represent any real jurisdiction, agency, officer, or incident. See [Data/DATA_DICTIONARY.md](../../Data/DATA_DICTIONARY.md).*
