# Module 13: Spillover and Contamination

> **Developed by Yin Zhang, PhD**, Assistant Professor, Department of Mathematics and Statistics, Washington State University

## The Question

What if some of the comparison agencies got a piece of the program anyway, and how much would it cost?

## The Idea in Plain Language

Every other failure in this series makes a program look better than it was. This one makes it look worse, which is why a program that genuinely works can be cancelled after a careful evaluation.

It is also the only bias that cannot be found in the data. You have to ask the agencies.

## The Method

> relabel one comparison agency as treated and refit, for each agency in turn
>
> then vary the **dose**, since spillover is rarely all or nothing

## Worked Example

![Two panels. The left plots the percentage points of effect lost against the contaminated agency's size on a log scale: Ashfell at 902 officers costs four points while Orrindale at eight costs nothing. The right plots the estimate against the share of the effect leaking to Ashfell, falling from minus 12.6 at zero percent to minus 3.5 at full leakage](Figures/fig_13_spillover.png)

| Agency also trained | Sworn officers | Estimate becomes | Points lost |
|---|---|---|---|
| **Ashfell** | 902 | **−8.6%** | **4.0** |
| Lakeshore County | 141 | −9.9% | 2.7 |
| Havenbrook | 95 | −11.6% | 1.0 |
| Prairie County | 38 | −13.0% | 0.4 |
| Kelsmoor | 31 | −11.8% | 0.8 |
| Dunmoor | 18 | −12.2% | 0.4 |
| Orrindale | 8 | −12.6% | 0.0 |

**The damage tracks the agency's size, not its similarity.** The pooled comparison rate weights agencies by the incidents they contribute, and Ashfell contributes about three quarters of them.

### Spillover is not all or nothing

| Share of the effect leaking to Ashfell | Estimate |
|---|---|
| 0% | −12.6% |
| 25% | −10.6% |
| 50% | −8.0% |
| 100% | −3.5% |

A quarter of the effect leaking costs two points. **There is no threshold below which spillover is safe to ignore**, and no diagnostic in the data that separates a contaminated comparison group from a program that simply worked less well.

### What can be done

| Response | What it buys | What it costs |
|---|---|---|
| **Ask the comparison agencies** | the only real answer | an email |
| Drop geographic neighbours | removes the likeliest route | a smaller, noisier comparison group |
| Report with and without them | bounds the exposure | nothing |
| Model distance from a treated agency | a dose response, if distance is the route | assumes the route |

| | Estimate | 95 percent interval |
|---|---|---|
| All seven comparison agencies | −12.6% | [−17.9, −6.9] |
| Dropping the two nearest | −11.4% | [−21.0, −0.6] |

Report both. Dropping the two largest comparison agencies nearly doubles the interval, which is the cost and the right cost to pay when a reviewer asks.

## Do It Yourself

> 📓 **Notebook:** [Module_13_Spillover_And_Contamination.ipynb](Notebooks/Module_13_Spillover_And_Contamination.ipynb)
> [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/OWNER/REPO/blob/main/Causal_Inference/Intermediate/Notebooks/Module_13_Spillover_And_Contamination.ipynb)
> About 25 minutes.

- Relabels each comparison agency as treated in turn
- Varies the dose of spillover at the largest comparison agency
- Compares the estimate with and without the nearest neighbours
- The exercise reverses the direction: partial implementation at a treated agency

## Pitfalls

| What goes wrong | What it looks like | What to do |
|---|---|---|
| Assuming the comparison group is clean | an estimate biased toward zero | ask, in writing |
| Choosing the nearest agencies as comparisons | the most similar and the most contaminated | prefer distance, or report both ways |
| Treating a conservative bias as acceptable | a working program cancelled | a biased estimate is wrong in either direction |
| Confusing partial implementation with a small effect | the wrong policy conclusion | collect implementation records |

## Check Your Understanding

<details>
<summary><b>1.</b> Contamination biases toward zero. Is that not the safe direction?</summary>

It is the safe direction for avoiding a false positive and the dangerous one for a program that works. An evaluation that reports 8 percent when the truth is 12 may fall below whatever threshold a funder set, and the program ends. "Conservative" is only a virtue when the cost of the two errors is asymmetric, and for a program that reduces use of force it is not obvious that it is.
</details>

<details>
<summary><b>2.</b> Why does Prairie County show a larger estimate, 13.0 percent, when it is relabelled as treated?</summary>

Because it is a small agency with a noisy series, and moving it between groups changes the estimate by more than its contamination would imply in either direction. The 0.4 point movement is not evidence about spillover at all; it is what happens when a small unit moves between two pools. That is worth noticing, because it means the leave one out exercise measures sensitivity to composition as well as to contamination.
</details>

<details>
<summary><b>3.</b> An estimate of 8 percent could be a real 8 percent effect everywhere, or a real 12 percent effect at two thirds of agencies. Does the distinction matter?</summary>

Enormously for policy and not at all for the arithmetic. A difference in differences estimates the effect of **being assigned** the program, which equals the effect of receiving it only when everyone assigned received it. If implementation was patchy, the right conclusion is that the program works where it is implemented and implementation is the problem, which points at a completely different intervention.
</details>

## Key Takeaway

Email the comparison agencies and ask what they ran. Then report the estimate with and without the likeliest contaminated ones.

---

| | |
|---|---|
| **Previous** | [Module 12: Placebo Tests](Module_12_Placebo_Tests.md) |
| **Next** | [Module 14: How Big an Effect Could You Have Detected?](Module_14_How_Big_An_Effect.md) |
| **Builds on** | [Module 4](Module_04_Building_A_Comparison_Group.md), Beginner [Topic 10](../Beginner/Topic_10_When_The_Comparison_Group_Moves_Too.md) |
| **Used again in** | [Module 15](Module_15_Sensitivity.md), [Module 16](Module_16_Writing_Up_A_Causal_Claim.md) |

$FOOT
