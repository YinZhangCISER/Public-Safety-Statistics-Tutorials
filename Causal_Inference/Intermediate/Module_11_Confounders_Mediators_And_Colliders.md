# Module 11: Confounders, Mediators and Colliders

> **Developed by Yin Zhang, PhD**, Assistant Professor, Department of Mathematics and Statistics, Washington State University

## The Question

Three variables sit beside a treatment and an outcome, they look identical in a spreadsheet, and the correct handling is different for each. How do you tell which is which?

## The Idea in Plain Language

By which way the arrows point, and that comes from knowing how the world works rather than from looking at the data. A confounder creates a spurious association. A mediator carries the real one. A collider creates a spurious association **only if you condition on it**.

## The Method

![Three node diagrams. In the first, a confounder box has arrows pointing out to both the treatment and the outcome, labelled control for it. In the second, a mediator sits on the path from treatment to outcome, labelled do not control for it. In the third, a collider has arrows pointing into it from both the treatment and the outcome, also labelled do not control for it](Figures/fig_11_confounders_mediators_colliders.png)

| Shape | Arrows | Rule |
|---|---|---|
| **Confounder** | it → treatment, it → outcome | control for it |
| **Mediator** | treatment → it → outcome | leave it alone |
| **Collider** | treatment → it, outcome → it | leave it alone |

## Worked Example

### A confounder: the statewide decline

| | Estimate |
|---|---|
| With month effects, which absorb it | **−12.6%** |
| Without them | −29.5% |
| The truth | −12.0% |

Failing to control for the confounder more than doubles the estimate. This is the case everyone knows.

### A mediator: the denominator

The outcome is use of force **per arrest**. If the training changed how many arrests officers made, then arrests sit on the path from the program to the measured rate.

| Outcome | Estimate | 95 percent interval |
|---|---|---|
| Use of force per arrest | −12.61% | [−17.93, −6.93] |
| Use of force, raw count | −12.57% | [−17.89, −6.90] |
| **Arrests** | **+0.08%** | **[−0.94, +1.10]** |
| Calls for service | +0.42% | [+0.12, +0.73] |

**Arrests did not move**, so the denominator is safe. The raw count and the rate agree to within a twentieth of a point, which is the check.

Estimating the arrests coefficient freely rather than fixing it at 1 gives **1.02** and changes the estimate not at all, which is the second check. If the program had reduced use of force partly by reducing arrests, the free covariate would absorb that route and the estimate would shrink.

**Calls for service moved 0.42 percent with an interval excluding zero.** That is a useful embarrassment: with 964 agency months and tens of thousands of calls, a difference far too small to matter is easily distinguishable from zero. Detectability and size are different things.

### A collider, constructed

Suppose the state reviews an agency if it **either** took the training **or** had a high use of force rate afterwards. The review is caused by both.

| | Correlation between "took the training" and "rate after" |
|---|---|
| Among all eleven agencies | **+0.66** |
| Among reviewed agencies only | **−0.37** |

**The sign flips.** Nothing changed about any agency. The only difference is which rows were looked at, and the rule for looking was caused by both variables.

An untrained agency appears in the reviewed group only if its rate was high; a trained agency appears regardless. Conditioning on review therefore selects the worst untrained agencies against all trained agencies, and manufactures a negative association.

**This is why "the sample was restricted to agencies under review" or "only agencies that responded to the survey were analysed" needs scrutiny.** Any filter that the treatment and the outcome both influence is a collider.

## The Decision Rule

For any variable, in this order:

1. **Could it have been affected by the program?** If yes, it is not a confounder. Leave it out, or handle it as a mediator in an analysis labelled as such.
2. **Could it have affected who got the program, and separately the outcome?** If yes, control for it.

**A variable measured after the treatment started is guilty until proven innocent.** That one rule prevents most mediator and collider mistakes.

## Do It Yourself

> 📓 **Notebook:** [Module_11_Confounders_Mediators_And_Colliders.ipynb](Notebooks/Module_11_Confounders_Mediators_And_Colliders.ipynb)
> [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/YinZhangCISER/Public-Safety-Statistics-Tutorials/blob/main/Causal_Inference/Intermediate/Notebooks/Module_11_Confounders_Mediators_And_Colliders.ipynb)
> About 30 minutes.

- Shows the confounder case by removing the month effects
- Tests whether the program moved the denominator, and fits arrests both ways
- Builds a collider from the real data and watches the correlation flip
- The exercise applies the decision rule to a variable that looks harmless

## Pitfalls

| What goes wrong | What it looks like | What to do |
|---|---|---|
| Controlling for everything available | the effect shrinks for no stated reason | apply the two questions to each variable |
| A post treatment control | a mediated estimate presented as total | anything measured after the start is suspect |
| Conditioning on a selection rule | a sign that flips between samples | ask what caused the filter |
| Treating a rate's denominator as neutral | a mediated measure | test whether the program moved it |
| Reading a tiny significant difference as a failure | a placebo declared failed on 0.42 percent | read the size, not the label |

## Check Your Understanding

<details>
<summary><b>1.</b> The arrests coefficient estimated freely is 1.02. Why does that matter?</summary>

Because using arrests as an offset assumes the coefficient is exactly 1, which is what "a rate" means. Estimating it freely and getting 1.02 says the assumption costs nothing here. If it had come out at 1.5, the denominator would not be behaving proportionally, and dividing by it would be doing something other than forming a rate. Time Series Advanced Module 6 makes the same check from the forecasting side.
</details>

<details>
<summary><b>2.</b> Calls for service moved 0.42 percent with an interval excluding zero. Is the design broken?</summary>

Almost certainly not, and the way to decide is arithmetic rather than a significance label. For a 0.42 percent change in call volume to produce a 12.6 percent change in use of force per arrest, the relationship between the two would have to be implausibly steep. Report the estimate, the interval, and that reasoning. A placebo with enormous power fails on noise, and reporting "the placebo failed" without the size is misleading in the other direction.
</details>

<details>
<summary><b>3.</b> An analyst restricts the sample to agencies that submitted complete data, and the effect changes. Confounder or collider?</summary>

Possibly a collider, and the question to ask is what causes an agency to submit complete data. If agencies under scrutiny report more completely, and both the program and a high use of force rate attract scrutiny, then completeness is caused by both and conditioning on it is exactly the collider in this module. The fact that the estimate changed is a reason to investigate the filter, not to pick whichever version looks better.
</details>

## Key Takeaway

Ask whether the program could have moved the variable before asking whether to control for it. Anything measured after the start is guilty until proven innocent.

---

| | |
|---|---|
| **Previous** | [Module 10: Selection on the Outcome](Module_10_Selection_On_The_Outcome.md) |
| **Next** | [Module 12: Placebo Tests](Module_12_Placebo_Tests.md) |
| **Builds on** | [Module 6](Module_06_Difference_In_Differences_As_A_Regression.md), Beginner [Topic 14](../Beginner/Topic_14_Confounding.md) |
| **Used again in** | [Module 12](Module_12_Placebo_Tests.md), [Module 16](Module_16_Writing_Up_A_Causal_Claim.md) |

*This module is part of a series developed for the Washington Data Exchange for Public Safety (WADEPS) through the Center for Interdisciplinary Statistical Education and Research (CISER) at Washington State University. Version 1.0, September 2026. Questions, errors, or suggestions: yin.zhang@wsu.edu*

*All examples use synthetic data created for teaching. They do not represent any real jurisdiction, agency, officer, or incident. See [Data/DATA_DICTIONARY.md](../../Data/DATA_DICTIONARY.md).*
