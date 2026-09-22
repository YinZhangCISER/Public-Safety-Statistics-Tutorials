# Module 12: Building a Peer Benchmark Series

> **Developed by Yin Zhang, PhD**, Assistant Professor, Department of Mathematics and Statistics, Washington State University

**The question this module answers:** *One agency's line moved. What line should it be sitting next to?*

---

## The Question

Everything in this series so far has worked on a single agency's series: splitting it, measuring its trend, adjusting it, setting limits on it. Every one of those tells you **what** happened and none of them tells you whether it happened anywhere else.

Beginner [Topic 14](../Beginner/Topic_14_Comparing_Multiple_Time_Series.md) established why that matters: a change that every agency shows is not the agency's doing, and a change only one agency shows is. Making that comparison needs a second line on the chart.

This module builds that line. It is the last piece of machinery [Module 16](Module_16_Did_Something_Change.md) needs, and the whole [Causal Inference series](../../Causal_Inference/) is built on it.

## The Idea in Plain Language

A **peer benchmark series** is a monthly series constructed from the agencies most like the one you are studying. It answers the question "what did this month look like for departments in the same situation", every month, for as long as the data runs.

Building one takes two decisions, and both go wrong in characteristic ways.

**Who belongs in the group.** Size alone is not enough: a 268 officer sheriff's office and a 412 officer city force are close in staffing and share almost nothing operationally.

**How to combine them into one line.** Pool the counts and the denominators; do not average the peers' rates. Averaging gives an agency with 500 arrests the same weight as one with 49,000.

## The Method

**Step one, the distance.** Agency characteristics mix numbers with labels, which ordinary distance measures cannot handle. **Gower distance** can: for a number, the absolute difference divided by that variable's range; for a label, 0 if they match and 1 if they do not; then average across variables. The result runs from 0, identical, to 1, different in every respect. This is the measure the WADEPS comparable agencies framework uses.

```python
for c in numeric:
    v = d[c].astype(float).values
    total += np.abs(v[:, None] - v[None, :]) / (v.max() - v.min())
for c in categorical:
    total += (d[c].values[:, None] != d[c].values[None, :]).astype(float)
distance = total / (len(numeric) + len(categorical))
```

One judgment is built in: agency size spans two orders of magnitude, so take logs of the size variables first. That makes the distance reflect **proportional** difference, which is how people actually think about agency size, and it changes the groups.

**Step two, the benchmark series.** Pool, do not average.

```python
w = monthly[monthly["agency_id"].isin(peers)].groupby("year_month")[["n_uof", "n_arrests"]].sum()
benchmark = 100 * w["n_uof"].rolling(12).sum() / w["n_arrests"].rolling(12).sum()
```

## Worked Example

### Who is whose peer

| Pair | Distance | Why |
|---|---|---|
| Millgate and Kelsmoor | **0.09** | both small municipal departments in the east |
| Tarnbridge and Havenbrook | **0.10** | both mid sized municipal departments in the west |
| Summit County and Lakeshore County | **0.12** | both sheriff's offices in the west |

Two agencies have no close peer, and that is a finding rather than a nuisance. **Ashfell**, the largest in the state, has nearest peers averaging **0.31** away, roughly three times Millgate's. **Pinecrest State University** is the only campus force, at **0.28**. For both, the honest answer is to say the peer group is weak and use the statewide figure, saying so.

### Pooling versus averaging

Stonewick's three nearest untreated peers run at 2.93, 2.35 and 2.49 per 100 arrests individually.

| Method | Benchmark |
|---|---|
| Simple average of the three rates | 2.59 |
| **Pooled counts over pooled arrests** | **2.51** |

Ashfell supplies **82 percent** of the group's arrests, so pooling lets it carry 82 percent of the weight and averaging gives it a third. Pooling is right: the benchmark should answer "what rate did a person arrested by one of these agencies face", not "what is the average of three agency level numbers".

### The benchmark series, and the trap in it

![Three panels. The top panel maps the twelve agencies by similarity, coloured by whether they adopted the training, with lines joining each to its nearest peer; Stonewick's two nearest are both orange. The lower left panel shows Stonewick's twelve month trailing rate against two different peer benchmarks. The lower right panel shows the estimated programme effect under three choices of comparison group, against a dashed line at the true effect](Figures/fig_m12_comparing_agencies.png)

Stonewick adopted the de escalation training in July 2023. Its three nearest peers are **Tarnbridge, Summit County and Ashfell**, and the first two **adopted the same programme**.

That is not a quirk of this dataset. Programmes are adopted by agencies that resemble each other, for the same reasons that make them resemble each other, so **a peer group built on agency characteristics will tend to be full of agencies that made the same decisions.**

### What it costs

| Comparison group | Estimated effect on Stonewick |
|---|---|
| Three nearest peers, no screening | **+0.3%** |
| Three nearest peers that were not trained | −7.1% |
| All agencies that were not trained | −6.9% |
| **The true effect built into the data** | **−12.0%** |

