# Topic 12: Who Chose to Participate?

> **Developed by Yin Zhang, PhD**, Assistant Professor, Department of Mathematics and Statistics, Washington State University

**The question this module answers:** *Agencies that join a program are not a random sample of agencies. Which differences matter, and how would you find them?*

---

## The Core Concept

Nobody is assigned to a public safety program by lottery. Agencies volunteer, or are nominated, or qualify, or are pushed into it.

Whatever the route, **the agencies that end up in the program differ from the ones that do not.** That is not a flaw in the program; it is what it means to have a selection process.

It becomes a measurement problem when the thing that made them different also affects the outcome. Then the comparison between the groups contains both the program and the reason they were chosen, with no way to tell them apart.

## Why It Matters

The usual reassurance is to check that the two groups look similar: similar size, similar region, similar crime rates. When they do, the comparison is declared fair.

That reassurance is worth much less than it appears, because **the characteristic that got an agency selected is usually not on the list being checked.**

## The Example

Compare the five trained agencies against the seven that were not, on every characteristic the dataset records.

![A dot plot comparing the trained agencies against the untrained ones as a ratio, with a vertical line at 1.0 meaning identical. Sworn officers, population served, violent crime rate, property crime rate and public safety budget share all sit within about 15 percent of 1.0 in grey. The use of force rate before the program sits far to the right at 1.43, marked in orange](Figures/fig_12_who_participated.png)

| Characteristic | Trained divided by untrained |
|---|---|
| Sworn officers | 1.10 |
| Population served | 1.13 |
| Violent crime rate | 0.85 |
| Property crime rate | 0.99 |
| Public safety budget share | 0.99 |
| **Use of force rate before the program** | **1.43** |

The two groups are close to interchangeable on size, on crime, and on budget. They are also mixed across regions and agency types.

**And the trained agencies' use of force rate was 43 percent higher before anything happened.** That is not a coincidence, and [Topic 13](Topic_13_Picking_The_Winners.md) explains it.

A reviewer who checked the first five rows would have concluded the groups were well matched. The one row that was not checked is the one that decides the answer.

## What To Watch For

- **Ask how agencies got in.** Volunteered, nominated, qualified by a threshold, or chosen by someone. Each has different consequences, and the answer is usually available by asking.
- **Check the outcome's own history, not just the covariates.** The most informative comparison between two groups is what the outcome was doing before. It is also the one most often left out of the balance table.
- **Volunteers are systematically unusual.** Agencies that sign up for a de escalation program tend to have leadership already focused on the issue, which is itself a cause of improvement.
- **Matching on observed characteristics does not fix unobserved ones.** Everything above was measured. Whatever made a chief say yes usually was not.

## 💡 The Insight

The groups will match on everything you thought to check. Selection happens on the thing you did not.

## Check Your Understanding

<details>
<summary><b>1.</b> The trained agencies have a 15 percent lower violent crime rate. Is that a problem for the comparison?</summary>

Probably not by itself. What matters is whether the difference affects how the use of force rate **changes** over the study period, not whether it affects the level. A constant difference in crime rates subtracts out of a difference in differences. It would matter if violent crime were falling at different speeds in the two groups, which is a question about trends, and that is [Topic 9](Topic_09_Were_They_Moving_Together_Before.md).
</details>

<details>
<summary><b>2.</b> An agency volunteers for a program because its new chief wants to reduce use of force. Name two ways that damages the evaluation.</summary>

First, the new chief is probably changing other things at the same time: supervision, discipline, recruitment, review of incidents. Any of those could move the outcome, and all of them arrive with the program. Second, agencies with reform minded leadership may already have been improving before the program, which is the pre trend problem from [Topic 9](Topic_09_Were_They_Moving_Together_Before.md). Selection on motivation produces both problems at once.
</details>

<details>
<summary><b>3.</b> If the two groups matched perfectly on every measured characteristic including the pre program outcome, would the comparison be safe?</summary>

Safer, and not safe. Matching on everything recorded says nothing about what was not recorded, and the reason an agency joined a program is frequently something no dataset holds: a change of leadership, a lawsuit, a consent decree, a single incident that made the news. The right response is not more matching but more honesty in the write up about how agencies were selected.
</details>

## Key Takeaway

Find out how agencies entered the program, write it in the report, and put the outcome's own pre program history in the balance table.

---

| | |
|---|---|
| **Previous** | [Topic 11: Why the Worst Performers Always Improve](Topic_11_Why_The_Worst_Performers_Always_Improve.md) |
| **Next** | [Topic 13: Picking the Winners Makes the Program Look Good](Topic_13_Picking_The_Winners.md) |
| **Builds on** | [Topic 7](Topic_07_What_Makes_A_Good_Comparison_Group.md), [Topic 11](Topic_11_Why_The_Worst_Performers_Always_Improve.md) |
| **Used again in** | [Topic 13](Topic_13_Picking_The_Winners.md), [Topic 16](Topic_16_Randomness_Solves_A_Problem.md), [Topic 20](Topic_20_Questions_To_Ask.md) |

*This module is part of a series developed for the Washington Data Exchange for Public Safety (WADEPS) through the Center for Interdisciplinary Statistical Education and Research (CISER) at Washington State University. Version 1.0, September 2026. Questions, errors, or suggestions: yin.zhang@wsu.edu*

*All examples use synthetic data created for teaching. They do not represent any real jurisdiction, agency, officer, or incident. See [Data/DATA_DICTIONARY.md](../../Data/DATA_DICTIONARY.md).*
