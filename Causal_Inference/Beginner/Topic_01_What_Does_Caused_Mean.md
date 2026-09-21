# Topic 1: What Does "Caused" Mean?

> **Developed by Yin Zhang, PhD**, Assistant Professor, Department of Mathematics and Statistics, Washington State University

**The question this module answers:** *A number went down after a program started. What would it take to say the program is the reason?*

---

## The Core Concept

Two sentences that sound almost identical mean very different things.

**"Use of force fell after the training."** This is a fact about records. Anyone with the data can check it, and nobody can argue with it.

**"The training lowered use of force."** This is a claim about **what would have happened otherwise**. It says that without the training, the number would have been higher. Nobody can check that directly, because it did not happen.

The first sentence needs data. The second needs data **and an argument**. Most disagreements about whether a program worked are really disagreements about the argument.

## Why It Matters

Budgets move on the second sentence. A program that appears to work gets renewed and copied; one that appears not to gets cancelled. If the first sentence is quietly allowed to stand in for the second, money follows numbers that were going to move anyway.

It runs in both directions, and the second direction is the one people forget:

- A program that did nothing gets credit for a decline that was already underway, and is expanded statewide.
- A program that genuinely helped is cancelled, because the numbers rose anyway for some other reason and nobody separated the two.

## The Example

Four agencies adopted a de escalation training program. Here is their use of force rate over seven years, with the month the training was fully in place marked.

![A line chart of the use of force rate at the agencies that took the training, falling steadily from about 4.0 per 100 arrests in 2019 to about 2.5 in 2026, with a vertical line marking the month the training was in place. Two labelled arrows point at the line, one before the training and one after, marking two competing explanations](Figures/fig_01_what_caused_means.png)

The rate fell. That part is not in dispute.

Now look at where the line was already going before the vertical line. It had been falling for four years, at roughly the same pace, for reasons that have nothing to do with a program that did not yet exist. **The chart is equally consistent with a training program that worked and with one that changed nothing at all.**

Nothing you can do to this chart will separate the two. No amount of zooming in, smoothing, or adding a trend line. The information needed is not on it.

## What To Watch For

- **"After" is doing all the work.** When a claim rests on the word after, ask what was happening before.
- **A steep decline is not stronger evidence.** A bigger drop after the program is also a bigger drop that might have happened anyway. Size is not proof.
- **The comparison is always there, even when it is invisible.** Every causal claim compares the world to some other world. If nobody says which, somebody has chosen one for you.

## 💡 The Insight

"It went down after the program started" and "the program brought it down" are different claims, and only the first is something a chart can show you.

## Check Your Understanding

<details>
<summary><b>1.</b> A chief says: "We put officers on foot patrol downtown in March, and by September calls were down 20 percent. Foot patrol works." What is the missing piece?</summary>

What downtown calls would have done from March to September **without** the foot patrol. Calls fall in most places in the autumn. They may have been falling since January. The neighbourhood may have changed for other reasons. Twenty percent is a real measurement, and on its own it says nothing about the patrol, because there is nothing to measure it against.
</details>

<details>
<summary><b>2.</b> If the chart above had shown a flat line for four years and then a sharp fall right at the vertical line, would that settle it?</summary>

It would be much better evidence, and still not settled. A sharp break at the right moment rules out "it was already falling," which is the most common alternative. It does not rule out something else changing in the same month: a new chief, a new reporting rule, a policy from the state, or a change in who was being arrested. Better evidence narrows the list of alternatives. It never empties it.
</details>

## Key Takeaway

Before accepting that a program worked, say out loud what you think would have happened without it. If you cannot, you do not yet have a causal claim.

---

| | |
|---|---|
| **Next** | [Topic 2: The Question Behind Every Policy Question](Topic_02_The_Question_Behind_Every_Policy_Question.md) |
| **Used again in** | every topic in this series |

*This module is part of a series developed for the Washington Data Exchange for Public Safety (WADEPS) through the Center for Interdisciplinary Statistical Education and Research (CISER) at Washington State University. Version 1.0, September 2026. Questions, errors, or suggestions: yin.zhang@wsu.edu*

*All examples use synthetic data created for teaching. They do not represent any real jurisdiction, agency, officer, or incident. See [Data/DATA_DICTIONARY.md](../../Data/DATA_DICTIONARY.md).*
