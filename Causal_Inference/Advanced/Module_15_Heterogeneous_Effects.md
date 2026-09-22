# Module 15: Heterogeneous Effects, and the Temptation to Find Them

> **Developed by Yin Zhang, PhD**, Assistant Professor, Department of Mathematics and Statistics, Washington State University

**The question this module answers:** *Four estimates span twelve points. Did the program work better somewhere?*

---

## The Question

**Here it did not**, and the module is about how to establish that rather than assert it. The same machinery then shows how easily a subgroup analysis manufactures a finding.

## Estimand and Assumptions

> a model with one coefficient per treated agency, tested against a model with one common coefficient, by likelihood ratio

| Assumption | Note |
|---|---|
| The comparison group is valid for each agency separately | inherited from the pooled design |
| The test has power against the heterogeneity that matters | **must be measured**, not assumed |
| Subgroups were specified before looking | otherwise the search is the finding |

## Estimation

```python
zh = smf.glm("n_uof ~ C(agency_id)+C(year_month)+phase+" + per_agency_terms, ...)
z0 = smf.glm("n_uof ~ C(agency_id)+C(year_month)+settled+phase", ...)
lr = 2 * (zh.llf - z0.llf)
```

## Worked Example

![A forest plot of four agency level estimates, from minus 8.9 to minus 21.1 percent with wide intervals, and a pooled estimate at minus 12.6 with a narrow one, against a dashed line at the true 12 percent. A note gives the test of a common effect as chi squared 4.56 on 3 degrees of freedom, p equals 0.207](Figures/fig_a15_heterogeneous.png)

| Agency | Estimate | 95 percent interval |
|---|---|---|
| Stonewick | −8.9% | [−15.4, −2.0] |
| Tarnbridge | −18.1% | [−25.8, −9.6] |
| Millgate | −15.1% | [−28.8, +1.2] |
| Pinecrest | −21.1% | [−38.7, +1.5] |
| **Pooled** | **−12.6%** | [−17.9, −6.9] |
| **The truth, at all four** | **−12.0%** | |

| Test of one common effect against four separate ones | |
|---|---|
| Chi squared | **4.56** on 3 df |
| p | **0.207** |

**No evidence of heterogeneity**, and the twelve point spread is what four noisy estimates of one number look like.

"The effect ranged from 9 to 21 percent across agencies" is true, misleading, and the kind of sentence that ends up in a summary.

### What the test could have detected

| Planted spread across the four agencies | Detected |
|---|---|
| 0 points | 1% |
| 10 points | **10%** |
| 20 points | **56%** |
| 30 points | 91% |

A ten point spread is found one time in ten. A twenty point spread is a coin flip.

**So "no evidence of heterogeneity" here means the effect does not differ across agencies by something like thirty points**, which is much weaker than "the effect is the same everywhere" and is what the data supports.

### Subgroups, and how easily one appears

| Split | In the subgroup | Not in it | Difference |
|---|---|---|---|
| Large agencies | −12.0% | −17.2% | 5.2 |
| Western region | −12.4% | −15.4% | 3.0 |
| **Municipal police** | **−12.2%** | **−20.6%** | **8.4** |
| Above median violent crime | −12.0% | −17.2% | 5.2 |
| Above median population | −12.0% | −17.2% | 5.2 |

**The true effect is −12.0 percent in every subgroup.** Differences of three to eight points appear anyway, and the largest is the kind of gap that gets a sentence in a summary.

With four treated units, any binary split produces groups small enough to differ by several points, and a search across five splits finds one that looks substantial.

| Protection | Cost |
|---|---|
| Pre register the subgroups | none, and it is the only real protection |
| Report every split examined | none |
| Correct for multiplicity | the surviving claims are weaker, correctly |
| Require a mechanism in advance | some genuine discoveries are missed |
| Report the homogeneity test first | none |

## Recovering the Planted Answer

The generator gives all five agencies the identical 12 percent effect. The homogeneity test correctly fails to reject, the pooled estimate recovers the truth, and **every apparent subgroup difference in the table above is manufactured.** The module's value is the second fact rather than the first.

## Diagnostics

| Check | Acceptable |
|---|---|
| The homogeneity test | reported before any per unit estimate |
| Its power against a spread that would matter | simulated |
| Subgroups | fixed in advance, all reported |
| The base rate for the search space | simulated under a constant effect |
| Per unit estimates | presented with intervals, never ranked in prose |

## Do It Yourself

> 📓 **Notebook:** [Module_15_Heterogeneous_Effects.ipynb](Notebooks/Module_15_Heterogeneous_Effects.ipynb)
> [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/OWNER/REPO/blob/main/Causal_Inference/Advanced/Notebooks/Module_15_Heterogeneous_Effects.ipynb)
> About 30 minutes.

The exercise measures how often a search across only three splits finds an eight point gap when the effect is constant.

## When Not To Use This

| Situation | Reach for |
|---|---|
| Many treated units | the test has power; heterogeneity is worth investigating |
| A mechanism predicted in advance | a pre registered interaction, reported whether or not it appears |
| Staggered adoption | [Module 7](Module_07_Staggered_Adoption.md); heterogeneity there also breaks the estimator |
| Four units and a hypothesis generated afterwards | nothing; say the design cannot address it |

## Reporting the Result

> Agency specific effects range from 8.9 to 21.1 percent. A likelihood ratio test of a common effect against four separate ones gives chi squared 4.56 on 3 degrees of freedom, p = 0.207, so the data provide no evidence that the effect differed across agencies. A simulation places the test's power at 10 percent against a spread of 10 percentage points and 56 percent against 20, so the absence of evidence bounds heterogeneity only at roughly 30 points. Five subgroup splits were examined, all specified before estimation; differences of 3 to 8 percentage points appear across them and none is reported as a finding, since a simulation under a constant effect produces gaps of this size routinely at this sample size.

## Further Reading

- Gelman, A., Hill, J. and Yajima, M. (2012). Why we usually do not have to worry about multiple comparisons. *Journal of Research on Educational Effectiveness*, 5.
- Athey, S. and Imbens, G. (2016). Recursive partitioning for heterogeneous causal effects. *PNAS*, 113.
- Wager, S. and Athey, S. (2018). Estimation and inference of heterogeneous treatment effects using random forests. *Journal of the American Statistical Association*, 113.

---

| | |
|---|---|
| **Previous** | [Module 14: Sensitivity Analysis and Partial Identification](Module_14_Sensitivity_And_Partial_Identification.md) |
| **Next** | [Module 16: The Causal Claim, What You Can Defend](Module_16_The_Causal_Claim.md) |
| **Builds on** | [Module 1](Module_01_Potential_Outcomes_And_Estimands.md), [Module 5](Module_05_Two_Way_Fixed_Effects.md), [Module 9](Module_09_Honest_Inference_With_Few_Clusters.md) |
| **Used again in** | [Module 16](Module_16_The_Causal_Claim.md) |

$FOOT
