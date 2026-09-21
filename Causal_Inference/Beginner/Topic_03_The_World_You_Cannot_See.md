# Topic 3: The World You Cannot See

> **Developed by Yin Zhang, PhD**, Assistant Professor, Department of Mathematics and Statistics, Washington State University

**The question this module answers:** *What exactly is the thing an effect is measured against, and why can nobody ever observe it?*

---

## The Core Concept

Picture two versions of the same five agencies over the same three years.

In the **first**, they adopted the training. This is the one that happened, and it left records.

In the **second**, everything else is identical. The same officers, the same neighbourhoods, the same weather, the same budget, the same statewide pressures. The only difference is that the training never happened. This version left no records, because it does not exist.

**The effect of the training is the difference between those two worlds.** That is not a metaphor. It is the definition.

The second world has a name: the **counterfactual**, meaning contrary to fact. Everything in this series is machinery for constructing a believable one.

## Why It Matters

Once the counterfactual is named, a large class of arguments becomes easy to settle. Any time someone claims an effect, you can ask: *what are you comparing to, and why is that a good stand in for the world without the program?*

And it explains why causal inference is hard in a way that measurement is not. The problem is not that the data are noisy or the sample is small. **The problem is that half of the comparison is missing by definition, for every unit, always.** No budget for better data collection fixes it.

## The Example

The same four agencies, drawn as two worlds.

![A line chart of the use of force rate. Up to the training date there is a single grey line. After it, the line splits: a solid blue line showing what was recorded, and a dashed grey line showing a constructed version of the same agencies without the training, continuing the earlier decline. The area between them is shaded and labelled as the effect](Figures/fig_03_world_you_cannot_see.png)

Up to the vertical line there is one line, because up to then the two worlds are the same. After it they separate.

**Only the solid line is data.** The dashed line was constructed by continuing the decline these agencies were already on. That is an assumption, not a measurement, and the whole estimate rests on it.

If that assumption is wrong, the shaded area is wrong by exactly as much. The estimate is never better than the counterfactual it was measured against.

## What To Watch For

- **The counterfactual is never in the data.** If someone shows you a chart of what would have happened, they built it. Ask how.
- **"Compared to last year" is a counterfactual.** A weak one: it assumes nothing else changed in a year, which is almost never true.
- **The best counterfactuals come from other people.** Agencies that did not take the training lived through the same year. That is why the next several topics are about finding them.
- **You can never check your counterfactual directly.** You can only check things it implies, which is what the parallel trends idea in [Topic 9](Topic_09_Were_They_Moving_Together_Before.md) does.

## 💡 The Insight

You are always comparing against a world that does not exist. The only choice is whether you construct it carefully or let it be chosen for you by accident.

## Check Your Understanding

<details>
<summary><b>1.</b> An agency compares its use of force this year against its own use of force last year. What counterfactual is it assuming?</summary>

That without the program, this year would have looked exactly like last year. That assumes no trend, no change in crime, no change in staffing, no change in recording practice, and no change in the weather. For the agencies in this dataset it is badly wrong, because everything was already falling by about 5 percent a year. [Topic 5](Topic_05_Things_Were_Already_Changing.md) measures that.
</details>

<details>
<summary><b>2.</b> Why can the counterfactual never be observed, even with perfect data?</summary>

Because it requires the same agencies, in the same months, both taking and not taking the training. An agency does one or the other. Perfect records of what did happen tell you nothing about what did not. This is why the missing half cannot be collected, only estimated from somewhere else, usually from agencies that made the other choice.
</details>

<details>
<summary><b>3.</b> Two analysts estimate the same program and get different answers, using the same data with no mistakes. How?</summary>

They built different counterfactuals. One continued the agency's own trend; the other used the agencies that did not participate. Both are defensible starting points and they do not have to agree. When two honest estimates differ, the disagreement is almost always about the world that did not happen, not about the world that did.
</details>

## Key Takeaway

Say what your counterfactual is, in one sentence, before you report any effect. If the sentence is embarrassing to write down, the estimate is not ready.

---

| | |
|---|---|
| **Previous** | [Topic 2: The Question Behind Every Policy Question](Topic_02_The_Question_Behind_Every_Policy_Question.md) |
| **Next** | [Topic 4: Before and After Is Not Enough](Topic_04_Before_And_After_Is_Not_Enough.md) |
| **Builds on** | [Topic 2](Topic_02_The_Question_Behind_Every_Policy_Question.md) |
| **Used again in** | [Topic 8](Topic_08_Two_Differences_Are_Better_Than_One.md), [Topic 17](Topic_17_When_You_Cannot_Randomize.md), [Topic 20](Topic_20_Questions_To_Ask.md) |

*This module is part of a series developed for the Washington Data Exchange for Public Safety (WADEPS) through the Center for Interdisciplinary Statistical Education and Research (CISER) at Washington State University. Version 1.0, September 2026. Questions, errors, or suggestions: yin.zhang@wsu.edu*

*All examples use synthetic data created for teaching. They do not represent any real jurisdiction, agency, officer, or incident. See [Data/DATA_DICTIONARY.md](../../Data/DATA_DICTIONARY.md).*
