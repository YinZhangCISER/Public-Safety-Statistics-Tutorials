# Topic 4: Before and After Is Not Enough

> **Developed by Yin Zhang, PhD**, Assistant Professor, Department of Mathematics and Statistics, Washington State University

**The question this module answers:** *The most natural comparison in the world is before against after. How wrong can it be?*

---

## The Core Concept

A before and after comparison uses the agency's own past as the counterfactual. It assumes that without the program, the future would have looked like the past.

That assumption is almost never true, and when it fails it fails in a predictable direction: **toward making the program look good.** Programs are usually started when a problem is at its worst, and things at their worst tend to get better.

## Why It Matters

This is the single most common way a public safety evaluation goes wrong, and it is not a mistake made by careless people. It is made by careful people who compute the right number for the wrong question.

In the dataset used throughout this series, the true effect of the training program is known exactly, because it was built in on purpose. It is a **12 percent** reduction. That makes it possible to grade a before and after comparison instead of arguing about it.

## The Example

The five agencies that adopted the training, comparing the period before it started against the period after it was fully in place.

![Two panels. The left shows two bars for the trained agencies, 3.48 use of force per 100 arrests before and 2.33 after, with an arrow marking a 33.1 percent fall. The right compares that 33.1 percent against the true effect of 12.0 percent as two horizontal bars](Figures/fig_04_before_and_after.png)

| | Use of force per 100 arrests |
|---|---|
| Before the training | **3.48** |
| After it was fully in place | **2.33** |
| **Change** | **−33.1%** |

Every number here is correct. The arithmetic is right, the data are right, the periods are right.

**And the answer is wrong by nearly a factor of three.** The training reduced use of force by 12 percent. A before and after comparison reports 33 percent.

Nothing was miscalculated. The comparison answered the question "what happened to these agencies?" and was then used to answer "what did the training do?" Those are different questions, and the gap between 33 and 12 is the price of swapping them.

## What To Watch For

- **The error is large, not marginal.** This is not a matter of a few percentage points. Nearly two thirds of the reported decline belongs to something else.
- **It is biased in a known direction.** Before and after comparisons flatter programs. If you only have one, you know which way it is wrong, which is worth something.
- **More data does not help.** Ten years of before and after is still before and after. The problem is the comparison, not the sample size.
- **It is still worth computing.** It answers a real question, and it is the number a chief already has in their head. Report it, label it, and then show the better one beside it.

## 💡 The Insight

A before and after comparison measures everything that changed, and then hands all the credit to the one thing you happened to be studying.

## Check Your Understanding

<details>
<summary><b>1.</b> Where did the missing 21 percentage points go?</summary>

Into everything else that changed between the two periods. The next topic shows the largest single piece: every agency in the state was already getting better, including the ones that never took the training. A before and after comparison cannot see that, because it never looks at another agency.
</details>

<details>
<summary><b>2.</b> Suppose the agencies had reported a 12 percent fall before and after, matching the true effect exactly. Would that have been good evidence?</summary>

No, and this is the uncomfortable part. It would have been the right number produced by a method that cannot support it. Given that everything was falling about 5 percent a year anyway, a 12 percent before and after fall would actually have implied the training made things **worse** than the trend. The method does not become sound because the answer happens to land in the right place.
</details>

<details>
<summary><b>3.</b> A program starts in the month a problem peaks. What does that do to a before and after comparison?</summary>

It makes it worse, and in the same direction. Peaks are followed by declines whether or not anyone intervenes, and programs are launched at peaks precisely because that is when a problem gets attention. [Topic 11](Topic_11_Why_The_Worst_Performers_Always_Improve.md) measures exactly how much of a decline this produces on its own.
</details>

## Key Takeaway

Never report a before and after change as the effect of a program. Report it as what it is, a description of the period, and find something to compare it against.

---

| | |
|---|---|
| **Previous** | [Topic 3: The World You Cannot See](Topic_03_The_World_You_Cannot_See.md) |
| **Next** | [Topic 5: Things Were Already Changing](Topic_05_Things_Were_Already_Changing.md) |
| **Builds on** | [Topic 3](Topic_03_The_World_You_Cannot_See.md) |
| **Used again in** | [Topic 8](Topic_08_Two_Differences_Are_Better_Than_One.md), [Topic 11](Topic_11_Why_The_Worst_Performers_Always_Improve.md), [Topic 19](Topic_19_Reading_A_Causal_Claim.md) |

*This module is part of a series developed for the Washington Data Exchange for Public Safety (WADEPS) through the Center for Interdisciplinary Statistical Education and Research (CISER) at Washington State University. Version 1.0, September 2026. Questions, errors, or suggestions: yin.zhang@wsu.edu*

*All examples use synthetic data created for teaching. They do not represent any real jurisdiction, agency, officer, or incident. See [Data/DATA_DICTIONARY.md](../../Data/DATA_DICTIONARY.md).*
