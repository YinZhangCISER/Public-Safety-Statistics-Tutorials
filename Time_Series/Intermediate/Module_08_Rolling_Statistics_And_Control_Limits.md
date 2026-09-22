# Module 8: Rolling Statistics and Control Limits

> **Developed by Yin Zhang, PhD**, Assistant Professor, Department of Mathematics and Statistics, Washington State University

**The question this module answers:** *Is this month outside the range this agency normally runs in, and how would I know?*

---

## The Question

"Is this month unusual?" is the question public safety data is asked most often. It is also the hardest to answer casually, because unusual has to mean unusual **compared to what**.

Comparing to last month brings in the season. Comparing to a long run average brings in the trend. Comparing to a fixed threshold ignores both. This module builds the comparison properly.

## The Idea in Plain Language

A control chart has two parts.

**A centre line**, which is what you expected. It must move, because the agency's level moves and the calendar moves.

**Limits**, which say how far a month can fall from the centre line before it stops being ordinary. For counts, the natural spread is about the square root of the expected value, so limits sit at

**expected ± 3 × √(dispersion × expected)**

The dispersion term is there because real administrative counts vary more than the square root rule alone allows. Measure it rather than assuming it is 1.

## The Method

Three steps, each fixing a failure of the one before.

1. **Fixed centre line.** Baseline mean, limits at mean ± 3√mean. Fails on any seasonal or trending series.
2. **Moving centre line.** Expected value is trend × season from [Module 5](Module_05_Decomposition.md). Fixes the season and the trend.
3. **Widen for dispersion.** Measure the Pearson dispersion on ordinary months and scale the limits by its square root.

```python
expected = np.exp(stl.trend + stl.seasonal)
phi = (((observed - expected) ** 2 / expected)[ordinary]).sum() / (ordinary.sum() - 1)
upper = expected + 3 * np.sqrt(phi * expected)
```

Note the word **ordinary** in step 3. Known events must be left out when measuring routine spread, or one event inflates the limits and hides the next.

## Worked Example

Tarnbridge Police Department, which has one documented week of civil unrest in June 2021.

### Step 1: a fixed limit, and why it fails

Baseline mean for 2019 and 2020 is **32.4**, so the upper limit is **49.4**. Three months clear it:

| Month | Count | What it was |
|---|---|---|
| July 2019 | 55 | an ordinary summer |
| **June 2021** | **176** | the civil unrest |
| June 2023 | 59 | an ordinary summer |

Two false alarms out of three. The limit does not know that summer exists, so it will raise an alarm every warm month for as long as the chart is used, and the people receiving those alarms will stop reading them. It also ignores the decline, so a baseline from 2019 is too high for 2025 and nothing will ever flag at the low end.

### Steps 2 and 3: a limit that moves, widened for real spread

![Two panels of Tarnbridge monthly counts. The left panel has one flat shaded band across the whole period, with ordinary summer months marked in orange as false alarms. The right panel has a band that rises and falls with the trend and the season, and only the June 2021 spike and two marginal months sit outside it](Figures/fig_m08_control_limits.png)

With the centre line moving, July 2019 drops off the list. Measuring dispersion on the ordinary months gives **φ = 1.59**, so the counts vary about 60 percent more than the square root rule alone allows, and the limits widen accordingly.

Three months remain, and **the ranking is the finding**:

| Month | Count | Expected | Limit | Times the limit |
|---|---|---|---|---|
| **June 2021** | 176 | 32.8 | 54.5 | **3.23** |
| June 2023 | 59 | 24.5 | 43.1 | 1.37 |
| November 2022 | 35 | 17.2 | 32.8 | 1.07 |

One of these is in a different league. The other two clear the limit by a third and a fifteenth respectively, and are worth a glance at the record and probably nothing more.

**A control chart is a screening tool, not a verdict.** It produces a short list. A person decides what is on it.

### What happens if you forget to exclude the event

Leave June 2021 in when measuring ordinary spread and the dispersion rises from 1.59 to **8.74**. The limits balloon, and the chart flags **one** month: the event that broke it. Everything else becomes invisible.

One extraordinary month, left in the spread calculation, disables the instrument.

### Small agencies cannot support a monthly chart

Orrindale averages **0.81** incidents a month, so its upper limit sits at **3.5**. Across 88 months exactly **one** reaches it, which is roughly what chance alone produces at three sigma.

