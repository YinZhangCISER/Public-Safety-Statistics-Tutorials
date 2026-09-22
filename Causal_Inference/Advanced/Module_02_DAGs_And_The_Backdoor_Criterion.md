# Module 2: Directed Acyclic Graphs and the Backdoor Criterion

> **Developed by Yin Zhang, PhD**, Assistant Professor, Department of Mathematics and Statistics, Washington State University

**The question this module answers:** *Which variables should be conditioned on, and which must not be, and can that be settled before any model is fitted?*

---

## The Question

A DAG is a picture of what causes what. It is not a statistical model and it is not estimated from the data: it is drawn from what is known about how the world produced these records.

Its value is that once drawn, **the adjustment set can be read off it mechanically**, before estimation, and so can the set that must be left alone.

## Estimand and Assumptions

Four nodes suffice for this study.

| Node | Meaning |
|---|---|
| **D** | the agency took the training |
| **Y** | use of force per arrest |
| **B** | the agency's baseline use of force rate |
| **T** | the statewide year, standing for everything moving over time |

Five edges, each from documented knowledge rather than from the data:

> **D → Y** the effect to be identified
> **B → D** the selection rule used the baseline rate
> **B → Y** a high baseline agency has a high rate later
> **T → Y** everything was falling statewide
> **T → D** the program was adopted at a particular time

A **backdoor path** is any path from D to Y starting with an arrow into D. There are two: **D ← B → Y** and **D ← T → Y**.

The **backdoor criterion**: a set identifies the effect if it blocks every backdoor path and contains no descendant of D.

## Estimation

```python
smf.glm("n_uof ~ base + C(year_month) + settled + phase", d, ...)   # B and T
smf.glm("n_uof ~ C(agency_id) + C(year_month) + settled + phase", d, ...)
```

## Worked Example

![Two node diagrams side by side. In the left, the baseline rate B and the statewide year T each have arrows into both the training D and the outcome Y, drawn in orange and labelled as two open backdoor paths. In the right the same graph with B and T shaded green, labelled as conditioning on agency and month, which closes both](Figures/fig_a02_dag.png)

![A horizontal chart of five adjustment sets with intervals. Conditioning on nothing gives minus 8.8 percent, on the baseline rate only minus 28.2, on month effects only plus 17.8, on both minus 11.0, and on agency plus month effects minus 12.6, against a dashed line at the true 12 percent. Beside each row is what the graph says is still open](Figures/fig_a03_identification.png)

| Conditioned on | Estimate | 95 percent interval | What the graph says is left open |
|---|---|---|---|
| Nothing | −8.8% | [−12.7, −4.8] | both paths open |
| B only | −28.2% | [−31.5, −24.7] | T still open |
| **T only** | **+17.8%** | [+11.8, +24.1] | B still open |
| **B and T** | **−11.0%** | [−16.2, −5.4] | both closed |
| **Agency and month effects** | **−12.6%** | [−17.9, −6.9] | both closed |
| **The truth** | **−12.0%** | | |

**This table could have been written before any of these models were run.**

The two sets the graph calls sufficient land on the truth. The three it calls insufficient do not, and **conditioning only on time gets the sign wrong**: with the baseline path open, the treated agencies' higher levels appear as a positive coefficient.

Agency fixed effects work because agency identity determines the baseline rate, so conditioning on the agency conditions on B and on everything else fixed about the agency. That is strictly more than the graph requires and it is cheap.

### The half of the criterion that is easier to violate

**No descendant of D.** Anything caused by the training is off limits.

| Did the program move | Estimate | 95 percent interval | Verdict |
|---|---|---|---|
| Arrests | +0.08% | [−0.94, +1.10] | not a descendant |
| Calls for service | +0.42% | [+0.12, +0.73] | a descendant, strictly |

Arrests are untouched, so using them as the denominator does not condition on a descendant.

