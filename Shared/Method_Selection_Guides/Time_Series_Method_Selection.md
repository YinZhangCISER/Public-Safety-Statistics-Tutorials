# Choosing a Time Series Method

*Developed by Yin Zhang, PhD, Assistant Professor, Data Analytics Program, Department of Mathematics and Statistics, Washington State University, for the Washington Data Exchange for Public Safety (WADEPS) through the Center for Interdisciplinary Statistical Education and Research (CISER).*

Find the question being asked, read across, go to the module. Every entry points at a module that works the example end to end.

---

## Before any method: four questions that come first

Most wrong answers in practice come from skipping these, not from picking the wrong model.

| Question | Why it decides everything downstream | Where it is taught |
|---|---|---|
| **Count or rate?** A rise in incidents at an agency whose arrests also rose is not a rise in anything | Every later comparison inherits the denominator | [Beginner Topic 5](../../Time_Series/Beginner/Topic_05_Counts_And_Rates.md), [Intermediate Module 3](../../Time_Series/Intermediate/Module_03_Choosing_A_Denominator.md) |
| **Is the calendar honest?** A month with no submission is missing, not zero | A model fitted over a gap treats the gap as a real decline | [Beginner Topic 6](../../Time_Series/Beginner/Topic_06_Missing_Time_Points_And_Reporting_Gaps.md), [Intermediate Module 2](../../Time_Series/Intermediate/Module_02_Building_An_Honest_Calendar.md) |
| **Are the last months provisional?** Records still being entered look like sudden improvement | The most recent point is the one most often quoted | [Beginner Topic 19](../../Time_Series/Beginner/Topic_19_Data_Quality_And_Pitfalls.md) |
| **Is the change bigger than the noise?** At eight sworn officers, one incident to three is a tripling | Small agencies generate large percentages from nothing | [Beginner Topic 10](../../Time_Series/Beginner/Topic_10_Noise_And_Irregular_Fluctuations.md), [Intermediate Module 4](../../Time_Series/Intermediate/Module_04_Why_Small_Agencies_Look_Volatile.md) |

---

## The question, and the method it calls for

| The question being asked | The method | What it requires | Where it is worked |
|---|---|---|---|
| Is this month unusual? | Rolling mean with control limits | A stable baseline period and a denominator | [Intermediate 8](../../Time_Series/Intermediate/Module_08_Rolling_Statistics_And_Control_Limits.md) |
| Is the series rising or falling? | A trend term in a count model | Seasonality handled, or the slope absorbs it | [Intermediate 6](../../Time_Series/Intermediate/Module_06_Measuring_The_Trend.md), [Advanced 8](../../Time_Series/Advanced/Module_08_Count_Regression_With_Harmonics.md) |
| Is summer really worse? | Decomposition, then seasonal adjustment | Three or more years of history | [Intermediate 5](../../Time_Series/Intermediate/Module_05_Decomposition.md), [Intermediate 7](../../Time_Series/Intermediate/Module_07_Seasonal_Adjustment.md) |
| How does this year compare with last? | Year over year change and indexing | A full twelve months on both sides | [Intermediate 9](../../Time_Series/Intermediate/Module_09_Year_Over_Year_And_Indexing.md) |
| How does this agency compare with its peers? | A peer benchmark series | Comparable agencies and a shared denominator | [Intermediate 12](../../Time_Series/Intermediate/Module_12_Building_A_Peer_Benchmark_Series.md) |
| What will next quarter look like? | Baseline forecast first, then a model | An honest holdout period | [Intermediate 13](../../Time_Series/Intermediate/Module_13_Baseline_Forecasts.md), [Intermediate 14](../../Time_Series/Intermediate/Module_14_Exponential_Smoothing.md), [Advanced 5](../../Time_Series/Advanced/Module_05_SARIMA.md), [Advanced 7](../../Time_Series/Advanced/Module_07_State_Space_And_ETS.md) |
| How wrong is the forecast allowed to be? | Forecast error measures on a holdout | Never scoring on the fitting period | [Intermediate 15](../../Time_Series/Intermediate/Module_15_Measuring_Forecast_Error.md) |
| Did something change at a date already known? | Interrupted time series | A long pre period and a reason the date is exogenous | [Advanced 11](../../Time_Series/Advanced/Module_11_Interrupted_Time_Series.md), [Intermediate 16](../../Time_Series/Intermediate/Module_16_Did_Something_Change.md) |
| Did something change, date unknown? | Structural break tests with the right critical values | Accepting that searching for the break inflates significance | [Advanced 12](../../Time_Series/Advanced/Module_12_Structural_Breaks.md) |
| Did the effect arrive gradually? | Intervention analysis with a transfer function | A hypothesis about the shape of the lag, stated first | [Advanced 13](../../Time_Series/Advanced/Module_13_Intervention_Analysis.md) |
| The counts are small and many months are zero | Poisson or negative binomial, not a normal model | Modelling the count rather than a log rate | [Advanced 2](../../Time_Series/Advanced/Module_02_Counts_Are_Not_Gaussian.md), [Advanced 9](../../Time_Series/Advanced/Module_09_Rare_Events.md) |
| Twelve agencies, one model | Panel and hierarchical models | Deciding what pools and what stays agency specific | [Advanced 10](../../Time_Series/Advanced/Module_10_Panel_And_Hierarchical.md) |
| Do the residuals still carry structure? | Autocorrelation diagnostics, then ARMA errors | Reading the plot as a diagnostic, not a result | [Intermediate 10](../../Time_Series/Intermediate/Module_10_Reading_Autocorrelation.md), [Advanced 6](../../Time_Series/Advanced/Module_06_Regression_With_ARMA_Errors.md) |
| Does this series need differencing? | Stationarity testing | Knowing what the test's null actually says | [Advanced 1](../../Time_Series/Advanced/Module_01_Stationarity_Tested.md) |
| How is any of it written up? | A reporting and reproducibility checklist | Recording what was tried, not only what was kept | [Advanced 14](../../Time_Series/Advanced/Module_14_Reporting_And_Reproducibility.md) |

---

## Which level to read

The same question is answered at three depths. Pick by what is going to be produced, not by background.

| If the output is | Read |
|---|---|
| A judgement about a chart someone else made | the [Beginner series](../../Time_Series/Beginner/), no code |
| A chart or a number produced from the data | the [Intermediate series](../../Time_Series/Intermediate/), notebooks with the statistics kept light |
| A model whose assumptions will be questioned | the [Advanced series](../../Time_Series/Advanced/), complete notebooks with diagnostics |

---

## Where a time series method stops

A time series method describes what a series did. It does not establish why, and interrupted time series is the boundary case that most often gets read as though it did.

**One series with a vertical line at the policy date cannot separate the policy from everything else that happened at that time**, including a trend that was already there. In the teaching data, a before and after comparison on the treated agencies returns a 33.1 percent reduction against a planted truth of 12 percent, and the entire gap is the secular decline that was underway before the program began.

When the question is whether an intervention caused a change, go to the [causal inference guide](Causal_Inference_Method_Selection.md).

---

*All examples use synthetic data created for teaching. They do not represent any real jurisdiction, agency, officer, or incident.*

*Questions, corrections, or suggestions: yin.zhang@wsu.edu*
