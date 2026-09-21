# Topic 14: Confounding, the Third Thing

> **Developed by Yin Zhang, PhD**, Assistant Professor, Department of Mathematics and Statistics, Washington State University

**The question this module answers:** *Six topics have described six problems. Is there one idea underneath them all?*

---

## The Core Concept

There is, and it has a name.

A **confounder** is something that affects both **who got the program** and **what happened to the outcome**. When one exists and is not accounted for, its influence gets counted as the program's.

The test has two parts and both must hold:

1. Does it differ between the group that got the program and the group that did not?
2. Does it affect the outcome on its own?

Something that fails either test is not a confounder and does not need to be dealt with.

## Why It Matters

Once the definition is clear, the previous topics stop being a list of separate traps and become one idea seen from different angles.

| Topic | The confounder |
|---|---|
| [5](Topic_05_Things_Were_Already_Changing.md) | time itself, since the before period and the after period differ in everything |
| [9](Topic_09_Were_They_Moving_Together_Before.md) | Summit County's own reform, which arrived with the trained group |
| [11](Topic_11_Why_The_Worst_Performers_Always_Improve.md) | having had a bad year, which is both why they were chosen and why they improved |
| [13](Topic_13_Picking_The_Winners.md) | the baseline rate, which determined selection and predicted the change |

## The Example

The confounder with the largest effect in this dataset is the statewide decline. It is a confounder in the before and after comparison because the "after" period is later in time, and later in time means lower for everybody.

![A bar chart with three bars in rate units. The trained agencies were at 3.59 use of force per 100 arrests before the training. Where the statewide decline alone would have put them is 2.89. Where they actually ended up is 2.53. Arrows between the bars label the two steps as minus 19.5 percent for the statewide decline and minus 12.5 percent for the training](Figures/fig_14_confounding.png)

| | Use of force per 100 arrests |
|---|---|
| The trained agencies, before | **3.59** |
| Where the statewide decline alone would have put them | **2.89** |
| Where they actually ended up | **2.53** |

The whole fall is 29.5 percent. **The statewide decline accounts for 19.5 points of it and the training for 12.5.** The two do not add to 29.5, because percentage changes multiply rather than add: a fall of 19.5 percent followed by a further fall of 12.5 percent leaves you at 70.5 percent of where you started, which is a total fall of 29.5 percent.

Handling the confounder is what the comparison group does. It measures the statewide decline directly, from agencies where the training cannot be responsible for it, and subtracts it.

## What To Watch For

- **Both conditions, or it is not a confounder.** A variable that differs between the groups but does not affect the outcome can be ignored. So can one that affects the outcome but is the same in both groups.
- **Time is the most common confounder and the least often named.** Any before and after comparison has it.
- **Some things must not be controlled for.** If the training reduced use of force **by** changing how officers handle a call, then adjusting for how the call was handled removes the effect you are trying to measure. Things caused by the program are not confounders and should be left alone. The Intermediate series takes this up properly.
- **A comparison group handles every confounder shared by both groups at once**, including the ones nobody thought of. That is its real power, and the reason it beats a long list of statistical adjustments.

## 💡 The Insight

A confounder has to do two jobs at once: change who gets the program, and change the outcome. Anything doing only one of them is not your problem.

## Check Your Understanding

<details>
<summary><b>1.</b> A new state law on reporting took effect in 2022 and applied to every agency. Is it a confounder for this evaluation?</summary>

Not for the comparison with the comparison group, because it hit both groups equally and subtracts out. It **is** a confounder for a before and after comparison, which cannot distinguish it from the training. This is the general pattern: a comparison group converts statewide confounders into harmless background.
</details>

<details>
<summary><b>2.</b> The trained agencies serve slightly larger populations. Confounder?</summary>

Test both conditions. It does differ between the groups, though only by about 13 percent. Does population size affect the change in the use of force **rate** over these years? There is no obvious reason it should, and the rate already divides by arrests. On the evidence it fails the second test, so it is not a confounder. Stating that reasoning is more useful than adding it to a model without comment.
</details>

<details>
<summary><b>3.</b> Why can a comparison group handle confounders nobody has thought of, when a statistical adjustment cannot?</summary>

Because the adjustment has to name the variable and measure it, while the comparison group does not. Anything that happened to both groups equally is removed by the subtraction whether or not anyone knew it happened. That is why finding a good comparison group is worth more than any amount of modelling, and why the assumption in [Topic 9](Topic_09_Were_They_Moving_Together_Before.md) is the one that matters: it is the assumption that the unnamed things really were shared.
</details>

## Key Takeaway

For anything you are worried about, ask both questions: does it differ between the groups, and does it move the outcome. Only things answering yes twice need handling.

---

| | |
|---|---|
| **Previous** | [Topic 13: Picking the Winners Makes the Program Look Good](Topic_13_Picking_The_Winners.md) |
| **Next** | [Topic 15: Correlation, Causation, and the Sentences In Between](Topic_15_Correlation_Causation_And_The_Sentences_In_Between.md) |
| **Builds on** | [Topic 5](Topic_05_Things_Were_Already_Changing.md), [Topic 9](Topic_09_Were_They_Moving_Together_Before.md), [Topic 13](Topic_13_Picking_The_Winners.md) |
| **Used again in** | [Topic 16](Topic_16_Randomness_Solves_A_Problem.md), [Topic 17](Topic_17_When_You_Cannot_Randomize.md), [Topic 20](Topic_20_Questions_To_Ask.md) |

*This module is part of a series developed for the Washington Data Exchange for Public Safety (WADEPS) through the Center for Interdisciplinary Statistical Education and Research (CISER) at Washington State University. Version 1.0, September 2026. Questions, errors, or suggestions: yin.zhang@wsu.edu*

*All examples use synthetic data created for teaching. They do not represent any real jurisdiction, agency, officer, or incident. See [Data/DATA_DICTIONARY.md](../../Data/DATA_DICTIONARY.md).*
