# Module 5: Difference in Differences, by Hand

> **Developed by Yin Zhang, PhD**, Assistant Professor, Department of Mathematics and Statistics, Washington State University

## The Question

Four numbers and one division. What exactly is being divided, and does it matter whether you subtract or divide?

## The Idea in Plain Language

Take how much the treated agencies changed, and remove how much the comparison agencies changed. Whatever is left did not happen everywhere.

There are two ways to say "how much a group changed": the difference in rate points, or the ratio. When the two groups start at different levels, these imply different counterfactuals and give different answers.

## The Method

> **subtractive** (rate after − rate before) for the treated, minus the same for the comparison group
>
> **proportional** (rate after ÷ rate before) for the treated, divided by the same for the comparison group

| Assumption | When it is the right one |
|---|---|
| Both groups would have changed by the same **number of rate points** | the groups already sit at similar levels |
| Both groups would have changed by the same **proportion** | the groups start at different levels, or the outcome is a rate or a count |

## Worked Example

Four cells, from raw counts.

| Group | Period | Use of force | Arrests | Rate per 100 |
|---|---|---|---|---|
| Took the training | before | 5,708 | 159,098 | **3.588** |
| | after | 2,342 | 92,625 | **2.528** |
| Did not | before | 7,398 | 276,710 | **2.674** |
| | after | 3,451 | 160,281 | **2.153** |

The comparison group fell by **0.520 rate points**, and by **19.5 percent**. Both describe the same two numbers.

![Two panels. The left shows the trained and comparison lines from before to after, plus two dashed counterfactual lines from the trained starting point: one falling by the same 0.52 rate points to 3.07, one falling by the same 19.5 percent to 2.89. The right compares the two resulting estimates, minus 15.0 and minus 12.5 percent, against a dashed line at the true 12 percent](Figures/fig_05_two_by_two.png)

| | Y(0) | Estimate |
|---|---|---|
| Same change in rate points | 3.067 | **−15.0%** |
| Same proportional change | 2.889 | **−12.5%** |
| **The truth** | | **−12.0%** |

Neither is an arithmetic mistake. The groups started at 3.59 and 2.67, so "the same change" means two different things.

The program in this dataset was built to multiply the rate by 0.88, so the proportional version recovers it. **In real work you do not know which, and the choice has to be argued rather than defaulted into.**

The whole method, on one line:

> (2.528 / 3.588) ÷ (2.153 / 2.674) − 1 = **−12.5 percent**

## Do It Yourself

> 📓 **Notebook:** [Module_05_Difference_In_Differences_By_Hand.ipynb](Notebooks/Module_05_Difference_In_Differences_By_Hand.ipynb)
> [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/OWNER/REPO/blob/main/Causal_Inference/Intermediate/Notebooks/Module_05_Difference_In_Differences_By_Hand.ipynb)
> About 25 minutes.

- Builds the four cells from raw incident and arrest counts
- Computes both scales side by side and names the assumption behind each
- The exercise moves the phase in months between periods

## Pitfalls

| What goes wrong | What it looks like | What to do |
|---|---|---|
| Not saying which scale was used | two analysts get 15.0 and 12.5 and argue | state it in the sentence |
| Using the additive scale on groups at different levels | an estimate biased toward the bigger starting level | use the proportional scale |
| Averaging monthly rates instead of pooling counts | small months weighted the same as large ones | sum the numerators and denominators, then divide |
| Folding the transition into one side | the effect diluted, or overstated | give the transition its own period |
| Reporting the point estimate alone | no way to judge it | [Module 6](Module_06_Difference_In_Differences_As_A_Regression.md) |

## Check Your Understanding

<details>
<summary><b>1.</b> Why does the additive version overstate the effect here?</summary>

Because the treated agencies started higher, at 3.59 against 2.67. Giving them the comparison group's **absolute** fall of 0.52 points is a smaller proportional fall for them than for the comparison group, so the counterfactual Y(0) sits too high at 3.07 and the gap to the observed 2.53 is too large. The direction of the error follows which group starts higher, so it is predictable once the two levels are on the page.
</details>

<details>
<summary><b>2.</b> An analyst averages each agency's monthly rate and then averages those across agencies. Why does that give a different answer?</summary>

Because it weights every agency month equally, so a month at Orrindale with 36 arrests counts as much as a month at Ashfell with 4,000. Pooling the counts first weights by exposure, which is what a rate means. Neither is wrong in principle, but they answer different questions, and the unweighted version is far noisier because the small agencies dominate the average. [Module 4](Module_04_Building_A_Comparison_Group.md) has the same distinction.
</details>

<details>
<summary><b>3.</b> The estimate is 12.5 and the truth is 12.0. How much of that 0.5 is worth interpreting?</summary>

None of it. This module produces a point estimate with no interval, and [Module 6](Module_06_Difference_In_Differences_As_A_Regression.md) shows the interval runs from about 18 percent down to 7 percent. A hand calculation is a way of understanding what the method does, not a way of reporting a result.
</details>

## Key Takeaway

Compute both scales, say which one you used and why, and never report a point estimate without the interval from Module 6.

---

| | |
|---|---|
| **Previous** | [Module 4: Building a Comparison Group](Module_04_Building_A_Comparison_Group.md) |
| **Next** | [Module 6: Difference in Differences, as a Regression](Module_06_Difference_In_Differences_As_A_Regression.md) |
| **Builds on** | [Module 4](Module_04_Building_A_Comparison_Group.md), Beginner [Topic 8](../Beginner/Topic_08_Two_Differences_Are_Better_Than_One.md) |
| **Used again in** | every module in this series |

*This module is part of a series developed for the Washington Data Exchange for Public Safety (WADEPS) through the Center for Interdisciplinary Statistical Education and Research (CISER) at Washington State University. Version 1.0, September 2026. Questions, errors, or suggestions: yin.zhang@wsu.edu*

*All examples use synthetic data created for teaching. They do not represent any real jurisdiction, agency, officer, or incident. See [Data/DATA_DICTIONARY.md](../../Data/DATA_DICTIONARY.md).*
