# Module 11: Instrumental Variables

> **Developed by Yin Zhang, PhD**, Assistant Professor, Department of Mathematics and Statistics, Washington State University

**The question this module answers:** *An instrument would identify the effect without any parallel trends assumption. Is there one in these records?*

---

## The Question

There is not. This module teaches the conditions, tests every candidate the dataset contains, and shows that **the candidate closest to relevant is the one most clearly invalid.**

## Estimand and Assumptions

> **Relevance.** The instrument predicts treatment. **Testable**; the usual bar is a first stage F above 10.
>
> **Exclusion.** The instrument affects the outcome only through treatment. **Not testable.**
>
> **Monotonicity.** Nobody is pushed out of treatment by the instrument. **Not testable.**

Two of three cannot be tested. That is the trade: instrumental variables replaces an assumption you can check weakly with assumptions you cannot check at all, in exchange for not needing parallel trends. What it identifies is the **LATE**, the effect for the units the instrument moves.

**A partial test of exclusion is available**: if a candidate is associated with the outcome **before** the program existed, it is reaching the outcome by some route other than a treatment that had not happened.

## Estimation

```python
sm.OLS(X["treated"], sm.add_constant(X[[candidate]])).fit()   # relevance
sm.OLS(X["pre_rate"], sm.add_constant(X[[candidate]])).fit()  # partial exclusion test
```

## Worked Example

![A scatter plot of five candidate instruments, with the first stage F statistic on a log x axis and the p value for association with the pre program outcome on the y axis. A shaded strip marks F above 10 and a dashed line marks p equal to 0.05. All five candidates sit far to the left of the strip, and the one furthest right, region is East, sits closest to the exclusion line](Figures/fig_a11_instrumental_variables.png)

| Candidate | First stage F | Relevance p | Associated with the pre program outcome, p |
|---|---|---|---|
| **Region is East** | **1.60** | 0.235 | **0.067** |
| Is a sheriff's office | 0.10 | 0.763 | 0.548 |
| County budget | 0.88 | 0.370 | 0.210 |
| County population | 1.30 | 0.282 | 0.157 |
| Public safety budget share | 0.01 | 0.941 | 0.220 |

**Not one candidate reaches an F of 1**, let alone 10.

And region, the strongest, is also the candidate most clearly associated with the outcome before the program existed. **The candidate closest to relevant is the one most clearly failing exclusion**, which is not a coincidence: variables that predict which agencies get a program usually do so by capturing something about those agencies, and that something usually reaches the outcome directly.

### Using one anyway

| | |
|---|---|
| First stage, region on treatment | −0.371, F = 1.60 |
| Reduced form, region on the change | +8.48 rate points |
| **The Wald ratio** | **−22.8%** |
| The truth | −12.0% |

**Notice what it is not: absurd.** A weak instrument estimate of 400 percent would be caught by anyone. This one looks like a plausible policy effect, and a reader given only the number cannot tell that its denominator is not distinguishable from zero.

The weak instrument pathology does not announce itself in the estimate. **The first stage F is what announces it**, which is why an F of 1.60 ends the analysis rather than starting it.

## Recovering the Planted Answer

**It cannot be**, and the reason is a property of the data rather than of the method: the generator contains no variable that pushes an agency into the program without also touching its use of force rate. The selection rule reads the outcome's own history, which is the one thing that can never be an instrument.

## Diagnostics

| Check | Acceptable |
|---|---|
| First stage F | above 10, reported always |
| Association with the outcome before treatment | absent |
| The exclusion argument | written in prose, before looking |
| Number of candidates considered | reported |
| Monotonicity | argued, since it cannot be tested |

## Do It Yourself

> 📓 **Notebook:** [Module_11_Instrumental_Variables.ipynb](Notebooks/Module_11_Instrumental_Variables.ipynb)
> [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/OWNER/REPO/blob/main/Causal_Inference/Advanced/Notebooks/Module_11_Instrumental_Variables.ipynb)
> About 30 minutes.

The exercise searches 300 pure noise candidates and finds that several clear an F of 4.

## What a Usable Instrument Would Look Like

| Property | What it would need |
|---|---|
| Relevance | something that pushed agencies into the program, strongly |
| Exclusion | with no other route to use of force |
| Monotonicity | never pushing an agency out |
| Plausible candidates | a lottery among eligible agencies, a funding formula with an arbitrary cutoff, a trainer's travel schedule |

**All three are design features, not data features.** They exist when someone builds them in, which is the argument in Beginner [Topic 16](../Beginner/Topic_16_Randomness_Solves_A_Problem.md) for randomising the first wave: it creates an instrument where none existed.

Searching an administrative dataset for an instrument after the fact almost never succeeds, and the searching is itself a specification problem: with enough candidates one will pass the relevance test by chance.

## Reporting the Result

> An instrumental variables design was considered. Five candidate instruments available in the agency records were tested: region, agency type, county budget, county population, and the share of county budget spent on public safety. The strongest first stage F statistic is 1.60, far below the conventional threshold of 10, so none is relevant. The strongest candidate, region, is also the most strongly associated with the use of force rate before the program began, p = 0.067, which is evidence against the exclusion restriction. No instrumental variables estimate is reported.

## Further Reading

- Angrist, J. D., Imbens, G. W. and Rubin, D. B. (1996). Identification of causal effects using instrumental variables. *Journal of the American Statistical Association*, 91.
- Bound, J., Jaeger, D. A. and Baker, R. M. (1995). Problems with instrumental variables estimation when the correlation between the instruments and the endogenous explanatory variable is weak. *Journal of the American Statistical Association*, 90.
- Lal, A., Lockhart, M., Xu, Y. and Zu, Z. (2024). How much should we trust instrumental variable estimates in political science? *Political Analysis*, 32.

---

| | |
|---|---|
| **Previous** | [Module 10: Propensity Scores and the Overlap Assumption](Module_10_Propensity_Scores.md) |
| **Next** | [Module 12: Regression Discontinuity](Module_12_Regression_Discontinuity.md) |
| **Builds on** | [Module 3](Module_03_Identification_Before_Estimation.md), [Module 10](Module_10_Propensity_Scores.md) |
| **Used again in** | [Module 12](Module_12_Regression_Discontinuity.md), [Module 16](Module_16_The_Causal_Claim.md) |

*This module is part of a series developed for the Washington Data Exchange for Public Safety (WADEPS) through the Center for Interdisciplinary Statistical Education and Research (CISER) at Washington State University. Version 1.0, September 2026. Questions, errors, or suggestions: yin.zhang@wsu.edu*

*All examples use synthetic data created for teaching. They do not represent any real jurisdiction, agency, officer, or incident. See [Data/DATA_DICTIONARY.md](../../Data/DATA_DICTIONARY.md).*
