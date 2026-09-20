# Topic 15: Lagged Effects

> **Prepared by Yin Zhang**, Center for Interdisciplinary Statistical Education and Research (CISER), Washington State University

**The question this module answers:** *A new training program launched three months ago and the numbers have not moved. Should it be cancelled?*

---

## The Core Concept

A **lag** is the delay between doing something and being able to see its effect in the data.

Almost nothing in a large organisation takes effect the moment it is announced. Training has to be delivered shift by shift. Officers have to practise a new skill enough times for it to become the thing they do under pressure. Supervisors have to reinforce it. And then enough incidents have to occur for the change in how they are handled to show up in a monthly count.

Every one of those steps takes time, and they run in sequence.

## Why It Matters

Evaluation deadlines are set by budget cycles and political calendars. Effects arrive on their own schedule. The two have nothing to do with each other, and when they collide the evaluation usually wins.

The result is a specific and expensive failure: **a program that works gets cancelled before it has had time to work.** The early numbers show nothing, which is exactly what they should show, and the absence of an effect that could not yet exist is read as proof that there is none.

The protection is to decide, in writing and in advance, when the effect is expected to appear and how big it should be by then. A prediction made before the data arrives can be checked. A judgment made afterwards cannot.

## The Example

In July 2023, five agencies in this dataset adopted a de escalation training program. Seven did not. The five were not picked at random: they were chosen because their use of force rates were the highest, which is why they start well above the others.

![Two panels. The left panel shows the twelve month trailing use of force rate for the two groups from 2020 to 2026, with the trained group starting near 3.9 and the others near 3.0, both declining, a dashed line marking the July 2023 start, and a circle marking September 2023 where the trained group has not moved. The right panel shows three bars: the gap between the groups was 20.9 percent before the program, 17.2 percent in the first three months, and 8.3 percent once the program was fully in place](Figures/fig_15_lagged_effects.png)

| Period | Trained agencies | The other agencies | Gap |
|---|---|---|---|
| 12 months before, July 2022 to June 2023 | 3.04 | 2.52 | trained are **20.9 percent** higher |
| First 3 months, July to September 2023 | 3.26 | 2.78 | trained are **17.2 percent** higher |
| Fully in place, November 2023 onward | 2.33 | 2.15 | trained are **8.3 percent** higher |

*Rates are use of force per 100 arrests. June 2021 in Cedar Falls is excluded throughout, for the reason given in [Topic 11](Topic_11_Outliers_And_Spikes.md).*

**Three months in, there is essentially nothing.** The gap moved from 20.9 percent to 17.2 percent, a change small enough to be ordinary month to month variation. A report written in the autumn of 2023 would have been accurate in saying that the trained agencies were no better off, and it would have been used to argue for ending the program.

**Once the program was fully in place, the gap halved.** It fell from 20.9 percent to 8.3 percent. Relative to the comparison agencies, the trained agencies ended up about 10 percent lower than they had been.

The program in this teaching dataset was built with a true effect of a 12 percent reduction, phased in over four months. See [Data/GROUND_TRUTH.md](../../Data/GROUND_TRUTH.md). The full effect did not exist in September 2023, because it had not finished arriving. The evaluation was not measuring a weak program. It was measuring a program that had not happened yet.

**Notice also that both groups fell.** The comparison agencies went from 2.52 to 2.15 without any training at all, because everything in this dataset is improving at about 5 percent a year. An evaluation that looked only at the trained agencies would have credited the program with their entire decline, which is several times the truth. That is why the comparison group from [Topic 14](Topic_14_Comparing_Multiple_Time_Series.md) is in every row of the table.

## What To Watch For

- **Write down the expected lag before launch.** "We expect to see a measurable difference by month six" is a testable commitment. Deciding afterwards what counts as enough time is not.
- **Bigger organisations lag longer.** Rolling training through 900 officers takes longer than through 30.
- **Measurement adds its own lag.** A twelve month trailing average in December of the launch year is mostly describing the year before the launch. See [Topic 13](Topic_13_Smoothing_And_Moving_Averages.md).
- **Distinguish the three reasons a program shows nothing.** It has not taken effect yet. It has taken effect and does not work. Or the measurement cannot detect an effect this size. These call for completely different responses, and the first months of data cannot tell them apart.
- **A lag runs both ways.** When a program ends, the numbers do not bounce back the next month either. A period of good results after cancellation is not evidence that the program was unnecessary.

## 💡 The Insight

The absence of an effect in month two is not evidence about the program. It is evidence about month two.

## Check Your Understanding

<details>
<summary><b>1.</b> In the autumn of 2023 an analyst reports that the trained agencies are still 17 percent above the others and recommends ending the program. What is wrong with the reasoning, not the arithmetic?</summary>

The arithmetic is right. The reasoning treats "no difference yet" as "no difference", when the program was still being rolled out and the full effect did not exist until November. The recommendation would have ended a program that went on to close more than half the gap. The correct report says the effect cannot yet be measured and names the date at which it can.
</details>

<details>
<summary><b>2.</b> The comparison agencies improved from 2.52 to 2.15 without any training. What would the trained agencies' improvement have looked like if nobody had checked the comparison group?</summary>

Much larger and entirely wrong. The trained agencies went from 3.04 to 2.33, a fall of about 23 percent, and all of it would have been credited to the program. But most of that fall is the statewide decline the comparison agencies also experienced. Subtracting what would have happened anyway leaves roughly 10 percent, which is close to the 12 percent actually built into this dataset. The comparison group is what converts a misleading 23 into a defensible 10.
</details>

<details>
<summary><b>3.</b> A program launches in January and the numbers fall sharply in February. Is that good news?</summary>

It is suspicious news. A large effect appearing in the very first month is faster than most real interventions can work, so the more likely explanations are seasonal decline from a January peak, ordinary noise, or a change in recording that coincided with the launch. A result arriving far earlier than the expected lag deserves as much scrutiny as one that never arrives at all.
</details>

## Key Takeaway

Decide when you expect to see an effect before you launch, measure against agencies that did not adopt the program, and refuse to judge before the date you named.

---

| | |
|---|---|
| **Previous** | [Topic 14: Comparing Multiple Time Series](Topic_14_Comparing_Multiple_Time_Series.md) |
| **Next** | [Topic 16: Autocorrelation, the Memory of Data](Topic_16_Autocorrelation.md) |
| **Builds on** | [Topic 13: Smoothing and Moving Averages](Topic_13_Smoothing_And_Moving_Averages.md), [Topic 14: Comparing Multiple Time Series](Topic_14_Comparing_Multiple_Time_Series.md) |
| **Used again in** | [Topic 20: How to Read a Time Series Chart](Topic_20_How_To_Read_A_Chart_Checklist.md), and throughout the [Causal Inference series](../../Causal_Inference/) |

*Prepared by Yin Zhang, Center for Interdisciplinary Statistical Education and Research (CISER), Washington State University. Version 1.0, September 2026. Questions, errors, or suggestions: yin.zhang@wsu.edu*

*All examples use synthetic data created for teaching. They do not represent any real jurisdiction, agency, officer, or incident. See [Data/DATA_DICTIONARY.md](../../Data/DATA_DICTIONARY.md).*
