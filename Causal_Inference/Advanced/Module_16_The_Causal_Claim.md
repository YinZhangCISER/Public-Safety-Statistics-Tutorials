# Module 16: The Causal Claim, What You Can Defend

> **Developed by Yin Zhang, PhD**, Assistant Professor, Department of Mathematics and Statistics, Washington State University

**The question this module answers:** *Fifteen modules and seven designs. What survives, and how is it written?*

---

## Every Design This Series Tried

![A horizontal bar chart of seven designs against a dashed line at the true 12 percent. Before and after reports 33.1 percent, regression discontinuity plus 30.9, instrumental variables minus 22.8, synthetic control minus 25.1, propensity score no defensible estimate, difference in differences with all five treated minus 17.0, and the checked version minus 12.6. Each row carries the diagnostic that condemns it](Figures/fig_a16_the_causal_claim.png)

| Design | Reported | The diagnostic that condemns it |
|---|---|---|
| Before and after | −33.1% | no comparison group |
| Regression discontinuity | **+30.9%** | two agencies within 0.30 of the cutoff |
| Instrumental variables | −22.8% | strongest first stage F is 1.60 |
| Synthetic control | +11.3% to −25.1% | pre period fit error 25 to 48 percent |
| Propensity score | none | 4 percent overlap, 2 units survive trimming |
| Difference in differences, all five | −17.0% | one agency on its own pre trend |
| **Difference in differences, checked** | **−12.6%** | |
| **The truth** | **−12.0%** | |

**Four of the seven had no business being run, and each says so in a single diagnostic that requires no fitting**: a count of units near a cutoff, a first stage F, a pre period fit error, an overlap range.

Every one of those four still produces a number with a standard error, and three produce a number with the wrong sign or double the truth.

## The Checks, Assembled

| | |
|---|---|
| Estimand | ATT, weighted by incidents, over 30 settled months |
| Estimate | −12.6%, model interval [−17.9, −6.9] |
| **Cluster bootstrap interval** | **[−20.9, −8.0]**, the one reported |
| Randomisation inference | p = 0.030 over 400 four agency reassignments |
| Smallest detectable effect | 8.6% |
| Pre trend difference | −0.70% a year [−3.31, +1.97] |
| Placebo on arrests | +0.08% [−0.94, +1.10] |
| Homogeneity across agencies | chi squared 4.56 on 3 df, p = 0.207 |
| Breakdown point, hidden trend | −3.4% a year, inside the pre period interval |
| Unobserved selection needed | 3.3 times the pull of the observed controls |
| Agencies excluded | 1 treated, pre trend of −12.0% a year |
| Months excluded | 1, documented civil unrest |

## The Claim

> **ESTIMAND.** The average treatment effect on the treated, weighted by incidents, over the 30 months after full implementation, for the four agencies retained. The average treatment effect is not identified: agencies were selected on the pre program outcome and the groups overlap over 4 percent of that variable's range.
>
> **IDENTIFICATION.** Parallel trends, no anticipation, no interference, and a stable outcome definition, with agency and calendar month fixed effects closing the two backdoor paths in the assumed graph. Four alternative designs were considered and ruled out on diagnostics stated in the appendix.
>
> **ESTIMATE.** Use of force ran 12.6 percent below the comparison agencies, cluster bootstrap interval from 20.9 to 8.0 percent below. A randomisation test over 400 reassignments places the estimate at p = 0.030. The design could have detected a reduction of 8.6 percent or larger.
>
> **WHAT WAS CHECKED.** Pre program trends differ by 0.70 percent a year, interval 1.97 above to 3.31 below. Arrests, the exposure measure, were unaffected. Placebo interventions at eight pre program dates all return intervals covering zero. Effects do not differ detectably across the four agencies, though the test would miss a spread below about thirty points.
>
> **WHERE IT IS FRAGILE.** A hidden trend difference of 3.4 percent a year would erase the estimate, and the pre period cannot exclude one of 3.31. Partial identification without the parallel trends assumption bounds the effect only within 75 percentage points. Unobserved selection would have to be 3.3 times as influential as everything observed.
>
> **WHAT IS NOT CLAIMED.** That the program would have this effect at agencies unlike these five; that the effect arrived abruptly rather than gradually; that it persists beyond 30 months; that any single agency's estimate is informative.

Five paragraphs. **The last two are what make the first three worth reading**, and they are the ones cut for length.

## The Ten Second Version

> "At the four agencies that adopted the training and were comparable beforehand, use of force fell about 13 percent more than at similar agencies over the next two and a half years, with a range of 8 to 21 percent. The agencies were chosen because their rates were already the highest in the state, which the analysis adjusted for but cannot rule out entirely."

Four things survive compression: **what it was compared to, the range, the window, and how the agencies were chosen.**

**The selection mechanism is the one people cut and should not.** It is the single fact most likely to change a reader's conclusion, it is short, and omitting it is the difference between a summary and a sales pitch.

## What This Level Establishes

| | Module |
|---|---|
| A design produces a number whether or not it is identified | 3 |
| Precision is not evidence of identification | 3 |
| The estimand depends on the link function | 5 |
| The pre trend test would miss the violation that mattered | 6 |
| Staggered adoption breaks the estimator two separate ways | 7 |
| Four designs fail here, each on one free diagnostic | 8, 10, 11, 12 |
| The model interval is too narrow at eleven clusters | 9 |
| The placebo null depends on how many units you pretend to treat | 13 |
| Worst case bounds built on the wrong support are wrong, not conservative | 14 |
| A subgroup search finds a gap when there is none | 15 |

**Ten of these are reasons to report less than the software offers.** That is what the level is for.

## Do It Yourself

> 📓 **Notebook:** [Module_16_The_Causal_Claim.ipynb](Notebooks/Module_16_The_Causal_Claim.ipynb)
> [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/YinZhangCISER/Public-Safety-Statistics-Tutorials/blob/main/Causal_Inference/Advanced/Notebooks/Module_16_The_Causal_Claim.ipynb)
> About 30 minutes.

The exercise writes the ten second version and lists what it had to drop.

## Where This Goes

Six series, three levels each, one dataset, one known answer of 12 percent.

The [Time Series series](../../Time_Series/) covers what the outcome is doing: trends, seasonality, counts, breaks, and forecasting. This series covers whether anything was done to it.

Both end in the same place: **an estimate, an interval, a list of what was checked, and a list of what is still open.** Anything shorter is a claim; that is a finding.

---

| | |
|---|---|
| **Previous** | [Module 15: Heterogeneous Effects, and the Temptation to Find Them](Module_15_Heterogeneous_Effects.md) |
| **Next** | the [Time Series series](../../Time_Series/), if you have not read it |
| **Builds on** | every module in this series |
| **Used again in** | every evaluation you sign |

$FOOT
