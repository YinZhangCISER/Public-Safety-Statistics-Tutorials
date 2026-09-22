# Module 4: Selection Mechanisms and What They Do to an Estimate

> **Developed by Yin Zhang, PhD**, Assistant Professor, Department of Mathematics and Statistics, Washington State University

**The question this module answers:** *Selection bias is treated as one thing with one direction. Is it?*

---

## The Question

It is not. **What was selected on determines both the sign and the size of the bias, and what the estimator conditions on determines how much survives.**

This module measures three selection rules in a world where the program does not exist, so whatever the estimator returns is the whole of the bias.

## Estimand and Assumptions

The planted effect is known exactly: a factor of 0.88 on the rate, phased in at 0, 25, 58, 83 and 100 percent over five months from July 2023. Dividing it back out of the observed counts gives the counterfactual mean for every agency month, and a world in which nothing was done.

> mu0 = observed count ÷ 0.88^w, where w is the phase in weight

Counts at treated agencies after full implementation rise by 13.6 percent, which is the planted effect removed.

## Estimation

```python
s["y"] = rng.poisson(s["mu0"])          # resample a no program world
smf.glm("y ~ C(agency_id)+C(year_month)+settled+phase", s, ...)
```

## Worked Example

Three rules, each choosing five of twelve agencies, plus random assignment.

| Rule | Agencies chosen |
|---|---|
| Highest level before | Tarnbridge, Pinecrest, Millgate, Stonewick, Havenbrook |
| Steepest downward trend before | Summit, Pinecrest, Stonewick, Prairie, Ashfell |
| Worst last six months before | Tarnbridge, Havenbrook, Millgate, Stonewick, Kelsmoor |

![A violin plot of four selection rules in a world with no program. Highest level before centres at plus 3.01 percent, steepest downward trend at minus 1.94, worst last six months at plus 4.83, and random assignment at minus 0.11 with a much wider spread, against a dashed line at zero](Figures/fig_a04_selection.png)

| Selection rule | Mean bias | Simulation sd |
|---|---|---|
| Highest level before | **+3.01%** | 3.06 |
| Steepest downward trend before | **−1.94%** | 3.25 |
| Worst last six months before | **+4.83%** | 2.80 |
| At random | **−0.11%** | 8.74 |

**The true effect in this world is zero.** Four rules, four different answers.

**Selecting on the level costs +3.01 percent**, which *understates* a reduction. Agency fixed effects absorb the level itself, so what is left is the part of a high pre period average that was luck, and it has already partly reverted by the time the post period starts.

**Selecting on the recent level costs +4.83 percent**, the largest here, because six months of a small agency's rate is mostly noise and reverts hard.

**Selecting on the trend costs −1.94 percent**, and it is the dangerous one: it biases **toward** finding an effect. That is what Summit County is, and why Intermediate [Module 8](../Intermediate/Module_08_When_Parallel_Trends_Fails.md) had to remove it.

**Random assignment costs −0.11 percent**, the only unbiased rule. Note its spread of 8.74 against roughly 3 for the others: **random assignment buys freedom from bias, not precision.**

### The general statement

| Selected on | Direction of bias | Why |
|---|---|---|
| the **level** of the outcome | toward zero, if levels are conditioned on | mean reversion already partly spent |
| a **recent** level | toward zero, more strongly | a short window is mostly noise |
| the **trend** in the outcome | **toward the hypothesis** | the trend continues into the post period |
| something unrelated to the outcome | none | no backdoor path |

**The direction people assume, that selection flatters a program, holds only for selection on trends.**

That is not a licence to relax about level based selection. It means the sign has to be reasoned about in each case, and that the estimator matters as much as the rule.

## Recovering the Planted Answer

The dataset's own rule is selection on the level, and this module measures its cost at **+3.01 percentage points** with the estimator actually used. That is the same direction as the gap between the reported 12.6 and the planted 12.0, and roughly three times its size, which is a reminder that these biases sit inside sampling noise rather than beside it.

## Diagnostics

| Check | Acceptable |
|---|---|
| The selection rule is documented, in writing | obtained from the program, not inferred |
| The variable selected on is named | and its relation to the outcome stated |
| The bias direction is reasoned, not assumed | using the table above |
| The estimator's conditioning set is stated alongside | the pair determines the bias |
| A no program simulation is run where feasible | it costs minutes and settles the argument |

## Do It Yourself

> 📓 **Notebook:** [Module_04_Selection_Mechanisms.ipynb](Notebooks/Module_04_Selection_Mechanisms.ipynb)
> [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/YinZhangCISER/Public-Safety-Statistics-Tutorials/blob/main/Causal_Inference/Advanced/Notebooks/Module_04_Selection_Mechanisms.ipynb)
> About 35 minutes.

The exercise repeats the three rules without agency fixed effects, and the level based biases change most.

## When Not To Use This

| Situation | Reach for |
|---|---|
| The selection rule is unknown | report that; it is the most important missing fact |
| Selection was on an unobserved variable | [Module 14](Module_14_Sensitivity_And_Partial_Identification.md) |
| Selection was on a threshold of a running variable | [Module 12](Module_12_Regression_Discontinuity.md) |
| The true counterfactual cannot be constructed | a placebo on untreated units, Intermediate [Module 12](../Intermediate/Module_12_Placebo_Tests.md) |

## Reporting the Result

> Agencies were selected on their pre program use of force rate, the study's outcome. A simulation that removes the planted effect and reapplies the selection rule to the resulting no program world estimates the bias of this rule, under the specification used, at +3.0 percentage points, that is, toward understating a reduction. Selection on the pre program trend rather than the level would bias in the opposite direction, toward overstating, by 1.9 points; the one treated agency whose pre program trend differed materially was excluded for that reason.

## Further Reading

- Heckman, J. J. (1979). Sample selection bias as a specification error. *Econometrica*, 47.
- Ashenfelter, O. (1978). Estimating the effect of training programs on earnings. *Review of Economics and Statistics*, 60. The original dip.
- Chabé-Ferret, S. (2015). Analysis of the bias of matching and difference in difference under alternative earnings and selection processes. *Journal of Econometrics*, 185.

---

| | |
|---|---|
| **Previous** | [Module 3: Identification Before Estimation](Module_03_Identification_Before_Estimation.md) |
| **Next** | [Module 5: Two Way Fixed Effects Done Properly](Module_05_Two_Way_Fixed_Effects.md) |
| **Builds on** | [Module 2](Module_02_DAGs_And_The_Backdoor_Criterion.md), Intermediate [Module 10](../Intermediate/Module_10_Selection_On_The_Outcome.md) |
| **Used again in** | [Module 10](Module_10_Propensity_Scores.md), [Module 12](Module_12_Regression_Discontinuity.md), [Module 14](Module_14_Sensitivity_And_Partial_Identification.md) |

*This module is part of a series developed for the Washington Data Exchange for Public Safety (WADEPS) through the Center for Interdisciplinary Statistical Education and Research (CISER) at Washington State University. Version 1.0, September 2026. Questions, errors, or suggestions: yin.zhang@wsu.edu*

*All examples use synthetic data created for teaching. They do not represent any real jurisdiction, agency, officer, or incident. See [Data/DATA_DICTIONARY.md](../../Data/DATA_DICTIONARY.md).*