With the trained peers left in, **the programme disappears entirely**. The benchmark fell for the same reason Stonewick fell, so the comparison subtracts the effect from itself.

Screening the peers recovers roughly −7 percent. That is the right method and it is still short of −12, because this is one agency over thirty months. The multi agency estimate in [Data/GROUND_TRUTH.md](../../Data/GROUND_TRUTH.md) recovers −12.6 percent using every trained agency at once. **A single agency does not carry enough information to measure a 12 percent effect,** which is [Module 4](Module_04_Why_Small_Agencies_Look_Volatile.md) again in a new setting.

## Do It Yourself

> 📓 **Notebook:** [Module_12_Building_A_Peer_Benchmark_Series.ipynb](Notebooks/Module_12_Building_A_Peer_Benchmark_Series.ipynb)
> [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/YinZhangCISER/Public-Safety-Statistics-Tutorials/blob/main/Time_Series/Intermediate/Notebooks/Module_12_Building_A_Peer_Benchmark_Series.ipynb)
> About 25 minutes.

The notebook implements Gower distance in about ten lines, builds peer groups, constructs the benchmark series, demonstrates pooling against averaging, reproduces the contamination result, and ends with an exercise that drops a variable from the distance to show how much the groups depend on what you chose to include.

## Pitfalls

| What goes wrong | What it looks like | What to do |
|---|---|---|
| Matching on size alone | a campus force paired with a rural sheriff's office | use several characteristics |
| Raw size in the distance | every small agency equally close to every other | take logs of size variables |
| Averaging peer rates | a tiny agency weighted like a large one | pool counts over pooled denominators |
| **Peers who received the same intervention** | **the effect vanishes** | screen the peer group on exposure, then rebuild |
| Peers who are themselves extreme | an agency looks good because its peers are worse | report the statewide comparison too |
| A peer comparison without the peer distance | a weak comparison read as a strong one | publish the distance next to the verdict |
| A benchmark from one year | a comparison that cannot see a change | build the whole series, every month |
| Publishing peer groups agencies have not seen | a comparison nobody accepts, so nothing changes | let agencies review their group first |

## Check Your Understanding

<details>
<summary><b>1.</b> Why does including trained agencies in the comparison group make the estimated effect go to zero rather than merely shrink it?</summary>

Because the comparison is a difference. The estimate is how much the agency changed minus how much the benchmark changed. If two of the three benchmark agencies received the same programme, the benchmark falls for the same reason the agency falls, and the difference between them removes the effect instead of isolating it. Here two of three peers were treated, which was enough to cancel it almost exactly. Had all three been treated, the estimate could have come out positive, and a report would have concluded the programme made things worse.
</details>

<details>
<summary><b>2.</b> Stonewick's peer group is full of trained agencies. Is that bad luck with this dataset?</summary>

No, it is the normal case. Agencies adopt a programme because of what they are: their size, their rate, their leadership, their funding. A peer group built on those same characteristics is therefore enriched with agencies that made the same decision. The more carefully the peer group is matched, the more likely this is. The remedy is not a better distance measure but an extra step: screen the peer group on whether its members were exposed to the thing you are studying, and say in the report that you did.
</details>

<details>
<summary><b>3.</b> Why pool the peers' counts rather than average their rates?</summary>

Because the benchmark is supposed to represent the experience of a person encountering one of these agencies, and most of those encounters happen at the largest one. In this example Ashfell supplies 82 percent of the group's arrests. Pooling gives it 82 percent of the weight; averaging gives it a third, which lets two agencies with a tenth of the activity move the benchmark as much as the one with most of it. Averaging is defensible only when the question really is about agencies as units rather than about the people they encounter, and then it should be said explicitly.
</details>

## Key Takeaway

A comparison group is a series, not a name. Choose the members on several characteristics, screen them for the intervention you are studying, pool their counts rather than averaging their rates, and publish how far away they were.

---

| | |
|---|---|
| **Previous** | [Module 11: Lead and Lag Between Two Series](Module_11_Lead_And_Lag.md) |
| **Next** | Part IV, beginning with Module 13: Baseline Forecasts You Must Beat |
| **Builds on** | [Beginner Topic 14](../Beginner/Topic_14_Comparing_Multiple_Time_Series.md), [Module 3](Module_03_Choosing_A_Denominator.md), [Module 4](Module_04_Why_Small_Agencies_Look_Volatile.md), [Module 9](Module_09_Year_Over_Year_And_Indexing.md) |
| **Used again in** | [Module 16](Module_16_Did_Something_Change.md), Advanced Module 10, and the whole [Causal Inference series](../../Causal_Inference/) |

*This module is part of a series developed for the Washington Data Exchange for Public Safety (WADEPS) through the Center for Interdisciplinary Statistical Education and Research (CISER) at Washington State University. Version 1.0, September 2026. Questions, errors, or suggestions: yin.zhang@wsu.edu*

*All examples use synthetic data created for teaching. They do not represent any real jurisdiction, agency, officer, or incident. See [Data/DATA_DICTIONARY.md](../../Data/DATA_DICTIONARY.md).*
