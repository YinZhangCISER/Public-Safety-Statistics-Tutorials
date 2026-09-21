# Module 13: Intervention Analysis and Transfer Functions

> **Developed by Yin Zhang, PhD**, Assistant Professor, Department of Mathematics and Statistics, Washington State University

**The question this module answers:** *Can the shape of a response be estimated rather than assumed, and what does it look like when the data cannot support one?*

---

## The Question

Every intervention estimate so far has assumed a shape. A step says the effect arrives all at once and stays. That is a modelling choice, and it is usually made silently.

Intervention analysis, in the sense Box and Tiao gave the term, estimates the **shape** of a response rather than assuming it: how fast it arrives, whether it decays, whether it was a pulse rather than a step.

The honest finding of this module is that the shape is much harder to recover than the size, and that the usual model selection tools will not tell you so. Working out what a dataset cannot support is the last technical skill this series teaches, and it is the one that stops a report from overreaching.

## Model and Assumptions

| Shape | What it says | Where you see it |
|---|---|---|
| **Step** | the level changes and stays changed | a policy, a permanent staffing change |
| **Pulse** | one period is affected, then it returns | a single event, a weather month |
| **Gradual** | the effect builds toward a new level | training spreading through a department |

The gradual case is a **first order transfer function**: each month the effect moves a fixed fraction of the way from where it is to where it is heading.

> x(t) = δ · x(t−1) + (1 − δ) · input(t),   and the effect is ω · x(t)

One parameter, δ, controls the speed. The programme here is gradual by construction: 0, then 25, 58, 83 and 100 percent of a 12 percent reduction over five months.

| Assumption | Diagnostic | Consequence of failing |
|---|---|---|
| The candidate shapes differ where the data is | how many months do they disagree about | the shapes are not distinguishable |
| The decay parameter is identified | does AIC turn around inside the grid | the estimate runs to the boundary |
| The effect is large relative to the noise | compare it with the residual scale | the shape is noise |
| The intervention is the only thing that changed then | [Module 12](Module_12_Structural_Breaks.md) | the shape belongs to something else |

## Estimation

```python
for delta in np.arange(0, 1, 0.05):
    d["tf"] = transfer(d, delta)
    poisson("n_uof ~ C(agency_id) + C(year_month) + tf", d)
```

## Worked Example

![Two panels. The left plots one estimated coefficient per month around the intervention with very wide intervals, swinging between minus 34 and plus 24 percent, against a smooth orange curve showing the phase in that is actually present. The right plots, against the decay parameter, the effect the model claims at full strength falling from minus 12 to minus 53 percent, the average over the settled months staying flat near minus 12, and a dotted AIC line that descends monotonically to the edge of the grid](Figures/fig_a13_intervention.png)

### The event study, and why it cannot see the shape

The assumption free approach estimates one coefficient per month relative to the start.

| Months since the start | Estimate | 95 percent interval | The truth |
|---|---|---|---|
| +0 | −33.8% | [−52.0, −8.7] | 0.0% |
| +1 | −28.1% | [−48.3, +0.0] | −3.1% |
| +2 | **+24.0%** | [−11.5, +73.8] | −7.1% |
| +3 | −10.6% | [−36.9, +26.7] | −10.1% |
| +4 | +13.7% | [−22.1, +65.8] | −12.0% |
| +6 | −26.1% | [−50.1, +9.4] | −12.0% |

The truth walks smoothly from 0 to −12 and stays. The estimates swing from −34 to +24 percent, with intervals from forty points wide at best to over eighty at worst.

**The event study is uninformative here, and it is the fashionable choice.** A plot of these coefficients shows a jagged line a reader will interpret as dynamics. There are none in it. It is worth running to check that the pre period coefficients are flat; as an estimate of a response shape at this sample size it is not usable.

### Three shapes, fitted properly

| Shape | Effect at full strength | Interval | AIC |
|---|---|---|---|
| Abrupt step at month 4 | **−12.0%** | [−17.3, −6.3] | **4743.9** |
| Linear ramp over 4 months | −11.4% | [−16.7, −5.7] | 4745.7 |
| The true phase in | −11.2% | [−16.5, −5.5] | 4746.1 |

All three land within a point of the truth, and the AIC spread is 2.2 points. **The wrong shape fits as well as the right one**, and the crudest of the three has the best AIC. Over a 30 month settled window the shapes differ in only four months, so the data has almost nothing to distinguish them with.

### Letting the data choose the decay

| Decay | AIC | Half life | Effect at full strength | Average over settled months |
|---|---|---|---|---|
| 0.00 | 4742.0 | 0.0 mo | −12.1% | −12.1% |
| 0.50 | 4743.7 | 1.0 mo | −11.9% | −11.9% |
| 0.80 | 4742.3 | 3.1 mo | −13.2% | −12.5% |
| 0.90 | 4740.6 | 6.6 mo | −15.6% | −12.9% |
| 0.95 | 4739.8 | 13.5 mo | −20.5% | −12.8% |
| 0.99 | **4739.6** | **69.0 mo** | **−52.9%** | **−12.4%** |

**AIC improves all the way to the edge of the grid and never turns around.** Across the whole range it moves 2.4 points, which is nothing, while the model's substantive claim moves from a 12 percent effect fully arrived within a month to a 53 percent effect with a 69 month half life.

The decay parameter is not identified. The likelihood surface is almost flat and tilts very slightly toward the boundary, and AIC, asked to choose, walks off the edge.

Now read the last column. **The average effect over the settled window sits between 12 and 13 percent for every value of the decay**, including the absurd ones.

### What is identified and what is not

