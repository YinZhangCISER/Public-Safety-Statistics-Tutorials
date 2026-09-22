# Choosing a Causal Inference Design

*Developed by Yin Zhang, PhD, Assistant Professor, Data Analytics Program, Department of Mathematics and Statistics, Washington State University, for the Washington Data Exchange for Public Safety (WADEPS) through the Center for Interdisciplinary Statistical Education and Research (CISER).*

**The design is chosen by what the data contains, not by what the analyst prefers.** This page walks the choice, then gives the diagnostic that rules each design out before any model is fitted.

---

## First, is the question causal?

| The question | What it needs |
|---|---|
| How many, where, and when? | a description, no design required |
| Is this agency higher than its peers? | a comparison, no design required |
| **Did the program cause the change?** | **a design, and an argument about a world that was not observed** |

A causal question always compares the observed world against one that did not happen. The whole difficulty is that the second one has to be constructed. See [Beginner Topic 3](../../Causal_Inference/Beginner/Topic_03_The_World_You_Cannot_See.md).

---

## The design the data allows

Read from the top. The first row whose requirement is met is the design to use.

| If the data has | The design | Where it is worked |
|---|---|---|
| Treatment assigned at random | Compare the groups directly | [Beginner Topic 16](../../Causal_Inference/Beginner/Topic_16_Randomness_Solves_A_Problem.md) |
| A comparison group, a pre period, and pre trends that match | **Difference in differences** | [Intermediate 5](../../Causal_Inference/Intermediate/Module_05_Difference_In_Differences_By_Hand.md) to [Intermediate 8](../../Causal_Inference/Intermediate/Module_08_When_Parallel_Trends_Fails.md), [Advanced 5](../../Causal_Inference/Advanced/Module_05_Two_Way_Fixed_Effects.md), [Advanced 6](../../Causal_Inference/Advanced/Module_06_Event_Studies_And_Pre_Trend_Testing.md) |
| The same, but units adopted at different dates | Staggered adoption estimators, not plain two way fixed effects | [Advanced 7](../../Causal_Inference/Advanced/Module_07_Staggered_Adoption.md) |
| One treated unit, many untreated donors, and a close pre period fit | Synthetic control | [Advanced 8](../../Causal_Inference/Advanced/Module_08_Synthetic_Control.md) |
| Assignment by a threshold, with many units close to it | Regression discontinuity | [Advanced 12](../../Causal_Inference/Advanced/Module_12_Regression_Discontinuity.md) |
| Something that shifts treatment and affects the outcome no other way | Instrumental variables | [Advanced 11](../../Causal_Inference/Advanced/Module_11_Instrumental_Variables.md) |
| Rich covariates and treated and untreated units that genuinely overlap | Propensity score methods | [Advanced 10](../../Causal_Inference/Advanced/Module_10_Propensity_Scores.md) |
| No comparison group, but a known date and a long series | Interrupted time series, with its limits stated | [Time Series Advanced 11](../../Time_Series/Advanced/Module_11_Interrupted_Time_Series.md) |
| **None of the above** | Bounds, or a description with no causal claim | [Advanced 14](../../Causal_Inference/Advanced/Module_14_Sensitivity_And_Partial_Identification.md), [Intermediate 16](../../Causal_Inference/Intermediate/Module_16_Writing_Up_A_Causal_Claim.md) |

---

## The diagnostic that comes before the estimate

Every design below can be ruled out by one check that requires no model. **Run the check first.** An unusable design still returns a number with a standard error attached, and three of the four unusable ones in the teaching data return a plausible looking number, one of them significant with the wrong sign.

| Design | The check | It is arithmetic, not a model |
|---|---|---|
| Difference in differences | Pre period trends, group by group | A group mean per period |
| Staggered adoption | Which cohorts serve as controls for which | Counting treatment dates |
| Synthetic control | Pre period fit error, and whether the treated unit lies inside the donors' range | Comparing two ranges |
| Regression discontinuity | How many units lie within a defensible bandwidth | Counting |
| Instrumental variables | First stage F, and the instrument's association with the pre period outcome | One regression, before the design |
| Propensity scores | The overlap range, and how many units survive trimming | Comparing two ranges |
| Any of them | Placebo dates, and outcomes the program could not have touched | The same estimator on a different column |

---

## What the checks found in the teaching data

Seven designs applied to one program whose true effect is a 12.0 percent reduction.

