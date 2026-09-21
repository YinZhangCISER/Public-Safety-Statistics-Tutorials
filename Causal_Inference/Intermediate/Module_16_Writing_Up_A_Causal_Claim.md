# Module 16: Writing Up a Causal Claim

> **Developed by Yin Zhang, PhD**, Assistant Professor, Department of Mathematics and Statistics, Washington State University

## The Question

Fifteen modules produced one number and a dozen checks. What does the thing that leaves the building actually say?

## The Idea in Plain Language

The report is not the estimate. It is the estimate, the comparison it was measured against, everything that was excluded, what the design could have detected, and where the result is fragile. Each of those is one sentence, and leaving any of them out changes what a reader will conclude.

## Every Estimate This Series Produced

![A horizontal bar chart of four estimates of one 12 percent effect: before and after at 33.1 percent, agency effects with no time term at 29.5, difference in differences with all five trained agencies at 17.0, and the checked difference in differences at 12.6, against a dashed line at the true 12 percent. Each row carries a short note saying what it absorbed](Figures/fig_16_writing_up.png)

| Analysis | Estimate | Why it is wrong |
|---|---|---|
| Before and after, the five trained agencies | −33.1% | no comparison group |
| Agency effects, nothing absorbing time | −29.5% | the settled term picks up the statewide decline |
| Difference in differences, all five trained | −17.0% | one agency was on its own pre trend |
| **Difference in differences, checked** | **−12.6%** | |
| **The truth** | **−12.0%** | |

**Every one was computed correctly.** They differ only in which sources of variation the analyst accounted for.

## The Checks, Assembled

| | |
|---|---|
| Estimate | −12.6% [−17.9, −6.9] |
| Smallest detectable effect | 8.6% |
| Pre program trend difference | −0.70% a year [−3.31, +1.97] |
| Placebo on the denominator, arrests | +0.08% [−0.94, +1.10] |
| Randomisation test | beyond 97 percent of 400 reassignments |
| Agencies excluded | 1 treated, for a pre trend of −12.0% a year |
| Months excluded | 1, documented civil unrest |
| Hidden trend needed to zero the estimate | about −3.4% a year |

## The Paragraph

> Across 11 agencies and 88 months, use of force at the four agencies that adopted de escalation training ran 12.6 percent below the comparison agencies over the 30 months after the training was fully in place, 95 percent interval from 6.9 to 17.9 percent below. Rates are incidents per arrest.
>
> One treated agency was excluded because its use of force rate was already falling at 12.0 percent a year before the program began, against 4 to 6 percent elsewhere; including it raises the estimate to 17.0 percent. One month of documented civil unrest was excluded. The pre program trends of the two groups differ by 0.70 percent a year, interval from 3.31 below to 1.97 above.
>
> The design could have detected a reduction of 8.6 percent or larger. Arrests, the denominator, were unaffected (+0.08 percent), so the result is not an artefact of changing arrest practice. A randomisation test over 400 reassignments of the treatment label places the estimate beyond 97 percent of what the procedure produces from chance alone.
>
> The estimate is robust to contamination of the comparison group but not to an unmeasured trend difference: a hidden trend of 3.4 percent a year favouring the treated agencies would eliminate it, and the pre period cannot exclude a difference that large. The agencies were selected for the program on the basis of their pre program use of force rate, which is this study's outcome.

Around 230 words. **What it does not contain**: the word "caused", any claim about agencies outside the study, and any decimal place the interval does not support.

## The One Sentence Version

A press release will shorten whatever it is given, so write the shortest defensible version yourself.

> **Defensible:** "Use of force fell 13 percent more at the four agencies that adopted the training than at comparable agencies over the same period, with a range of 7 to 18 percent."
>
> **Not defensible:** "The training cut use of force by 13 percent."

The difference is one verb and the absence of a comparison.

## The Checklist

**Before estimating**
- [ ] The comparison group rule is written down
- [ ] The intervention date is fixed
- [ ] The smallest detectable effect is computed and given to whoever commissioned the work

**Before believing the estimate**
- [ ] Pre program trends, agency by agency, with intervals
- [ ] The estimate under every defensible comparison group rule
- [ ] A leave one out check if one agency dominates
- [ ] Placebo dates, placebo outcomes, placebo groups
- [ ] Whether the program moved the denominator

**Before writing**
- [ ] Every exclusion listed with its reason and its cost
- [ ] The interval, not just the estimate
- [ ] How recipients were selected
- [ ] A sensitivity result for the main assumption
- [ ] Nothing causal that the design cannot support

## Do It Yourself

> 📓 **Notebook:** [Module_16_Writing_Up_A_Causal_Claim.ipynb](Notebooks/Module_16_Writing_Up_A_Causal_Claim.ipynb)
> [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/OWNER/REPO/blob/main/Causal_Inference/Intermediate/Notebooks/Module_16_Writing_Up_A_Causal_Claim.ipynb)
> About 25 minutes.

- Reproduces every estimate the series produced, in one table
- Assembles all the checks into one block
- Generates the paragraph from the fitted numbers rather than by hand
- The exercise writes the one sentence version

## Pitfalls

| What goes wrong | What it looks like | What to do |
|---|---|---|
| Reporting the estimate alone | a number with no way to judge it | the interval, always |
| Burying the exclusions | an unreproducible result | list each with its cost |
| Omitting the detectable effect | a null result read as no effect | one sentence |
| Omitting the selection mechanism | the most damaging fact discovered by a reviewer | put it in the same paragraph as the estimate |
| Writing "caused" | a claim the design cannot support | say what was compared to what |

## Check Your Understanding

<details>
<summary><b>1.</b> The paragraph discloses that agencies were selected on the outcome, which invites a reader to discount the result. Why include it?</summary>

Because a reader who discovers it independently discounts the whole report rather than one paragraph. Disclosure also lets you state the mitigation in the same breath: the pre trend check was run and the groups are consistent with parallel trends. A fact that is going to come out is worth presenting with its answer attached.
</details>

<details>
<summary><b>2.</b> Why does the one sentence version round 12.6 to 13?</summary>

Because the interval runs from 7 to 18 and a tenth of a point is not supported by it. Carrying the decimal into a press sentence implies a precision the study does not have, and a reader who sees 12.6 will treat it as a measurement. Round to the precision the interval supports, which here is the nearest percentage point at best.
</details>

<details>
<summary><b>3.</b> The report says the result is not robust to an unmeasured trend difference. Does that make the study worthless?</summary>

No, and stating the fragility is what makes it usable. The study establishes that the trained agencies improved substantially more than comparable agencies over the same period, that the difference is not explained by the observable characteristics recorded, and that it would take a specific unobserved violation of a specific size to overturn it. A reader can weigh that against what else they know. A report that omitted the limitation would offer them less, not more.
</details>

## Key Takeaway

Write the estimate, the comparison, the exclusions, the detectable effect, and the fragility. Then write the one sentence version yourself before somebody else does.

---

## Where This Goes Next

This level built one estimate and checked it. The [Advanced series](../Advanced/) takes up what these checks leave open: what identification means formally, why the designs that were not available here are not available, what happens when adoption is staggered, how to do inference with a handful of clusters, and how far partial identification can take an answer when the assumptions cannot be defended.

---

| | |
|---|---|
| **Previous** | [Module 15: Sensitivity](Module_15_Sensitivity.md) |
| **Next** | the [Advanced series](../Advanced/) |
| **Builds on** | every module in this series |
| **Used again in** | every evaluation you write |

$FOOT
