# Module 12: Comparing Agencies Fairly

> **Developed by Yin Zhang, PhD**, Assistant Professor, Department of Mathematics and Statistics, Washington State University

**The question this module answers:** *Compared against whom?*

---

## The Question

Beginner [Topic 14](../Beginner/Topic_14_Comparing_Multiple_Time_Series.md) said to compare an agency against others over the same months. [Module 4](Module_04_Why_Small_Agencies_Look_Volatile.md) said to use a funnel rather than a ranking. Both left the hardest question open.

Comparing a 902 officer city force against an eight officer rural department answers nothing, no matter how carefully the arithmetic is done. Before any comparison can be fair, someone has to decide who is comparable, and that decision usually goes unmade and unrecorded.

This is the problem the WADEPS comparable agencies framework exists to solve.

## The Idea in Plain Language

Agencies differ on many things at once: how many officers they have, how many people they serve, what kind of agency they are, where they are, what the crime environment looks like, how much of the local budget they take.

A **distance** collapses all of that into one number per pair: 0 means identical, 1 means different in every respect. The nearest few agencies are the peer group.

The complication is that agency data mixes **numbers** with **labels**. Ordinary distance measures cannot handle that mixture. **Gower distance** can, by treating each variable in the way it deserves and then averaging.

## The Method

For each variable, compute a contribution between 0 and 1, then average across variables.

- **A number:** the absolute difference divided by that variable's range across all agencies.
- **A label:** 0 if the two agencies match, 1 if they do not.

```python
for c in numeric:
    v = d[c].astype(float).values
    total += np.abs(v[:, None] - v[None, :]) / (v.max() - v.min())
for c in categorical:
    v = d[c].values
    total += (v[:, None] != v[None, :]).astype(float)
distance = total / (len(numeric) + len(categorical))
```

**One judgment call is built into this.** Agency size spans two orders of magnitude, from 8 officers to 902. On a raw scale that makes every small agency look equally close to every other small agency, while the largest sits alone at one end. Taking logs of the size variables first makes the distance reflect **proportional** difference, which is the sensible reading of size.

## Worked Example

The twelve agencies, using officer count, population served, both crime rates, budget share and county population as numbers, plus agency type and region as labels.

![Two panels. The left panel is a map of the twelve agencies positioned so that similar agencies sit close together, coloured by agency type, with a line joining each agency to its single nearest peer. The right panel is a dumbbell chart showing, for each agency, its own rate and the pooled rate of its three nearest peers, against a vertical line for the statewide rate](Figures/fig_m12_comparing_agencies.png)

### The peer groups are sensible

| Pair | Distance | Why |
|---|---|---|
| Millgate and Northgate | **0.09** | both small municipal departments in the east |
| Cedar Falls and Harbor Point | **0.10** | both mid sized municipal departments in the west |
| Summit County and Lakeshore County | **0.12** | both sheriff's offices in the west |

### Two agencies have no peer, and that is a finding

| Agency | Mean distance to its three nearest |
|---|---|
| **Grandview** | **0.31** |
| **Pinecrest State University** | **0.28** |
| Millgate | 0.16 |
| Northgate | 0.13 |

Grandview is the largest agency in the state and its nearest peers sit roughly three times as far away as Millgate's do. Pinecrest is the only campus force, so its peers differ from it on agency type by construction.

For both, the honest answer is to say the peer group is weak and compare against the statewide figure instead, **saying so in the report**. A peer comparison presented without its distance invites the reader to assume the peers were good.

### Does the comparison group change the verdict?

| Agency | Rate | Against the state | Rank | Against its peers | Rank | Places moved |
|---|---|---|---|---|---|---|
| **Pinecrest State University** | 2.83 | +0.26 | 5 | **+0.57** | **2** | **3** |
| Elkhorn | 2.89 | +0.32 | 4 | +0.05 | 6 | 2 |
| **Harbor Point** | 2.79 | **+0.23** | 7 | **−0.27** | 8 | 1 |
| Cedar Falls | 3.34 | +0.77 | 1 | +0.58 | 1 | 0 |
| Grandview | 2.32 | −0.25 | 9 | −0.56 | 9 | 0 |

Most agencies move a place or two. **Pinecrest moves three**, and it is also one of the two agencies whose peer group is weakest, so both of its numbers need a caveat.

**Harbor Point changes sign.** It is above the statewide rate and below its peers, because its peers are Cedar Falls and Riverbend, two of the highest rate agencies in the state. Whether Harbor Point looks good or bad is entirely a question of who it is placed next to, and neither answer is wrong.

