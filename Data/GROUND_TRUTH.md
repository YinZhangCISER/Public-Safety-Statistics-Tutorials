# Ground Truth

**The answer key for the synthetic WADEPS teaching dataset**

*Developed by Yin Zhang, PhD, Assistant Professor, Data Analytics Program, Department of Mathematics and Statistics, Washington State University, for the Washington Data Exchange for Public Safety (WADEPS) through the Center for Interdisciplinary Statistical Education and Research (CISER).*

---

> **Instructors:** this page gives away the answers. If you are working through the exercises, come back after you have made your own estimate.

Real data never tells you whether your analysis was right. This dataset does. Eleven patterns were deliberately built into it, each with a known size, a known date, and a known cause. Every tutorial that estimates something can therefore be checked: did the method recover the number that was put there on purpose, and did the shortcut method get it wrong?

Running `python verify_ground_truth.py` re estimates all eleven from the published CSV files and reports PASS or FAIL against the values below.

---

## 1. A common secular trend

Every agency's use of force rate declines at a log slope of **0.050 per year**, which is about **4.9 percent per year**, throughout the whole period. One agency is the exception, see item 8.

*Why it is there:* so that a before and after comparison has something to be fooled by. Any program evaluated against its own past will appear to work, because everything was already improving.

*Where it is used:* Intermediate Modules 6 and 16, Advanced Modules 1 and 11, and the whole Causal Inference series.

## 2. Annual seasonality with a July peak

The use of force rate carries a cosine seasonal factor peaking in **July** with an amplitude of **0.20**, so July runs about 20 percent above the annual average and January about 20 percent below. Calls for service carry their own seasonal factors, which differ by incident type: offenses against persons peak hardest in July, property offenses in August, civil caretaking in January.

*Why it is there:* so that a month to month comparison is misleading and a year over year comparison is not.

*Where it is used:* Beginner Topics 8 and 18, Intermediate Modules 5, 7 and 9, Advanced Modules 5 and 8.

## 3. An agency on the academic calendar

**A010, Pinecrest State University Police**, ignores the weather. Its calls peak in **September and October**, fall off through spring, and collapse in **June and July** when the campus empties.

*Why it is there:* so that "summer is the busy season" is visibly false for at least one agency, and so that pooling agencies with different seasonal shapes has a visible cost.

*Where it is used:* Intermediate Modules 5 and 12, Advanced Module 10.

## 4. One documented outlier month

**A002, Tarnbridge Police Department, June 2021.** A week of civil unrest multiplied that month's use of force by **4.0** and its public order calls for service by **2.5**. The month sits roughly eight standard deviations above the agency's own median.

*Why it is there:* so that averages computed with and without it tell different stories, and so that a model fitted without handling it produces visibly bad residuals.

*Where it is used:* Beginner Topics 11 and 12, Intermediate Modules 8 and 13, Advanced Modules 3 and 12.

## 5. A three month reporting gap

**A009, Prairie County Sheriff's Office** submitted nothing for **March, April and May 2022** during a records management system migration. Those rows are **absent from every file**, not present with zero or blank values.

*Why it is there:* so that a reader learns the difference between a zero and a missing value the hard way, and so that any method requiring a regular time index fails loudly until the calendar is repaired.

*Where it is used:* Beginner Topic 6, Intermediate Modules 2 and 8, Advanced Module 1.

## 6. A classification definition change

**A003, Havenbrook Police Department**, beginning **January 2023**, began routing 30 percent of the calls it used to label `Other` into `Public Order Offense`. The share of public order calls jumps by about 55 percent, the `Other` share drops by about 29 percent, and **total call volume does not change at all**.

*Why it is there:* so that a category level series shows a dramatic break with no real world cause, and so that checking the total is shown to be the diagnostic that catches it.

*Where it is used:* Beginner Topic 19, Intermediate Module 1, Advanced Module 12.

## 7. Two provisional months

**May and June 2026** are incomplete. Records are still being entered, so counts are thinned to about **72 percent** and **45 percent** of what they will eventually be. The `provisional` flag in `agency_monthly.csv` marks them.

*Why it is there:* so that the most recent point on every chart looks like a sudden improvement, and so that every tutorial has to drop it before fitting or forecasting.

*Where it is used:* Beginner Topic 19, Intermediate Modules 2 and 13, Advanced Modules 3 and 14.

## 8. One agency with a different pre existing trend

**A007, Summit County Sheriff's Office**, declines at a log slope of **0.130 per year**, about **12.2 percent per year**, rather than the 4.9 percent everyone else follows. It began an aggressive internal reform in 2019, before the program studied below.

*Why it is there:* this is the parallel trends violation. A007 adopted the training program, so leaving it in a difference in differences comparison inflates the estimated effect. The pre period trend test is what catches it.

*Where it is used:* Advanced Module 11, Causal Inference Intermediate and Advanced series.

## 9. A policy intervention with a known effect and a known lag

A **de escalation training program** started in **July 2023** at five agencies: **A001, A002, A004, A007 and A010**.

| Fact | Value |
|---|---|
| True effect once fully in place | **a 12 percent reduction** in the use of force rate |
| Phase in | 0 percent in month 0, then 25, 58, 83, and 100 percent of full effect |
| Fully in place from | **November 2023** |
| Acts on | the rate per arrest, not the raw count |

**The program was not assigned at random.** The five agencies with the highest baseline use of force rates were selected. Treated agencies therefore sit above the controls in level, before the program does anything.

*Why it is there:* this is the central teaching example of the whole repository. A naive before and after comparison on the treated agencies alone returns roughly a 30 percent reduction, two and a half times the truth, because it absorbs the secular decline of item 1. A difference in differences estimate that excludes A007 recovers the 12 percent.

*Where it is used:* Beginner Topic 15, Intermediate Module 16, Advanced Modules 11 and 13, and the entire Causal Inference series.

## 10. Two agencies too small to analyze alone

**A006, Orrindale Police Department** has 8 sworn officers and averages well under one use of force incident per month, with a large share of months at zero. **A011, Dunmoor Tribal Police** has 18. Their monthly rates swing wildly for no reason other than sampling noise.

*Why it is there:* so that "this agency's rate tripled" can be shown to mean "it went from one incident to three", and so that rare event methods have something to be necessary for.

*Where it is used:* Intermediate Module 4, Advanced Modules 2 and 9.

## 11. Incomplete call for service coverage

**A006 and A011** are marked `Partial` in `cfs_data_submitted`, mirroring the real WADEPS finding that smaller and more rural agencies are the most likely to have gaps in call data.

*Why it is there:* so that peer comparison exercises have to cope with a missing denominator, exactly as the real comparable agencies framework does.

*Where it is used:* Intermediate Module 12.

---

## What is not planted

Everything else is sampling noise. Calls for service, arrests and use of force counts are drawn from negative binomial distributions around the means implied by the patterns above. If you find a pattern that is not on this list, you have found noise, and noticing that is itself the lesson of Beginner Topic 10.

## A note on the random seed

The generator is seeded so that results are identical on every machine. The specific seed was chosen from a scan of candidate seeds so that the planted effects are recovered cleanly rather than obscured by an unlucky draw. That is a teaching decision, not a statistical one. With a different seed every pattern above is still present in expectation, but a given estimate may land further from its target. Advanced Module 3 makes exactly this point about the difference between an estimate and the thing it estimates.

---

*Questions, corrections, or suggestions: yin.zhang@wsu.edu*
