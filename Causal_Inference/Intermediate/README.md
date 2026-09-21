# Causal Inference, Intermediate Level

### Building one estimate, and checking it until it can be defended

*Developed by Yin Zhang, PhD, Assistant Professor, Data Analytics Program, Department of Mathematics and Statistics, Washington State University, for the Washington Data Exchange for Public Safety (WADEPS) through the Center for Interdisciplinary Statistical Education and Research (CISER).*

For law enforcement staff, government analysts and undergraduates who have some background and want to do the work. Sixteen modules, each with a Jupyter notebook that runs on the published data.

> **Publication status:** complete. All sixteen modules are published, each with a notebook.

---

## The worked example

One program, adopted by five agencies in July 2023, with a true effect built into the teaching data of exactly **12 percent**. Every method can therefore be graded rather than argued about.

| Analysis | Estimate | What it missed |
|---|---|---|
| Before and after, the five trained agencies | −33.1% | no comparison group |
| Agency effects, nothing absorbing time | −29.5% | the statewide decline |
| Difference in differences, all five trained | −17.0% | one agency on its own pre trend |
| **Difference in differences, checked** | **−12.6%** | |
| **The truth** | **−12.0%** | |

---

## Part I. Foundations

| # | Module | The question it answers |
|---|---|---|
| 1 | [From "It Went Down" to "The Program Did It"](Module_01_From_It_Went_Down_To_The_Program_Did_It.md) | Which sentence do these records support? |
| 2 | [Potential Outcomes Without the Algebra](Module_02_Potential_Outcomes_Without_The_Algebra.md) | What exactly is being estimated? |
| 3 | [The Counterfactual You Have to Construct](Module_03_The_Counterfactual_You_Have_To_Construct.md) | Three ways to build Y(0), and what to do when they disagree |
| 4 | [Building a Comparison Group](Module_04_Building_A_Comparison_Group.md) | Who is in, and how much does it matter? |

## Part II. Difference in differences, properly

| # | Module | The question it answers |
|---|---|---|
| 5 | [Difference in Differences, by Hand](Module_05_Difference_In_Differences_By_Hand.md) | Four numbers, and whether to subtract or divide |
| 6 | [Difference in Differences, as a Regression](Module_06_Difference_In_Differences_As_A_Regression.md) | What a model adds, and which specification |
| 7 | [Testing Parallel Trends](Module_07_Testing_Parallel_Trends.md) | What can be tested, and how much the test is worth |
| 8 | [When Parallel Trends Fails](Module_08_When_Parallel_Trends_Fails.md) | Four responses, and why the sophisticated one fails |

## Part III. The things that break it

| # | Module | The question it answers |
|---|---|---|
| 9 | [Regression to the Mean](Module_09_Regression_To_The_Mean.md) | How large is it here, and what sets its size? |
| 10 | [Selection on the Outcome](Module_10_Selection_On_The_Outcome.md) | What does the selection rule produce on its own? |
| 11 | [Confounders, Mediators and Colliders](Module_11_Confounders_Mediators_And_Colliders.md) | Which to control for and which never to |
| 12 | [Placebo Tests](Module_12_Placebo_Tests.md) | Does the analysis produce effects out of nothing? |

## Part IV. What to report

| # | Module | The question it answers |
|---|---|---|
| 13 | [Spillover and Contamination](Module_13_Spillover_And_Contamination.md) | The one bias that hides a real effect |
| 14 | [How Big an Effect Could You Have Detected?](Module_14_How_Big_An_Effect.md) | The number every null result needs |
| 15 | [Sensitivity](Module_15_Sensitivity.md) | How wrong would the assumption have to be? |
| 16 | [Writing Up a Causal Claim](Module_16_Writing_Up_A_Causal_Claim.md) | The thing that leaves the building |

---

## Results this level establishes

| Finding | Module |
|---|---|
| The additive and proportional scales give 15.0 and 12.5 percent from the same four cells | 5 |
| Ten percent of agency months have zero use of force, so a log rate regression drops the smallest agencies | 6 |
| The parallel trends test finds a 2 percent a year violation only **16 percent** of the time | 7 |
| Agency specific trends turn a real 12 percent effect into a null result, because the treated period is 0.82 correlated with time | 8 |
| These agencies' levels correlate 0.94 across two year windows and **−0.04** across adjacent months | 9 |
| A program that does not exist reports −9.2 percent when given to the worst three agencies | 10 |
| Conditioning on a collider flips a correlation from +0.66 to **−0.37** | 11 |
| A randomisation test puts the estimate beyond 97 percent of 400 random reassignments | 12 |
| One contaminated comparison agency costs up to 4 percentage points, in proportion to its size | 13 |
| Quadrupling the treated group buys **one** percentage point of detectable effect | 14 |
| A hidden trend of 3.4 percent a year would erase the estimate, and the pre period cannot rule it out | 15 |

## Running the notebooks

Each notebook reads the CSV files in [Data/](../../Data/) directly and runs end to end in a few minutes. Open them in Colab from the badge in each module, or locally:

```
cd Notebooks
jupyter lab
```

## Reproducing the figures

```
cd Figures
python make_figures.py
```

---

## Where to go next

| If you want | Go to |
|---|---|
| The ideas without the code | the [Beginner series](../Beginner/) |
| Identification, staggered adoption, few clusters, partial identification | the [Advanced series](../Advanced/) |
| Trends, seasonality and what a rate is | the [Time Series series](../../Time_Series/) |
| What was planted in the teaching data | [Data/GROUND_TRUTH.md](../../Data/GROUND_TRUTH.md) |

---

*All examples use synthetic data created for teaching. They do not represent any real jurisdiction, agency, officer, or incident.*

*Questions, corrections, or suggestions: yin.zhang@wsu.edu*
