# Causal Inference, Advanced Level

### Identification first, estimation second, and knowing which designs the data cannot support

*Developed by Yin Zhang, PhD, Assistant Professor, Data Analytics Program, Department of Mathematics and Statistics, Washington State University, for the Washington Data Exchange for Public Safety (WADEPS) through the Center for Interdisciplinary Statistical Education and Research (CISER).*

For agency data analysts, graduate students outside statistics, and early career researchers. Sixteen modules with complete Python notebooks.

Notation is used freely, proofs are not. The emphasis throughout is on **what a design assumes, how the assumption is checked, and what the output looks like when the design should not have been run at all.**

> **Publication status:** complete. All sixteen modules are published, each with a notebook.

---

## Seven designs, one 12 percent effect

| Design | Reported | The diagnostic that condemns it |
|---|---|---|
| Before and after | −33.1% | no comparison group |
| Regression discontinuity | +30.9% | two agencies within 0.30 of the cutoff |
| Instrumental variables | −22.8% | strongest first stage F is 1.60 |
| Synthetic control | +11.3% to −25.1% | pre period fit error 25 to 48 percent |
| Propensity score | none | 4 percent overlap, 2 units survive trimming |
| Difference in differences, all five | −17.0% | one agency on its own pre trend |
| **Difference in differences, checked** | **−12.6%** | |
| **The truth** | **−12.0%** | |

**Four of the seven had no business being run, and each says so in a single diagnostic that requires no fitting.**

---

## Part I. Identification

| # | Module | The question it answers |
|---|---|---|
| 1 | [Potential Outcomes, Estimands, and What You Are Actually Estimating](Module_01_Potential_Outcomes_And_Estimands.md) | Which quantity is the target? |
| 2 | [Directed Acyclic Graphs and the Backdoor Criterion](Module_02_DAGs_And_The_Backdoor_Criterion.md) | What to condition on, decided before fitting |
| 3 | [Identification Before Estimation](Module_03_Identification_Before_Estimation.md) | What has to be assumed, and what failure looks like |
| 4 | [Selection Mechanisms and What They Do to an Estimate](Module_04_Selection_Mechanisms.md) | Does selection bias have one direction? |

## Part II. Difference in differences and its relatives

| # | Module | The question it answers |
|---|---|---|
| 5 | [Two Way Fixed Effects Done Properly](Module_05_Two_Way_Fixed_Effects.md) | Is "the TWFE estimate" one number? |
| 6 | [Event Studies and Pre Trend Testing](Module_06_Event_Studies_And_Pre_Trend_Testing.md) | What is the plot evidence of? |
| 7 | [Staggered Adoption and the Negative Weights Problem](Module_07_Staggered_Adoption.md) | How much is negative weights, and how much is something else? |
| 8 | [Synthetic Control](Module_08_Synthetic_Control.md) | What has to be true for the picture to mean anything? |
| 9 | [Honest Inference with Few Clusters](Module_09_Honest_Inference_With_Few_Clusters.md) | Eleven agencies do not supply asymptotics. What is the interval? |

## Part III. Designs this data cannot support

Each module teaches the method in full, applies it, and reads the diagnostic that rules it out. **Knowing when not to reach for a design is the point.**

| # | Module | What the data says |
|---|---|---|
| 10 | [Propensity Scores and the Overlap Assumption](Module_10_Propensity_Scores.md) | 4 percent overlap, and separation is partly mechanical at n = 12 |
| 11 | [Instrumental Variables](Module_11_Instrumental_Variables.md) | strongest first stage F is 1.60, and that candidate fails exclusion |
| 12 | [Regression Discontinuity](Module_12_Regression_Discontinuity.md) | two agencies near the cutoff, and the estimate has the wrong sign |

## Part IV. What survives

| # | Module | The question it answers |
|---|---|---|
| 13 | [Placebo, Permutation and Falsification Tests](Module_13_Placebo_Permutation_And_Falsification.md) | Which null? |
| 14 | [Sensitivity Analysis and Partial Identification](Module_14_Sensitivity_And_Partial_Identification.md) | How badly would the assumption have to fail? |
| 15 | [Heterogeneous Effects, and the Temptation to Find Them](Module_15_Heterogeneous_Effects.md) | Did it work better somewhere? |
| 16 | [The Causal Claim, What You Can Defend](Module_16_The_Causal_Claim.md) | What survives, and how is it written? |

---

## Results this level establishes

| Finding | Module |
|---|---|
| Two weightings of the same ATT differ by 3 points; the ATE is not identified | 1 |
| Conditioning on time alone gets the sign wrong, at +17.8 percent | 2 |
| An unidentified specification has a **narrower** interval and is wrong by 17 points | 3 |
| Selection on the level biases by +3.01, on the trend by −1.94, at random by −0.11 | 4 |
| Poisson and linear TWFE are 5 points apart because Stonewick is 61 percent of the incidents | 5 |
| The pre trend test finds a 2 percent a year violation **16 percent** of the time | 6 |
| Staggered adoption costs 3.79 points from heterogeneity and 3.73 from non parallel trends, separately | 7 |
| Four of five treated agencies sit above every synthetic control donor | 8 |
| Model and cluster robust intervals agree to four decimals on 11 clusters, which is the warning | 9 |
| Four columns of pure noise separate these 12 units in 6 percent of draws | 10 |
| The strongest candidate instrument is also the one failing exclusion | 11 |
| Regression discontinuity returns the **wrong sign** at every bandwidth, significantly | 12 |
| The same estimate gives p = 0.25 or p = 0.030 depending on the placebo null | 13 |
| A worst case bound built on the wrong support **excludes the truth** | 14 |
| Five subgroup splits produce gaps of 3 to 8 points against a constant effect | 15 |

## Running the notebooks

Each notebook reads the CSV files in [Data/](../../Data/) directly and runs end to end in a few minutes. Several run simulations and take longer. Open them in Colab from the badge in each module, or locally:

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
| One estimate, built and checked | the [Intermediate series](../Intermediate/) |
| Trends, seasonality, counts and forecasting | the [Time Series series](../../Time_Series/) |
| What was planted in the teaching data | [Data/GROUND_TRUTH.md](../../Data/GROUND_TRUTH.md) |

---

*All examples use synthetic data created for teaching. They do not represent any real jurisdiction, agency, officer, or incident.*

*Questions, corrections, or suggestions: yin.zhang@wsu.edu*
