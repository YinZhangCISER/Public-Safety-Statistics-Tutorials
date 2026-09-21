# Topic 6: Missing Time Points and Reporting Gaps

> **Developed by Yin Zhang, PhD**, Assistant Professor, Department of Mathematics and Statistics, Washington State University

**The question this module answers:** *The line on this chart has no break in it. Does that mean every month is actually in there?*

---

## The Core Concept

A time series is a chain. Every link is one time period, and the links have to be in order with none left out.

When a period is missing, two things can be true, and they are not the same thing at all:

- **A zero** means the agency reported, and the answer was none. That is information.
- **A gap** means the agency did not report. That is the absence of information.

Charting software treats them very differently, and neither treatment is safe by default.

## Why It Matters

Gaps in public safety data are common and rarely random. They happen because a records system was being replaced, because a paper backlog was never entered, because a small agency lost the one person who did the reporting, or because a reporting requirement changed mid year.

The danger is that most charting tools **draw straight through a gap**. The line looks continuous, the reader sees no problem, and a period nobody has any information about gets silently filled in with a guess.

Worse, gaps often line up with exactly the periods people most want to know about. A system replacement is a disruptive event. The months it eats are not ordinary months.

## The Example

Prairie County Sheriff's Office, calls for service. Here is what the file actually contains for 2022.

| Month | Jan | Feb | Mar | Apr | May | Jun | Jul | Aug |
|---|---|---|---|---|---|---|---|---|
| **Calls for service** | 1,296 | 1,415 | *no row* | *no row* | *no row* | 1,559 | 1,657 | 1,572 |

March, April and May are not zero. They are not blank. **The rows do not exist.** The agency was migrating to a new records management system and never submitted them.

![Three panels. The left panel draws a continuous line straight across the missing months, so nothing looks wrong. The middle panel leaves the line broken with the three months shaded and labelled as never submitted. The right panel shows Elkhorn's 2023 counts as bars, with orange dots marking the four months that reported a genuine zero](Figures/fig_06_missing_and_zero.png)

**Left: the line runs straight through.** This is what happens by default. The chart shows a smooth rise from February to June. Nobody looking at it would know that three fifths of that rise is invented.

**Middle: the gap is left open.** Same data, drawn honestly. Now the reader can see that there is a hole, and can ask about it.

**What actually happened in those months?** Nobody knows. The plausible answers are far apart:

- If calls ran at the usual level, about 1,450 a month, then roughly 4,350 calls are missing from every total that includes 2022.
- If the migration also disrupted dispatch, the true number could be lower.
- If the migration caused a backlog that was later entered under June, then June's 1,559 is inflated and the following months are wrong too.

The straight line picks one of these silently. It picks the most comforting one.

**Right: a zero is not a gap.** Elkhorn Police Department has eight officers. In 2023 it reported 0, 2, 1, 0, 2, 0, 4, 0, 2, 1, 1, 1. Four of those months are genuine zeros, marked with orange dots. Elkhorn reported, and the honest answer was none. Those months belong in every average. Prairie County's three months do not.

## What To Watch For

- **Ask whether the gap is random.** A missing month caused by one employee's vacation is very different from one caused by an event that also changed what the data would have shown.
- **Never let a tool fill a gap without saying so.** If a number was estimated, it should be labelled as estimated everywhere it appears.
- **A zero must be stored as a zero.** If an agency's reporting system writes blanks instead of zeros for quiet months, its averages will come out too high, because the quiet months are dropped rather than counted.
- **The last month or two are usually incomplete.** Grandview recorded 43,408 calls in April 2026, then 32,513 in May and 21,758 in June. Nothing happened in Grandview. Those records are still being entered. Data this recent is called **provisional** and should be flagged, not plotted as though it were final. [Topic 19](Topic_19_Data_Quality_And_Pitfalls.md) returns to this.

## 💡 The Insight

A zero is an answer. A gap is a question. A chart that draws them the same way has answered a question nobody could answer.

## Check Your Understanding

<details>
<summary><b>1.</b> An annual report shows Prairie County had 16,900 calls for service in 2022, down 11 percent from 2021. Is that a real decline?</summary>

No. The 2022 total is the sum of nine months, because three were never submitted. Comparing nine months to twelve produces a decline of roughly a quarter before anything real happens at all. The honest options are to report the nine month total clearly labelled as such, or to compare the same nine months in both years, or to say that 2022 cannot be compared.
</details>

<details>
<summary><b>2.</b> A small agency's file has no rows at all for several quiet months. Its reported average is 3.1 incidents a month. Is that average too high, too low, or right?</summary>

Too high. The quiet months are the ones that went missing, so the average is being taken over only the busier months. If the missing months were genuine zeros, they should be included, and including them would pull the average down. This is exactly why the distinction between a zero and a gap matters for something as ordinary as an average.
</details>

<details>
<summary><b>3.</b> Why is a gap that coincides with a records system replacement more troubling than a gap caused by a staff vacancy?</summary>

Because the system replacement is itself an event that could change the numbers. Categories may be defined differently in the new system, and a backlog may be entered all at once afterwards. So the gap is not just missing information, it is a warning that the data on either side of it may not be comparable. A vacancy removes information without changing what the rest of the series means.
</details>

## Key Takeaway

Before trusting any line, ask which periods are actually in the file. Then ask why the missing ones are missing, and whether the reason could also have changed the numbers.

---

| | |
|---|---|
| **Previous** | [Topic 5: Counts and Rates](Topic_05_Counts_And_Rates.md) |
| **Next** | [Topic 7: Trend, the Long Term Direction](Topic_07_Trend.md) |
| **Builds on** | [Topic 3: Visualizing a Time Series](Topic_03_Visualizing_A_Time_Series.md) |
| **Used again in** | [Topic 13: Smoothing and Moving Averages](Topic_13_Smoothing_And_Moving_Averages.md), [Topic 19: Data Quality and Common Pitfalls](Topic_19_Data_Quality_And_Pitfalls.md) |

*This module is part of a series developed for the Washington Data Exchange for Public Safety (WADEPS) through the Center for Interdisciplinary Statistical Education and Research (CISER) at Washington State University. Version 1.0, September 2026. Questions, errors, or suggestions: yin.zhang@wsu.edu*

*All examples use synthetic data created for teaching. They do not represent any real jurisdiction, agency, officer, or incident. See [Data/DATA_DICTIONARY.md](../../Data/DATA_DICTIONARY.md).*
