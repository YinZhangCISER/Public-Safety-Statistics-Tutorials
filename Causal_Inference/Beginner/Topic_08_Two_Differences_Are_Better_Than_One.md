# Topic 8: Two Differences Are Better Than One

> **Developed by Yin Zhang, PhD**, Assistant Professor, Department of Mathematics and Statistics, Washington State University

**The question this module answers:** *How do you actually combine a before and after comparison with a comparison group?*

---

## The Core Concept

You have two comparisons available, and each one is missing something.

- **Before against after** tells you how much your agency changed, and cannot separate the program from everything else.
- **You against them, after** tells you how you differ from other agencies, and cannot separate the program from differences that were always there.

Put together, each fixes the other's problem:

> **take the change at the trained agencies, then subtract the change at the untrained ones**

What is left is the part of the change that did not happen everywhere. Because two differences are being taken, this is called **difference in differences**. No arithmetic beyond subtraction is involved.

## Why It Matters

This is the workhorse of policy evaluation, in public safety and everywhere else. It is simple enough to draw on a whiteboard and it removes the largest single source of error in a before and after comparison.

It is also not magic, and the honest version of this topic includes the fact that on this dataset it does not get the right answer on the first try.

## The Example

![A line chart with two points on each line. The blue line runs from 3.48 before to 2.33 after for the trained agencies. The grey line runs from 2.67 to 2.15 for the comparison agencies. A dashed green line runs from the blue starting point to 2.80, showing where the trained agencies would have landed if they had changed by the same percentage as the comparison group. A double headed orange arrow between 2.80 and 2.33 is labelled as the effect, 16.9 percent](Figures/fig_08_two_differences.png)

Four numbers, and one subtraction.

| | Before | After | Change |
|---|---|---|---|
| Took the training | 3.48 | 2.33 | **−33.1%** |
| Did not | 2.67 | 2.15 | **−19.5%** |
| **The difference between the two changes** | | | **−16.9%** |

Read it in words. The trained agencies fell by a third. The untrained ones fell by a fifth without doing anything. The training can only be credited with the part that is left over.

The dashed green line on the chart is the counterfactual from [Topic 3](Topic_03_The_World_You_Cannot_See.md), now built out of real data rather than guessed: it is where the trained agencies would have landed if they had changed by the same percentage as everyone else. That is 2.80. They actually landed at 2.33.

## The part that is usually left out

The true effect is **12.0 percent**. Difference in differences gives **16.9 percent**.

| Method | Answer | Error |
|---|---|---|
| Before and after | −33.1% | nearly 3 times too big |
| **Difference in differences** | **−16.9%** | **about 40 percent too big** |
| The truth | −12.0% | |

This is a large improvement and it is not yet correct. Something about the comparison is still wrong, and [Topic 9](Topic_09_Were_They_Moving_Together_Before.md) finds it.

**Most published evaluations stop here.** That is the reason for saying plainly that stopping here is not enough.

## What To Watch For

- **State all four numbers.** A reader who can see the 2x2 table can check your subtraction and judge your comparison group. A reader given only the final percentage can do neither.
- **Percentages, not raw differences.** Subtracting rates directly works too, but percentage changes are easier to compare across agencies of different sizes.
- **It removes what is common, and only that.** Anything that happened to the trained agencies alone is still inside the estimate. That is the door [Topic 9](Topic_09_Were_They_Moving_Together_Before.md) walks through.
- **One number is not an answer.** Every estimate has uncertainty attached, and a difference in differences from twelve agencies has a great deal of it.

## 💡 The Insight

Subtract what happened to everybody else. Then remember that you have only removed what was common to both groups, and check whether anything else was not.

## Check Your Understanding

<details>
<summary><b>1.</b> Using the table, where does the counterfactual value of 2.80 come from?</summary>

The comparison agencies fell 19.5 percent. Apply that same percentage fall to the trained agencies' starting value: 3.48 reduced by 19.5 percent is 2.80. That is the claim being made, that without the training they would have changed by the same proportion as everyone else. The estimate is the gap between 2.80 and the 2.33 they actually reached.
</details>

<details>
<summary><b>2.</b> Suppose the comparison agencies had risen 5 percent instead of falling. What would the estimate be?</summary>

Larger. The counterfactual would be 3.48 raised by 5 percent, about 3.65, and the trained agencies still reached 2.33, giving roughly a 36 percent reduction. This shows that a difference in differences estimate can exceed a before and after estimate. The direction of the correction depends entirely on what the comparison group did, which is why choosing the group honestly matters so much.
</details>

<details>
<summary><b>3.</b> Difference in differences still overstates the effect by about five percentage points. What kind of thing could cause that?</summary>

Something that happened to the trained agencies and not the comparison agencies, other than the training. It cannot be anything statewide, because that affects both groups and subtracts out. It has to be specific to the group that took the program, which narrows the search considerably. The next topic finds exactly one such thing.
</details>

## Key Takeaway

Report all four cells of the table, not only the difference. Then ask what else was true of the treated group and not the comparison group.

---

| | |
|---|---|
| **Previous** | [Topic 7: What Makes a Good Comparison Group](Topic_07_What_Makes_A_Good_Comparison_Group.md) |
| **Next** | [Topic 9: Were They Moving Together Before?](Topic_09_Were_They_Moving_Together_Before.md) |
| **Builds on** | [Topic 4](Topic_04_Before_And_After_Is_Not_Enough.md), [Topic 6](Topic_06_Comparing_Yourself_To_Someone_Else.md), [Topic 7](Topic_07_What_Makes_A_Good_Comparison_Group.md) |
| **Used again in** | [Topic 9](Topic_09_Were_They_Moving_Together_Before.md), [Topic 10](Topic_10_When_The_Comparison_Group_Moves_Too.md), [Topic 17](Topic_17_When_You_Cannot_Randomize.md) |

*This module is part of a series developed for the Washington Data Exchange for Public Safety (WADEPS) through the Center for Interdisciplinary Statistical Education and Research (CISER) at Washington State University. Version 1.0, September 2026. Questions, errors, or suggestions: yin.zhang@wsu.edu*

*All examples use synthetic data created for teaching. They do not represent any real jurisdiction, agency, officer, or incident. See [Data/DATA_DICTIONARY.md](../../Data/DATA_DICTIONARY.md).*
