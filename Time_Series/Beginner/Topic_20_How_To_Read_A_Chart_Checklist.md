# Topic 20: How to Read a Time Series Chart

> **Developed by Yin Zhang, PhD**, Assistant Professor, Department of Mathematics and Statistics, Washington State University

**The question this module answers:** *A chart has just been put on the screen. What should be checked, and in what order?*

---

## The Core Concept

Everything in this series comes down to a habit: **ask the same twelve questions of every chart, in the same order, before forming any opinion about it.**

The order matters. Questions 1 and 2 establish what is being shown. Questions 3 to 7 read the patterns. Questions 8 to 11 test whether the apparent finding survives context. Question 12 asks whether the data can be trusted at all. Skipping to the end and reacting to the shape is how most misreadings happen.

None of this requires mathematics. It requires refusing to react until the list is finished.

## The Twelve Questions

| # | Question | What you are looking for | Topic |
|---|---|---|---|
| **What am I looking at** ||||
| 1 | What is the time unit? | Daily, monthly, yearly. Does it match the question being asked? | [4](Topic_04_Time_Units_Frequency_And_Aggregation.md) |
| 2 | Does the vertical axis start at zero? | If not, the movement is being magnified. | [3](Topic_03_Visualizing_A_Time_Series.md) |
| **What is in it** ||||
| 3 | Is there a trend? | A direction sustained across years, not months. | [7](Topic_07_Trend.md) |
| 4 | Is there seasonality? | The same months high or low every year. | [8](Topic_08_Seasonality.md) |
| 5 | Are there outliers? | A point far outside the normal range, with an event behind it. | [11](Topic_11_Outliers_And_Spikes.md) |
| 6 | Is any period missing? | A line drawn across months that were never submitted. | [6](Topic_06_Missing_Time_Points_And_Reporting_Gaps.md) |
| 7 | Is there more than one series, and do they move together? | Together means a shared cause. Apart means a local one. | [14](Topic_14_Comparing_Multiple_Time_Series.md) |
| **Does the finding survive** ||||
| 8 | Is this a count or a rate? | A count rises when activity rises. Ask what the denominator is. | [5](Topic_05_Counts_And_Rates.md) |
| 9 | What did the same period last year look like? | The only comparison that removes the season. | [18](Topic_18_Year_Over_Year_Comparison.md) |
| 10 | Could a lag be involved? | Did something change three to six months before this? | [15](Topic_15_Lagged_Effects.md) |
| 11 | Is this movement bigger than usual for this series? | Compare the step to the steps this series normally takes. | [10](Topic_10_Noise_And_Irregular_Fluctuations.md), [13](Topic_13_Smoothing_And_Moving_Averages.md) |
| **Can I trust it** ||||
| 12 | Could a data problem explain this? | Reclassification, new system, reporting lag, backlog. Check the total. | [19](Topic_19_Data_Quality_And_Pitfalls.md) |

## A Worked Example

![Tarnbridge Police Department monthly use of force incidents from 2019 to 2026, with numbered callouts marking that the axis starts at zero, the ordinary range of roughly 15 to 45 a month, the documented outlier of 176 in June 2021, the yearly average drifting downward, and the final two months shown in orange as incomplete](Figures/fig_20_reading_a_chart.png)

Working the list against this chart:

**1. Time unit.** Monthly, over seven and a half years. Appropriate for almost any question about this agency.

**2. Axis.** Starts at zero. The June 2021 spike really is about six times a normal month, and the chart is not exaggerating it.

**3. Trend.** Yes, downward. The yearly average falls from 31.7 incidents a month in 2019 to 21.0 in 2025, a reduction of about a third.

**4. Seasonality.** Not visible here, and this is worth dwelling on. Averaged across all seven years, July runs about 40 percent above this agency's annual average. But Tarnbridge records only about 25 incidents a month, so in any single year the noise is larger than the seasonal signal and the peaks do not line up to the eye. **Absence from the chart is not absence from the data.** Checking seasonality properly means averaging the same month across years, as in [Topic 8](Topic_08_Seasonality.md), not looking harder at this picture.

**5. Outliers.** One, and it is unmissable: June 2021, 176 incidents against a typical month of 31, caused by a documented week of civil unrest. Every average that includes it needs a footnote. See [Topic 11](Topic_11_Outliers_And_Spikes.md).

