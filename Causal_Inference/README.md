# Causal Inference for Public Safety Data

*Developed by Yin Zhang, PhD, Assistant Professor, Data Analytics Program, Department of Mathematics and Statistics, Washington State University, for the Washington Data Exchange for Public Safety (WADEPS) through the Center for Interdisciplinary Statistical Education and Research (CISER).*

Time series tells you what happened and when. This series takes up the question every policy conversation eventually reaches: **did the program cause the change, or would it have happened anyway?**

The same three levels, the same synthetic WADEPS dataset, and the same de escalation training program with a true effect of exactly 12 percent, so that every method can be graded against the answer it is supposed to find.

| Level | Modules | For | Code | Status |
|---|---|---|---|---|
| [Beginner](Beginner/) | 20 | No statistics background at all | None | **Complete** |
| [Intermediate](Intermediate/) | 16 | Some background, wants to do it | Jupyter notebooks, gentle | **4 of 16 published** |
| [Advanced](Advanced/) | 16 | Fits models and reports results | Jupyter notebooks, complete | Planned |

---

## Beginner. Twenty topics, no mathematics

### What a causal claim is

| # | Topic |
|---|---|
| 1 | What Does "Caused" Mean? |
| 2 | The Question Behind Every Policy Question |
| 3 | The World You Cannot See |

### Why the obvious comparisons are not enough

| # | Topic |
|---|---|
| 4 | Before and After Is Not Enough |
| 5 | Things Were Already Changing |
| 6 | Comparing Yourself to Someone Else |
| 7 | What Makes a Good Comparison Group |
| 8 | Two Differences Are Better Than One |

### How a comparison breaks

| # | Topic |
|---|---|
| 9 | Were They Moving Together Before? |
| 10 | When the Comparison Group Moves Too |
| 11 | Why the Worst Performers Always Improve |
| 12 | Who Chose to Participate? |
| 13 | Picking the Winners Makes the Program Look Good |
| 14 | Confounding: The Third Thing |

### Deciding what to believe

| # | Topic |
|---|---|
| 15 | Correlation, Causation, and the Sentences In Between |
| 16 | Randomness Solves a Problem You Cannot Otherwise Solve |
| 17 | When You Cannot Randomize |
| 18 | How Long Do You Have to Wait? |
| 19 | Reading a Causal Claim in the News |
| 20 | Questions to Ask Before You Believe a Program Worked |

## Intermediate. Sixteen modules with notebooks

| # | Module |
|---|---|
| 1 | From "It Went Down" to "The Program Did It" |
| 2 | Potential Outcomes Without the Algebra |
| 3 | The Counterfactual You Have to Construct |
| 4 | Building a Comparison Group |
| 5 | Difference in Differences, by Hand |
| 6 | Difference in Differences, as a Regression |
| 7 | Testing Parallel Trends |
| 8 | When Parallel Trends Fails |
| 9 | Regression to the Mean |
| 10 | Selection on the Outcome |
| 11 | Confounders, Mediators and Colliders |
| 12 | Placebo Tests |
| 13 | Spillover and Contamination |
| 14 | How Big an Effect Could You Have Detected? |
| 15 | Sensitivity: How Wrong Would the Assumption Have to Be? |
| 16 | Writing Up a Causal Claim |

## Advanced. Sixteen modules with complete notebooks

### Part I. Identification

| # | Module |
|---|---|
| 1 | Potential Outcomes, Estimands, and What You Are Actually Estimating |
| 2 | Directed Acyclic Graphs and the Backdoor Criterion |
| 3 | Identification Before Estimation |
| 4 | Selection Mechanisms and What They Do to an Estimate |

### Part II. Difference in differences and its relatives

| # | Module |
|---|---|
| 5 | Two Way Fixed Effects Done Properly |
| 6 | Event Studies and Pre Trend Testing |
| 7 | Staggered Adoption and the Negative Weights Problem |
| 8 | Synthetic Control |
| 9 | Honest Inference with Few Clusters |

### Part III. Designs this data cannot support

Each of these three modules teaches the method in full, applies it, and then reads the diagnostic that says it does not apply here. Knowing when not to reach for a design is the point.

| # | Module | What the data says |
|---|---|---|
| 10 | Propensity Scores and the Overlap Assumption | perfect separation, no common support |
| 11 | Instrumental Variables | no instrument exists in these records |
| 12 | Regression Discontinuity | the selection rule is close to a cutoff, and close is not enough |

### Part IV. What survives

| # | Module |
|---|---|
| 13 | Placebo, Permutation and Falsification Tests |
| 14 | Sensitivity Analysis and Partial Identification |
| 15 | Heterogeneous Effects, and the Temptation to Find Them |
| 16 | The Causal Claim: What You Can Defend |

---

## What this series is graded against

Everything is estimated from `Data/`, whose eleven planted patterns are listed in [GROUND_TRUTH.md](../Data/GROUND_TRUTH.md). Four of them do most of the work here.

| Planted pattern | What it makes possible |
|---|---|
| A statewide decline of 4.9 percent a year | a before and after comparison that is fooled by it |
| A program with a true effect of exactly 12 percent | every estimate can be graded |
| Selection of the five agencies with the highest baseline rates | selection on the outcome, and regression to the mean |
| One agency already declining at 12 percent a year | a parallel trends violation with a known cause |

*All examples use synthetic data created for teaching. They do not represent any real jurisdiction, agency, officer, or incident.*

*Questions, corrections, or suggestions: yin.zhang@wsu.edu*
