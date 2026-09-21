# Module 8: When Parallel Trends Fails

> **Developed by Yin Zhang, PhD**, Assistant Professor, Department of Mathematics and Statistics, Washington State University

## The Question

One treated agency was on a different path before the program started. What are the options, and does the sophisticated one work?

## The Idea in Plain Language

Four responses are available, and they can all be run against a known answer. The result is not the one most people expect.

## The Method

| Response | The idea |
|---|---|
| **Do nothing** | report the estimate and note the violation |
| **Drop the agency** | it does not meet the design's requirement |
| **Agency specific trends** | give every agency its own slope, compare deviations from it |
| **Rebuild the comparison group** | restrict it to agencies whose trends match |

## Worked Example

![A horizontal chart of four responses with intervals. Doing nothing gives minus 17.0 percent. Dropping Summit County gives minus 12.6 and sits on the dashed truth line. Agency specific linear trends gives minus 8.3 and both it and the fourth option have intervals crossing zero, each labelled interval includes zero](Figures/fig_08_when_parallel_trends_fails.png)

| Response | Estimate | 95 percent interval | Width | Covers zero |
|---|---|---|---|---|
| Do nothing, keep Summit County | −17.0% | [−21.8, −11.8] | 9.9 | |
| **Drop Summit County** | **−12.6%** | **[−17.9, −6.9]** | 11.0 | |
| Agency specific linear trends | −8.3% | [−17.8, +2.4] | 20.2 | **yes** |
| Both | −7.7% | [−17.8, +3.6] | 21.4 | **yes** |
| **The truth** | **−12.0%** | | | |

**Dropping the agency recovers the truth. Everything else does worse.**

Doing nothing gives 17.0 percent, the violation showing up as an inflated effect. The two specifications with agency specific trends give 8.3 and 7.7 percent, and their intervals include zero. **A real 12 percent effect has been turned into a null result by the fix.**

### Why the sophisticated fix fails

| | |
|---|---|
| Months before the program | 54 |
| Months after it settled | 30 |
| Correlation between the settled indicator and time | **0.821** |

The program starts in the last third of the series, so a downward step at that point and a steeper downward slope over the whole period explain the same data. An agency specific trend term and the treatment indicator are fighting over the same variation: the trend absorbs part of the effect and the standard error doubles.

This is the same mechanism as Time Series Advanced [Module 11](../../Time_Series/Advanced/Module_11_Interrupted_Time_Series.md), where adding a slope term to a pure level change produced a significant slope that did not exist.

**Agency specific trends are not a general remedy.** They work when the treated period is long relative to the pre period and the violation really is a smooth slope difference. Neither holds here.

### Rebuilding the comparison group

Restricting the comparison group to the four agencies whose own pre trend falls between 2 and 8 percent down gives **−12.3 percent [−17.7, −6.6]**, against −12.6 [−17.9, −6.9] from all seven.

The interval did not widen, and there is a reason: the four that remain still include Ashfell, which carries about three quarters of the comparison group's incidents. **Precision is lost in proportion to the incidents dropped, not the agencies.**

## Do It Yourself

> 📓 **Notebook:** [Module_08_When_Parallel_Trends_Fails.ipynb](Notebooks/Module_08_When_Parallel_Trends_Fails.ipynb)
> [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/OWNER/REPO/blob/main/Causal_Inference/Intermediate/Notebooks/Module_08_When_Parallel_Trends_Fails.ipynb)
> About 25 minutes.

- Runs all four responses against the known answer
- Measures the collinearity that makes agency specific trends fail
- Rebuilds the comparison group by trend and compares
- The exercise moves the failing agency into the comparison group

## Pitfalls

| What goes wrong | What it looks like | What to do |
|---|---|---|
| Reaching for agency specific trends by default | a wider interval and a smaller effect | check the collinearity first |
| Dropping an agency without saying so | an unreproducible number | report both estimates and the reason |
| Moving the failing agency to the comparison group | contamination, and a smaller estimate | exclude it from the study instead |
| Dropping agencies until the test passes | a design chosen by its answer | fix the rule in advance |
| Reporting only the specification that worked | a hidden specification search | disclose what was tried and set aside |

## What to Write

> *One treated agency was excluded because its use of force rate was already declining at 12.0 percent a year before the program began, against 4 to 6 percent at every other agency in the study, with non overlapping intervals. The agency began an internal reform in 2019. Including it raises the estimate from 12.6 to 17.0 percent. A specification with agency specific linear trends was also fitted and is not reported as the primary result: the treated period occupies the final third of the series, so the trend terms are nearly collinear with the treatment indicator and the interval widens to include zero.*

## Check Your Understanding

<details>
<summary><b>1.</b> The agency specific trends specification has the widest interval and the estimate furthest from the truth. Would AIC have warned you?</summary>

Not usefully. Adding eleven trend terms improves the in sample fit, so AIC will often favour the richer model even when the extra terms are eating the effect. The warning comes from the correlation between the treatment indicator and time, which is 0.82 here, and from the interval doubling. **Check identification before fit.**
</details>

<details>
<summary><b>2.</b> Why is moving Summit County to the comparison group worse than dropping it?</summary>

Because it took the training. Putting a treated unit among the untrained means the comparison group's decline contains a real program effect, and dividing by it removes part of what is being measured. The notebook shows the estimate falling to 7.4 percent. It also still carries its own steep pre trend, pushing the comparison group down for a second, unrelated reason. Two biases, both in the same direction.
</details>

<details>
<summary><b>3.</b> Suppose three of the five treated agencies had failed the pre trend test. What then?</summary>

The design is not usable, and saying so is the correct output. Dropping three of five leaves an estimate from two agencies with an interval too wide to be worth reporting, and keeping them means the estimate is mostly their private trends. The honest report states the pre trend differences, states that the comparison group is not a valid counterfactual for these agencies, and does not produce a headline number.
</details>

## Key Takeaway

Drop the agency, say so, and report both estimates. Reach for agency specific trends only after checking that the treatment indicator is not collinear with time.

---

| | |
|---|---|
| **Previous** | [Module 7: Testing Parallel Trends](Module_07_Testing_Parallel_Trends.md) |
| **Next** | [Module 9: Regression to the Mean](Module_09_Regression_To_The_Mean.md) |
| **Builds on** | [Module 7](Module_07_Testing_Parallel_Trends.md), Time Series Advanced [Module 11](../../Time_Series/Advanced/Module_11_Interrupted_Time_Series.md) |
| **Used again in** | [Module 13](Module_13_Spillover_And_Contamination.md), [Module 16](Module_16_Writing_Up_A_Causal_Claim.md) |

*This module is part of a series developed for the Washington Data Exchange for Public Safety (WADEPS) through the Center for Interdisciplinary Statistical Education and Research (CISER) at Washington State University. Version 1.0, September 2026. Questions, errors, or suggestions: yin.zhang@wsu.edu*

*All examples use synthetic data created for teaching. They do not represent any real jurisdiction, agency, officer, or incident. See [Data/DATA_DICTIONARY.md](../../Data/DATA_DICTIONARY.md).*
