# Time Series, Intermediate Level

### Building, measuring, and forecasting a series yourself

*Developed by Yin Zhang, PhD, Assistant Professor, Data Analytics Program, Department of Mathematics and Statistics, Washington State University, for the Washington Data Exchange for Public Safety (WADEPS) through the Center for Interdisciplinary Statistical Education and Research (CISER).*

For officers, agency staff, government analysts, and undergraduate students who can read a chart and a percentage and now want to produce one. Sixteen modules, each about ten minutes to read with a fifteen minute Jupyter notebook that runs in Google Colab with no setup.

Formulas appear, but every one of them is followed by the same statement in plain words. All sixteen modules are published.

---

## Part I. Getting the Data Right

*Most analytical errors happen before any method is applied.*

| # | Module | The question it answers |
|---|---|---|
| 1 | [From Incident Records to a Time Series](Module_01_From_Incident_Records_To_A_Time_Series.md) | How do I turn a file of individual calls into a monthly series? |
| 2 | [Building an Honest Calendar](Module_02_Building_An_Honest_Calendar.md) | What do I do about missing months, zeros, and records still being entered? |
| 3 | [Choosing a Denominator](Module_03_Choosing_A_Denominator.md) | Per resident, per call, per officer, or per arrest, and what if the denominator has a trend of its own? |
| 4 | [Why Small Agencies Look Volatile](Module_04_Why_Small_Agencies_Look_Volatile.md) | Why does an 8 officer agency's rate swing so wildly, and what can I say about it? |

## Part II. Describing the Series

| # | Module | The question it answers |
|---|---|---|
| 5 | [Decomposition into Trend, Season and Remainder](Module_05_Decomposition.md) | How do I split one line into the three things it is made of? |
| 6 | [Measuring the Trend](Module_06_Measuring_The_Trend.md) | How much is it changing per year, and how sure am I? |
| 7 | [Seasonal Adjustment](Module_07_Seasonal_Adjustment.md) | When am I entitled to say "adjusted for season"? |
| 8 | [Rolling Statistics and Control Limits](Module_08_Rolling_Statistics_And_Control_Limits.md) | Is this month outside the range this agency normally runs in? |

## Part III. Comparing and Relating

| # | Module | The question it answers |
|---|---|---|
| 9 | [Year over Year, Rolling Totals and Indexing](Module_09_Year_Over_Year_And_Indexing.md) | Which comparison should go in the monthly report? |
| 10 | [Reading ACF and PACF as Pictures](Module_10_Reading_Autocorrelation.md) | How much memory does this series have? |
| 11 | [Lead and Lag Between Two Series](Module_11_Lead_And_Lag.md) | Does call volume move before use of force does? |
| 12 | [Building a Peer Benchmark Series](Module_12_Building_A_Peer_Benchmark_Series.md) | What line should this agency's series sit next to? |

## Part IV. Forecasting and Change Detection

| # | Module | The question it answers |
|---|---|---|
| 13 | [Baseline Forecasts You Must Beat](Module_13_Baseline_Forecasts.md) | What is the simplest forecast, and why does it usually win? |
| 14 | [Exponential Smoothing in Plain Language](Module_14_Exponential_Smoothing.md) | How do I forecast a series with both trend and season? |
| 15 | [How Wrong Is the Forecast?](Module_15_Measuring_Forecast_Error.md) | Which error measure, and why does the popular one break on small counts? |
| 16 | [Did Something Change?](Module_16_Did_Something_Change.md) | How do I compare before and after without fooling myself? |

---

## The notebooks

Each module has one notebook in [Notebooks/](Notebooks/). They open in Google Colab, read the data straight from this repository, and run top to bottom with nothing installed. Every code cell is introduced in plain language first.

To run them locally: `pip install -r ../../requirements.txt`

## Where this leads

Module 16 shows that a before and after comparison is not enough to establish that a program worked, and hands off to the [Causal Inference series](../../Causal_Inference/). Readers who want to fit and defend a formal model continue to the [Advanced level](../Advanced/).

---

*All examples use synthetic data created for teaching. They do not represent any real jurisdiction, agency, officer, or incident.*

*Questions, corrections, or suggestions: yin.zhang@wsu.edu*
