# Module 12: Regression Discontinuity

> **Developed by Yin Zhang, PhD**, Assistant Professor, Department of Mathematics and Statistics, Washington State University

**The question this module answers:** *The selection rule is close to a threshold. Is close enough?*

---

## The Question

It is not, and the reason is not the one people expect. This module separates **fuzziness**, which is survivable, from **an empty neighbourhood**, which is not.

## Estimand and Assumptions

> assignment is determined by whether a **running variable** crosses a cutoff, and the effect is the jump in the outcome at the cutoff

| Assumption | Diagnostic | Type |
|---|---|---|
| **Sharpness** | does the cutoff predict treatment | arithmetic |
| **Enough mass near the cutoff** | count units inside a defensible bandwidth | arithmetic |
| Continuity | would the outcome have been smooth without the program | an argument |
| No manipulation | is the density smooth at the cutoff | an argument |

The identified quantity is **local**: the effect at the cutoff, not the ATT and not the ATE.

## Estimation

```python
sm.OLS(inside["post_rate"],
       sm.add_constant(inside[["above", "running_variable"]])).fit()
```

## Worked Example

![Two panels. The left plots each agency's pre program use of force rate by treatment status with a cutoff at 3.16, marking Summit County below the cutoff and treated and Havenbrook above it and not treated. The right shows the number of agencies inside four bandwidths: two at 0.15 and 0.30, six at 0.50 and eight at 0.80](Figures/fig_a12_regression_discontinuity.png)

### How sharp is it

| Side of a cutoff at 3.159 | Treated |
|---|---|
| Above | 4 of 5 |
| Below | 1 of 7 |

**Two of twelve fall on the wrong side**, one in each direction. The design is **fuzzy**, which is not fatal by itself: a fuzzy design uses the cutoff as an instrument for treatment.

The cutoff's first stage F is **7.60**, below the conventional bar of 10. Fuzziness is a real cost here, and it is not the binding problem.

### The problem that is binding

| Bandwidth | Agencies inside | Treated | Control |
|---|---|---|---|
| 0.15 | **2** | 1 | 1 |
| 0.30 | **2** | 1 | 1 |
| 0.50 | 6 | 4 | 2 |
| 0.80 | 8 | 4 | 4 |
| 1.20 | 12 | 5 | 7 |

Regression discontinuity estimates a **local** effect. Here the local sample is two agencies. Widening the bandwidth to get more units means the estimate is no longer local, and at 0.80 it holds eight of twelve, which is most of the panel.

**There is no bandwidth that is both local and populated.**

And the two agencies at the cutoff are the two least suitable in the dataset: Summit County is the pre trend violator excluded from the main analysis, and Havenbrook reclassified its call categories in January 2023.

### What it reports anyway

| Bandwidth | Jump at the cutoff | p |
|---|---|---|
| 0.50 | **+0.991** rate points | 0.020 |
| 0.80 | **+0.977** | 0.010 |
| 1.20 | **+0.756** | 0.008 |
| **The truth** | **about −0.38** | |

**The design returns the wrong sign, at every bandwidth, significantly.**

With six to twelve points, a linear control for the running variable cannot absorb the fact that agencies above the cutoff have structurally higher rates, so the level difference the selection rule created is read as a jump.

This is what a regression discontinuity produces when it should not have been run: numbers with p values attached, pointing the wrong way. **The diagnostic that should have stopped it is the count of units near the cutoff, and it required no fitting.**

## Recovering the Planted Answer

**It does not**, and it produces a confidently wrong one instead. The generator's rule is "the five agencies with the highest rates", which is a **rank based** rule rather than a threshold rule.

**Rank based selection does not create a discontinuity**, because the cutoff depends on the whole distribution rather than on a fixed value and moves whenever the candidate set changes. "The worst five" and "everyone above 3.0" look similar and only the second supports this design.

## Diagnostics

| Check | Acceptable |
|---|---|
| Units within a defensible bandwidth | enough to fit a local polynomial |
| First stage F, if fuzzy | above 10 |
| Sensitivity to the bandwidth | the estimate stable across reasonable choices |
| Sensitivity to the cutoff | the cutoff published in advance, not chosen |
| Density of the running variable at the cutoff | smooth, no bunching |

## Do It Yourself

> 📓 **Notebook:** [Module_12_Regression_Discontinuity.ipynb](Notebooks/Module_12_Regression_Discontinuity.ipynb)
> [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/YinZhangCISER/Public-Safety-Statistics-Tutorials/blob/main/Causal_Inference/Advanced/Notebooks/Module_12_Regression_Discontinuity.ipynb)
> About 30 minutes.

The exercise varies the cutoff across five defensible values and the estimated jump moves with it.

## When This Design Is Right

| Requirement | Here |
|---|---|
| A rule stated in advance with a numeric cutoff | approximately |
| **Many units near the cutoff** | **two** |
| A running variable measured before assignment | yes |
| No ability to manipulate position | plausible |
| Continuity of everything else at the cutoff | untestable with two units |

**Public safety programs often have something that looks like a threshold and almost never have enough agencies near it.** A state with three hundred agencies and a rule applied to all of them is a different situation.

## Reporting the Result

> A regression discontinuity design was considered. Treatment was allocated to the five agencies with the highest pre program use of force rates, which is a rank based rule rather than a threshold, so no fixed cutoff exists; taking the midpoint between the fifth and sixth ranked agencies as a cutoff leaves two of twelve agencies on the wrong side. The binding obstacle is density: two agencies lie within 0.30 of that cutoff, and a bandwidth wide enough to contain six or more covers most of the panel and is no longer local. Estimates fitted at three bandwidths return a positive jump of about one rate point with p values below 0.02, the opposite sign to the effect the design is attempting to measure.

## Further Reading

- Imbens, G. W. and Lemieux, T. (2008). Regression discontinuity designs: a guide to practice. *Journal of Econometrics*, 142.
- Calonico, S., Cattaneo, M. D. and Titiunik, R. (2014). Robust nonparametric confidence intervals for regression discontinuity designs. *Econometrica*, 82.
- Cattaneo, M. D., Idrobo, N. and Titiunik, R. (2020). *A Practical Introduction to Regression Discontinuity Designs*. Cambridge University Press.

---

| | |
|---|---|
| **Previous** | [Module 11: Instrumental Variables](Module_11_Instrumental_Variables.md) |
| **Next** | [Module 13: Placebo, Permutation and Falsification Tests](Module_13_Placebo_Permutation_And_Falsification.md) |
| **Builds on** | [Module 4](Module_04_Selection_Mechanisms.md), [Module 11](Module_11_Instrumental_Variables.md) |
| **Used again in** | [Module 16](Module_16_The_Causal_Claim.md) |

*This module is part of a series developed for the Washington Data Exchange for Public Safety (WADEPS) through the Center for Interdisciplinary Statistical Education and Research (CISER) at Washington State University. Version 1.0, September 2026. Questions, errors, or suggestions: yin.zhang@wsu.edu*

*All examples use synthetic data created for teaching. They do not represent any real jurisdiction, agency, officer, or incident. See [Data/DATA_DICTIONARY.md](../../Data/DATA_DICTIONARY.md).*
