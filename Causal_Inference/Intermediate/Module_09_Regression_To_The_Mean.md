# Module 9: Regression to the Mean

> **Developed by Yin Zhang, PhD**, Assistant Professor, Department of Mathematics and Statistics, Washington State University

## The Question

Anything picked for being extreme tends to look better next time. How large is that effect here, and what determines its size?

## The Idea in Plain Language

A measurement has a real part and a noisy part. Something selected for being extreme is usually somewhat extreme in the real part **and** had an unusual draw of the noisy part. The real part persists, the noise is redrawn, and the measurement moves toward the middle.

The size of the movement is set entirely by **how much of the measurement is noise**. That is a property of the measurement, not of the agencies.

## The Method

> regress the change on the starting level, among units that received nothing
>
> and separately, split the baseline period in half and correlate the two halves

The first quantifies the reversion. The second says how much of the ranking was real in the first place, which predicts how much reversion there should be.

## Worked Example

Seven agencies, none of which took the training.

![Two panels. The left plots each agency's percent change against its starting rate, with a fitted line sloping down at 13.9 points per unit, annotated p equals 0.15 and R squared 0.37. The right plots each agency's rate in the first half of the pre period against the second half, with the points close to the diagonal and a correlation of 0.94](Figures/fig_09_regression_to_mean.png)

| | |
|---|---|
| Slope of change on starting level | **−13.9** points per unit |
| p value | 0.149 |
| R squared | 0.37 |
| Agencies | 7 |

The slope points the expected way and **is not statistically distinguishable from zero** with seven agencies. Report it as what it is: suggestive, underpowered, and in the direction the mechanism predicts.

### How much of the ranking is real

| Measurement window | Correlation between two independent windows |
|---|---|
| Two adjacent single months | **−0.04** |
| Two halves of the pre period, about two years each | **+0.94** |

Same agencies, same outcome. **Over two years these agencies' levels are almost entirely real; over one month they are almost entirely luck.**

That is why the reversion in the left panel is weak: a two year average has little noise for the mechanism to work on. Rank the same agencies on a single month and the reversion is enormous.

## Do It Yourself

> 📓 **Notebook:** [Module_09_Regression_To_The_Mean.ipynb](Notebooks/Module_09_Regression_To_The_Mean.ipynb)
> [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/OWNER/REPO/blob/main/Causal_Inference/Intermediate/Notebooks/Module_09_Regression_To_The_Mean.ipynb)
> About 25 minutes.

- Regresses change on starting level among agencies that received nothing
- Compares the split half correlation against the adjacent month correlation
- The exercise simulates agencies whose true rate never changes

## Pitfalls

| What goes wrong | What it looks like | What to do |
|---|---|---|
| Selecting on a single period | reversion that swamps any real effect | rank on several years |
| Calling reversion an effect | a program credited with arithmetic | compare against units selected the same way |
| Assuming reversion is always large | a real effect dismissed as reversion | measure the split half correlation |
| Testing for it with a handful of units | p = 0.15 read as "no reversion" | report the slope and the interval |

## Check Your Understanding

<details>
<summary><b>1.</b> The slope is 13.9 points per unit with p = 0.149. Should it be reported?</summary>

Yes, with the p value and the sample size. Reporting only the slope overstates it; reporting only "not significant" hides a mechanism that is known to exist and is pointing the right way. With seven units almost nothing reaches significance, so a non significant result here carries very little information either way, and saying that is more honest than picking a side.
</details>

<details>
<summary><b>2.</b> Why does the single month correlation come out near zero rather than merely low?</summary>

Because month to month variation in these agencies is dominated by Poisson noise around a small mean. Several of them average two or three incidents a month, so one month's count is essentially a random draw and carries almost no information about which agency it came from. A correlation near zero means the single month ranking is a ranking of luck.
</details>

<details>
<summary><b>3.</b> A state targets the worst ten agencies by a three year average. How worried should you be about reversion?</summary>

Less than with a one year average and not zero. A three year average is mostly real level, as the 0.94 correlation here suggests, so most of the selected agencies are genuinely high rather than unlucky. The remedy is the same regardless: draw the comparison group from the same ranking, so whatever reversion exists happens on both sides.
</details>

## Key Takeaway

Measure the split half correlation before worrying about reversion, and draw the comparison group from the same ranking that chose the recipients.

---

| | |
|---|---|
| **Previous** | [Module 8: When Parallel Trends Fails](Module_08_When_Parallel_Trends_Fails.md) |
| **Next** | [Module 10: Selection on the Outcome](Module_10_Selection_On_The_Outcome.md) |
| **Builds on** | [Module 4](Module_04_Building_A_Comparison_Group.md), Beginner [Topic 11](../Beginner/Topic_11_Why_The_Worst_Performers_Always_Improve.md) |
| **Used again in** | [Module 10](Module_10_Selection_On_The_Outcome.md), [Module 12](Module_12_Placebo_Tests.md) |

*This module is part of a series developed for the Washington Data Exchange for Public Safety (WADEPS) through the Center for Interdisciplinary Statistical Education and Research (CISER) at Washington State University. Version 1.0, September 2026. Questions, errors, or suggestions: yin.zhang@wsu.edu*

*All examples use synthetic data created for teaching. They do not represent any real jurisdiction, agency, officer, or incident. See [Data/DATA_DICTIONARY.md](../../Data/DATA_DICTIONARY.md).*
