# Module 3: Identification Before Estimation

> **Developed by Yin Zhang, PhD**, Assistant Professor, Department of Mathematics and Statistics, Washington State University

**The question this module answers:** *What exactly has to be assumed, how is each assumption checked, and what does a failure of identification look like in the output?*

---

## The Question

**Identification** asks whether the quantity you want is a function of the distribution you can observe, given your assumptions. It is settled before any data is touched, and no amount of estimation repairs a failure of it.

| Step | Question | Answered by |
|---|---|---|
| **Estimand** | which quantity | [Module 1](Module_01_Potential_Outcomes_And_Estimands.md) |
| **Identification** | is it a function of observables under stated assumptions | [Module 2](Module_02_DAGs_And_The_Backdoor_Criterion.md) and this one |
| **Estimation** | how to compute it and how uncertain it is | everything else |

Most applied work starts at step three. The cost is that a failure at step two produces a precise number with a small standard error and no meaning.

## Estimand and Assumptions

For the difference in differences used throughout:

> **A1 Parallel trends.** E[Y(0)_after − Y(0)_before | D=1] = E[Y(0)_after − Y(0)_before | D=0]
>
> **A2 No anticipation.** Y(0) is the outcome for treated units in the pre period
>
> **A3 SUTVA.** One agency's treatment does not change another's outcome
>
> **A4 Stable composition.** The units and the measure mean the same thing throughout

| Assumption | Diagnostic | Result |
|---|---|---|
| **A1** | pre period trend difference | −0.70% a year **[−3.31, +1.97]** |
| **A2** | fake intervention at 2022-07 | −4.65% [−12.36, +3.74] |
| **A3** | effect on arrests | +0.08% [−0.94, +1.10] |
| **A4** | the data dictionary | one agency reclassified calls in 2023-01, not the outcome used here |

Every diagnostic passes in the sense of not rejecting, and **not one establishes its assumption.**

A1's interval reaches 3.31 percent a year, enough to matter. A2 tests anticipation at one arbitrary date. A3 checks one of many possible spillover routes. A4 rests on reading documentation.

**That is the normal state of an observational design**, and the write up should say so in those terms rather than reporting that the assumptions were verified.

## Estimation

```python
# identification is settled here, in prose, before this line is written
smf.glm("n_uof ~ C(agency_id)+C(year_month)+settled+phase", d, ...)
```

## Worked Example

What a failure of identification looks like in the output: nothing.

| Specification | Estimate | Interval width | AIC |
|---|---|---|---|
| **Agency and month effects** | **−12.6%** | 11.0 | **4,744** |
| The same, no time term at all | −29.5% | **6.8** | 5,251 |
| The same, no agency term at all | +17.8% | 12.4 | 5,055 |
| **The truth** | **−12.0%** | | |

The specification with no time term has a **narrower** interval than the identified one, 6.8 points against 11.0, and it is wrong by 17 percentage points. **Precision is not evidence of identification.**

AIC does happen to prefer the identified specification here. **That is luck rather than a property.** AIC compares fit, and identification is not about fit: a model can fit better while estimating something other than the effect, which is exactly what agency specific trends did in Intermediate [Module 8](../Intermediate/Module_08_When_Parallel_Trends_Fails.md).

### Identification for the designs this series does not use

| Design | What it needs | Available here |
|---|---|---|
| Randomisation | assignment independent of potential outcomes | no, selection was on the outcome |
| Matching | overlap in the confounders | no, [Module 10](Module_10_Propensity_Scores.md) |
| Instrumental variables | relevance, exclusion, monotonicity | no instrument exists, [Module 11](Module_11_Instrumental_Variables.md) |
| Regression discontinuity | a sharp threshold with continuity around it | close, not sharp, [Module 12](Module_12_Regression_Discontinuity.md) |
| **Difference in differences** | **parallel trends** | **yes, with the caveat on A1** |

Four of five are unavailable, each for a reason statable in one line. Part III works through them.

## Recovering the Planted Answer

The generator satisfies A2, A3 and A4 by construction, and satisfies A1 for four of the five treated agencies. The design recovers 12.6 percent against a planted 12.0 when the fifth is removed.

**What the dataset also demonstrates is that the diagnostics cannot tell you that.** A1's interval is wide enough to admit a violation that would erase the estimate, and it is only because the truth is known that the assumption can be confirmed.

## Diagnostics

| Check | Acceptable |
|---|---|
| Each assumption written as a statement about potential outcomes | before estimation |
| A named diagnostic for each | with its interval, not its p value |
| Explicit note that passing is not proof | in the limitations |
| Interval width compared across specifications | narrower is not better |
| The designs ruled out, with reasons | one line each |

## Do It Yourself

> 📓 **Notebook:** [Module_03_Identification_Before_Estimation.ipynb](Notebooks/Module_03_Identification_Before_Estimation.ipynb)
> [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/YinZhangCISER/Public-Safety-Statistics-Tutorials/blob/main/Causal_Inference/Advanced/Notebooks/Module_03_Identification_Before_Estimation.ipynb)
> About 30 minutes.

The exercise tests the no anticipation assumption at four dates rather than one.

## When Not To Use This

| Situation | What to do |
|---|---|
| No assumption makes the estimand a function of observables | report that, not a number |
| The assumptions hold only for a subgroup | change the estimand to that subgroup |
| An assumption has no diagnostic at all | say so; A4 here is an example |
| The diagnostics reject | [Module 14](Module_14_Sensitivity_And_Partial_Identification.md), partial identification |

## Reporting the Result

> Identification rests on parallel trends, no anticipation, no interference between agencies, and a stable outcome definition. The pre program trend difference between the groups is 0.70 percent a year, 95 percent interval from 3.31 below to 1.97 above; a placebo intervention dated eighteen months early returns 4.65 percent with an interval covering zero; the program did not move arrests, the exposure measure; and the one documented definition change in the dataset affects a call category not used as an outcome here. None of these establishes the corresponding assumption, and the interval on the pre trend difference is wide enough to admit a violation large enough to change the conclusion, which is quantified in the sensitivity analysis.

## Further Reading

- Manski, C. F. (1995). *Identification Problems in the Social Sciences*. Harvard University Press.
- Lewbel, A. (2019). The identification zoo: meanings of identification in econometrics. *Journal of Economic Literature*, 57.
- Roth, J., Sant'Anna, P., Bilinski, A. and Poe, J. (2023). What's trending in difference in differences. *Journal of Econometrics*, 235.

---

| | |
|---|---|
| **Previous** | [Module 2: Directed Acyclic Graphs and the Backdoor Criterion](Module_02_DAGs_And_The_Backdoor_Criterion.md) |
| **Next** | [Module 4: Selection Mechanisms and What They Do to an Estimate](Module_04_Selection_Mechanisms.md) |
| **Builds on** | [Module 1](Module_01_Potential_Outcomes_And_Estimands.md), [Module 2](Module_02_DAGs_And_The_Backdoor_Criterion.md) |
| **Used again in** | every module in this series |

*This module is part of a series developed for the Washington Data Exchange for Public Safety (WADEPS) through the Center for Interdisciplinary Statistical Education and Research (CISER) at Washington State University. Version 1.0, September 2026. Questions, errors, or suggestions: yin.zhang@wsu.edu*

*All examples use synthetic data created for teaching. They do not represent any real jurisdiction, agency, officer, or incident. See [Data/DATA_DICTIONARY.md](../../Data/DATA_DICTIONARY.md).*