| Quantity | Identified here | Why |
|---|---|---|
| Average effect over a stated window | **yes**, 12 to 13 percent | it is essentially a mean difference |
| Whether the effect is a step or a drift | no | [Module 11](Module_11_Interrupted_Time_Series.md), the two trade off exactly |
| How fast the effect arrived | no | the decay runs to the boundary |
| Whether the effect is permanent | no | the series ends 30 months in |
| Month by month dynamics | no | intervals up to eighty points wide |

Only the first row belongs in a report as a number. The others belong in the limitations paragraph, **named explicitly**, because a reader who is not told will assume they were established.

### When shape estimation does work

Tarnbridge's documented unrest month, fitted three ways:

| Shape | Effect | AIC | Pearson dispersion |
|---|---|---|---|
| **Pulse** | **+343.8%** | **575.9** | **1.41** |
| Geometric decay | +271.8% | 617.1 | 1.87 |
| Step | +54.6% | 768.6 | 4.73 |

Decisive, unlike everything above. The difference is that the unrest month runs four and a half times the surrounding level and a pulse and a step disagree about 58 of the 88 months, while the programme effect is 12 percent and the candidate shapes disagree about four.

**Shape is identifiable when the effect is large relative to the noise and the candidates differ over much of the sample.** Neither condition holds for a gradual policy effect measured over a few years, which is the case people most want a transfer function for.

## Recovering the Planted Answer

The generator phases the programme in over five months at 0, 25, 58, 83 and 100 percent of a 12 percent reduction.

**The size is recovered** by every specification tried, from −11.2 to −12.1 percent. **The phase in shape is not recovered by anything.** The event study cannot see it, three candidate shapes fit indistinguishably, and a free decay parameter runs to the boundary while AIC applauds.

That is the planted lesson: the dataset contains a real gradual response, and the correct conclusion from analysing it is that the response shape is not estimable.

## Diagnostics

| Check | Acceptable |
|---|---|
| Event study pre period coefficients | flat and near zero |
| Does AIC turn around inside the decay grid | yes, or the parameter is not identified |
| Spread of AIC across candidate shapes | if under about 4 points, the shapes are indistinguishable |
| How many months the candidate shapes disagree about | enough to matter |
| The average over the window | stable across shapes, or nothing is identified |

## Do It Yourself

> 📓 **Notebook:** [Module_13_Intervention_Analysis.ipynb](Notebooks/Module_13_Intervention_Analysis.ipynb)
> [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/OWNER/REPO/blob/main/Time_Series/Advanced/Notebooks/Module_13_Intervention_Analysis.ipynb)
> About 35 minutes.

The exercise fits the Tarnbridge unrest month as a pulse, a step and a decay, and works out why shape selection succeeds there and fails for the programme.

## The Handoff to Causal Inference

Everything in Part IV estimated an **association between a date and an outcome**, as carefully as time series methods allow. None of it established that the programme caused the change.

| What this series can answer | What it cannot |
|---|---|
| Did the rate change when the programme started | Would it have changed anyway |
| Is the change larger than the comparison agencies' | Are those agencies a valid counterfactual |
| Is it larger than noise | Did something else happen in November 2023 |
| Is the pre period consistent with the design | Why these five agencies adopted it |

That last row matters most here, and it is knowable: the [answer key](../../Data/GROUND_TRUTH.md) says the five agencies with the **highest baseline rates** were selected. Selection on the outcome is the oldest problem in evaluation, and no time series method touches it.

The [Causal Inference series](../../Causal_Inference/) starts there.

## Reporting the Result

> The programme's effect was estimated under three response shapes and with a freely estimated first order decay. All specifications place the average reduction over the 30 months following full implementation between 11 and 13 percent. The shapes cannot be distinguished: AIC differs by 2.2 points across them, and a freely estimated decay parameter improves AIC monotonically to the boundary of its range while the implied long run effect rises from 12 to 53 percent. The average effect over the stated window is therefore reported, and no claim is made about how quickly the effect arrived, whether it is still growing, or whether it is permanent.

## Further Reading

- Box, G. E. P. and Tiao, G. C. (1975). Intervention analysis with applications to economic and environmental problems. *Journal of the American Statistical Association*, 70. The original.
- Hyndman, R. J. and Athanasopoulos, G. *Forecasting: Principles and Practice*, chapter on dynamic regression. Free at otexts.com/fpp3.
- Roth, J., Sant'Anna, P. et al. (2023). What's trending in difference in differences. *Journal of Econometrics*, 235. On event study designs and what they do and do not deliver.

---

| | |
|---|---|
| **Previous** | [Module 12: Structural Breaks and Changepoints](Module_12_Structural_Breaks.md) |
| **Next** | [Module 14: Reporting, and Work That Outlives You](Module_14_Reporting_And_Reproducibility.md) |
| **Builds on** | [Module 11](Module_11_Interrupted_Time_Series.md), [Module 12](Module_12_Structural_Breaks.md), [Module 3](Module_03_Model_Selection_And_Uncertainty.md) |
| **Used again in** | [Module 14](Module_14_Reporting_And_Reproducibility.md), the [Causal Inference series](../../Causal_Inference/) |

*This module is part of a series developed for the Washington Data Exchange for Public Safety (WADEPS) through the Center for Interdisciplinary Statistical Education and Research (CISER) at Washington State University. Version 1.0, September 2026. Questions, errors, or suggestions: yin.zhang@wsu.edu*

*All examples use synthetic data created for teaching. They do not represent any real jurisdiction, agency, officer, or incident. See [Data/DATA_DICTIONARY.md](../../Data/DATA_DICTIONARY.md).*
