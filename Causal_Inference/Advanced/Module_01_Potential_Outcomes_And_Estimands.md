# Module 1: Potential Outcomes, Estimands, and What You Are Actually Estimating

> **Developed by Yin Zhang, PhD**, Assistant Professor, Department of Mathematics and Statistics, Washington State University

**The question this module answers:** *Several quantities could be called "the effect of the program". Which one does this design reach, and which one is being reported?*

---

## The Question

Reporting one estimand while describing another is the most common failure in applied causal work, and it happens silently: nothing in the output flags it.

## Estimand and Assumptions

For unit *i*, **Y_i(1)** and **Y_i(0)** are the outcomes under treatment and control. One is observed.

| Estimand | Definition | Answers |
|---|---|---|
| **ATE** | E[Y(1) − Y(0)] over all units | would it help if everyone took it |
| **ATT** | E[Y(1) − Y(0) given D = 1] | did it help those who took it |
| **ATU** | E[Y(1) − Y(0) given D = 0] | would it have helped the others |
| **LATE** | the effect for units an instrument moves | did it help the compliers |

A difference in differences identifies the **ATT** and nothing else.

**And "the ATT" is still not one number**, because averaging over agencies and averaging over incidents are different operations.

## Estimation

```python
smf.glm("n_uof ~ C(agency_id)+C(year_month)+settled+phase", d,
        family=sm.families.Poisson(), offset=d["lo"]).fit()
```

## Worked Example

![A forest plot of four agency level estimates with wide intervals, ranging from minus 9.35 to minus 20.65 percent, then two summary rows: the ATT weighted equally across agencies at minus 15.67 and the ATT weighted by incidents at minus 12.61, against a dashed line at the true 12 percent](Figures/fig_a01_estimands.png)

| | Estimate | 95 percent interval |
|---|---|---|
| Stonewick | −9.35% | [−15.8, −2.4] |
| Tarnbridge | −17.22% | [−25.1, −8.5] |
| Millgate | −15.45% | [−29.2, +0.9] |
| Pinecrest | −20.65% | [−38.5, +2.3] |
| **ATT, agencies weighted equally** | **−15.67%** | |
| **ATT, weighted by incidents** | **−12.61%** | [−17.9, −6.9] |
| **The truth** | **−12.00%** | |

**Three percentage points apart, and both are the ATT.**

The pooled Poisson weights each agency by the incidents it contributes, so Stonewick's 57 incidents a month count for more than Pinecrest's 3.6. Averaging the four agency level estimates weights each agency equally.

| Weighting | The question it answers |
|---|---|
| By incidents | what happened to a typical **incident**, which is what a statewide total responds to |
| By agency | what happened at a typical **agency**, which is what a chief deciding whether to adopt cares about |

The planted effect is identical everywhere, so the truth is the same for both and the three point gap is sampling noise amplified by giving small noisy agencies equal weight.

### Why the ATE is not available

Four of the top five agencies by baseline rate were selected. **There is no untreated agency at the top of the distribution and no treated agency at the bottom**, so the data contain no information about what the program does to a low rate agency.

Claiming an ATE requires assuming the effect is constant across the distribution. That may be reasonable and it is an assumption, not a finding.

### Under heterogeneity the weights stop being a detail

Simulating a world where the effect is 20 percent at the two large agencies and 4 percent at the two small ones:

| | Estimate | Its target |
|---|---|---|
| ATT weighted by incidents | −17.3% | −18.2% |
| ATT weighted by agency | −14.1% | −12.0% |

Incident shares: Stonewick 61 percent, Tarnbridge 28, Millgate 8, Pinecrest 4.

Neither is biased. **With heterogeneous effects the weighting scheme is part of the estimand and belongs in its definition.**

## Recovering the Planted Answer

The dataset builds a **12 percent** reduction, identical at all five agencies. Both weightings of the ATT are therefore estimating the same 12 percent, and the gap between 12.61 and 15.67 is a measure of how much noise equal weighting admits when agency sizes differ by a factor of fifteen.

## Diagnostics

| Check | Acceptable |
|---|---|
| The estimand is named before the model is fitted | in the protocol |
| The weighting is stated | "weighted by incidents" or "by agency" |
| The averaging window is stated | "over the 30 months after full implementation" |
| Overlap in the selection variable | if none, the ATE is not available and the text says so |
| Effect heterogeneity | if present, the two weightings must be reported separately |

## Do It Yourself

> 📓 **Notebook:** [Module_01_Potential_Outcomes_And_Estimands.ipynb](Notebooks/Module_01_Potential_Outcomes_And_Estimands.ipynb)
> [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/OWNER/REPO/blob/main/Causal_Inference/Advanced/Notebooks/Module_01_Potential_Outcomes_And_Estimands.ipynb)
> About 30 minutes.

The exercise varies the averaging window and finds that it too is part of the estimand.

## When Not To Use This

| Situation | Reach for |
|---|---|
| The question is about units outside the treated group | nothing here reaches it; say so |
| Effects plausibly vary with agency size | report both weightings, and [Module 15](Module_15_Heterogeneous_Effects.md) |
| Treatment arrives at different times | [Module 7](Module_07_Staggered_Adoption.md), where the weights get stranger |
| An instrument exists | the LATE, [Module 11](Module_11_Instrumental_Variables.md) |

## Reporting the Result

> The estimand is the average treatment effect on the treated, weighted by incidents, over the 30 months following full implementation, for the four agencies retained in the analysis. Weighting agencies equally instead gives 15.7 percent; the two are not distinguishable given the sample and they answer different questions. The average treatment effect is not identified by this design: agencies were selected on the pre program outcome and there is no overlap between the groups in that variable, so the data carry no information about the effect at agencies with low baseline rates.

## Further Reading

- Imbens, G. W. and Rubin, D. B. (2015). *Causal Inference for Statistics, Social, and Biomedical Sciences*. Cambridge University Press. Chapters 1 to 3.
- Angrist, J. D. and Pischke, J. S. (2009). *Mostly Harmless Econometrics*. Princeton University Press. Chapter 2.
- Słoczyński, T. (2022). Interpreting OLS estimands when treatment effects are heterogeneous. *Review of Economics and Statistics*, 104.

---

| | |
|---|---|
| **Next** | [Module 2: Directed Acyclic Graphs and the Backdoor Criterion](Module_02_DAGs_And_The_Backdoor_Criterion.md) |
| **Builds on** | Intermediate [Module 2](../Intermediate/Module_02_Potential_Outcomes_Without_The_Algebra.md) |
| **Used again in** | every module in this series |

*This module is part of a series developed for the Washington Data Exchange for Public Safety (WADEPS) through the Center for Interdisciplinary Statistical Education and Research (CISER) at Washington State University. Version 1.0, September 2026. Questions, errors, or suggestions: yin.zhang@wsu.edu*

*All examples use synthetic data created for teaching. They do not represent any real jurisdiction, agency, officer, or incident. See [Data/DATA_DICTIONARY.md](../../Data/DATA_DICTIONARY.md).*
