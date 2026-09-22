# Module 5: Two Way Fixed Effects Done Properly

> **Developed by Yin Zhang, PhD**, Assistant Professor, Department of Mathematics and Statistics, Washington State University

**The question this module answers:** *"The TWFE estimate" is spoken of as one number. Is it?*

---

## The Question

It is not. **The linear and the count versions weight the units differently, and on this panel they are five percentage points apart.** Neither is biased; they estimate different things.

## Estimand and Assumptions

> **Poisson** log(mu) = log(arrests) + agency + month + b·settled
>
> **Linear** rate = agency + month + b·settled

Both are difference in differences with agency and month fixed effects on the same 964 rows. The Poisson version is fitted to counts, so an agency month contributes in proportion to the incidents it contains. The linear version on a rate treats every agency month as one observation.

| Assumption | Shared | Differs |
|---|---|---|
| Parallel trends | yes | on the scale each model imposes |
| Weighting | | incidents against agency months |
| Handling of zeros | | Poisson keeps them, a log rate drops them |

## Estimation

```python
smf.glm("n_uof ~ C(agency_id)+C(year_month)+settled+phase", d,
        family=sm.families.Poisson(), offset=d["lo"]).fit()
smf.ols("rate ~ C(agency_id)+C(year_month)+settled+phase", d).fit()
```

## Worked Example

![Two panels. The left shows two intervals, the linear estimator at minus 18.2 percent and the Poisson at minus 12.6, against a dashed line at the true 12 percent. The right shows each treated agency's share of incidents against its share of agency months: Stonewick 61 against 25 percent, Pinecrest 4 against 25](Figures/fig_a05_twfe.png)

| | Estimate | 95 percent interval |
|---|---|---|
| Poisson with an offset | **−12.61%** | [−17.9, −6.9] |
| Linear on the rate | **−0.658 rate points** = −18.2% | [−1.057, −0.259] |
| **The truth** | **−12.00%** | |

**Five percentage points apart.**

| Agency | Share of incidents | Share of agency months | Its own estimate |
|---|---|---|---|
| **Stonewick** | **61%** | 25% | **−9.3%** |
| Tarnbridge | 28% | 25% | −17.2% |
| Millgate | 8% | 25% | −15.4% |
| Pinecrest | 4% | 25% | −20.6% |

Stonewick carries 61 percent of the incidents and a quarter of the months, and its own estimate is the smallest of the four. The Poisson model lands nearer to Stonewick's number; the linear model lands nearer to the simple average, which the small noisy agencies pull down.

**This is the estimand question from [Module 1](Module_01_Potential_Outcomes_And_Estimands.md) arriving through the back door.** Choosing a link function chooses a weighting, usually without anyone noticing.

### Confirming the diagnosis

| | Estimate |
|---|---|
| Linear, unweighted | −18.2% |
| Linear, weighted by arrests | −15.1% |
| Poisson with an offset | −12.6% |
| The truth | −12.0% |

Weighting the linear model by exposure closes more than half the gap. **The weights were most of the difference; the remainder is the functional form.**

## Recovering the Planted Answer

The planted effect is multiplicative on the rate, which is what a log link imposes and what a linear model in the rate does not. The Poisson version recovers 12.6 against a planted 12.0. The linear version is not wrong about its own estimand; it is estimating an agency weighted, additively scaled quantity that happens to be 18.2 percent of the pre period mean.

## Diagnostics

| Check | Acceptable |
|---|---|
| Both versions fitted | and both reported if they differ |
| Unit sizes compared | if they span a factor of ten, expect a gap |
| Exposure weighted linear version | as the bridge between the two |
| Zero months counted | if more than a few percent, the log rate is not an option |
| The estimand named | before either is chosen |

## Do It Yourself

> 📓 **Notebook:** [Module_05_Two_Way_Fixed_Effects.ipynb](Notebooks/Module_05_Two_Way_Fixed_Effects.ipynb)
> [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/YinZhangCISER/Public-Safety-Statistics-Tutorials/blob/main/Causal_Inference/Advanced/Notebooks/Module_05_Two_Way_Fixed_Effects.ipynb)
> About 30 minutes.

The exercise drops the largest and smallest treated agencies and watches the two estimators converge.

## When Not To Use This

| Situation | Reach for |
|---|---|
| Units adopt at different times | [Module 7](Module_07_Staggered_Adoption.md) first; TWFE may not estimate anything nameable |
| Effects vary across units | [Module 15](Module_15_Heterogeneous_Effects.md), and report both weightings |
| Few clusters | [Module 9](Module_09_Honest_Inference_With_Few_Clusters.md) for the interval |
| One treated unit | [Module 8](Module_08_Synthetic_Control.md), with its diagnostics |

## Reporting the Result

> The estimator is a Poisson regression of monthly use of force counts on agency and calendar month fixed effects and indicators for the program's phase in and settled periods, with the log of arrests as an offset. It estimates the average treatment effect on the treated weighted by incidents. A linear specification on the rate, which weights agency months equally, gives 18.2 percent of the pre period mean; weighting that specification by arrests gives 15.1 percent. The gap between the specifications is a weighting difference rather than a disagreement about the data, and arises because the treated agencies differ in size by a factor of fifteen.

## Further Reading

- Wooldridge, J. M. (2010). *Econometric Analysis of Cross Section and Panel Data*, 2nd edition. MIT Press. Chapters 10 and 18.
- Solon, G., Haider, S. J. and Wooldridge, J. M. (2015). What are we weighting for? *Journal of Human Resources*, 50.
- Gourieroux, C., Monfort, A. and Trognon, A. (1984). Pseudo maximum likelihood methods: applications to Poisson models. *Econometrica*, 52.

---

| | |
|---|---|
| **Previous** | [Module 4: Selection Mechanisms and What They Do to an Estimate](Module_04_Selection_Mechanisms.md) |
| **Next** | [Module 6: Event Studies and Pre Trend Testing](Module_06_Event_Studies_And_Pre_Trend_Testing.md) |
| **Builds on** | [Module 1](Module_01_Potential_Outcomes_And_Estimands.md), Intermediate [Module 6](../Intermediate/Module_06_Difference_In_Differences_As_A_Regression.md) |
| **Used again in** | [Module 7](Module_07_Staggered_Adoption.md), [Module 9](Module_09_Honest_Inference_With_Few_Clusters.md), [Module 15](Module_15_Heterogeneous_Effects.md) |

*This module is part of a series developed for the Washington Data Exchange for Public Safety (WADEPS) through the Center for Interdisciplinary Statistical Education and Research (CISER) at Washington State University. Version 1.0, September 2026. Questions, errors, or suggestions: yin.zhang@wsu.edu*

*All examples use synthetic data created for teaching. They do not represent any real jurisdiction, agency, officer, or incident. See [Data/DATA_DICTIONARY.md](../../Data/DATA_DICTIONARY.md).*
