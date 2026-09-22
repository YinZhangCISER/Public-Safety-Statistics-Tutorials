# Module 15: Sensitivity, How Wrong Would the Assumption Have to Be?

> **Developed by Yin Zhang, PhD**, Assistant Professor, Department of Mathematics and Statistics, Washington State University

## The Question

The estimate rests on an assumption nobody can verify. How badly would it have to fail before the conclusion changes, and is a failure that large plausible?

## The Idea in Plain Language

Stop arguing about whether the assumption holds. Instead, break it on purpose by a known amount and watch the estimate move. Then find something that says whether a violation of that size is credible.

The second step is the one people skip. A sensitivity analysis produces a number; it is only informative next to a benchmark.

## The Method

> add a hidden trend of size δ favouring the treated agencies, refit, and find the δ that drives the estimate to zero
>
> then compare that δ against what the pre period says the trend difference actually is

## Worked Example

### How large a hidden trend it would take

| Hidden trend, percent a year | Estimate | 95 percent interval | Still excludes zero |
|---|---|---|---|
| 0.0 | −12.6% | [−17.9, −6.9] | yes |
| −1.0 | −9.1% | [−14.7, −3.2] | yes |
| **−2.0** | −5.5% | [−11.2, +0.6] | **no** |
| −3.0 | −1.6% | [−7.6, +4.7] | no |
| −4.0 | +2.4% | [−3.9, +9.0] | no |

It takes about **3.4 percent a year** to drive the estimate to zero, and about **2.0 percent a year** for the interval to start covering zero.

### Is that a plausible violation

![A line chart of the estimate against the size of a hidden trend difference, rising from minus 12.6 percent at zero to plus 11 percent at minus 6 percent a year, crossing zero at minus 3.4. A green vertical line marks the observed pre period difference of 0.70 percent a year, and a shaded green band shows the interval the pre period cannot rule out, reaching to minus 3.31](Figures/fig_15_sensitivity.png)

| | |
|---|---|
| Observed pre program trend difference | **−0.70% a year** |
| Its 95 percent interval | **[−3.31, +1.97]** |
| Needed to zero out the estimate | about **−3.4% a year** |
| Needed for the interval to cover zero | about **−2.0% a year** |

**This is not a reassuring result, and reporting it as one would be wrong.**

The point estimate of 0.70 is far smaller than the 3.4 required. But the interval reaches **3.31 percent a year**, almost exactly the violation that would wipe the estimate out, and well past the 2.0 that would make the interval cover zero.

The honest summary: **the pre period is consistent with parallel trends, and also consistent with a violation nearly large enough to explain the entire result.** Fifty four months of pre period on eleven agencies cannot distinguish those two states of the world.

### The second assumption, with a different verdict

| Share of the effect reaching every comparison agency | Estimate |
|---|---|
| 0% | −12.6% |
| 40% | −8.8% |
| 80% | −4.2% |
| 100% | −1.8% |

It takes essentially **complete** contamination to reduce the estimate to nothing. That is a claim about seven agencies all quietly running the same program, which is checkable by asking them and implausible on its face.

**Two sensitivity analyses, two very different verdicts. Report both.**

## How to Write It

> *The estimate is robust to contamination of the comparison group: every comparison agency would have to have received the full program effect for the estimate to fall to zero. It is less robust to an unmeasured difference in trends. A trend difference of 3.4 percent a year favouring the treated agencies would eliminate the estimate, and 2.0 percent a year would widen the interval to include zero. The observed pre program trend difference is 0.70 percent a year, but its 95 percent interval extends to 3.31 percent a year, so a violation of the size required cannot be excluded on the available pre period.*

Three sentences, and a reader now knows exactly where the result is fragile.

## Do It Yourself

> 📓 **Notebook:** [Module_15_Sensitivity.ipynb](Notebooks/Module_15_Sensitivity.ipynb)
> [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/YinZhangCISER/Public-Safety-Statistics-Tutorials/blob/main/Causal_Inference/Intermediate/Notebooks/Module_15_Sensitivity.ipynb)
> About 25 minutes.

- Breaks parallel trends by a known amount and tracks the estimate
- Benchmarks the required violation against the observed pre period interval
- Repeats the exercise for contamination
- The exercise varies how long the hidden trend has been running

## Pitfalls

| What goes wrong | What it looks like | What to do |
|---|---|---|
| Reporting the breakdown point with no benchmark | "a 3.4 percent trend would be needed" and nothing else | compare it against the pre period interval |
| Treating a large breakdown point as proof | robustness claimed that the data does not support | check whether the interval reaches it |
| One sensitivity analysis | the fragile assumption not the one tested | test each assumption separately |
| Sensitivity run only when the result is convenient | a selective robustness claim | run it either way and report it |

## Check Your Understanding

<details>
<summary><b>1.</b> The required violation is 3.4 and the observed point estimate is 0.70. Why is that not enough to declare the result robust?</summary>

Because the point estimate is not the relevant quantity. The question is what the data rules out, and the interval on the pre trend difference reaches 3.31 percent a year. A world in which the treated agencies were on a 3 percent steeper path is entirely consistent with the 54 months of pre period available. Declaring robustness on the point estimate alone ignores the uncertainty in exactly the quantity the sensitivity analysis is about.
</details>

<details>
<summary><b>2.</b> The contamination sensitivity is reassuring and the trend sensitivity is not. Should the report lead with the reassuring one?</summary>

No, and the temptation is the reason this module exists. Report both, in the order of how much they threaten the conclusion. A reader who is given the comfortable result first and the uncomfortable one in an appendix has been managed rather than informed, and a reviewer will find the appendix.
</details>

<details>
<summary><b>3.</b> What would actually reduce the uncertainty in the trend difference?</summary>

A longer pre period, more than a longer follow up. The trend difference is estimated from the months before the program, so those are the months that sharpen it, and a longer pre period also shortens the window in which an undetected trend could have started unseen. That is the opposite of the usual instinct, which is to wait longer after the program.
</details>

## Key Takeaway

Find the violation that would break the conclusion, then find something that says whether a violation that large is credible. Report both numbers together.

---

| | |
|---|---|
| **Previous** | [Module 14: How Big an Effect Could You Have Detected?](Module_14_How_Big_An_Effect.md) |
| **Next** | [Module 16: Writing Up a Causal Claim](Module_16_Writing_Up_A_Causal_Claim.md) |
| **Builds on** | [Module 7](Module_07_Testing_Parallel_Trends.md), [Module 13](Module_13_Spillover_And_Contamination.md) |
| **Used again in** | [Module 16](Module_16_Writing_Up_A_Causal_Claim.md) |

$FOOT
