# Module 12: Placebo Tests

> **Developed by Yin Zhang, PhD**, Assistant Professor, Department of Mathematics and Statistics, Washington State University

## The Question

Does the analysis produce effects out of nothing? Run it somewhere the answer is known to be zero and find out.

## The Idea in Plain Language

Three kinds of placebo, all cheap, all routinely skipped.

| Test | What it catches |
|---|---|
| **Fake dates** | an estimator that finds an effect in any window |
| **Fake outcomes** | an effect that is really something else changing |
| **Fake treatment groups** | an inference too confident for the sample size |

## The Method

> **fake dates** run the estimator with an intervention date inside the pre period
>
> **fake outcomes** run it on the real dates against something the program should not touch
>
> **fake groups** reassign the treatment label at random several hundred times and see where the real estimate falls

## Worked Example

![Two panels. The left shows five fake intervention dates inside the pre period, with estimates from minus 0.8 to minus 4.6 percent and every interval crossing a dashed line at zero. The right shows three outcomes: use of force at minus 12.61 percent, arrests at plus 0.08 with an interval covering zero, and calls for service at plus 0.42 with an interval from 0.12 to 0.73](Figures/fig_12_placebo_tests.png)

### Fake dates

| Fake start date | Estimate | 95 percent interval | Covers zero |
|---|---|---|---|
| 2020-07 | −0.8% | [−7.7, +6.7] | yes |
| 2021-01 | −2.6% | [−9.1, +4.4] | yes |
| 2021-07 | −2.7% | [−9.2, +4.4] | yes |
| 2022-01 | −3.6% | [−10.5, +3.9] | yes |
| 2022-07 | −4.6% | [−12.4, +3.7] | yes |

Every interval covers zero, which is the pass.

**The point estimates are not zero and they drift**, from 0.8 to 4.6 percent as the fake date moves later. That drift is the residual pre trend gap of 0.71 percent a year accumulating over a longer fake post period. A placebo returning exactly zero would be surprising. What matters is whether the drift is small next to the real estimate, and 4.6 against 12.6 is on the edge of comfortable. **Report it rather than declaring a pass.**

### Fake outcomes

| Outcome | Estimate | 95 percent interval | Covers zero |
|---|---|---|---|
| Use of force per arrest, the real outcome | −12.61% | [−17.93, −6.93] | no |
| Arrests | +0.08% | [−0.94, +1.10] | yes |
| **Calls for service** | **+0.42%** | **[+0.12, +0.73]** | **no** |

Arrests pass cleanly. Calls for service **fail**, by 0.42 percent.

That is the moment to look at size rather than label. A 0.42 percent change in call volume is not a plausible route to a 12.6 percent change in use of force, and with tens of thousands of calls a month the test detects differences far below anything that matters. **A placebo with enormous power fails on noise.**

### Fake treatment groups

Reassign the treatment label at random 400 times.

| | |
|---|---|
| Median of the random estimates | −2.4% |
| Middle 90 percent | −11.9% to +11.7% |
| **The real estimate** | **−12.6%** |
| Random draws at least this negative | **3.0%** |

This is a **randomisation test** and it assumes nothing about the shape of the sampling distribution. It asks how unusual the actual assignment is among all the ways five agencies could have been labelled treated.

It is the right test when there are few units, because the model based interval relies on asymptotics that eleven agencies do not supply. It agrees with the model interval here, which is reassuring and was not guaranteed.

## Do It Yourself

> 📓 **Notebook:** [Module_12_Placebo_Tests.ipynb](Notebooks/Module_12_Placebo_Tests.ipynb)
> [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/OWNER/REPO/blob/main/Causal_Inference/Intermediate/Notebooks/Module_12_Placebo_Tests.ipynb)
> About 25 minutes.

- Runs the estimator at five fake dates inside the pre period
- Runs it against two outcomes the program should not touch
- Builds a randomisation distribution from 400 label reassignments
- The exercise places a second fake start inside the treated period

## Pitfalls

| What goes wrong | What it looks like | What to do |
|---|---|---|
| Running one placebo | a noisy result treated as decisive | run all three kinds |
| Expecting exactly zero | a pass declared on a drifting estimate | report the drift and compare it to the real estimate |
| Reading a significant placebo as fatal | a design abandoned over 0.42 percent | read the size |
| Choosing the fake date after seeing results | a placebo that always passes | fix the dates in advance |
| Reporting only the placebos that passed | a hidden search | report all of them |

## Check Your Understanding

<details>
<summary><b>1.</b> The randomisation test gives 3.0 percent and the model interval excludes zero. Why run both?</summary>

Because they rest on different things. The model interval assumes the standard errors from eleven agencies behave asymptotically, which is optimistic. The randomisation test assumes only that the labelling could have been otherwise. When they agree, as here, the result does not depend on which you believe. When they disagree, the randomisation test is usually the one to trust with this few units.
</details>

<details>
<summary><b>2.</b> The fake date estimates drift from 0.8 to 4.6 percent. Is that a pass or a fail?</summary>

Neither cleanly, which is why the drift should be reported rather than reduced to a verdict. The intervals all cover zero, so nothing is detected, and the trend in the point estimates is exactly what a 0.71 percent a year pre trend gap predicts. The honest reading is that the design carries a small known bias in the same direction as the effect, and the estimate of 12.6 percent should be read as having a point or so of that inside it.
</details>

<details>
<summary><b>3.</b> A colleague proposes using a neighbouring state as a fake outcome. Is that a placebo test?</summary>

It is a different design, sometimes called a placebo group, and it is useful for a different purpose. A fake outcome asks whether the program moved something it should not have. A placebo group asks whether the estimator finds an effect among units the program never reached. Both are worth running; the one in this module's section 4 is the within sample version of the second.
</details>

## Key Takeaway

Run all three placebos, fix the fake dates before looking, and report the drift and the sizes rather than a pass or fail.

---

| | |
|---|---|
| **Previous** | [Module 11: Confounders, Mediators and Colliders](Module_11_Confounders_Mediators_And_Colliders.md) |
| **Next** | [Module 13: Spillover and Contamination](Module_13_Spillover_And_Contamination.md) |
| **Builds on** | [Module 7](Module_07_Testing_Parallel_Trends.md), [Module 10](Module_10_Selection_On_The_Outcome.md), [Module 11](Module_11_Confounders_Mediators_And_Colliders.md) |
| **Used again in** | [Module 15](Module_15_Sensitivity.md), [Module 16](Module_16_Writing_Up_A_Causal_Claim.md) |

*This module is part of a series developed for the Washington Data Exchange for Public Safety (WADEPS) through the Center for Interdisciplinary Statistical Education and Research (CISER) at Washington State University. Version 1.0, September 2026. Questions, errors, or suggestions: yin.zhang@wsu.edu*

*All examples use synthetic data created for teaching. They do not represent any real jurisdiction, agency, officer, or incident. See [Data/DATA_DICTIONARY.md](../../Data/DATA_DICTIONARY.md).*
