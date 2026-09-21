# Module 16: Did Something Change?

> **Developed by Yin Zhang, PhD**, Assistant Professor, Department of Mathematics and Statistics, Washington State University

**The question this module answers:** *A programme launched. Did it work, and how would anyone know?*

---

## The Question

This is where the whole series has been heading, and it is the question public safety data is asked most often. A training programme started, a policy changed, a commander arrived. The numbers went down. Did the thing cause it?

The module answers it three ways on the same data, against an effect whose true size is known, and shows what each answer is worth.

## The Idea in Plain Language

You need something to compare the actual outcome against: **what would have happened anyway**. There are three ways to get one, and they differ in what they require.

| Answer | What it compares against | What it requires |
|---|---|---|
| **Before and after** | the agency's own past | nothing, and it is worth nothing |
| **Difference in differences** | agencies that did not adopt it | comparable agencies, and parallel pre trends |
| **Forecast counterfactual** | what a model fitted before the launch expected | a forecastable series, and no other shock |

The second and third fail in different ways, which is why doing both is stronger than doing either.

## The Method

Set the dates first. The programme began in **July 2023** and was fully in place by **November 2023**, so the post period starts in November and the phase in months are excluded rather than diluted into the estimate.

```python
naive = 100 * (treated_after / treated_before - 1)
did   = 100 * ((treated_after / treated_before) /
               (control_after / control_before) - 1)
```

For the third, fit on the pre period only and forecast forward:

```python
model = ExponentialSmoothing(np.log(pre), trend="add", seasonal="add",
                             seasonal_periods=12,
                             initialization_method="estimated").fit()
counterfactual = np.exp(model.forecast(horizon))
```

## Worked Example

Four agencies adopted the de escalation training and are usable. Summit County also adopted it and is excluded for a reason given below. Seven agencies did not adopt it and form the comparison group.