### Combine the peer group with the funnel

A peer group says **who** to compare against. The funnel from [Module 4](Module_04_Why_Small_Agencies_Look_Volatile.md) says **whether the gap is larger than sampling can explain**. Report both, plus the peer distance, and a reader can see all three of the things that could undermine the comparison.

## Do It Yourself

> 📓 **Notebook:** [Module_12_Comparing_Agencies_Fairly.ipynb](Notebooks/Module_12_Comparing_Agencies_Fairly.ipynb)
> [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/OWNER/REPO/blob/main/Time_Series/Intermediate/Notebooks/Module_12_Comparing_Agencies_Fairly.ipynb)
> About 25 minutes.

The notebook implements Gower distance from scratch in about ten lines, builds the peer groups and the comparison table, combines the peer group with a funnel, and ends with an exercise that drops agency type from the variable list to show how much the peer groups depend on what you chose to include.

## Pitfalls

| What goes wrong | What it looks like | What to do |
|---|---|---|
| Matching on size alone | a campus force paired with a rural sheriff's office | use several characteristics |
| Raw size in the distance | every small agency equally close to every other | take logs of size variables |
| Reporting a peer comparison without the peer distance | a weak comparison read as a strong one | publish the distance next to the verdict |
| Peers who are themselves extreme | an agency judged good because its peers are worse | report the statewide comparison as well |
| Leaving a characteristic out | the peer groups ignore something that matters | the list is a domain judgment, not a technical one |
| Missing data on a peer variable | agencies silently excluded, or matched on fewer variables | two agencies here have partial call data; say so |
| Publishing peer groups agencies have not seen | a comparison nobody accepts, so nothing changes | let agencies review their group first |

## Check Your Understanding

<details>
<summary><b>1.</b> Harbor Point is above the statewide rate and below its peers. Which is the right number to publish?</summary>

Both, with the peer group named. The two statements answer different questions: how Harbor Point compares to policing across the state, and how it compares to departments facing similar conditions. Publishing only the statewide figure implies the state is an appropriate benchmark. Publishing only the peer figure hides that its peers are among the highest rate agencies in the state. The disagreement between them is itself the most informative thing in the comparison.
</details>

<details>
<summary><b>2.</b> Why is taking logs of officer count before computing the distance a substantive decision rather than a technical one?</summary>

Because it defines what "similar in size" means. On a raw scale the gap between 8 and 54 officers is negligible next to the gap between 412 and 902, so every small agency looks like every other and the largest agency is isolated. On a log scale, 8 against 54 is a larger difference than 412 against 902, because one is nearly seven times the other and the second is about twice. The second reading matches how people actually think about agency size, but it is a choice and it changes the peer groups, so it belongs in the methodology note.
</details>

<details>
<summary><b>3.</b> Grandview's nearest peers average 0.31 away. What should a report about Grandview do?</summary>

Say so, and lean on the statewide comparison instead. With twelve agencies and one very large one, there is no honest peer group for Grandview, and forcing one produces a comparison against agencies less than half its size. The right report states that no comparable peer exists in the data, gives the statewide figure, and notes that a fair comparison would need agencies of similar scale from outside the state. Presenting a peer number without the distance would let a reader assume a comparison that was never available.
</details>

## Key Takeaway

Decide who is comparable before comparing, use Gower distance so numbers and labels can sit in the same measure, and always publish how far away the peers were.

---

| | |
|---|---|
| **Previous** | [Module 11: Lead and Lag Between Two Series](Module_11_Lead_And_Lag.md) |
| **Next** | Part IV, beginning with Module 13: Baseline Forecasts You Must Beat |
| **Builds on** | [Beginner Topic 14](../Beginner/Topic_14_Comparing_Multiple_Time_Series.md), [Module 3](Module_03_Choosing_A_Denominator.md), [Module 4](Module_04_Why_Small_Agencies_Look_Volatile.md) |
| **Used again in** | Advanced Module 10 |

*This module is part of a series developed for the Washington Data Exchange for Public Safety (WADEPS) through the Center for Interdisciplinary Statistical Education and Research (CISER) at Washington State University. Version 1.0, September 2026. Questions, errors, or suggestions: yin.zhang@wsu.edu*

*All examples use synthetic data created for teaching. They do not represent any real jurisdiction, agency, officer, or incident. See [Data/DATA_DICTIONARY.md](../../Data/DATA_DICTIONARY.md).*
