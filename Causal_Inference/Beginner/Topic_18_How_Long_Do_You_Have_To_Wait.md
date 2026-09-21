# Topic 18: How Long Do You Have to Wait?

> **Developed by Yin Zhang, PhD**, Assistant Professor, Department of Mathematics and Statistics, Washington State University

**The question this module answers:** *Everything was done correctly and the result was "no significant effect." Does that mean the program did not work?*

---

## The Core Concept

An evaluation can be right about everything and still produce nothing, because it did not wait long enough.

Monthly incident counts bounce around. To tell a real 12 percent change from that bouncing takes a certain number of months, and until you have them, the honest answer is **"not enough evidence yet"** rather than **"it did not work."**

Those two sentences are routinely written the same way, and they mean opposite things.

## Why It Matters

Program funding runs in one and two year cycles. Evaluations are commissioned to arrive before the next budget. The result is a large number of reports that measure an effect too early and report the absence of evidence as evidence of absence.

A program that genuinely works can be cancelled this way, by a study that did nothing wrong.

## The Example

The same program, the same agencies, the same correct method. The only thing that changes is when the report was written.

![Five estimates with confidence intervals, at 8, 14, 20, 26 and 30 months after the training was fully in place. The 8 month estimate is minus 5.7 percent with an interval crossing zero, marked in orange. The later four are minus 9.0, minus 10.1, minus 11.7 and minus 12.6 percent, with intervals that exclude zero, and they close in on a dashed line at the true 12 percent](Figures/fig_18_how_long.png)

| Report written | Estimate | 95 percent interval | What it would say |
|---|---|---|---|
| **8 months in** | **−5.7%** | **[−15.3, +5.0]** | **"no significant effect"** |
| 14 months in | −9.0% | [−16.2, −1.1] | a significant reduction |
| 20 months in | −10.1% | [−16.4, −3.3] | a significant reduction |
| 26 months in | −11.7% | [−17.3, −5.7] | a significant reduction |
| 30 months in | −12.6% | [−17.9, −6.9] | a significant reduction |

The program's real effect was **12 percent the whole time**. It did not grow. The evidence grew.

At eight months the interval runs from a 15 percent reduction to a 5 percent increase. That interval is **compatible with the truth** and also compatible with nothing at all, which is exactly what "not enough evidence yet" means.

## What To Watch For

- **"No significant effect" is not "no effect."** It means the interval includes zero. Look at the interval: if it also includes a large effect, the study has not ruled anything out.
- **Ask what the study could have detected.** A good report states the smallest effect it had a fair chance of finding. If that number is bigger than any effect anyone expected, the study was never going to work.
- **Decide the reporting date in advance.** Checking every month and reporting when the result turns significant is a different procedure with a different, much higher, false positive rate.
- **Small agencies need longer, or need pooling.** An agency with one incident a month may never accumulate enough evidence on its own, no matter how long it waits.
- **An early null is still worth publishing**, phrased correctly: "after eight months the data cannot distinguish an effect of 15 percent from no effect at all."

## 💡 The Insight

Absence of evidence is not evidence of absence, and the difference between them is usually just a calendar.

## Check Your Understanding

<details>
<summary><b>1.</b> At eight months the estimate is 5.7 percent and the truth is 12. Was the estimate wrong?</summary>

Not in any useful sense. The truth of 12 percent sits comfortably inside the interval from 15.3 down to 5.0 up, which is what an interval is for. A single estimate from limited data lands somewhere in a range; this one landed on the low side. What would be wrong is reporting the 5.7 percent point estimate as the effect, or reporting the interval as evidence that the program did nothing.
</details>

<details>
<summary><b>2.</b> Why do the intervals get narrower as time passes, when the monthly numbers are just as noisy?</summary>

Because there are more of them. Each additional month of treated data adds evidence about the same underlying difference, and averaging over more months makes the accidental ups and downs cancel out. The noise per month is unchanged; the noise in the average shrinks.
</details>

<details>
<summary><b>3.</b> A council wants an answer in six months. What should be promised?</summary>

An honest description of what six months can deliver, given before the work starts. On this data that is an interval about twenty points wide, which will almost certainly include zero, so the study cannot distinguish a working program from a useless one. The right response is to say so up front and propose either a longer window, a larger group of agencies, or an interim report that explicitly reports what has not yet been ruled out.
</details>

## Key Takeaway

Before starting, work out what the study could detect. Before believing a null result, ask what it could have detected.

---

| | |
|---|---|
| **Previous** | [Topic 17: When You Cannot Randomize](Topic_17_When_You_Cannot_Randomize.md) |
| **Next** | [Topic 19: Reading a Causal Claim in the News](Topic_19_Reading_A_Causal_Claim.md) |
| **Builds on** | [Topic 8](Topic_08_Two_Differences_Are_Better_Than_One.md), [Topic 9](Topic_09_Were_They_Moving_Together_Before.md) |
| **Used again in** | [Topic 19](Topic_19_Reading_A_Causal_Claim.md), [Topic 20](Topic_20_Questions_To_Ask.md) |

*This module is part of a series developed for the Washington Data Exchange for Public Safety (WADEPS) through the Center for Interdisciplinary Statistical Education and Research (CISER) at Washington State University. Version 1.0, September 2026. Questions, errors, or suggestions: yin.zhang@wsu.edu*

*All examples use synthetic data created for teaching. They do not represent any real jurisdiction, agency, officer, or incident. See [Data/DATA_DICTIONARY.md](../../Data/DATA_DICTIONARY.md).*
