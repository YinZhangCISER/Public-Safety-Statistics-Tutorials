# Module 14: Sensitivity Analysis and Partial Identification

> **Developed by Yin Zhang, PhD**, Assistant Professor, Department of Mathematics and Statistics, Washington State University

**The question this module answers:** *When an assumption cannot be defended, what is left?*

---

## The Question

Two things. **Sensitivity analysis** asks how badly the assumption would have to fail. **Partial identification** drops it and reports what the data alone can bound.

Three of them run here give three different verdicts, including one that is uncomfortable and one that fails outright.

## Estimand and Assumptions

| Analysis | Drops | Keeps |
|---|---|---|
| Hidden trend sensitivity | nothing; it parameterises the failure | the model |
| Partial identification | parallel trends entirely | a minimal support assumption |
| Unobserved selection | nothing; it extrapolates from the observed controls | that unobservables resemble observables |

## Estimation

```python
s["adj"] = np.log(s["n_arrests"]) + np.log(1 + delta / 100) * s["tr"] * s["yrc"]
fit(s, KEEP, offset=s["adj"])
```

## Worked Example

![Two panels. The left plots the estimate against the size of a hidden trend, crossing zero at 3.4 percent a year, with a shaded band showing the range the pre period cannot rule out reaching almost to that point. The right shows two bounds: one from no assumption at all running from minus 0 to plus 45 and excluding the truth, and one anchored on the treated group's own before value running from minus 30 to plus 45 and containing it](Figures/fig_a14_sensitivity.png)

### Sensitivity to an unmeasured trend

| Hidden trend | Estimate | Interval | Excludes zero |
|---|---|---|---|
| 0.0% a year | −12.6% | [−17.9, −6.9] | yes |
| −1.0% | −9.1% | [−14.7, −3.2] | yes |
| −2.0% | −5.5% | [−11.2, +0.6] | **no** |
| −3.0% | −1.6% | [−7.6, +4.7] | no |

It takes about **3.4 percent a year** to erase the estimate, and the pre period's interval reaches **3.31**.

**The breakdown point sits just inside what the data cannot rule out.** That is a real caveat and should be reported as one rather than as robustness.

### Partial identification, and a bound that fails

Y(1) for the treated group after the program is **2.528**. The untreated agencies after the program span **[1.738, 2.538]**.

| Bound | The effect lies in | Contains the truth |
|---|---|---|
| **A.** Y(0) somewhere in the untreated span | **[−0.4%, +45.5%]** | **no** |
| **B.** Y(0) no higher than the treated group's own before value | [−29.5%, +45.5%] | yes |

**Bound A excludes the truth of −12 percent**, and it is not a valid bound here. The reason is the overlap failure from [Module 10](Module_10_Propensity_Scores.md): the treated agencies' Y(0) sits above every untreated agency's observed rate, so the untreated range is not a range Y(0) lives in.

**A worst case bound built on the wrong support is not conservative. It is wrong.** Reporting it as an assumption free bound would be the most misleading claim in this series.

Bound B is valid, uses one weak assumption, contains the truth, and is **75 percentage points wide.** That is the honest trade partial identification offers here.

### How much unobserved selection would be needed

| | Estimate |
|---|---|
| With no controls | −8.80% |
| With full controls | −12.61% |
| The observed controls moved it | **−3.80 points** |
| To reach zero, unobservables must move it | **+12.61 points, or 3.3 times that pull** |

Conventionally a ratio above 1 is taken as reassuring. **Two caveats:** Oster's statistic is defined for least squares with R squared and this is a Poisson model, so the ratio is an analogy rather than the published statistic; and the logic assumes unobservables resemble observables in how they relate to treatment.

## Recovering the Planted Answer

The truth is a 12 percent reduction. Sensitivity analysis does not recover it, which is not its job: it establishes that the reported estimate survives a hidden trend of up to 2 percent a year and does not survive 3.4, and that the pre period cannot distinguish between those worlds.

## Diagnostics

| Check | Acceptable |
|---|---|
| The breakdown point, with a benchmark | never reported alone |
| The support used for any worst case bound | verified to contain the treated units' counterfactual |
| Whether the bound contains the point estimate | if not, the support is wrong |
| Every sensitivity analysis run | reported, including the reassuring ones |
| Method assumptions when borrowed across model families | stated as analogies |

## Do It Yourself

> 📓 **Notebook:** [Module_14_Sensitivity_And_Partial_Identification.ipynb](Notebooks/Module_14_Sensitivity_And_Partial_Identification.ipynb)
> [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/OWNER/REPO/blob/main/Causal_Inference/Advanced/Notebooks/Module_14_Sensitivity_And_Partial_Identification.ipynb)
> About 35 minutes.

The exercise implements the simplest Rambachan and Roth relative magnitude bound: the conclusion survives a post period violation up to twice the largest one visible before the program, and not three times.

## Three Verdicts

| Analysis | Verdict |
|---|---|
| Unmeasured trend | **uncomfortable**: the breakdown point is inside the pre period's interval |
| Partial identification | **uninformative**: 75 points wide, and the naive version is invalid |
| Unobserved selection | **reassuring**: 3.3 times the observed pull would be needed |

**Report all three.** Reporting only the third is a selective robustness claim; reporting only the first understates what the design achieved.

## Reporting the Result

> The estimate survives an unmeasured trend difference of up to 2 percent a year and is eliminated by one of 3.4 percent; the pre program interval on that difference reaches 3.31 percent a year, so a violation of the size required cannot be excluded. Under a relative magnitude bound the conclusion of a reduction survives a post program violation of twice the largest one visible before the program. Dropping the parallel trends assumption entirely and bounding the counterfactual only by the treated group's own pre program level gives an interval 75 percentage points wide; a bound built instead from the range of untreated outcomes is invalid here, because the treated agencies' counterfactual lies above that range. Unobserved selection would have to be 3.3 times as influential as all observed controls combined to erase the estimate.

## Further Reading

- Manski, C. F. (2003). *Partial Identification of Probability Distributions*. Springer.
- Rambachan, A. and Roth, J. (2023). A more credible approach to parallel trends. *Review of Economic Studies*, 90.
- Oster, E. (2019). Unobservable selection and coefficient stability. *Journal of Business and Economic Statistics*, 37.
- Cinelli, C. and Hazlett, C. (2020). Making sense of sensitivity: extending omitted variable bias. *Journal of the Royal Statistical Society Series B*, 82.

---

| | |
|---|---|
| **Previous** | [Module 13: Placebo, Permutation and Falsification Tests](Module_13_Placebo_Permutation_And_Falsification.md) |
| **Next** | [Module 15: Heterogeneous Effects, and the Temptation to Find Them](Module_15_Heterogeneous_Effects.md) |
| **Builds on** | [Module 6](Module_06_Event_Studies_And_Pre_Trend_Testing.md), [Module 10](Module_10_Propensity_Scores.md), Intermediate [Module 15](../Intermediate/Module_15_Sensitivity.md) |
| **Used again in** | [Module 16](Module_16_The_Causal_Claim.md) |

$FOOT
