# Topic 6: Comparing Yourself to Someone Else

> **Developed by Yin Zhang, PhD**, Assistant Professor, Department of Mathematics and Statistics, Washington State University

**The question this module answers:** *If an agency's own past is a bad counterfactual, what is a better one?*

---

## The Core Concept

Other agencies lived through the same years. They faced the same laws, the same statewide pressures, the same economy, the same weather, the same news. Some of them did not take the program.

**Those agencies are a version of what your agency would have looked like without it.** Not a perfect version, and the rest of this series is about how they fall short. But a far better one than your own past, because they are living in the same present.

This is called a **comparison group** or a **control group**, and constructing one is the single highest value move available in a public safety evaluation.

## Why It Matters

A before and after comparison has to assume nothing else changed. A comparison group does not have to assume that. It only has to assume that whatever else changed, changed for both groups.

That is a much weaker assumption, and weaker assumptions are the whole business. **Every improvement in causal work is a trade of a strong assumption for a weaker one.**

## The Example

The same chart as [Topic 1](Topic_01_What_Does_Caused_Mean.md), with the seven agencies that never took the training added.

![A line chart with two lines over seven years. The blue line is the agencies that took the training, starting near 4.0 use of force per 100 arrests; the grey line is the seven that did not, starting near 3.0. Both fall steadily. A vertical line marks the month the training was in place, after which the blue line falls somewhat more steeply than the grey](Figures/fig_06_comparison_group.png)

Two things are now visible that were not before.

**The grey line falls too.** The comparison agencies improved over the same period, without any training. That improvement is the statewide drift from [Topic 5](Topic_05_Things_Were_Already_Changing.md), and it is now a measured quantity rather than an unknown.

**The two lines start at different heights.** The trained agencies began well above the others, at around 4.0 against 3.0. That gap is not a problem yet, and [Topic 13](Topic_13_Picking_The_Winners.md) explains where it came from. What matters here is that the gap exists before anything happened, so it cannot have been caused by the training.

## What To Watch For

- **Levels do not have to match.** The two lines can start far apart. What matters is whether they were **moving** alike, which is [Topic 9](Topic_09_Were_They_Moving_Together_Before.md).
- **The comparison group must not have taken the program.** Obvious, and violated more often than you would expect, usually because a similar program ran under a different name.
- **More agencies is better than one.** A single comparison agency has its own accidents. [Topic 7](Topic_07_What_Makes_A_Good_Comparison_Group.md) is about this.
- **The comparison group can be affected by the program without taking it.** Neighbouring agencies share officers, training academies and radio channels. [Topic 10](Topic_10_When_The_Comparison_Group_Moves_Too.md).

## 💡 The Insight

Your own past lives in a different world from your present. Another agency lives in the same one.

## Check Your Understanding

<details>
<summary><b>1.</b> The two lines start about one full point apart. Is that a reason to reject the comparison?</summary>

No. A difference in level is expected and it does not bias the comparison, because the same gap exists before the program and can be subtracted out. What would be a problem is a difference in **direction**: if the two lines were converging or diverging before the program started, then subtracting one from the other would not remove the drift. That is the check in [Topic 9](Topic_09_Were_They_Moving_Together_Before.md).
</details>

<details>
<summary><b>2.</b> Why is "the same laws and the same weather" the argument for using other agencies?</summary>

Because those are the things a before and after comparison cannot hold fixed. Your agency in 2019 and your agency in 2025 differ in every statewide condition. Your agency and a neighbouring agency in 2025 share almost all of them. The comparison group is a way of holding time constant, which is exactly what the before and after comparison fails to do.
</details>

## Key Takeaway

Find agencies that did not take the program and put them on the same chart, before doing any arithmetic.

---

| | |
|---|---|
| **Previous** | [Topic 5: Things Were Already Changing](Topic_05_Things_Were_Already_Changing.md) |
| **Next** | [Topic 7: What Makes a Good Comparison Group](Topic_07_What_Makes_A_Good_Comparison_Group.md) |
| **Builds on** | [Topic 3](Topic_03_The_World_You_Cannot_See.md), [Topic 5](Topic_05_Things_Were_Already_Changing.md) |
| **Used again in** | [Topic 8](Topic_08_Two_Differences_Are_Better_Than_One.md), [Topic 9](Topic_09_Were_They_Moving_Together_Before.md), [Topic 10](Topic_10_When_The_Comparison_Group_Moves_Too.md) |

*This module is part of a series developed for the Washington Data Exchange for Public Safety (WADEPS) through the Center for Interdisciplinary Statistical Education and Research (CISER) at Washington State University. Version 1.0, September 2026. Questions, errors, or suggestions: yin.zhang@wsu.edu*

*All examples use synthetic data created for teaching. They do not represent any real jurisdiction, agency, officer, or incident. See [Data/DATA_DICTIONARY.md](../../Data/DATA_DICTIONARY.md).*