**6. Missing periods.** None. Tarnbridge submitted every month. Another agency in this dataset did not, so this question has to be asked rather than assumed.

**7. Other series.** Only one is shown, which is the chart's main weakness. Nothing here can distinguish something Tarnbridge did from something that happened across the state. The comparison agencies from [Topic 14](Topic_14_Comparing_Multiple_Time_Series.md) belong on this chart.

**8. Count or rate.** Count. The decline could partly reflect fewer arrests rather than less force per arrest. On the rate, Tarnbridge ran at 3.34 per 100 arrests in 2023, the highest of the twelve agencies, even though its count was only third. See [Topic 5](Topic_05_Counts_And_Rates.md). **The count chart and the rate chart tell different stories about this agency, and the count chart is the flattering one.**

**9. Same period last year.** Available for every month and not shown. A year over year column would be the single most useful addition.

**10. Lag.** Yes. Tarnbridge adopted the de escalation training in July 2023. Anything in the second half of 2023 should be read with the four month phase in from [Topic 15](Topic_15_Lagged_Effects.md) in mind.

**11. Bigger than usual.** For most of the series, no. The month to month movement of roughly 15 to 45 is what this agency normally does. June 2021 is the one exception.

**12. Data problems.** The final two months, in orange, are provisional and still being entered. They must be excluded from any average or trend. See [Topic 19](Topic_19_Data_Quality_And_Pitfalls.md).

**The verdict.** A genuinely improving agency, with one documented crisis month, whose progress should be checked against comparison agencies and expressed as a rate before anyone celebrates. That conclusion took twelve questions and no mathematics at all.

## What To Watch For

- **Work the list before forming an opinion,** not afterwards to justify one.
- **Most charts fail question 7 or question 8.** One series, and a count rather than a rate. Those two omissions account for most misreadings in public safety reporting.
- **A question you cannot answer is a finding.** If nobody can say whether the last month is provisional, that is the thing to report.
- **Keep the list where the charts are.** It is a reference, not something to memorise.

## 💡 The Insight

Good analysis is not about knowing more methods. It is about asking the same questions every time, including the ones whose answers are inconvenient.

## Check Your Understanding

<details>
<summary><b>1.</b> Which question in the list would most often have caught the Havenbrook reclassification from Topic 19?</summary>

Question 12, and specifically its instruction to check the total. The public order category jumped 54 percent while total calls rose 3 percent, which is the signature of calls being relabelled rather than added. Question 5 might also have flagged it, since the jump was sudden and landed on a clean administrative date, but the total is what settles it.
</details>

<details>
<summary><b>2.</b> A chart shows one agency, monthly counts, axis starting at 40, most recent month included, no comparison agency. Which questions has it already failed?</summary>

Question 2, because the truncated axis exaggerates every movement. Question 7, because one series cannot separate a local cause from a shared one. Question 8, because counts without a denominator confuse volume with behaviour. And probably question 12, since the most recent month is almost certainly provisional. Four failures before anyone has looked at the line.
</details>

<details>
<summary><b>3.</b> Why is question 4 answered "not visible here" for Tarnbridge rather than "no"?</summary>

Because those are different claims. "No" would mean the agency has no seasonal pattern, which is false: averaged over seven years its July runs about 40 percent above the annual average. "Not visible here" means this particular chart cannot show it, because at roughly 25 incidents a month the random variation is larger than the seasonal effect in any single year. Answering "no" would lead someone to schedule summer staffing as though July were an ordinary month.
</details>

## Key Takeaway

Print the twelve questions and keep them with the reports. Work through them in order, every time, and do not react until the list is finished.

---

| | |
|---|---|
| **Previous** | [Topic 19: Data Quality and Common Pitfalls](Topic_19_Data_Quality_And_Pitfalls.md) |
| **Next** | The [Intermediate level](../Intermediate/), which builds these series from records and measures them in code |
| **Builds on** | Every topic in this series |

*This module is part of a series developed for the Washington Data Exchange for Public Safety (WADEPS) through the Center for Interdisciplinary Statistical Education and Research (CISER) at Washington State University. Version 1.0, September 2026. Questions, errors, or suggestions: yin.zhang@wsu.edu*

*All examples use synthetic data created for teaching. They do not represent any real jurisdiction, agency, officer, or incident. See [Data/DATA_DICTIONARY.md](../../Data/DATA_DICTIONARY.md).*
