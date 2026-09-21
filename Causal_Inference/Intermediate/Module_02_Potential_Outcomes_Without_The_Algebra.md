# Module 2: Potential Outcomes Without the Algebra

> **Developed by Yin Zhang, PhD**, Assistant Professor, Department of Mathematics and Statistics, Washington State University

## The Question

What exactly is being estimated, and which of the several things that could be called "the effect" does a comparison group actually give?

## The Idea in Plain Language

For every agency there are two versions of the same period: the one where it took the program and the one where it did not. Only one of them leaves records. Writing both down, and giving them names, turns several vague arguments into checkable statements.

## The Method

> **Y(1)** the rate given that the agency took the program
>
> **Y(0)** the rate had it not
>
> **the effect for that agency** Y(1) divided by Y(0)

**One of the two is always missing**, for every agency, always. That is the fundamental problem of causal inference, and every method in this series is a way of filling the missing column.

Three averages can be formed and they are not the same number.

| Name | Averaged over | The question it answers |
|---|---|---|
| **ATT** | the agencies that **took** the program | did it help the ones who got it |
| **ATU** | the agencies that **did not** | would it have helped the others |
| **ATE** | **all** agencies | would it help on average if everyone took it |

A difference in differences gives the **ATT** and is silent about the other two.

| Assumption | Consequence of failing |
|---|---|
| Y(0) for the treated would have moved like Y(0) for the comparison group | the estimate is biased by the difference |
| One agency's treatment does not change another's outcome | spillover, Module 13 |
| The program is the same thing at every agency | the average hides a mixture |

## Worked Example

Four trained agencies. Y(1) is what was recorded; Y(0) is constructed by applying the comparison group's change of 0.805 to each agency's own starting rate.

![A grouped bar chart for four agencies. Each has a grey bar for Y(0), the constructed counterfactual, and a blue bar for Y(1), what was recorded, with an orange arrow between them labelled with the percentage difference: Stonewick 9.2, Tarnbridge 17.2, Millgate 15.5 and Pinecrest 21.0 percent](Figures/fig_02_potential_outcomes.png)

| Agency | Y(1), observed | Y(0), constructed | Effect |
|---|---|---|---|
| Stonewick | 2.58 | 2.84 | −9.2% |
| Tarnbridge | 2.48 | 2.99 | −17.2% |
| Millgate | 2.44 | 2.89 | −15.5% |
| Pinecrest | 2.30 | 2.91 | −21.0% |

**The true effect is 12 percent at all four.** The spread from 9 to 21 percent is entirely noise, and reading a story into the ranking would be reading noise. Pooled, these four give an ATT of **−12.5 percent**.

### What is not identified

The ATU and the ATE are not available here, and saying so is a finding rather than an omission. The five trained agencies had the **highest use of force rates in the state**, and a program that helps at the top of the distribution may do nothing in the middle. Reporting the ATT as though it were the ATE is how a program gets rolled out statewide on evidence that does not cover statewide.

## Do It Yourself

> 📓 **Notebook:** [Module_02_Potential_Outcomes_Without_The_Algebra.ipynb](Notebooks/Module_02_Potential_Outcomes_Without_The_Algebra.ipynb)
> [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/OWNER/REPO/blob/main/Causal_Inference/Intermediate/Notebooks/Module_02_Potential_Outcomes_Without_The_Algebra.ipynb)
> About 20 minutes.

- Prints which potential outcome is observed for each agency and which is not
- Builds Y(0) from the comparison group and computes the per agency effects
- States which of the three estimands the design delivers
- The exercise builds Y(0) a second way and compares

## Pitfalls

| What goes wrong | What it looks like | What to do |
|---|---|---|
| Reading the per agency spread as heterogeneity | "it worked best at Pinecrest" | check whether the spread exceeds what noise produces |
| Reporting the ATT as the ATE | a statewide rollout recommendation | say which agencies the estimate covers |
| Forgetting Y(0) is constructed | treating the counterfactual as data | name the construction in the sentence |
| Assuming one agency does not affect another | an effect that leaks into the comparison group | Module 13 |

## Check Your Understanding

<details>
<summary><b>1.</b> Pinecrest shows −21 percent and Stonewick −9.2. Did the program work better at Pinecrest?</summary>

There is no evidence of that. Both agencies received the identical planted effect of 12 percent, so the entire 12 point spread is sampling noise from two agencies over 30 months. In real data you would not know the truth, which is why the question has to be answered by comparing the spread against what noise alone produces rather than by looking at the ranking. Module 15 does that formally.
</details>

<details>
<summary><b>2.</b> Why can a difference in differences never estimate the ATU?</summary>

Because it would require Y(1) for the agencies that did not take the program, and nothing in the data speaks to it. The comparison agencies were never trained, so there is no observation anywhere of what training does to an agency like them. Estimating the ATU requires either randomisation, which would have put some of them in the program, or a modelling assumption that the effect is the same everywhere, which is a strong claim and should be stated as one.
</details>

<details>
<summary><b>3.</b> The pre program trends of the two groups overlap heavily. Does that verify the assumption?</summary>

No, and the reason is worth being precise about. Before the program both groups were untreated, so both lines are Y(0), and agreeing then is not the same as agreeing afterwards. The assumption is about Y(0) in the after period, which is never observed for the treated group. Pre period agreement makes the assumption harder to dismiss. That is the most any evidence can do for it.
</details>

## Key Takeaway

Write Y(1) and Y(0) for each agency, say which average you are reporting, and say which ones the data cannot give.

---

| | |
|---|---|
| **Previous** | [Module 1: From "It Went Down" to "The Program Did It"](Module_01_From_It_Went_Down_To_The_Program_Did_It.md) |
| **Next** | [Module 3: The Counterfactual You Have to Construct](Module_03_The_Counterfactual_You_Have_To_Construct.md) |
| **Builds on** | [Module 1](Module_01_From_It_Went_Down_To_The_Program_Did_It.md), Beginner [Topic 3](../Beginner/Topic_03_The_World_You_Cannot_See.md) |
| **Used again in** | every module in this series |

*This module is part of a series developed for the Washington Data Exchange for Public Safety (WADEPS) through the Center for Interdisciplinary Statistical Education and Research (CISER) at Washington State University. Version 1.0, September 2026. Questions, errors, or suggestions: yin.zhang@wsu.edu*

*All examples use synthetic data created for teaching. They do not represent any real jurisdiction, agency, officer, or incident. See [Data/DATA_DICTIONARY.md](../../Data/DATA_DICTIONARY.md).*
