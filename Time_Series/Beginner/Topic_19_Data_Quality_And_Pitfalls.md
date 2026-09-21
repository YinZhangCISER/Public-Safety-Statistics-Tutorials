# Topic 19: Data Quality and Common Pitfalls

> **Developed by Yin Zhang, PhD**, Assistant Professor, Department of Mathematics and Statistics, Washington State University

**The question this module answers:** *One category of calls jumped 54 percent. Did something happen, or did the data change?*

---

## The Core Concept

A time series does not record what happened. It records **what was written down about what happened**.

Between the event and the number there is a dispatcher, a classification scheme, a records system, a reporting deadline, and a person with a keyboard. A change to any of those moves the number without anything moving in the world.

These are **data artifacts**, and they look exactly like real findings. They are often larger than real findings, because a real change of 10 percent is a big deal while a reclassification can move a category by 50 percent overnight.

## Why It Matters

An artifact mistaken for a finding sends an organisation after a problem that does not exist, and it damages trust in the data permanently once discovered. An artifact mistaken for a finding in the other direction hides a real problem behind an apparent improvement.

The good news is that most artifacts have a signature. Once you know what to look for, they are easier to spot than genuine change.

## The Example

Harbor Point Police Department reclassified some of its dispatch codes in January 2023. Calls that used to be labelled `Other` began to be labelled `Public Order Offense`. No new calls, no change in what officers did, only a change in the label.

| | 2022 monthly average | 2023 monthly average | Change |
|---|---|---|---|
| Public order calls | 653 | 1,005 | **up 54 percent** |
| Calls labelled Other | 1,122 | 834 | **down 26 percent** |
| **All calls for service** | **4,527** | **4,649** | **up 3 percent** |

![Two panels. The left panel shows Harbor Point's public order calls and total calls, each divided by its own 2022 average, from mid 2021 to mid 2024. Public order calls jump above 1.4 at the start of 2023 and stay there, while the total line stays flat around 1.0 throughout. The right panel shows total statewide calls for service by month, with the final two months shown in orange at roughly three quarters and one half of the normal level](Figures/fig_19_data_quality.png)

**A briefing built on the first row alone would report a public order crisis.** Up 54 percent, sustained, starting on a clean date.

**The third row rules it out.** Total calls for service rose 3 percent. If public order incidents had genuinely surged, total calls would have risen with them. They did not, because the extra public order calls were subtracted from somewhere else. The second row says where.

**That is the diagnostic, and it is a simple one: check the total.** A real increase in one category adds to the total. A reclassification moves calls between categories and leaves the total alone.

**The other pitfall in the chart** is on the right. The last two months of every dataset are lower than the months before them, and nothing has happened. Records are still being entered. Statewide calls run near 100,000 a month, then show 77,000 and 50,000 for the two most recent months. Those are called **provisional** and they are incomplete by construction. Any chart that plots them without marking them shows a sharp improvement that will quietly disappear in six weeks.

## The Six Pitfalls

| Pitfall | What it looks like | How to check |
|---|---|---|
| **Reclassification** | One category jumps or drops sharply on a clean date. The total does not move. | Compare the category against the total. Ask for the policy memo and its date. |
| **New records system** | Several series shift at once, on the same date, with no external event. | Ask when the system was replaced. Treat before and after as separate series until proven otherwise. |
| **Reporting lag** | The most recent one or two months are unusually low. | Mark them provisional and exclude them. Recheck in 60 days. See [Topic 6](Topic_06_Missing_Time_Points_And_Reporting_Gaps.md). |
| **Backlog entry** | A single month spikes, then the following months are normal. | Ask whether records were entered in a batch. A real spike has a real event behind it. See [Topic 11](Topic_11_Outliers_And_Spikes.md). |
| **Under reporting** | A quiet period that coincides with a staffing shortage or a system outage. | Cross check against another source, such as arrests or calls for service. |
| **Missing periods** | A line runs smoothly across months that were never submitted. | List the periods actually present in the file before plotting anything. |

## What To Watch For

- **Ask for the date, then ask what else happened on it.** Artifacts start on administrative dates: the first of a month, the start of a fiscal year, the day a contract began. Real change rarely does.
- **A clean break is suspicious.** Genuine change is usually gradual, because of the lag and the memory in [Topics 15](Topic_15_Lagged_Effects.md) and [16](Topic_16_Autocorrelation.md). A series that steps to a new level in one month and stays there is more likely to be a definition change.
- **Check the total whenever a category moves.** This single habit catches most reclassifications.
- **Data quality is not a technical footnote.** Deciding whether the numbers can support a decision is part of making the decision.

## 💡 The Insight

Before asking what caused a change in the data, ask whether anything changed in the world at all. Sometimes only the paperwork moved.

## Check Your Understanding

<details>
<summary><b>1.</b> Harbor Point's public order calls rose 54 percent while its total calls rose 3 percent. Why does the second number settle the question?</summary>

Because calls have to come from somewhere. A genuine increase of 352 public order calls a month would push the total up by roughly the same amount, which would be about 8 percent. The total barely moved, so those calls were not new; they were relabelled from another category. The `Other` category falling by 288 a month confirms it.
</details>

<details>
<summary><b>2.</b> A dashboard shows statewide calls for service falling sharply in the two most recent months. A manager asks what caused the drop. What is the answer?</summary>

Most likely nothing. Those months are provisional and their records are still being entered. The right response is to exclude them, state that they are incomplete, and look again in about two months, by which time they will almost certainly have risen to the normal level. A dashboard that does not mark provisional months will generate this same false alarm every single month.
</details>

<details>
<summary><b>3.</b> An agency's assault calls drop 40 percent in one month and stay at the new level. Its total calls also drop 40 percent and stay there. Is this a reclassification?</summary>

No, and that makes it more worrying, not less. A reclassification moves calls between categories and leaves the total alone. Here the total fell too, so the calls did not move elsewhere; they stopped being recorded. The likely explanations are a system failure, a change in what gets submitted, or a genuine collapse in reporting. Any of those needs urgent attention, and none of them is a 40 percent improvement in public safety.
</details>

## Key Takeaway

When a number moves, check the total, check the date, and ask what changed administratively. Only then start looking for a cause in the world.

---

| | |
|---|---|
| **Previous** | [Topic 18: Year over Year Comparison](Topic_18_Year_Over_Year_Comparison.md) |
| **Next** | [Topic 20: How to Read a Time Series Chart](Topic_20_How_To_Read_A_Chart_Checklist.md) |
| **Builds on** | [Topic 6: Missing Time Points and Reporting Gaps](Topic_06_Missing_Time_Points_And_Reporting_Gaps.md), [Topic 11: Outliers and Spikes](Topic_11_Outliers_And_Spikes.md) |
| **Used again in** | [Topic 20: How to Read a Time Series Chart](Topic_20_How_To_Read_A_Chart_Checklist.md) |

*This module is part of a series developed for the Washington Data Exchange for Public Safety (WADEPS) through the Center for Interdisciplinary Statistical Education and Research (CISER) at Washington State University. Version 1.0, September 2026. Questions, errors, or suggestions: yin.zhang@wsu.edu*

*All examples use synthetic data created for teaching. They do not represent any real jurisdiction, agency, officer, or incident. See [Data/DATA_DICTIONARY.md](../../Data/DATA_DICTIONARY.md).*
