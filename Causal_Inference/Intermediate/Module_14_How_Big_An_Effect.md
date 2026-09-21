# Module 14: How Big an Effect Could You Have Detected?

> **Developed by Yin Zhang, PhD**, Assistant Professor, Department of Mathematics and Statistics, Washington State University

## The Question

Before an evaluation starts, and before a null result is believed, what is the smallest effect this design had a fair chance of finding?

## The Idea in Plain Language

An estimate with a wide interval and an estimate of zero look the same in a summary table and mean completely different things. The minimum detectable effect is the one number that separates them, and it takes four lines to compute.

## The Method

> at 80 percent power and a 5 percent two sided test, an effect must be about **2.8 standard errors** from zero
>
> the standard error is the one the model already reports

## Worked Example

| | |
|---|---|
| Standard error on the log scale | 0.0321 |
| **Smallest detectable effect** | **8.6%** |
| The study's estimate | −12.6% |
| The truth | −12.0% |

The design could reliably find an effect of 8.6 percent or larger, and the real effect was 12. **That is why this study worked**, and it is a statement that could have been made before any outcome was examined.

![Two panels. The left plots the smallest detectable effect against months of follow up, falling from 14.2 percent at eight months to 8.6 at thirty, crossing a dashed line at the true 12 percent between 12 and 14 months. The right shows it as bars against the number of treated agencies: 9.7, 8.8, 8.6 and 8.6 percent for one through four](Figures/fig_14_detectable_effect.png)

| Follow up | Smallest detectable effect | Can it see 12 percent |
|---|---|---|
| 8 months | 14.2% | **no** |
| 14 months | 11.2% | yes |
| 20 months | 9.9% | yes |
| 26 months | 8.9% | yes |
| 30 months | 8.6% | yes |

| Agencies given the program | Smallest detectable effect |
|---|---|
| 1 | 9.7% |
| 2 | 8.8% |
| 3 | 8.6% |
| **4** | **8.6%** |

Follow up length matters a great deal. **The number of treated agencies barely matters at all**: quadrupling it buys about one percentage point.

That is not what most people expect. Precision depends on the incidents on **both** sides of the comparison, and here the comparison group is dominated by a single large agency whose contribution is fixed. **Adding treated units to a study whose comparison group is thin is close to useless.**

## Reporting a Null Result

| Instead of | Write |
|---|---|
| "no significant effect" | "no effect was detected; the study could detect a reduction of 8.6 percent or more" |
| "the program did not work" | "an effect smaller than 8.6 percent would not have been visible here" |
| "results were inconclusive" | "the interval runs from 17.9 percent below to 6.9 percent above" |

## Do It Yourself

> 📓 **Notebook:** [Module_14_How_Big_An_Effect.ipynb](Notebooks/Module_14_How_Big_An_Effect.ipynb)
> [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/OWNER/REPO/blob/main/Causal_Inference/Intermediate/Notebooks/Module_14_How_Big_An_Effect.ipynb)
> About 20 minutes.

- Computes the detectable effect from the standard error the model already gives
- Varies the follow up length and the number of treated agencies
- The exercise simulates the study under a true effect of 5 percent

## Pitfalls

| What goes wrong | What it looks like | What to do |
|---|---|---|
| Computing it after a null result | it reads as an excuse | compute it before the study |
| Adding treated units to gain power | four times the cost, one point of gain | compute the table first |
| Using the rule of thumb on count data | a slightly optimistic number | simulate, it takes a minute |
| Reporting power instead of the detectable effect | a number nobody can interpret | report the effect size, in the outcome's units |

## Check Your Understanding

<details>
<summary><b>1.</b> Why does adding treated agencies help so little here?</summary>

Because the variance of the estimate depends on the incidents in both groups, and the comparison group's contribution is unchanged. Ashfell alone contributes about three quarters of the comparison group's incidents, so the comparison side is already as precise as it is going to get from these seven agencies. The binding constraint is the comparison group, and the way to improve it is to add comparison agencies, not treated ones.
</details>

<details>
<summary><b>2.</b> A funder wants results in eight months. What should the response be?</summary>

That eight months gives a detectable effect of 14.2 percent, so the study cannot distinguish a working program from a useless one unless the effect is larger than anything the program plausibly delivers. Say so before the work starts, and propose either a longer window, more comparison agencies, or an interim report that states explicitly what has not been ruled out.
</details>

<details>
<summary><b>3.</b> The rule of thumb gives 8.6 percent and the simulation in the notebook gives a slightly different answer. Which should be reported?</summary>

The simulation, when the difference matters. The 2.8 standard errors rule assumes the standard error does not change when the effect does, which is not exactly true for count data. For a rough figure the rule is fine; for a number going into a funding proposal, run 150 simulations and report what actually happened.
</details>

## Key Takeaway

Compute the smallest detectable effect before the study, not after, and put it in the same sentence as any null result.

---

| | |
|---|---|
| **Previous** | [Module 13: Spillover and Contamination](Module_13_Spillover_And_Contamination.md) |
| **Next** | [Module 15: Sensitivity](Module_15_Sensitivity.md) |
| **Builds on** | [Module 6](Module_06_Difference_In_Differences_As_A_Regression.md), Beginner [Topic 18](../Beginner/Topic_18_How_Long_Do_You_Have_To_Wait.md) |
| **Used again in** | [Module 16](Module_16_Writing_Up_A_Causal_Claim.md) |

$FOOT