![Two panels. The left panel shows the trained agencies' six month average rate, with a dashed line showing what a model fitted before the programme predicted, and the gap between them shaded. The right panel shows three estimates as bars against a dashed line at the true effect of minus 12 percent](Figures/fig_m16_did_something_change.png)

| Answer | Estimated effect |
|---|---|
| Before and after, no comparison | **−24.9%** |
| Difference in differences | **−11.3%** |
| Forecast counterfactual | **−11.1%** |
| **The truth built into the data** | **−12.0%** |

**The before and after answer is more than double the truth.** Its arithmetic is correct. It is measuring the programme plus the statewide decline of about 5 percent a year that [GROUND_TRUTH.md](../../Data/GROUND_TRUTH.md) built into every agency, and it has no way to separate them. The comparison group fell by about 15 percent over the same window **without any training at all**.

**The other two land within about a point of the truth, from completely different directions.** One borrows other agencies; the other borrows the agency's own past behaviour. They share no assumptions, and **two such methods agreeing is worth more than either alone.**

### What each good answer requires

**Difference in differences assumes parallel trends**: before the programme, the two groups were moving in the same direction at the same speed. That is testable.

| | Difference in pre programme slopes |
|---|---|
| Trained against comparison group | **−0.56% a year**, interval −5.63 to +4.78, p = 0.83 |

Small, and the interval comfortably covers zero. The assumption holds.

**It holds only because Summit County was removed first.** That agency was already declining at about 12 percent a year before the programme began, roughly three times everyone else, and it is flagged as the parallel trends violator in the answer key.

| Difference in differences | Estimate |
|---|---|
| With Summit County left in | **−14.2%** |
| With Summit County removed | **−11.3%** |

One agency with a different pre existing trajectory moved the answer by three points.

**The forecast counterfactual assumes the pre programme pattern would have continued.** There is no direct test of that, and it is the method's main weakness: any statewide shock after the launch is counted as programme effect. What you can check is whether the model forecasts this series well over stretches where nothing happened, which is [Module 15](Module_15_Measuring_Forecast_Error.md).

Its rough interval here runs **−13.6% to −8.5%**, and that interval ignores uncertainty in the fitted parameters, so treat it as a lower bound on how wrong the estimate could be.

### A single agency cannot do this

Run the same calculation on Millgate alone:

| Millgate only | Estimate |
|---|---|
| Before and after | −31.2% |
| Difference in differences | −18.7% |
| Four agencies pooled | −11.3% |
| The truth | −12.0% |

The whole post programme estimate rests on **181 incidents**. The method is not the problem; a 12 percent effect is simply not measurable from one small agency. That is [Module 4](Module_04_Why_Small_Agencies_Look_Volatile.md) arriving for the last time, and it is an argument for designing an evaluation with enough agencies **before** a programme launches rather than assembling one afterwards from whoever happened to adopt it.

## Do It Yourself

> 📓 **Notebook:** [Module_16_Did_Something_Change.ipynb](Notebooks/Module_16_Did_Something_Change.ipynb)
> [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/OWNER/REPO/blob/main/Time_Series/Intermediate/Notebooks/Module_16_Did_Something_Change.ipynb)
> About 25 minutes.

The notebook computes all three answers, tests parallel trends, shows what leaving the violator in costs, builds the interval, and ends with the single agency exercise.

## Where This Stops

Every method here answers "how much did the numbers move, beyond what they would have done anyway". **None of them establishes why.**

The two good answers both rest on an assumption that cannot be verified from the outcome data alone: that the comparison group, or the forecast, really does represent what would have happened. Checking those assumptions properly, knowing when they fail, and knowing what to do instead is the subject of the [Causal Inference series](../../Causal_Inference/).

What this module establishes is the minimum standard. **A before and after comparison with no comparison group and no counterfactual is not evidence**, and in this dataset it is wrong by a factor of two.

## Pitfalls

| What goes wrong | What it looks like | What to do |
|---|---|---|
| Before and after with nothing else | the secular trend counted as programme effect | never report it alone |
| A comparison group that adopted the programme | the effect cancels itself out | screen them, [Module 12](Module_12_Building_A_Peer_Benchmark_Series.md) |
| Parallel trends never tested | one divergent agency biases everything | fit the pre period slopes and compare |
| The phase in months counted as post | a real effect diluted toward zero | start the post period when the thing was fully in place |
| A single small agency | an estimate dominated by its own noise | pool the treated agencies |
| A point estimate with no interval | precision that does not exist | report a range, and say what it ignores |
| Only one method | no way to know whether the assumption held | do both, and report both |

## Check Your Understanding

<details>
<summary><b>1.</b> The before and after figure is −24.9 percent and the truth is −12. Where did the extra 13 points come from?</summary>

From the statewide decline that was already running. The comparison group, which adopted nothing, fell by about 15 percent over the same window. Before and after has no way to see that, so it attributes the whole movement to the programme. The effect is not an error in the arithmetic but in what the arithmetic was asked to compare against: the agency's own past, which was already improving for reasons that had nothing to do with the training.
</details>

<details>
<summary><b>2.</b> Why is agreement between difference in differences and the forecast counterfactual more convincing than either result on its own?</summary>

Because they fail in unrelated ways. Difference in differences is wrong if the comparison group was not on a parallel path; it is unaffected by a shock that hit everyone. The forecast counterfactual is wrong if anything else changed after the launch; it is unaffected by the choice of comparison agencies. For both to be wrong by the same amount in the same direction, two independent things would have to have gone wrong together. That is a much stronger position than one estimate, however carefully constructed.
</details>

<details>
<summary><b>3.</b> Summit County adopted the programme. Why exclude it, and is that not choosing the data to fit the answer?</summary>

It is excluded because it fails a test specified in advance and applied to every agency: its pre programme slope differs sharply from the comparison group's, so it violates the assumption difference in differences depends on. That is a methodological exclusion, not a convenient one, and the distinction is whether the rule was stated before the result was seen.

The protection is to report both figures, as above, so a reader can see the exclusion cost three points and judge it. Excluding an agency and reporting only the improved number would be exactly the practice this question is worried about.
</details>

## Key Takeaway

Never report a before and after comparison on its own. Build a comparison group, or forecast a counterfactual, and when you can, do both and report both. Then be clear that you have measured how much the numbers moved, not why.

---

| | |
|---|---|
| **Previous** | [Module 15: How Wrong Is the Forecast?](Module_15_Measuring_Forecast_Error.md) |
| **Next** | The [Advanced series](../Advanced/), and the [Causal Inference series](../../Causal_Inference/) |
| **Builds on** | [Beginner Topic 15](../Beginner/Topic_15_Lagged_Effects.md), [Module 6](Module_06_Measuring_The_Trend.md), [Module 12](Module_12_Building_A_Peer_Benchmark_Series.md), [Module 14](Module_14_Exponential_Smoothing.md) |
| **Used again in** | Advanced Modules 11 and 13, and the whole Causal Inference series |

*This module is part of a series developed for the Washington Data Exchange for Public Safety (WADEPS) through the Center for Interdisciplinary Statistical Education and Research (CISER) at Washington State University. Version 1.0, September 2026. Questions, errors, or suggestions: yin.zhang@wsu.edu*

*All examples use synthetic data created for teaching. They do not represent any real jurisdiction, agency, officer, or incident. See [Data/DATA_DICTIONARY.md](../../Data/DATA_DICTIONARY.md).*
