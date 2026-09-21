# Module 4: Why Small Agencies Look Volatile

> **Developed by Yin Zhang, PhD**, Assistant Professor, Department of Mathematics and Statistics, Washington State University

**The question this module answers:** *An eight officer department's rate is the highest in the state. Is it a problem agency, or is it just small?*

---

## The Question

Small agencies swing wildly from month to month and appear at both ends of every ranking. Most of that is arithmetic, not behaviour.

This matters because rankings get published, and a small agency at the top of one is treated exactly like a large agency at the top of one. They are not the same finding, and the difference is measurable.

## The Idea in Plain Language

When you count events that happen more or less independently, the count has a built in wobble. The typical size of that wobble is close to **the square root of the count**.

Ten expected incidents come with a wobble of about three, which is 30 percent of ten. A hundred expected incidents come with a wobble of about ten, which is 10 percent of a hundred. The absolute wobble grows with size; the **relative** wobble shrinks.

So an agency averaging one incident a month will routinely record zero, one, two or three, and every one of those is an ordinary month. Expressed as percentage change it will produce headlines forever.

## The Method

**Step one: how much should it wobble?** Measure variability as the standard deviation divided by the mean, then compare it against `1 / sqrt(mean)`, which is what counting alone would produce. What is left over is real structure.

```python
v["variability"] = v["sd"] / v["mean"]
v["expected_from_counting"] = 1 / np.sqrt(v["mean"])
v["extra"] = v["variability"] - v["expected_from_counting"]
```

**Step two: is this agency actually different?** Compare each agency against the pooled rate, using a margin of error that depends on its own exposure. For a rate built from a count over a denominator, that margin is

```python
se = scale * np.sqrt(p * (1 - p) / denominator)
```

where `p` is the pooled rate expressed as a proportion. Agencies more than about two standard errors from the pooled rate are further out than their sample size can explain. Plotting rate against denominator with that band drawn on gives a **funnel plot**, which is the standard tool for exactly this problem.

## Worked Example

**Step one.** Variability against agency size, across all twelve agencies:

| Agency | Average a month | Variability | Counting alone would give | Extra |
|---|---|---|---|---|
| Two Rivers Tribal | 0.80 | 1.08 | 1.12 | **0.00** |
| Elkhorn | 0.81 | 1.08 | 1.11 | **0.00** |
| Northgate | 2.78 | 0.75 | 0.60 | 0.15 |
| Prairie County | 2.84 | 0.72 | 0.59 | 0.13 |
| Millgate | 7.55 | 0.43 | 0.36 | 0.07 |
| Lakeshore County | 10.83 | 0.37 | 0.30 | 0.07 |
| Summit County | 22.33 | 0.40 | 0.21 | 0.19 |
| Cedar Falls | 27.84 | 0.32 | 0.19 | 0.13 |
| Riverbend | 57.65 | 0.29 | 0.13 | 0.15 |
| Grandview | 99.84 | 0.29 | 0.10 | **0.19** |

Read the last column. For the two smallest agencies it is essentially zero: **their monthly variation is entirely counting noise, and there is nothing in it to interpret.** For Grandview the observed variability is about three times what counting alone would produce, and that excess is the seasonal pattern and the trend. A large agency's monthly movements are worth reading. A small agency's are not.

**Step two.** The funnel plot, 2023, against a statewide rate of **2.57 per 100 arrests**:

![Two panels. The left panel plots each agency's variability against its average monthly count on a log scale, with an orange curve showing what counting noise alone would produce; the smallest agencies sit on the curve and the largest sit well above it. The right panel is a funnel plot of the 2023 rate against the number of arrests, with a shaded band that narrows as the denominator grows](Figures/fig_m04_small_agencies.png)

| Agency | Arrests | Rate | Verdict |
|---|---|---|---|
| Two Rivers Tribal | 462 | 2.81 | within range |
| **Elkhorn** | 484 | **2.89** | **within range** |
| Pinecrest State University | 1,343 | 2.83 | within range |
| Prairie County | 1,516 | 2.24 | within range |
| Northgate | 1,706 | 2.70 | within range |
| Millgate | 2,792 | 2.94 | within range |
| Harbor Point | 4,904 | 2.79 | within range |
| Lakeshore County | 5,801 | 1.93 | **below** |
| Cedar Falls | 10,271 | 3.34 | **above** |
| Summit County | 10,385 | 2.23 | **below** |
| Riverbend | 23,190 | 2.96 | **above** |
| **Grandview** | 49,035 | **2.32** | **below** |

This is the result worth pausing on. In the raw ranking **Elkhorn sits fourth** at 2.89, above eight larger agencies. The funnel puts it **within range**: with 484 arrests you cannot distinguish 2.89 from 2.57.

Meanwhile **Grandview sits only ninth** in the raw ranking, and the funnel flags it as genuinely **below**, because with 49,035 arrests a gap of a quarter of a point can be established. **The agencies the funnel picks out are the large ones, which is the opposite of what a league table does.**

**One caution.** Pool seven years instead of one and the band narrows until **eleven of the twelve** agencies fall outside it. That is not a finding about policing; it follows from having 765,000 arrests. Once a sample is large enough, every difference becomes detectable, and the question changes from *can these be told apart* to *is the difference big enough to act on*. Always report the size of the gap next to the verdict.

## Do It Yourself

> 📓 **Notebook:** [Module_04_Why_Small_Agencies_Look_Volatile.ipynb](Notebooks/Module_04_Why_Small_Agencies_Look_Volatile.ipynb)
> [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/OWNER/REPO/blob/main/Time_Series/Intermediate/Notebooks/Module_04_Why_Small_Agencies_Look_Volatile.ipynb)
> Opens in Google Colab, runs top to bottom, about 20 minutes.

The notebook builds both tables, draws both plots, and ends with a reusable `funnel` function. The exercise runs the funnel over one year and then two, so you can watch agencies change verdict without changing behaviour.

## Pitfalls

| What goes wrong | What it looks like | What to do |
|---|---|---|
| Ranking agencies of very different sizes | small agencies at both extremes every year | funnel plot instead of a league table |
| Percentage change on a small base | "up 300 percent" meaning one became four | report the counts, suppress percentages below a threshold |
| Reading a small agency's monthly chart | explanations for movements that are pure noise | compare variability against one over the square root of the mean first |
| Treating "within range" as a clean bill of health | a genuinely high agency dismissed because it is small | it means undetectable at this sample size, not equal |
| Treating "outside the band" as important | with enough data everything is flagged | report the size of the difference, not only the verdict |
| Suppressing small agencies entirely | the smallest agencies never get examined | pool years, or pool similar agencies, rather than dropping them |

## Check Your Understanding

<details>
<summary><b>1.</b> Elkhorn has the fourth highest rate in 2023 and the funnel says "within range". Does that mean Elkhorn is fine?</summary>

No. It means the data cannot tell. With 484 arrests and 14 incidents, Elkhorn's true rate could plausibly be anywhere from well below the state average to well above it, and one year of data cannot narrow it further. "Within range" is a statement about the evidence, not about the agency. If Elkhorn genuinely needs examining, the route is to pool several years or to compare it against other very small agencies, not to read more into a single year.
</details>

<details>
<summary><b>2.</b> Grandview's variability is 0.29 and counting alone would give 0.10. What is the other 0.19?</summary>

Real structure. Grandview is large enough that sampling noise contributes little, so almost everything you see in its monthly series is something: the July peak, the winter trough, and the multi year decline. That is exactly why a large agency's monthly chart repays attention and a small agency's does not. The same calculation tells you which kind of agency you are looking at before you start interpreting anything.
</details>

<details>
<summary><b>3.</b> Pooling seven years pushes eleven of twelve agencies outside the funnel. Should the funnel be abandoned?</summary>

No, but the verdict should stop being the headline. The funnel answers "is this difference larger than sampling can explain", and with enough data the answer is almost always yes. What changes with sample size is detectability, not importance. Report the difference in the units people care about, for example 0.25 incidents per 100 arrests, alongside the verdict, and let the reader judge whether a gap that size warrants action.
</details>

## Key Takeaway

Before comparing agencies, check how much of each one's movement is counting noise. Then use a funnel rather than a ranking, and report the size of the difference next to the verdict.

---

| | |
|---|---|
| **Previous** | [Module 3: Choosing a Denominator](Module_03_Choosing_A_Denominator.md) |
| **Next** | Part II, beginning with Module 5: Decomposition into Trend, Season and Remainder |
| **Builds on** | [Beginner Topic 10](../Beginner/Topic_10_Noise_And_Irregular_Fluctuations.md), [Module 3](Module_03_Choosing_A_Denominator.md) |
| **Used again in** | [Module 8: Rolling Statistics and Control Limits](Module_08_Rolling_Statistics_And_Control_Limits.md), [Module 12: Building a Peer Benchmark Series](Module_12_Building_A_Peer_Benchmark_Series.md) |

*This module is part of a series developed for the Washington Data Exchange for Public Safety (WADEPS) through the Center for Interdisciplinary Statistical Education and Research (CISER) at Washington State University. Version 1.0, September 2026. Questions, errors, or suggestions: yin.zhang@wsu.edu*

*All examples use synthetic data created for teaching. They do not represent any real jurisdiction, agency, officer, or incident. See [Data/DATA_DICTIONARY.md](../../Data/DATA_DICTIONARY.md).*
