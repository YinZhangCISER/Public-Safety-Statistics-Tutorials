# Causal Inference, Beginner Level

### Did the program cause the change, or would it have happened anyway?

*Developed by Yin Zhang, PhD, Assistant Professor, Data Analytics Program, Department of Mathematics and Statistics, Washington State University, for the Washington Data Exchange for Public Safety (WADEPS) through the Center for Interdisciplinary Statistical Education and Research (CISER).*

For anyone who reads a report claiming a program worked, and has to decide whether to believe it. No statistics background, no mathematics, no code. Twenty short topics, each with one figure.

> **Publication status:** complete. All twenty topics are published.

---

## The worked example

Every topic uses the same case. Five agencies adopted a de escalation training program in July 2023. The program's true effect is known exactly, because the teaching dataset was built with it planted: a **12 percent reduction** in the use of force rate.

That makes it possible to grade each method rather than argue about it.

| What was done | What it reported |
|---|---|
| Before and after, at the agencies that took the training | −33.1% |
| Subtracting what happened at agencies that did not | −16.9% |
| The same, after checking the years before the program | **−12.5%** |
| **The truth** | **−12.0%** |

---

## What a causal claim is

| # | Topic | The question it answers |
|---|---|---|
| 1 | [What Does "Caused" Mean?](Topic_01_What_Does_Caused_Mean.md) | What would it take to say a program is the reason? |
| 2 | [The Question Behind Every Policy Question](Topic_02_The_Question_Behind_Every_Policy_Question.md) | Which of the four questions in the room is the causal one? |
| 3 | [The World You Cannot See](Topic_03_The_World_You_Cannot_See.md) | What is an effect measured against? |

## Why the obvious comparisons are not enough

| # | Topic | The question it answers |
|---|---|---|
| 4 | [Before and After Is Not Enough](Topic_04_Before_And_After_Is_Not_Enough.md) | How wrong can the most natural comparison be? |
| 5 | [Things Were Already Changing](Topic_05_Things_Were_Already_Changing.md) | How much would have arrived without the program? |
| 6 | [Comparing Yourself to Someone Else](Topic_06_Comparing_Yourself_To_Someone_Else.md) | What is a better counterfactual than your own past? |
| 7 | [What Makes a Good Comparison Group](Topic_07_What_Makes_A_Good_Comparison_Group.md) | Similar agencies, or several of them? |
| 8 | [Two Differences Are Better Than One](Topic_08_Two_Differences_Are_Better_Than_One.md) | How do the two comparisons combine? |

## How a comparison breaks

| # | Topic | The question it answers |
|---|---|---|
| 9 | [Were They Moving Together Before?](Topic_09_Were_They_Moving_Together_Before.md) | How do you find out whether a comparison group is any good? |
| 10 | [When the Comparison Group Moves Too](Topic_10_When_The_Comparison_Group_Moves_Too.md) | What if some of them got the program anyway? |
| 11 | [Why the Worst Performers Always Improve](Topic_11_Why_The_Worst_Performers_Always_Improve.md) | Why does anything measured at its worst get better? |
| 12 | [Who Chose to Participate?](Topic_12_Who_Chose_To_Participate.md) | Which differences between the groups matter? |
| 13 | [Picking the Winners Makes the Program Look Good](Topic_13_Picking_The_Winners.md) | What if the selection rule uses the outcome? |
| 14 | [Confounding, the Third Thing](Topic_14_Confounding.md) | Is there one idea underneath all of these? |

## Deciding what to believe

| # | Topic | The question it answers |
|---|---|---|
| 15 | [Correlation, Causation, and the Sentences In Between](Topic_15_Correlation_Causation_And_The_Sentences_In_Between.md) | What are you actually allowed to say? |
| 16 | [Randomness Solves a Problem You Cannot Otherwise Solve](Topic_16_Randomness_Solves_A_Problem.md) | Why is a coin toss the gold standard? |
| 17 | [When You Cannot Randomize](Topic_17_When_You_Cannot_Randomize.md) | What is available when the program was already given out? |
| 18 | [How Long Do You Have to Wait?](Topic_18_How_Long_Do_You_Have_To_Wait.md) | Does "no significant effect" mean it did not work? |
| 19 | [Reading a Causal Claim in the News](Topic_19_Reading_A_Causal_Claim.md) | How much can you tell from a headline? |
| 20 | [Questions to Ask Before You Believe a Program Worked](Topic_20_Questions_To_Ask.md) | All of it, on one page. |

---

## The six questions

Topic 20 reduces the series to these. None requires any mathematics.

1. What would have happened otherwise?
2. Who did not get it, and what happened to them?
3. Were the two groups moving together before?
4. How were the recipients chosen?
5. Could the comparison group have been affected too?
6. How long did the study wait?

---

## Where to go next

| If you want | Go to |
|---|---|
| To compute these yourself | the [Intermediate series](../Intermediate/) |
| To understand trends and seasonality in the outcome | [Time Series, Beginner](../../Time_Series/Beginner/) |
| To see what was planted in the teaching data | [Data/GROUND_TRUTH.md](../../Data/GROUND_TRUTH.md) |

## Reproducing the figures

```
cd Figures
python make_figures.py
```

Every figure is rebuilt from the CSV files in [Data/](../../Data/). Nothing is drawn by hand.

---

*All examples use synthetic data created for teaching. They do not represent any real jurisdiction, agency, officer, or incident.*

*Questions, corrections, or suggestions: yin.zhang@wsu.edu*
