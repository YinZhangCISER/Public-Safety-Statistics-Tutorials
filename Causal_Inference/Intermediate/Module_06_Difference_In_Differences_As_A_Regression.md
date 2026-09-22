# Module 6: Difference in Differences, as a Regression

> **Developed by Yin Zhang, PhD**, Assistant Professor, Department of Mathematics and Statistics, Washington State University

## The Question

The hand calculation gave 12.5 percent. What does a regression add, and which specification should be the default?

## The Idea in Plain Language

A regression reproduces the same comparison and buys three things the arithmetic cannot: an interval, fixed effects that handle agency and month differences without naming them, and somewhere to put everything the rest of the series needs to add.

## The Method

> **incidents ~ Poisson**, with **log(arrests)** as an offset, **agency** effects, **month** effects, and indicators for the **phase in** and **settled** periods

In words: model the count directly, let each agency have its own baseline and each month its own level, and read the settled coefficient as a proportional change.

**Not least squares on the log rate.** Ten percent of the agency months in this dataset have zero use of force incidents, and the log of zero drops them. The dropped rows are the smallest agencies and the quietest months, so the loss is systematic.

| Assumption | Diagnostic |
|---|---|
| Something in the model absorbs time | is there a `post` indicator or month effects |
| Exposure enters proportionally | estimate the arrests coefficient freely once, check it covers 1 |
| Variance matches the mean | Pearson dispersion near 1 |
| The phase in is modelled separately | its coefficient lies between zero and the settled effect |

## Worked Example

![Two panels. The left shows three specifications with their intervals, all landing between 12.5 and 12.6 percent against a dashed line at the true 12 percent. The right shows their AIC values as bars: 5168, 5138 and 4744, with the agency and month effects specification much lower](Figures/fig_06_did_as_regression.png)

| Specification | Estimate | 95 percent interval | AIC |
|---|---|---|---|
| Group and period indicators | −12.6% | [−17.9, −6.9] | 5,168 |
| Agency fixed effects | −12.5% | [−17.8, −6.9] | 5,138 |
| **Agency and month fixed effects** | **−12.6%** | **[−17.9, −6.9]** | **4,744** |
| **The truth** | **−12.0%** | | |

Two things are true at once.

**The estimate barely moves.** All three specifications agree to a tenth of a point, and the intervals are essentially identical. The simple specification was not wrong.

**The fit improves by more than 400 AIC points.** Month effects capture the seasonal pattern and the statewide trend that a single  indicator was approximating with one step.

### The specification that does fail

| | Estimate |
|---|---|
| Agency effects, **no time term at all** | **−29.5%** |

Remove everything that absorbs time and the settled indicator picks up four years of statewide decline. **Something must account for time.** A `post` indicator is the minimum; month effects are the safe default.

### The coefficient worth reading

The phase in coefficient comes out at **−9.4 percent**, between zero and the settled effect of −12.6. That is what a partially implemented program should look like. If it had come out positive, as it does when the time structure is missing, that is a signal to go back rather than a finding.

## Do It Yourself

> 📓 **Notebook:** [Module_06_Difference_In_Differences_As_A_Regression.ipynb](Notebooks/Module_06_Difference_In_Differences_As_A_Regression.ipynb)
> [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/YinZhangCISER/Public-Safety-Statistics-Tutorials/blob/main/Causal_Inference/Intermediate/Notebooks/Module_06_Difference_In_Differences_As_A_Regression.ipynb)
> About 25 minutes.

- Counts the zero months that would break a log rate regression
- Fits three specifications and the one that fails, with AIC
- Reads the phase in coefficient and the dispersion as diagnostics
- The exercise gives each trained agency its own coefficient

## Pitfalls

| What goes wrong | What it looks like | What to do |
|---|---|---|
| Least squares on the log rate | ten percent of rows silently dropped | Poisson with an offset |
| No time term | an estimate more than twice the truth | month effects, or at minimum a `post` indicator |
| Reading only the coefficient of interest | a broken model that looks fine | read the phase in coefficient too |
| Treating a better AIC as a better estimate | over interpreting a specification choice | report the estimate under all of them |
| Ignoring dispersion | intervals too narrow | check it; 1.12 here is acceptable |

## Check Your Understanding

<details>
<summary><b>1.</b> Time Series Advanced Module 10 found that agency effects without month effects gave 29.5 percent instead of 12. Here agency effects give 12.5. What is different?</summary>

The `post` indicator. In that module the specification had agency effects and the treatment indicator and nothing else, so the treatment indicator had to absorb the statewide decline. Here the second specification includes `post`, which does that job. The notebook reproduces the failure by dropping `post`, and it gives 29.5 percent exactly as in the earlier module. **The lesson is about what absorbs time, not about which fixed effects are named.**
</details>

<details>
<summary><b>2.</b> If the estimate is the same under all three specifications, why prefer the one with month effects?</summary>

Because you do not know in advance that the estimate will be the same, and you cannot use the fact that it was to justify the choice you made before seeing it. Month effects absorb any statewide shock of any shape, including ones nobody anticipated, and they cost nothing here. The AIC improvement says they are capturing real structure rather than noise.
</details>

<details>
<summary><b>3.</b> The interval runs from 17.9 to 6.9 percent below. What can and cannot be said?</summary>

That the data are consistent with a reduction anywhere between about 7 and 18 percent, and not consistent with zero. What cannot be said is that the effect is 12.6 percent; that is the centre of a range, not a measurement. A report that gives the interval lets a reader decide whether a 7 percent effect would still justify the program's cost, which is usually the actual question.
</details>

## Key Takeaway

Poisson with an offset, agency and month effects, a separate phase in term, and read every coefficient in the output rather than only the one you wanted.

---

| | |
|---|---|
| **Previous** | [Module 5: Difference in Differences, by Hand](Module_05_Difference_In_Differences_By_Hand.md) |
| **Next** | [Module 7: Testing Parallel Trends](Module_07_Testing_Parallel_Trends.md) |
| **Builds on** | [Module 5](Module_05_Difference_In_Differences_By_Hand.md), Time Series Advanced [Module 8](../../Time_Series/Advanced/Module_08_Count_Regression_With_Harmonics.md) |
| **Used again in** | [Module 7](Module_07_Testing_Parallel_Trends.md) onward |

*This module is part of a series developed for the Washington Data Exchange for Public Safety (WADEPS) through the Center for Interdisciplinary Statistical Education and Research (CISER) at Washington State University. Version 1.0, September 2026. Questions, errors, or suggestions: yin.zhang@wsu.edu*

*All examples use synthetic data created for teaching. They do not represent any real jurisdiction, agency, officer, or incident. See [Data/DATA_DICTIONARY.md](../../Data/DATA_DICTIONARY.md).*
