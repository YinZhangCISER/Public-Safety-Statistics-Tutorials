# Module 13: Placebo, Permutation and Falsification Tests

> **Developed by Yin Zhang, PhD**, Assistant Professor, Department of Mathematics and Statistics, Washington State University

**The question this module answers:** *A placebo test compares the estimate against a null. Which null?*

---

## The Question

Intermediate [Module 12](../Intermediate/Module_12_Placebo_Tests.md) ran three placebos and they agreed. This module asks the question that one could not, and finds that **a common way of building the null is wrong for this design.**

## Estimand and Assumptions

| Test | What is faked | What it catches |
|---|---|---|
| **Placebo date** | the intervention date | an estimator that finds effects in any window |
| **Placebo group** | which units were treated | an inference too confident for the sample size |
| **Falsification** | the outcome | an effect that is really something else changing |

The in space placebo, standard in the synthetic control literature, pretends **each untreated unit in turn** was the treated one. The permutation null reassigns the **whole treatment pattern**. They are not the same thing when more than one unit was treated.

## Estimation

```python
one  = [fit(d, [a])[0] for a in COMPARISON]              # one at a time
four = [fit(d, rng.choice(ids, 4, replace=False))[0] for _ in range(400)]
```

## Worked Example

![A chart with two rows. The top row plots seven orange points, one per untreated agency pretended treated alone, spread from minus 16 to plus 24 percent, giving p equals 0.25. The bottom row shows a green violin of 400 draws where four agencies are pretended treated, much narrower, giving p equals 0.030. A black line marks the real estimate at minus 12.6](Figures/fig_a13_placebo.png)

| Agency pretended treated alone | Estimate |
|---|---|
| Havenbrook | −1.9% |
| Kelsmoor | +11.8% |
| Orrindale | −7.3% |
| Lakeshore County | +9.1% |
| Prairie County | −15.5% |
| **Dunmoor** | **+23.8%** |
| Ashfell | −2.7% |

| Null | Spread | p for the real estimate |
|---|---|---|
| One agency, 7 draws | 12.2 | **0.25** |
| Four agencies, 400 draws | 7.8 | **0.030** |

**The same estimate, p = 0.25 against one null and p = 0.030 against the other.**

The one agency null is far more dispersed, because a single agency's estimate is much noisier than an average of four. Comparing a four agency estimate against a one agency null uses a reference distribution that is too wide and understates the evidence.

**The null must be built by pretending to treat the same number of units that were actually treated.** In space placebos are correct for synthetic control with one treated unit, and are the wrong null for a multi unit difference in differences.

### Falsification, and a test with too much power

| Outcome | Estimate | 95 percent interval |
|---|---|---|
| Use of force per arrest | −12.61% | [−17.93, −6.93] |
| Arrests | +0.08% | [−0.94, +1.10] |
| **Calls for service** | **+0.42%** | **[+0.12, +0.73]** |

Calls move by an amount that is detectable and is not a pathway. **A falsification test with enormous power fails on noise**, and the response is to report the size rather than the verdict.

### How many placebos is too many

Eight placebo dates were run and **none rejects**. At five percent each, **0.4 false rejections are expected across eight tests by chance alone**; across twenty, one is expected, which someone would then have to explain away.

| Practice | Why |
|---|---|
| Fix the placebo list before looking | otherwise the choice is the result |
| Report every placebo run | including the ones that failed |
| State the expected number of false rejections | it is the denominator for any that do |

## Recovering the Planted Answer

The generator gives no effect anywhere before November 2023 and none to the seven comparison agencies, so every placebo here has a true value of zero. All eight placebo dates and both falsification outcomes behave accordingly. **The four agency permutation null is the one that reproduces the design's actual assignment**, and it is the one that places the real estimate at p = 0.030.

## Diagnostics

| Check | Acceptable |
|---|---|
| The placebo null treats as many units as the design did | always |
| Number of placebos run | fixed in advance and reported whole |
| Expected false rejections | stated |
| A failing falsification test | read by size, not by label |
| The assignment set for a permutation null | named |

## Do It Yourself

> 📓 **Notebook:** [Module_13_Placebo_Permutation_And_Falsification.ipynb](Notebooks/Module_13_Placebo_Permutation_And_Falsification.ipynb)
> [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/OWNER/REPO/blob/main/Causal_Inference/Advanced/Notebooks/Module_13_Placebo_Permutation_And_Falsification.ipynb)
> About 30 minutes.

The exercise restricts the permutation to assignments resembling the real treated group, and the p value moves.

## When Not To Use This

| Situation | Reach for |
|---|---|
| One treated unit | the in space placebo is correct there |
| No untreated units at all | no placebo is available; say so |
| A single placebo that fails | investigate, do not discard the design |
| Many placebos, one failing | compare against the expected count |

## Reporting the Result

> Placebo tests were run at eight pre program dates fixed in advance, none of which rejects at the five percent level; 0.4 false rejections are expected across eight tests. Two falsification outcomes were examined: arrests are unaffected, and calls for service move by 0.42 percent with an interval excluding zero, a difference too small to constitute a pathway to a 12.6 percent change in the use of force rate. The permutation null was constructed by reassigning treatment to four agencies, matching the number actually treated, over 400 draws, and places the estimate at p = 0.030. A null built by pretending each untreated agency in turn was treated alone gives p = 0.25 and is not the appropriate reference for a four agency design.

## Further Reading

- Abadie, A., Diamond, A. and Hainmueller, J. (2010). Synthetic control methods for comparative case studies. *Journal of the American Statistical Association*, 105. The in space placebo.
- Athey, S. and Imbens, G. W. (2017). The econometrics of randomized experiments. *Handbook of Economic Field Experiments*, 1.
- Eggers, A. C., Tuñón, G. and Dafoe, A. (2024). Placebo tests for causal inference. *American Journal of Political Science*, 68.

---

| | |
|---|---|
| **Previous** | [Module 12: Regression Discontinuity](Module_12_Regression_Discontinuity.md) |
| **Next** | [Module 14: Sensitivity Analysis and Partial Identification](Module_14_Sensitivity_And_Partial_Identification.md) |
| **Builds on** | [Module 9](Module_09_Honest_Inference_With_Few_Clusters.md), Intermediate [Module 12](../Intermediate/Module_12_Placebo_Tests.md) |
| **Used again in** | [Module 16](Module_16_The_Causal_Claim.md) |

$FOOT
