# Topic 20: Questions to Ask Before You Believe a Program Worked

> **Developed by Yin Zhang, PhD**, Assistant Professor, Department of Mathematics and Statistics, Washington State University

**The question this module answers:** *All of it, on one page.*

---

## The Core Concept

Nineteen topics reduce to six questions. None of them requires any mathematics, all of them can be asked in a meeting, and each one has stopped a bad claim.

![Six boxes in a row connected by arrows, numbered one to six. What would have happened otherwise, from Topic 3. Who did not get it and what happened to them, from Topic 6. Were the two groups moving together before, from Topic 9. How were the recipients chosen, from Topic 13. Could the comparison group have been affected too, from Topic 10. How long did the study wait, from Topic 18](Figures/fig_20_questions_to_ask.png)

## The Six Questions

**1. What would have happened otherwise?**
Every effect is a gap against a world that did not happen. If nobody can describe that world in a sentence, there is no causal claim on the table yet. [Topic 3](Topic_03_The_World_You_Cannot_See.md)

**2. Who did not get it, and what happened to them?**
Without a comparison group the answer will be two to three times too large, because everything was already improving. [Topic 6](Topic_06_Comparing_Yourself_To_Someone_Else.md)

**3. Were the two groups moving together before?**
One picture of the years before the program. This is the cheapest check in the series and it caught five percentage points of error in the worked example. [Topic 9](Topic_09_Were_They_Moving_Together_Before.md)

**4. How were the recipients chosen?**
If the rule mentions the outcome, an apparent effect was guaranteed before the program began. [Topic 13](Topic_13_Picking_The_Winners.md)

**5. Could the comparison group have been affected too?**
The only bias that hides a real effect, and the only one that cannot be found in the data. You have to ask the agencies. [Topic 10](Topic_10_When_The_Comparison_Group_Moves_Too.md)

**6. How long did the study wait?**
"No significant effect" after eight months means there is not enough evidence yet. [Topic 18](Topic_18_How_Long_Do_You_Have_To_Wait.md)

## What the Six Questions Did Here

The worked example ran through this series with a known answer of **12 percent**.

| What was asked | What the estimate became |
|---|---|
| Nothing; just before and after | −33.1% |
| Question 2: who did not get it | −16.9% |
| Question 3: were they moving together before | **−12.5%** |
| **The truth** | **−12.0%** |

Questions 4, 5 and 6 did not change this estimate. They established that it could be trusted: the selection rule explains why the before and after number was so far out, no comparison agency was contaminated, and thirty months was long enough.

**A question that changes nothing is not a wasted question.** It is the difference between a number that survived scrutiny and one that was never examined.

## What To Watch For

- **Ask them in order.** Each depends on the one before. There is no point asking about contamination before establishing that a comparison group exists.
- **"We do not know" is an acceptable answer.** "We did not ask" is not.
- **The answers belong in the report**, not in the analyst's head. A reader cannot check what was not written down.
- **A claim that survives all six is still not proof.** It is a defensible estimate with a stated uncertainty, which is the most that observational data offers.

## 💡 The Insight

The six questions are not a test the analysis has to pass. They are the report: what was compared, to whom, why those, who else changed, and how long anyone waited.

## Check Your Understanding

<details>
<summary><b>1.</b> Which question would have caught the largest single error in the worked example?</summary>

Question 2. Going from no comparison group to a comparison group moved the estimate from 33.1 percent to 16.9, about sixteen percentage points. Question 3 moved it a further four. The first comparison group is always the biggest improvement available, and it is usually the cheapest.
</details>

<details>
<summary><b>2.</b> An evaluation answers all six well and reports a 12 percent reduction with an interval from 7 to 18. A council member asks whether the program will work in their city. What is the honest answer?</summary>

That the study cannot say. It measured five agencies that had the highest use of force rates in the state, and an effect at the extreme is not necessarily an effect in the middle. This is the fifth rung of the ladder in [Topic 15](Topic_15_Correlation_Causation_And_The_Sentences_In_Between.md), and reaching it needs studies in more than one place. The estimate is good evidence that the program can work somewhere, which is worth saying plainly and is not the same claim.
</details>

<details>
<summary><b>3.</b> Someone objects that these questions are a recipe for never believing anything. Is that fair?</summary>

No, and it is worth answering directly. The questions produced a usable number here: 12.5 percent against a truth of 12.0, from observational records with no randomisation. What they rule out is not belief but **unexamined** belief. The alternative to asking them is not more confident conclusions; it is conclusions that are wrong by a factor of three and nobody notices.
</details>

## Key Takeaway

Print the six questions. Ask them of every evaluation that crosses your desk, including your own.

---

## Where This Goes Next

This level covered the ideas. The [Intermediate series](../Intermediate/) does the arithmetic and puts it in notebooks: building a comparison group properly, computing a difference in differences and testing its assumption, measuring regression to the mean, running placebo tests, and working out what an effect would have to be for a study to detect it.

For the machinery underneath the outcome measurements themselves, the [Time Series series](../../Time_Series/) covers trends, seasonality, and what a rate is.

---

| | |
|---|---|
| **Previous** | [Topic 19: Reading a Causal Claim in the News](Topic_19_Reading_A_Causal_Claim.md) |
| **Next** | the [Intermediate series](../Intermediate/) |
| **Builds on** | every topic in this series |
| **Used again in** | every evaluation you read |

*This module is part of a series developed for the Washington Data Exchange for Public Safety (WADEPS) through the Center for Interdisciplinary Statistical Education and Research (CISER) at Washington State University. Version 1.0, September 2026. Questions, errors, or suggestions: yin.zhang@wsu.edu*

*All examples use synthetic data created for teaching. They do not represent any real jurisdiction, agency, officer, or incident. See [Data/DATA_DICTIONARY.md](../../Data/DATA_DICTIONARY.md).*
