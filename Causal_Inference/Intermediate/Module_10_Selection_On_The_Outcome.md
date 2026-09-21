# Module 10: Selection on the Outcome

> **Developed by Yin Zhang, PhD**, Assistant Professor, Department of Mathematics and Statistics, Washington State University

## The Question

The five agencies were chosen for having the highest use of force rates, and the use of force rate is the outcome. How much does that cost, and what determines whether it costs anything at all?

## The Idea in Plain Language

Run the real analysis on a program that does not exist, given to agencies chosen by the same kind of rule. Whatever it reports is manufactured, and it measures what the selection rule does on its own.

## The Method

> apply the selection rule to units that received **nothing**, then run the same estimator
>
> and separately, compare the pre program trends of the groups the rule created

## Worked Example

The selection was close to "take the worst five". Four of the top five were chosen and the fifth chosen agency sits sixth.

### The balance table, and the row that matters

| Characteristic | Trained | Not trained | Ratio |
|---|---|---|---|
| Sworn officers | 193.6 | 176.1 | 1.10 |
| Population served | 107,400 | 95,400 | 1.13 |
| Violent crime rate | 2.76 | 3.25 | 0.85 |
| Property crime rate | 16.30 | 16.51 | 0.99 |
| Public safety budget share | 25.6 | 25.8 | 0.99 |
| **Use of force rate before the program** | **3.58** | **2.50** | **1.43** |

**A balance table that stopped at the first five rows would have been reassuring and wrong.**

### What the selection rule produces on its own

![A horizontal bar chart of four analyses. The real program before and after gives 29.5 percent, difference in differences gives 12.5 against a true 12. A program that does not exist, given to the worst three untrained agencies, gives 9.2 percent; given to the best three, it gives plus 10.5 percent. For those two the true answer is zero](Figures/fig_10_selection_on_outcome.png)

| What was analysed | Estimate | True answer |
|---|---|---|
| The real program, before and after only | −29.5% | −12.0% |
| The real program, difference in differences | **−12.5%** | −12.0% |
| **No program, given to the worst three untrained** | **−9.2%** | **0.0%** |
| **No program, given to the best three untrained** | **+10.5%** | **0.0%** |

A program that does not exist reports a 9.2 percent reduction, three quarters of the real effect, purely from how the recipients were picked.

### Why the real estimate survives anyway

| Study | Treated pre trend | Its comparison's pre trend | Gap |
|---|---|---|---|
| **The real study** | −5.17% a year | −4.46% a year | **−0.71** |
| Worst three placebo | −4.83% a year | −1.55% a year | **−3.29** |
| Best three placebo | +2.13% a year | −4.68% a year | **+6.81** |

There it is, in the last column. The real study's groups differ in pre trend by 0.71 points a year, which is nothing. The two placebos differ by 3.29 and 6.81, and those gaps are what the analysis reports as effects.

**Selection on the outcome does not bias the estimate by itself. It creates the conditions for bias, and the parallel trends check is what tells you whether the conditions turned into a problem.** The check passes here and would have failed for both placebos.

That is a more useful statement than "never select on the outcome", which is advice nobody in a funding agency can follow.

## Do It Yourself

> 📓 **Notebook:** [Module_10_Selection_On_The_Outcome.ipynb](Notebooks/Module_10_Selection_On_The_Outcome.ipynb)
> [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/OWNER/REPO/blob/main/Causal_Inference/Intermediate/Notebooks/Module_10_Selection_On_The_Outcome.ipynb)
> About 25 minutes.

- Ranks every agency on the outcome and marks who was selected
- Builds the balance table including the outcome's own history
- Runs the placebo at both ends of the ranking
- The exercise repeats the placebo at every group size

## Pitfalls

| What goes wrong | What it looks like | What to do |
|---|---|---|
| A balance table without the outcome's history | two groups declared well matched | always include it |
| Assuming selection on the outcome is fatal | a usable study abandoned | check the pre trends |
| Assuming it is harmless because the groups match | 9 percent out of nothing | run the placebo |
| One placebo treated as decisive | a noisy result over interpreted | run several, report all |

## What to Write

> *Agencies were selected for the program on the basis of their pre program use of force rate, which is the study's outcome. The treated agencies' pre program rate averaged 43 percent above the comparison agencies', while the two groups differ by less than 15 percent on every other recorded characteristic. Selection on the outcome creates a risk of regression to the mean; the pre program trends of the two groups differ by 0.70 percent a year with a 95 percent interval from 3.31 below to 1.97 above, which does not indicate a trajectory difference large enough to account for the estimate.*

## Check Your Understanding

<details>
<summary><b>1.</b> The worst three placebo reports 9.2 percent, and those agencies' own pre trend is 4.83 percent a year, close to the comparison group's 4.46. Where does the bias come from?</summary>

From the other half of that comparison. The worst three are compared against the remaining **four**, whose pre trend is 1.55 percent a year, and the gap between 4.83 and 1.55 is 3.29 points. A placebo comparison has two sides, and taking the extreme three from a group of seven necessarily leaves the opposite extreme as the comparison. Both halves have to be checked.
</details>

<details>
<summary><b>2.</b> A funder insists on giving a program to the neediest agencies. What should be asked for?</summary>

That the comparison group be drawn from the same ranking. Give the program to a random half of the agencies above the threshold and put the rest on a waiting list. Both halves were selected on the outcome, so both regress equally and the comparison is clean. If that is refused, ask for the eligibility rule in writing before the program starts, so the pre trend check can be run on the correct groups.
</details>

<details>
<summary><b>3.</b> Would matching the two groups on the pre program rate have fixed the problem?</summary>

Not here, and it is worth knowing why. Matching requires agencies at similar levels in both groups, and the selection was nearly deterministic: four of the top five were taken. There is essentially no overlap in the variable that decided selection, so there is nothing to match to. Advanced Module 10 measures this directly and finds the two groups perfectly separated.
</details>

## Key Takeaway

Ask how recipients were chosen, put the outcome's own history in the balance table, and run the placebo at both ends of the ranking.

---

| | |
|---|---|
| **Previous** | [Module 9: Regression to the Mean](Module_09_Regression_To_The_Mean.md) |
| **Next** | [Module 11: Confounders, Mediators and Colliders](Module_11_Confounders_Mediators_And_Colliders.md) |
| **Builds on** | [Module 7](Module_07_Testing_Parallel_Trends.md), [Module 9](Module_09_Regression_To_The_Mean.md), Beginner [Topic 13](../Beginner/Topic_13_Picking_The_Winners.md) |
| **Used again in** | [Module 12](Module_12_Placebo_Tests.md), [Module 15](Module_15_Sensitivity.md), [Module 16](Module_16_Writing_Up_A_Causal_Claim.md) |

*This module is part of a series developed for the Washington Data Exchange for Public Safety (WADEPS) through the Center for Interdisciplinary Statistical Education and Research (CISER) at Washington State University. Version 1.0, September 2026. Questions, errors, or suggestions: yin.zhang@wsu.edu*

*All examples use synthetic data created for teaching. They do not represent any real jurisdiction, agency, officer, or incident. See [Data/DATA_DICTIONARY.md](../../Data/DATA_DICTIONARY.md).*
