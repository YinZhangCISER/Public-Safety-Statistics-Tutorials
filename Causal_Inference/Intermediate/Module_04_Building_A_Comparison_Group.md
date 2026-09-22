# Module 4: Building a Comparison Group

> **Developed by Yin Zhang, PhD**, Assistant Professor, Department of Mathematics and Statistics, Washington State University

## The Question

Which agencies belong in the comparison group, how much does the answer depend on that choice, and how do you show a reader it was not chosen to produce the answer?

## The Idea in Plain Language

Write the admission rule in one sentence, before looking at any outcome. Then run every other defensible rule and report what each one gives. If they agree, the objection that the group was chosen to suit the answer has been closed off. If they disagree, that is the finding.

## The Method

A rule has three jobs.

| Job | Why |
|---|---|
| Exclude anyone who got the program | including under another name |
| Be statable in one sentence, before results | so it cannot be adjusted afterwards |
| Admit enough **incidents** to be steady | one agency's accidents otherwise become the estimate |

Resembling the treated agencies is **not** on the list. Similarity helps only when it makes the counterfactual trend more alike, which is a narrower claim than it sounds.

## Worked Example

Four rules that could each be written down in advance.

![Two panels. The left is a grid of dots showing which of the seven untrained agencies each of four rules admits. The right is a bar chart of the difference in differences estimate each rule produces, all between 12.0 and 12.8 percent, against a dashed line at the true 12 percent](Figures/fig_04_building_a_comparison_group.png)

| Rule | Agencies | Comparison group changed | Estimate |
|---|---|---|---|
| Everyone not trained | 7 | −19.5% | −12.5% |
| Municipal police only | 4 | −19.9% | −12.0% |
| At least 30 sworn officers | 5 | −19.5% | −12.4% |
| Complete call data | 5 | −19.2% | −12.8% |
| **The truth** | | | **−12.0%** |

A spread of **0.8 points**. That is the result you hope for and must never assume, and it is exactly what a sceptical reader wants to know and cannot learn from a single number.

### When the rules disagree

| A rule nobody should use | Agencies | Estimate |
|---|---|---|
| The three smallest agencies | 3 | −20.5% |
| The three largest agencies | 3 | −12.5% |
| One agency, chosen for being nearby | 1 | **+2.3%** |

One of these produces the wrong sign. But notice that the three **largest** agencies, also only three of them, do as well as any rule above.

**What matters is how many incidents the comparison group contains, not how many agencies.** Three small departments together record fewer incidents in four years than one large one records in a few months.

### The rule worth writing down

> *All agencies that did not adopt the program, excluding any that adopted a comparable program under another name, and excluding any whose pre program trend differs significantly from the treated group. Exclusions listed individually with reasons.*

## Do It Yourself

> 📓 **Notebook:** [Module_04_Building_A_Comparison_Group.ipynb](Notebooks/Module_04_Building_A_Comparison_Group.ipynb)
> [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/YinZhangCISER/Public-Safety-Statistics-Tutorials/blob/main/Causal_Inference/Intermediate/Notebooks/Module_04_Building_A_Comparison_Group.ipynb)
> About 25 minutes.

- Prints the seven candidate agencies with the characteristics a rule might use
- Applies four defensible rules and three bad ones, and reports all seven estimates
- The exercise is a leave one out check on the pooled comparison group

## Pitfalls

| What goes wrong | What it looks like | What to do |
|---|---|---|
| Choosing the group after seeing results | an estimate that cannot be defended | write the rule first, in the protocol |
| Reporting only one rule | a reader who cannot tell whether it matters | report the table, it costs four lines |
| A comparison group of one or two | an estimate that can flip sign | count incidents, not agencies |
| One member dominating the pool | an estimate that is really one agency | leave one out, see below |
| Excluding an agency without saying so | an unreproducible number | list every exclusion with its reason |

## Check Your Understanding

<details>
<summary><b>1.</b> Dropping Ashfell moves the estimate from 12.5 to 14.7 percent, far more than dropping any other agency. Why?</summary>

Because Ashfell accounts for **76.8 percent of all the use of force incidents in the comparison group**. Pooling by incident gives each agency weight proportional to its size, so the pooled comparison rate is very nearly Ashfell's own rate wearing six other names. Nothing in the four rule table would have revealed that, which is why the leave one out check is worth running whenever one member is much larger than the rest.
</details>

<details>
<summary><b>2.</b> Would weighting each agency equally rather than by size be better?</summary>

It is not better or worse; it answers a different question. Weighting by incidents gives the average effect across **incidents**, which is usually what a policy question means. Weighting agencies equally gives the average effect across **agencies**, which lets Orrindale's eight officers count as much as Ashfell's nine hundred. Both are legitimate and they can differ substantially. The failure is not choosing one, it is not saying which was chosen.
</details>

<details>
<summary><b>3.</b> All four defensible rules give essentially the same answer. Does that mean the comparison group is a good one?</summary>

It means the answer does not hinge on which agencies were admitted, which removes one objection. It says nothing about whether the group is a valid counterfactual: all four rules draw from the same seven agencies, so if something affected all seven, every rule inherits it. Robustness across rules and validity of the design are different questions, and the second one is [Module 7](Module_07_Testing_Parallel_Trends.md).
</details>

## Key Takeaway

Write the admission rule before looking at outcomes, report what every other defensible rule gives, and run a leave one out check when one member dominates.

---

| | |
|---|---|
| **Previous** | [Module 3: The Counterfactual You Have to Construct](Module_03_The_Counterfactual_You_Have_To_Construct.md) |
| **Next** | [Module 5: Difference in Differences, by Hand](Module_05_Difference_In_Differences_By_Hand.md) |
| **Builds on** | [Module 3](Module_03_The_Counterfactual_You_Have_To_Construct.md), Beginner [Topic 7](../Beginner/Topic_07_What_Makes_A_Good_Comparison_Group.md) |
| **Used again in** | [Module 5](Module_05_Difference_In_Differences_By_Hand.md), [Module 7](Module_07_Testing_Parallel_Trends.md), [Module 13](Module_13_Spillover_And_Contamination.md) |

*This module is part of a series developed for the Washington Data Exchange for Public Safety (WADEPS) through the Center for Interdisciplinary Statistical Education and Research (CISER) at Washington State University. Version 1.0, September 2026. Questions, errors, or suggestions: yin.zhang@wsu.edu*

*All examples use synthetic data created for teaching. They do not represent any real jurisdiction, agency, officer, or incident. See [Data/DATA_DICTIONARY.md](../../Data/DATA_DICTIONARY.md).*
