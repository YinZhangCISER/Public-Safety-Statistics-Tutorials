# Module 13: Baseline Forecasts You Must Beat

> **Developed by Yin Zhang, PhD**, Assistant Professor, Department of Mathematics and Statistics, Washington State University

**The question this module answers:** *Before building anything, what would a method with no ideas in it predict?*

---

## The Question

A forecast is easy to admire in isolation. It tracks the shape, the numbers look plausible, and nobody asks what the alternative was.

The alternative matters, because a model that fails to beat a one line rule is worse than useless. It costs time to build, it costs attention to maintain, and it will outlive the person who made it.

## The Idea in Plain Language

Compute, before fitting anything, what these would have predicted:

| Baseline | The rule |
|---|---|
| **Last value** | next month equals this month |
| **Mean of all history** | next month equals the long run average |
| **Rolling twelve month mean** | next month equals the average of the last year |
| **Same month last year** | next July equals last July |
| **Drift** | keep going in the direction the series has been heading |
| **Seasonal naive plus drift** | last July, adjusted for a year of drift |

Write the numbers down. They are the bar.

## The Method

**Split by time, never at random.** A random split lets the model learn from the future. Forecasting is judged on whether you could have said it in advance, so the test period must come after everything the model saw.

```python
train = s.loc[:"2024-12"]
test  = s.loc["2025-01":"2025-12"]
```

Then score every baseline on the test period, and only then start modelling.

## Worked Example

Grandview Police Department. Train on 72 months through December 2024, forecast the twelve months of 2025.

![Two panels. The left panel shows the series through 2024 in grey, the held back 2025 in black, and three baseline forecasts overlaid. The right panel ranks all six baselines by average error, with seasonal naive plus drift best at 15.6 and the mean of all history worst at 25.2](Figures/fig_m13_baselines.png)

| Baseline | Average error, incidents a month |
|---|---|
| **Seasonal naive plus drift** | **15.6** |
| Same month last year | 15.9 |
| Last value | 20.5 |
| Rolling twelve month mean | 21.1 |
| Drift | 21.4 |
| Mean of all history | 25.2 |

**The seasonal baselines win, and comfortably.** Both say the same thing: whatever happened this month last year, expect roughly that again. For a series with a strong annual pattern that is a genuinely good forecast, and it costs nothing to compute or to explain to anyone.

**The mean of all history is worst**, because it ignores both the season and the trend and is therefore wrong in a different direction every month. **Last value is poor** too: December is a quiet month, and repeating it across a year predicts a permanent winter.

So any model proposed for Grandview has to come in under **15.6**, on data it has not seen, by a margin large enough to be worth maintaining.

### The ranking is not universal

Run the same six baselines on Elkhorn, the eight officer department, and the order **reverses**:

| Baseline | Average error |
|---|---|
| Last value | 0.58 |
| Drift | 0.58 |
| Mean of all history | 0.62 |
| Rolling twelve month mean | 0.69 |
| **Same month last year** | **0.92** |

The flat baselines win and the seasonal one comes last. Elkhorn has no seasonal shape large enough to see through the noise, so reaching back twelve months just imports an extra month of randomness. Every baseline is within half an incident of every other, on a series averaging 0.81 a month.

**Knowing a series is unforecastable is a result.** It saves building something that would be maintained for years while adding nothing.

## Do It Yourself

> 📓 **Notebook:** [Module_13_Baseline_Forecasts.ipynb](Notebooks/Module_13_Baseline_Forecasts.ipynb)
> [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/OWNER/REPO/blob/main/Time_Series/Intermediate/Notebooks/Module_13_Baseline_Forecasts.ipynb)
> About 15 minutes.

The notebook builds all six, ranks them, works out what margin a model would have to achieve, and ends with a reusable `baseline_table` function plus the Elkhorn exercise.

## Pitfalls

| What goes wrong | What it looks like | What to do |
|---|---|---|
| A random train and test split | excellent scores that do not survive deployment | always split by time |
| Never computing the baseline | a model with an error of 12 that felt good | write the baseline down first |
| Tuning on the test set | the holdout stops being a holdout | keep a period you have not looked at |
| Assuming seasonal naive is always the bar | for small agencies it is the worst baseline | compute all six |
| A test period containing a known event | the model blamed for a riot | pick a quiet window, or say so |
| Reporting only the model's error | the reader cannot tell whether it was worth it | report the baseline next to it, always |

## Check Your Understanding

<details>
<summary><b>1.</b> Why is a random train and test split wrong for forecasting?</summary>

Because it lets the model see the future. With randomly chosen test months, the model trains on months either side of every test point and effectively interpolates rather than forecasts. The resulting error will be far lower than anything achievable in practice, where the model has only the past. The question a forecast answers is "could you have said this in advance", and only a split by time asks it.
</details>

<details>
<summary><b>2.</b> A new model achieves an average error of 14.8 on Grandview's 2025. Is it worth deploying?</summary>

Probably not. The best baseline is 15.6, so the model buys about a 5 percent improvement in exchange for code that has to be maintained, documented, explained and re estimated. Against that, "whatever happened this month last year" needs no maintenance and can be described in one sentence. A margin worth taking on is usually 20 percent or more, and it should hold at several origins rather than one, which is [Module 15](Module_15_Measuring_Forecast_Error.md).
</details>

<details>
<summary><b>3.</b> Why does the baseline ranking reverse between Grandview and Elkhorn?</summary>

Because seasonal naive is only useful when there is a seasonal pattern large enough to exceed the noise. Grandview's July runs about 45 percent above its annual average on a base of 100 incidents, which easily clears the noise. Elkhorn averages 0.81 incidents a month, so any seasonal signal is buried, and using last July's number imports the randomness of a single small month for no gain. The lesson generalises: the right baseline depends on the series, so compute all of them.
</details>

## Key Takeaway

Write down what a rule with no ideas in it would predict, before you fit anything. If your model does not clear that bar by a wide margin, the bar is the better answer.

---

| | |
|---|---|
| **Previous** | [Module 12: Building a Peer Benchmark Series](Module_12_Building_A_Peer_Benchmark_Series.md) |
| **Next** | [Module 14: Exponential Smoothing in Plain Language](Module_14_Exponential_Smoothing.md) |
| **Builds on** | [Module 9](Module_09_Year_Over_Year_And_Indexing.md), [Beginner Topic 17](../Beginner/Topic_17_Stationarity.md) |
| **Used again in** | [Module 14](Module_14_Exponential_Smoothing.md), [Module 15](Module_15_Measuring_Forecast_Error.md) |

*This module is part of a series developed for the Washington Data Exchange for Public Safety (WADEPS) through the Center for Interdisciplinary Statistical Education and Research (CISER) at Washington State University. Version 1.0, September 2026. Questions, errors, or suggestions: yin.zhang@wsu.edu*

*All examples use synthetic data created for teaching. They do not represent any real jurisdiction, agency, officer, or incident. See [Data/DATA_DICTIONARY.md](../../Data/DATA_DICTIONARY.md).*