There is no useful monthly chart here. The fix is to change the time unit until the counts can say something: pooled to years, Orrindale runs 8, 10, 9, 13, 14, 4, 9, against an upper limit of about 19, and nothing flags. That is Beginner [Topic 4](../Beginner/Topic_04_Time_Units_Frequency_And_Aggregation.md) applied to a new purpose.

## Do It Yourself

> 📓 **Notebook:** [Module_08_Rolling_Statistics_And_Control_Limits.ipynb](Notebooks/Module_08_Rolling_Statistics_And_Control_Limits.ipynb)
> [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/YinZhangCISER/Public-Safety-Statistics-Tutorials/blob/main/Time_Series/Intermediate/Notebooks/Module_08_Rolling_Statistics_And_Control_Limits.ipynb)
> About 20 minutes.

The notebook walks all three steps, shows what a rolling mean does to an event, demonstrates the dispersion trap directly, pools Orrindale to years, and ends with a reusable `control_chart` function. The exercise runs it on Havenbrook and asks whether a use of force chart notices a reclassification of calls for service.

## Pitfalls

| What goes wrong | What it looks like | What to do |
|---|---|---|
| Flat centre line on a seasonal series | an alarm every summer, forever | move the centre with trend × season |
| Assuming the dispersion is 1 | limits too tight, a stream of marginal flags | measure it on ordinary months |
| Measuring dispersion with the event left in | limits so wide nothing is ever detected again | exclude documented events first |
| Reporting flags as in or out | three alarms treated as equally serious | rank by how far past the limit each sits |
| A monthly chart for a tiny agency | nothing detectable, or one flag a decade | change the time unit, or pool agencies |
| Using a rolling mean to detect | the mean moves a year after the event | rolling windows smooth, they do not detect |
| Charting the wrong series | a data problem in one category invisible in another | monitor the series the risk lives in, and its total |

## Check Your Understanding

<details>
<summary><b>1.</b> The rolling 12 month mean for Tarnbridge jumps after June 2021 and stays elevated for a year. Why is that a problem for detection?</summary>

Because a rolling window carries an event for as long as the window is. The mean moves only after the event has entered it, and then it stays moved until the event drops out twelve months later. By the time the rolling mean has responded, the event is old news, and while it remains in the window the elevated mean makes subsequent months look normal by comparison. Rolling windows are for smoothing and description, not for detection.
</details>

<details>
<summary><b>2.</b> Tarnbridge' dispersion is 1.59 when the unrest month is excluded and 8.74 when it is not. What is the practical consequence of using the second number?</summary>

The limits widen by about a factor of two and a third, and the chart stops detecting anything except that one event. The month that broke the instrument becomes the only thing the instrument can see. This is why documented events must be removed before measuring routine spread. It is also an argument for keeping a written record of known events, since the exclusion has to be justified rather than chosen because it improves the result.
</details>

<details>
<summary><b>3.</b> A chart flags three months. One is at 3.2 times its limit and two are at about 1.1. How should that be reported?</summary>

As one finding and two items for review, not as three alarms. Report the exceedance ratio next to each flag so the reader can see the difference. A month at 1.07 times the limit is at the edge of what a three sigma rule produces by chance a few times in a hundred, so with 88 months a couple of marginal flags are expected even if nothing at all has happened. Presenting them at the same weight as a threefold exceedance destroys the credibility of the chart.
</details>

## Key Takeaway

Move the centre line with the trend and the season, measure the dispersion on ordinary months only, and rank the flags by how far past the limit they sit. The chart screens; a person decides.

---

| | |
|---|---|
| **Previous** | [Module 7: Seasonal Adjustment](Module_07_Seasonal_Adjustment.md) |
| **Next** | Part III, beginning with Module 9: Year over Year, Rolling Totals and Indexing |
| **Builds on** | [Module 4](Module_04_Why_Small_Agencies_Look_Volatile.md), [Module 5](Module_05_Decomposition.md), [Module 7](Module_07_Seasonal_Adjustment.md) |
| **Used again in** | [Module 16](Module_16_Did_Something_Change.md), and Advanced Modules 2 and 12 |

*This module is part of a series developed for the Washington Data Exchange for Public Safety (WADEPS) through the Center for Interdisciplinary Statistical Education and Research (CISER) at Washington State University. Version 1.0, September 2026. Questions, errors, or suggestions: yin.zhang@wsu.edu*

*All examples use synthetic data created for teaching. They do not represent any real jurisdiction, agency, officer, or incident. See [Data/DATA_DICTIONARY.md](../../Data/DATA_DICTIONARY.md).*
