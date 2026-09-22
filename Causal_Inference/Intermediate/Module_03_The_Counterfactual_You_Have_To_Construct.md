# Module 3: The Counterfactual You Have to Construct

> **Developed by Yin Zhang, PhD**, Assistant Professor, Department of Mathematics and Statistics, Washington State University

## The Question

Y(0) has to be built from something. What are the options, how much does the answer depend on which one is chosen, and what does it mean when two of them disagree?

## The Idea in Plain Language

Three sources are available for a counterfactual: the agency's own past, the agency's own trajectory, and other agencies. They use different information and they do not have to agree. When they do agree, that is worth reporting. When they disagree, at least one is wrong and it is worth finding out which.

## The Method

| Construction | Y(0) is | It assumes |
|---|---|---|
| **Own past, unchanged** | the before period rate | nothing changed in four years |
| **Own pre program trend** | the pre period trend extrapolated forward | whatever was happening kept happening |
| **Comparison agencies' path** | the before rate scaled by the comparison group's change | the two groups would have moved together |

Only the third uses information from outside the agency, which is its advantage and the reason it is the default.

## Worked Example

Stonewick alone, after the program. The recorded rate is **2.58**.

![A horizontal chart showing one vertical line at the recorded value of 2.58 and three horizontal bars reaching out to three different constructed counterfactuals: 3.53 from its own past, 2.81 from its own pre program trend, and 2.84 from the comparison agencies. The implied effects are minus 26.9, minus 8.2 and minus 9.2 percent](Figures/fig_03_three_counterfactuals.png)

| Counterfactual | Y(0) | Implied effect |
|---|---|---|
| Its own past, assumed unchanged | 3.53 | **−26.9%** |
| Its own pre program trend, extrapolated | 2.81 | −8.2% |
| The comparison agencies' path | 2.84 | −9.2% |
| **The truth** | | **−12.0%** |

Same records, three answers. The first is wrong by more than a factor of two, and predictably so: assuming nothing would have changed credits the program with four years of statewide decline.

The other two land at 8 and 9 percent and are still not right. **That is not a failure of the counterfactual.** One agency does not contain enough information to resolve a 12 percent effect against any comparison. Pooling four agencies moves them to 13.2 and 12.5.

### When two constructions disagree

| Agency | From comparison | From own trend | Gap |
|---|---|---|---|
| Stonewick | −9.2% | −8.2% | 1.1 |
| Millgate | −15.5% | −18.4% | 3.0 |
| Tarnbridge | −17.2% | −23.2% | 6.1 |
| **Pinecrest** | **−21.0%** | **−12.2%** | **8.8** |

Pinecrest disagrees by nine points, more than twice any other agency, and there is a reason that is in the data dictionary rather than the numbers. **Pinecrest is the campus police agency.** Its activity follows the academic calendar, peaking in September and collapsing in June and July, while every other agency in the state peaks in summer.

Assuming Pinecrest would have moved with the others is exactly the assumption to doubt, and the gap flagged it before anyone looked it up.

## Do It Yourself

> 📓 **Notebook:** [Module_03_The_Counterfactual_You_Have_To_Construct.ipynb](Notebooks/Module_03_The_Counterfactual_You_Have_To_Construct.ipynb)
> [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/YinZhangCISER/Public-Safety-Statistics-Tutorials/blob/main/Causal_Inference/Intermediate/Notebooks/Module_03_The_Counterfactual_You_Have_To_Construct.ipynb)
> About 25 minutes.

- Builds all three counterfactuals for one agency, then for four pooled
- Ranks the trained agencies by how far the two defensible constructions disagree
- The exercise builds a fourth counterfactual from size matched agencies

## Pitfalls

| What goes wrong | What it looks like | What to do |
|---|---|---|
| Using the own past construction | an estimate two to three times too large | never; report it only as a description |
| Treating agreement as verification | "both methods confirm the effect" | say the two agree, not that either is proved |
| Ignoring a large disagreement | one agency quietly driving the average | look up what is unusual about it |
| Extrapolating a pre trend too far | a counterfactual with no data behind it | keep the after period short relative to the before |
| Matching on a variable that does not drive the trend | a noisier estimate for no gain | Module 4 |

## Check Your Understanding

<details>
<summary><b>1.</b> Pooling moves the own trend construction from −8.2 to −13.2 percent. Why does pooling help so much?</summary>

Because each agency's own trend is estimated from its own noisy history, and four such estimates average out much of that noise. At Stonewick alone the pre period slope is fitted to 54 months of one agency's counts; pooled, it rests on four times as much data. The construction did not change, only the amount of evidence behind it.
</details>

<details>
<summary><b>2.</b> Pinecrest's own trend construction gives −12.2 percent, exactly the truth. Does that make it the better construction?</summary>

No, and this is the trap. Landing on the right answer once is not evidence about a method, because in real work the right answer is unknown. What is evidence is the **reason** the two constructions disagree, which is a documented feature of the agency. The lesson is to investigate large gaps, not to prefer whichever construction produced a number you like.
</details>

<details>
<summary><b>3.</b> An agency has only two years of history before the program. Which construction should be used?</summary>

The comparison group, and the own trend construction should be treated with suspicion. Two years is barely enough to separate a trend from seasonality, so the extrapolation would carry large uncertainty that the point estimate hides. The comparison group construction does not need the agency's own history at all, which is another reason it is the default.
</details>

## Key Takeaway

Name the counterfactual, report the estimate under the most credible alternative as well, and investigate any agency where the two disagree sharply.

---

| | |
|---|---|
| **Previous** | [Module 2: Potential Outcomes Without the Algebra](Module_02_Potential_Outcomes_Without_The_Algebra.md) |
| **Next** | [Module 4: Building a Comparison Group](Module_04_Building_A_Comparison_Group.md) |
| **Builds on** | [Module 2](Module_02_Potential_Outcomes_Without_The_Algebra.md), Beginner [Topic 3](../Beginner/Topic_03_The_World_You_Cannot_See.md) |
| **Used again in** | [Module 4](Module_04_Building_A_Comparison_Group.md), and every estimate in this series |

*This module is part of a series developed for the Washington Data Exchange for Public Safety (WADEPS) through the Center for Interdisciplinary Statistical Education and Research (CISER) at Washington State University. Version 1.0, September 2026. Questions, errors, or suggestions: yin.zhang@wsu.edu*

*All examples use synthetic data created for teaching. They do not represent any real jurisdiction, agency, officer, or incident. See [Data/DATA_DICTIONARY.md](../../Data/DATA_DICTIONARY.md).*