| Design | Reported | The diagnostic that condemns it |
|---|---|---|
| Before and after | −33.1% | no comparison group |
| Regression discontinuity | +30.9% | two agencies within 0.30 of the cutoff |
| Instrumental variables | −22.8% | strongest first stage F is 1.60 |
| Synthetic control | +11.3% to −25.1% | pre period fit error 25 to 48 percent |
| Propensity score | none defensible | 4 percent overlap, two units survive trimming |
| Difference in differences, all five treated | −17.0% | one agency on its own pre trend |
| **Difference in differences, checked** | **−12.6%** | |
| **The truth** | **−12.0%** | |

The full account is in [Advanced Module 16](../../Causal_Inference/Advanced/Module_16_The_Causal_Claim.md).

---

## The order of operations

Doing these out of order is what produces a confident wrong answer.

1. **State the estimand.** The effect on whom, over what window, compared with what. [Advanced 1](../../Causal_Inference/Advanced/Module_01_Potential_Outcomes_And_Estimands.md)
2. **Decide what to condition on, before fitting.** Drawing the graph first prevents conditioning on a collider. [Advanced 2](../../Causal_Inference/Advanced/Module_02_DAGs_And_The_Backdoor_Criterion.md)
3. **Establish identification.** A failure of identification is invisible in the output, and an unidentified specification in this data has a **narrower** interval than the correct one. [Advanced 3](../../Causal_Inference/Advanced/Module_03_Identification_Before_Estimation.md)
4. **Run the free diagnostic.** See the table above.
5. **Estimate**, with an interval that respects the number of clusters. [Advanced 9](../../Causal_Inference/Advanced/Module_09_Honest_Inference_With_Few_Clusters.md)
6. **Try to break it.** Placebo dates, falsification outcomes, permutation against the right null. [Advanced 13](../../Causal_Inference/Advanced/Module_13_Placebo_Permutation_And_Falsification.md)
7. **Say how fragile it is.** How large would an unobserved trend have to be to erase the result. [Advanced 14](../../Causal_Inference/Advanced/Module_14_Sensitivity_And_Partial_Identification.md)
8. **Write the claim with its comparison, its window, and how the units were selected.** [Advanced 16](../../Causal_Inference/Advanced/Module_16_The_Causal_Claim.md)

---

## The recurring mistakes, and where each is dismantled

| The mistake | Why it survives | Where |
|---|---|---|
| Before and after with no comparison | Everything was already improving, so the program looks effective | [Beginner Topic 4](../../Causal_Inference/Beginner/Topic_04_Before_And_After_Is_Not_Enough.md), [Beginner Topic 5](../../Causal_Inference/Beginner/Topic_05_Things_Were_Already_Changing.md) |
| Selecting the worst performers, then measuring improvement | They improve on their own, program or not | [Beginner Topic 11](../../Causal_Inference/Beginner/Topic_11_Why_The_Worst_Performers_Always_Improve.md), [Intermediate 9](../../Causal_Inference/Intermediate/Module_09_Regression_To_The_Mean.md) |
| Treating volunteers as comparable to non volunteers | Whoever chose to join differs in ways the data does not hold | [Beginner Topic 12](../../Causal_Inference/Beginner/Topic_12_Who_Chose_To_Participate.md), [Advanced 4](../../Causal_Inference/Advanced/Module_04_Selection_Mechanisms.md) |
| Controlling for a variable that sits after treatment | It is a mediator or a collider, and adding it creates bias | [Intermediate 11](../../Causal_Inference/Intermediate/Module_11_Confounders_Mediators_And_Colliders.md) |
| Reading an event study one coefficient at a time | The intervals are wide enough to contain almost anything | [Advanced 6](../../Causal_Inference/Advanced/Module_06_Event_Studies_And_Pre_Trend_Testing.md) |
| Reading a passed pre trend test as proof of parallel trends | The test detects a 2 percent a year violation only 16 percent of the time | [Advanced 6](../../Causal_Inference/Advanced/Module_06_Event_Studies_And_Pre_Trend_Testing.md) |
| Reporting a subgroup difference found by looking | Three to eight point gaps appear routinely when the effect is constant | [Advanced 15](../../Causal_Inference/Advanced/Module_15_Heterogeneous_Effects.md) |

---

## Which level to read

| If the output is | Read |
|---|---|
| A judgement about someone else's claim | the [Beginner series](../../Causal_Inference/Beginner/), no code |
| One estimate, built and defended | the [Intermediate series](../../Causal_Inference/Intermediate/) |
| A design whose assumptions will be challenged in review | the [Advanced series](../../Causal_Inference/Advanced/) |

---

*All examples use synthetic data created for teaching. They do not represent any real jurisdiction, agency, officer, or incident.*

*Questions, corrections, or suggestions: yin.zhang@wsu.edu*
