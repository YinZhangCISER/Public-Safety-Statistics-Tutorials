# Module 7: Testing Parallel Trends

> **Developed by Yin Zhang, PhD**, Assistant Professor, Department of Mathematics and Statistics, Washington State University

## The Question

The whole estimate rests on an assumption about a world nobody observes. What can be tested, and how much is the test worth?

## The Idea in Plain Language

The assumption is that without the program the two groups would have changed by the same proportion. That cannot be checked directly. What can be checked is its implication: **before the program, the two groups should have been moving at the same rate.**

Three ways to check it, in increasing formality and decreasing usefulness.

## The Method

> **look** one line per agency over the pre period
>
> **test** regress the pre period on time with a group by time interaction; the interaction is the difference in trends
>
> **placebo** run the real estimator on a fake intervention date inside the pre period

| What the test does | What it means | What it does not mean |
|---|---|---|
| Fails | the design is in trouble, act | the program had no effect |
| Passes | nothing was detected | the trends are parallel |
| Passes with a wide interval | the test had no power | anything at all |

## Worked Example

![A horizontal chart of every agency's pre program trend with confidence intervals, sorted. Summit County sits alone at minus 12 percent a year with an interval that does not reach the others. Most intervals are very wide, several spanning from 16 percent down to 30 percent up. A green vertical line marks the comparison group's own trend of 4.5 percent a year](Figures/fig_07_parallel_trends.png)

Two things are visible and the second is the one people miss.

**Summit County is an outlier**, falling at 12.0 percent a year against 4 to 6 for everyone else, with an interval that does not reach the others.

**Most of the intervals are enormous.** Orrindale's runs from 16 percent down to 31 percent up. Only three of the twelve agencies have an interval excluding zero.

### The group level test, and why it nearly missed

| | Difference in pre trends | 95 percent interval | p |
|---|---|---|---|
| Summit County excluded | −0.70% a year | [−3.31, +1.97] | 0.603 |
| **Summit County included** | **−2.16% a year** | **[−4.58, +0.32]** | **0.0875** |

With Summit County in, **p is 0.0875, which passes at the conventional threshold.** An analyst running only this test would have kept the agency and reported 17.0 percent against a truth of 12.

Averaging one badly behaved agency with four well behaved ones dilutes the violation almost out of existence.

### How much power the test has

Rather than assert that the test is weak, plant a pre trend difference of known size and count how often it is found.

| Planted difference | Found at p < 0.05 |
|---|---|
| 1 percent a year | **2%** of the time |
| 2 percent a year | **16%** |
| 3 percent a year | 40% |
| 5 percent a year | 87% |

The violation Summit County creates at the group level is 2.16 percent a year. **A violation that size is found one time in six.**

## Do It Yourself

> 📓 **Notebook:** [Module_07_Testing_Parallel_Trends.ipynb](Notebooks/Module_07_Testing_Parallel_Trends.ipynb)
> [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/YinZhangCISER/Public-Safety-Statistics-Tutorials/blob/main/Causal_Inference/Intermediate/Notebooks/Module_07_Testing_Parallel_Trends.ipynb)
> About 25 minutes.

- Tabulates every agency's pre program trend with its interval
- Runs the group level test with and without Summit County
- Simulates the test's power against planted violations of four sizes
- The exercise runs a placebo difference in differences inside the pre period

## Pitfalls

| What goes wrong | What it looks like | What to do |
|---|---|---|
| Testing the group and not the agencies | a violation diluted below detection | tabulate every agency separately |
| Reporting p without the interval | "trends are parallel, p = 0.09" | report the interval; here it reaches 4.6 percent a year |
| Treating a pass as verification | confidence the design does not support | say what the test could have detected |
| Assuming linear pre trends | a curved divergence missed | use the placebo version as well |
| Running the test after seeing the result | the choice to test becomes a choice of answer | fix the procedure in advance |

## Check Your Understanding

<details>
<summary><b>1.</b> The test with Summit County included gives p = 0.0875. Why is it wrong to conclude the trends are parallel?</summary>

Because the interval runs from 4.58 percent a year down to 0.32 percent up. A difference of 4 percent a year has not been ruled out, and sustained across the study period that would move the estimate by several points. A p value above 0.05 with an interval that wide says the test could not tell, not that there is nothing there.
</details>

<details>
<summary><b>2.</b> Only three of twelve agencies have a pre trend interval excluding zero. Is the per agency table therefore useless?</summary>

The opposite. It is precisely because the per agency test is so weak that Summit County standing clear of the others is informative: the violation had to be very large to show up at all. The table is also the only place the violation is visible, since the group test dilutes it. Use the table to look, and the interval to say how much looking was worth.
</details>

<details>
<summary><b>3.</b> The placebo in the exercise gives a small estimate with an interval containing zero. Does that confirm the design?</summary>

It supports it and does not confirm it, and the reason is the same weakness measured in the power table. A placebo that fails to reject could mean nothing happened or could mean the procedure cannot see what did. Report the placebo's interval alongside its point estimate, exactly as for the main result.
</details>

## Key Takeaway

Tabulate every agency's pre trend with its interval, run the group test, and report what the test could have detected rather than whether it passed.

---

| | |
|---|---|
| **Previous** | [Module 6: Difference in Differences, as a Regression](Module_06_Difference_In_Differences_As_A_Regression.md) |
| **Next** | [Module 8: When Parallel Trends Fails](Module_08_When_Parallel_Trends_Fails.md) |
| **Builds on** | [Module 6](Module_06_Difference_In_Differences_As_A_Regression.md), Beginner [Topic 9](../Beginner/Topic_09_Were_They_Moving_Together_Before.md) |
| **Used again in** | [Module 8](Module_08_When_Parallel_Trends_Fails.md), [Module 12](Module_12_Placebo_Tests.md), [Module 14](Module_14_How_Big_An_Effect.md) |

*This module is part of a series developed for the Washington Data Exchange for Public Safety (WADEPS) through the Center for Interdisciplinary Statistical Education and Research (CISER) at Washington State University. Version 1.0, September 2026. Questions, errors, or suggestions: yin.zhang@wsu.edu*

*All examples use synthetic data created for teaching. They do not represent any real jurisdiction, agency, officer, or incident. See [Data/DATA_DICTIONARY.md](../../Data/DATA_DICTIONARY.md).*
