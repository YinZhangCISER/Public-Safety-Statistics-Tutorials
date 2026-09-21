# Topic 19: Reading a Causal Claim in the News

> **Developed by Yin Zhang, PhD**, Assistant Professor, Department of Mathematics and Statistics, Washington State University

**The question this module answers:** *A headline says a program worked. Without the underlying data, how much can you tell?*

---

## The Core Concept

More than you would expect. A headline and two paragraphs usually reveal which comparison was made, and the comparison is most of the answer.

The reading is fast once you know what to look for. Three questions, in order.

1. **Compared to what?** The agency's own past, other agencies, or nothing stated.
2. **Who was chosen, and how?** Volunteers, the worst performers, everybody.
3. **Over how long?** Six months, or three years.

## Why It Matters

The same true effect can produce headlines ranging from "no significant effect" to "down by a third", with nothing dishonest anywhere.

## The Example

Every one of these headlines is a fair summary of a correctly computed number from this dataset. The true effect is **12 percent**.

![A horizontal bar chart of five headlines with the number behind each. Use of force down a third at participating agencies is 33.1 percent, Stonewick cuts use of force by more than a quarter is 26.9, training linked to 17 percent reduction is 16.9, training cuts use of force by 12 percent is 12.5 and is marked in green, and study finds no significant effect of training is 5.7 percent. A dashed line marks the true 12 percent](Figures/fig_19_reading_a_claim.png)

| Headline | The number behind it | What was actually done |
|---|---|---|
| "Use of force down a third at participating agencies" | −33.1% | before and after, all five |
| "Stonewick cuts use of force by more than a quarter" | −26.9% | one agency, before and after |
| "Training linked to 17 percent reduction" | −16.9% | difference in differences |
| **"Training cuts use of force by 12 percent"** | **−12.5%** | **difference in differences, checked** |
| "Study finds no significant effect of training" | −5.7% | the same, written up 8 months in |

**None of these is a lie.** Each reports a number that a competent analyst computed correctly. They span from a third down to nothing, and only one of them is the answer.

The last one deserves attention. It is the same method as the fourth, run correctly, reported too early. A reader who sees only that headline concludes the program failed.

## What To Watch For

- **"Linked to" and "associated with" mean no comparison group was checked, or the author is hedging.** Both are worth a question.
- **A single agency in the headline means a single agency in the study.** One agency cannot resolve a 12 percent effect.
- **No comparison named means before and after.** Assume the number is roughly two to three times too big.
- **"No significant effect" needs an interval.** Without one there is no way to tell "it did not work" from "nobody waited long enough."
- **Round numbers in headlines hide intervals.** "12 percent" is an estimate with a range of 7 to 18 around it, and the range is what tells you how much to trust it.
- **Check who paid and who chose.** Neither settles anything, and both are worth knowing.

## 💡 The Insight

The headline number is rarely wrong. What is missing is the comparison it was measured against, and that is what decides what it means.

## Check Your Understanding

<details>
<summary><b>1.</b> "Crime fell 18 percent in the precinct after the new patrol strategy launched." What is your first question?</summary>

What happened in the other precincts over the same months. If they also fell 15 percent, the strategy is credited with 3 points, not 18. This one question is worth more than any other, and in most cases the reporter can obtain the answer with one phone call.
</details>

<details>
<summary><b>2.</b> Two headlines from the same study: "training cuts use of force 12 percent" and "training linked to 17 percent reduction." Which is better reporting?</summary>

The second is more cautious in its verb and less accurate in its number; the first is more assertive and closer to the truth. Neither is well reported, because neither gives the interval or names the comparison group. Caution in the verb is not a substitute for describing the design, and a reader cannot tell from either which one to believe.
</details>

<details>
<summary><b>3.</b> A press release reports a 33 percent reduction; an academic paper on the same program reports 12. Has someone made an error?</summary>

Probably not. They almost certainly used different comparisons: the press release against the agencies' own past, the paper against comparison agencies. Both numbers are correct arithmetic and they answer different questions. The useful response is to ask each what it was compared against, rather than to assume one party is being dishonest.
</details>

## Key Takeaway

Ask "compared to what" before anything else. If the answer is the agency's own past, divide your confidence accordingly.

---

| | |
|---|---|
| **Previous** | [Topic 18: How Long Do You Have to Wait?](Topic_18_How_Long_Do_You_Have_To_Wait.md) |
| **Next** | [Topic 20: Questions to Ask Before You Believe a Program Worked](Topic_20_Questions_To_Ask.md) |
| **Builds on** | [Topic 4](Topic_04_Before_And_After_Is_Not_Enough.md), [Topic 15](Topic_15_Correlation_Causation_And_The_Sentences_In_Between.md), [Topic 18](Topic_18_How_Long_Do_You_Have_To_Wait.md) |
| **Used again in** | [Topic 20](Topic_20_Questions_To_Ask.md) |

*This module is part of a series developed for the Washington Data Exchange for Public Safety (WADEPS) through the Center for Interdisciplinary Statistical Education and Research (CISER) at Washington State University. Version 1.0, September 2026. Questions, errors, or suggestions: yin.zhang@wsu.edu*

*All examples use synthetic data created for teaching. They do not represent any real jurisdiction, agency, officer, or incident. See [Data/DATA_DICTIONARY.md](../../Data/DATA_DICTIONARY.md).*
