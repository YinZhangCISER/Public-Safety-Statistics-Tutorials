# Topic 2: Time Series and Cross Sectional Data

> **Level:** Beginner | **Reading time:** about 5 minutes
> **Prepared by Yin Zhang**, Center for Interdisciplinary Statistical Education and Research (CISER), Washington State University

**The question this module answers:** *A report ranks our agency against the one next door. Does that ranking mean we are doing worse?*

---

## The Core Concept

There are two ways to cut a dataset, and they answer completely different questions.

**Cross sectional data** is a photograph. Many agencies, one moment in time. It tells you who is where **right now**.

**Time series data** is a movie. One agency, many moments in time. It tells you which **direction** that agency is moving.

A photograph cannot show motion. That sounds obvious, and it is still the most common mistake in public safety reporting.

## Why It Matters

Rankings are photographs. Every year a report comes out placing agencies in order, and everyone reads their own position as a verdict on how they are doing.

It is not. A ranking tells you where an agency sits today. It says nothing about whether it is climbing or falling, and those are the facts that decide whether a current strategy should be kept or abandoned.

Two agencies at the same position can be going in opposite directions at speed.

## The Example

Summit County Sheriff's Office and Lakeshore County Sheriff's Office, measured as use of force incidents per 100 arrests.

**The photograph, 2023 only:**

| Agency | Use of force per 100 arrests, 2023 |
|---|---|
| Summit County | 2.23 |
| Lakeshore County | 1.93 |

Summit County is 16 percent higher. On the strength of that one row, a report would place Lakeshore ahead, and a council member would ask Summit what has gone wrong.

**The movie, 2019 through 2025:**

| Year | 2019 | 2020 | 2021 | 2022 | 2023 | 2024 | 2025 |
|---|---|---|---|---|---|---|---|
| **Summit County** | 3.62 | 3.72 | 3.14 | 2.58 | **2.23** | 1.67 | 1.66 |
| **Lakeshore County** | 2.84 | 2.27 | 2.43 | 2.57 | **1.93** | 2.28 | 2.20 |

![Two panels. The left panel shows 2023 alone as two bars, Summit County at 2.23 and Lakeshore County at 1.93. The right panel shows both agencies from 2019 to 2025, with Summit County falling steadily from 3.62 to 1.66 and crossing below Lakeshore County, which stays near 2.2 throughout](Figures/fig_02_snapshot_and_movie.png)

Summit County has cut its rate by more than half in six years and is still falling. Lakeshore County has been sitting between 1.9 and 2.9 the whole time with no direction at all.

The 2023 snapshot happens to catch them mid crossing. The very next year the order reverses, and nothing about either agency's underlying situation changed on the day the ranking flipped.

Whatever Summit County has been doing since 2019, the snapshot gives it no credit for any of it.

## What To Watch For

- **Each view is right for a different question.** Where should we send resources this quarter? That is a photograph question. Is this agency's situation improving? That is a movie question. Using one for the other is the error.
- **A crossing point is not an event.** When two lines cross, nothing happened that year. The crossing is a consequence of directions set long before.
- **Ask for at least three years.** Two points always make a line. Three or more show whether the line is real.

## 💡 The Insight

A ranking tells you where an agency stands. Only a time series tells you where it is going, and it is the direction that tells you whether to change course.

## Check Your Understanding

<details>
<summary><b>1.</b> Using the 2023 snapshot alone, which agency appears to be managing use of force better? Using all seven years, which one actually is?</summary>

The snapshot says Lakeshore, at 1.93 against 2.23. The full series says Summit County, which has fallen from 3.62 to 1.66 while Lakeshore has gone essentially nowhere. Summit County was in much worse shape in 2019 and has done something about it. The snapshot rewards the agency that started in a better place, not the one that improved.
</details>

<details>
<summary><b>2.</b> A city council wants to decide where to put four new crisis response staff next month. Which view should they use, and why?</summary>

The photograph. Where to put people right now is a question about current conditions, and the current numbers are the right input. The movie would matter for a different decision, such as whether to keep funding a program that started three years ago. Neither view is better in general. Each is better for its own question.
</details>

## Key Takeaway

Use a snapshot to allocate resources today. Use a series to judge whether anything is working. Never let a snapshot stand in as a performance review.

---

| | |
|---|---|
| **Previous** | [Topic 1: What Is a Time Series?](Topic_01_What_Is_A_Time_Series.md) |
| **Next** | [Topic 3: Visualizing a Time Series](Topic_03_Visualizing_A_Time_Series.md) |
| **Used again in** | [Topic 14: Comparing Multiple Time Series](Topic_14_Comparing_Multiple_Time_Series.md), [Topic 18: Year over Year Comparison](Topic_18_Year_Over_Year_Comparison.md) |

*Prepared by Yin Zhang, Center for Interdisciplinary Statistical Education and Research (CISER), Washington State University. Version 1.0, September 2026. Questions, errors, or suggestions: yin.zhang@wsu.edu*

*All examples use synthetic data created for teaching. They do not represent any real jurisdiction, agency, officer, or incident. See [Data/DATA_DICTIONARY.md](../../Data/DATA_DICTIONARY.md).*
