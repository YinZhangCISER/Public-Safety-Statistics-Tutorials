# Topic 10: When the Comparison Group Moves Too

> **Developed by Yin Zhang, PhD**, Assistant Professor, Department of Mathematics and Statistics, Washington State University

**The question this module answers:** *What happens if some of the comparison agencies were affected by the program without officially taking it?*

---

## The Core Concept

A comparison group is supposed to show what happens **without** the program. If some of its members got a piece of the program anyway, they improve too, and the gap between the groups shrinks.

The estimate then comes out **too small**. The program looks weaker than it was.

This is called **contamination** or **spillover**, and in public safety it is easy to arrange by accident. Officers transfer between agencies. Departments share a training academy. Neighbouring agencies work the same calls under mutual aid. A supervisor who took the training explains it to a friend at another department.

## Why It Matters

Every other failure in this series makes programs look **better** than they are. This one makes them look worse, and it is the reason a program that genuinely works can be cancelled after a careful evaluation.

It also has an uncomfortable property: the better the program, and the more people talk about it, the more it spreads, and the harder it becomes to measure.

## The Example

The estimate with a correctly labelled comparison group is **12.6 percent**, close to the true 12.0. Now suppose one comparison agency had in fact been running the same training quietly, and nobody recorded it.

![A horizontal bar chart of four estimates. The top bar, a correctly labelled comparison group, reaches minus 12.6 percent close to a dashed line at the true 12 percent. Below it three bars show what happens if Havenbrook, Lakeshore County or Ashfell had secretly been trained: minus 11.6, minus 9.9 and minus 8.6 percent, each further from the truth, with the number of officers at each agency noted beside the bar](Figures/fig_10_contamination.png)

| If this agency had secretly been trained | The estimate becomes | Sworn officers |
|---|---|---|
| Nobody | **−12.6%** | |
| Havenbrook | −11.6% | 95 |
| Lakeshore County | −9.9% | 141 |
| **Ashfell** | **−8.6%** | **902** |

One agency leaking is enough to lose a third of the effect, and the damage tracks the agency's size. Ashfell is the largest department in the dataset, so it carries the most weight in the comparison group's average, so its contamination does the most harm.

Nothing in the data would announce this. The estimate would simply be 8.6 percent, and it would look like a perfectly ordinary result.

## What To Watch For

- **Ask the comparison agencies directly.** "Did you run anything like this?" is one email and it is the only reliable check. The data cannot answer it.
- **Programs travel under different names.** A comparison agency may have adopted the same curriculum from a different vendor.
- **Geography is a warning sign.** The nearest agencies are the most likely to be contaminated and the most tempting to use as comparisons.
- **Shared academies contaminate whole regions.** If recruits from every agency in the county train together, a change to the academy curriculum reaches all of them.
- **An estimate that is too small is still wrong.** "We were conservative" is not a defence. A biased estimate does not become acceptable by being biased in a modest direction.

## 💡 The Insight

Contamination is the one bias that hides a real effect rather than inventing one, and it is the one nobody checks.

## Check Your Understanding

<details>
<summary><b>1.</b> Why does Ashfell leaking do more damage than Havenbrook leaking?</summary>

Because the comparison group's rate is computed from all seven agencies pooled together, and Ashfell has 902 sworn officers against Havenbrook's 95. Ashfell contributes far more incidents and arrests to the pooled total, so its behaviour dominates. When it falls extra, the comparison group's apparent decline gets larger, and the extra decline is subtracted from the program's credit.
</details>

<details>
<summary><b>2.</b> Would dropping the nearest agencies from the comparison group solve the problem?</summary>

It helps with geographic spillover and it costs something. Dropping agencies makes the comparison group smaller and noisier, and the agencies you drop may be the most similar ones. A reasonable approach is to report the estimate both ways, with and without the nearest neighbours, and let the difference between them stand as a measure of how much spillover could be affecting the answer.
</details>

<details>
<summary><b>3.</b> A program spreads so widely that every agency in the state adopts something like it. What can be measured?</summary>

Almost nothing, by this design. With no untreated agencies there is no comparison group, and with everyone changing at once there is nothing to subtract. This is a real situation, not a hypothetical, and the honest response is to say the design has no counterfactual available rather than to fall back on a before and after comparison and hope nobody notices.
</details>

## Key Takeaway

Before trusting a comparison group, ask its agencies whether they ran anything similar. The data will never tell you.

---

| | |
|---|---|
| **Previous** | [Topic 9: Were They Moving Together Before?](Topic_09_Were_They_Moving_Together_Before.md) |
| **Next** | [Topic 11: Why the Worst Performers Always Improve](Topic_11_Why_The_Worst_Performers_Always_Improve.md) |
| **Builds on** | [Topic 7](Topic_07_What_Makes_A_Good_Comparison_Group.md), [Topic 8](Topic_08_Two_Differences_Are_Better_Than_One.md) |
| **Used again in** | [Topic 19](Topic_19_Reading_A_Causal_Claim.md), [Topic 20](Topic_20_Questions_To_Ask.md) |

*This module is part of a series developed for the Washington Data Exchange for Public Safety (WADEPS) through the Center for Interdisciplinary Statistical Education and Research (CISER) at Washington State University. Version 1.0, September 2026. Questions, errors, or suggestions: yin.zhang@wsu.edu*

*All examples use synthetic data created for teaching. They do not represent any real jurisdiction, agency, officer, or incident. See [Data/DATA_DICTIONARY.md](../../Data/DATA_DICTIONARY.md).*