Calls for service move 0.42 percent with an interval excluding zero. By the strict reading that forbids them as a control; by any substantive reading a 0.42 percent movement is not a causal pathway. **The graph is a tool for thinking, not an oracle.**

## Recovering the Planted Answer

The generator implements exactly the graph above: a common time factor applied to every agency, a selection rule reading the baseline rate, and a treatment factor applied to five agencies. The adjustment sets that block both paths recover the planted 12 percent; the sets that block one recover something else, in a direction the graph predicts.

## Diagnostics

| Check | Acceptable |
|---|---|
| The graph is drawn before the model | and the edges are justified in prose |
| Every backdoor path enumerated | and each one either blocked or declared open |
| No control is a descendant of the treatment | test each post treatment variable |
| Unmeasured confounders named | as nodes, even though they cannot be conditioned on |
| A testable implication identified | the pre trend test is usually the one |

## Do It Yourself

> 📓 **Notebook:** [Module_02_DAGs_And_The_Backdoor_Criterion.ipynb](Notebooks/Module_02_DAGs_And_The_Backdoor_Criterion.ipynb)
> [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/YinZhangCISER/Public-Safety-Statistics-Tutorials/blob/main/Causal_Inference/Advanced/Notebooks/Module_02_DAGs_And_The_Backdoor_Criterion.ipynb)
> About 30 minutes.

The exercise adds an unmeasured node for reform minded leadership and works out what it does and what can still be tested.

## When Not To Use This

| It can | It cannot |
|---|---|
| tell you what to condition on, given the structure | tell you the structure |
| show a design is unidentified | show it is identified in reality |
| make an assumption visible and arguable | make it true |
| rule a control variable out | rule one in without the rest of the graph |

**Drawing a graph adds no information.** It makes whatever you already believed explicit enough to disagree with, which is most of its value.

## Reporting the Result

> Identification proceeds from a graph with four nodes: the treatment, the outcome, the agency's pre program use of force rate, and calendar time. Two backdoor paths exist, one through the baseline rate, which determined selection, and one through calendar time, during which rates fell statewide. Agency and calendar month fixed effects block both. No post treatment variable is used as a control; arrests, which appear as the exposure offset, were tested and are unaffected by the program. An unmeasured confounder in the position of the baseline rate, such as reform minded leadership, would not be blocked by this adjustment set; its testable implication is a pre program trend difference, which is estimated at 0.70 percent a year with an interval reaching 3.31.

## Further Reading

- Pearl, J. (2009). *Causality*, 2nd edition. Cambridge University Press. Chapter 3.
- Cinelli, C., Forney, A. and Pearl, J. (2024). A crash course in good and bad controls. *Sociological Methods and Research*, 53.
- Hernán, M. A. and Robins, J. M. *Causal Inference: What If*. Free at hsph.harvard.edu. Chapters 6 and 7.

---

| | |
|---|---|
| **Previous** | [Module 1: Potential Outcomes, Estimands, and What You Are Actually Estimating](Module_01_Potential_Outcomes_And_Estimands.md) |
| **Next** | [Module 3: Identification Before Estimation](Module_03_Identification_Before_Estimation.md) |
| **Builds on** | [Module 1](Module_01_Potential_Outcomes_And_Estimands.md), Intermediate [Module 11](../Intermediate/Module_11_Confounders_Mediators_And_Colliders.md) |
| **Used again in** | [Module 3](Module_03_Identification_Before_Estimation.md), [Module 4](Module_04_Selection_Mechanisms.md), and Part III |

*This module is part of a series developed for the Washington Data Exchange for Public Safety (WADEPS) through the Center for Interdisciplinary Statistical Education and Research (CISER) at Washington State University. Version 1.0, September 2026. Questions, errors, or suggestions: yin.zhang@wsu.edu*

*All examples use synthetic data created for teaching. They do not represent any real jurisdiction, agency, officer, or incident. See [Data/DATA_DICTIONARY.md](../../Data/DATA_DICTIONARY.md).*
