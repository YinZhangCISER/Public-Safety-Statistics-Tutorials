# Topic 17: Stationarity, the Stable Baseline

> **Prepared by Yin Zhang**, Center for Interdisciplinary Statistical Education and Research (CISER), Washington State University

**The question this module answers:** *When is an agency's past average a fair prediction of its future, and when is it worthless?*

---

## The Core Concept

A series is **stationary** when the level it moves around stays put. It bounces, but it bounces around the same value year after year, and the size of the bounces stays roughly the same too.

A series is **non stationary** when that level is moving: drifting up, drifting down, or swinging in a way that does not settle.

The practical test is a question about prediction. **If you took the average of the last seven years, would it be a sensible guess for next year?** If yes, the series is stationary enough to work with. If the answer is obviously no, it is not.

## Why It Matters

Almost every forecasting method assumes something is holding still. If nothing is, the method has nothing to anchor to, and its output will be confidently wrong.

More immediately, stationarity decides whether a historical average means anything at all. Agencies publish averages constantly: the five year average, the average for this month across recent years, the department's usual level. Every one of those statements assumes the thing being averaged has a stable level to be the average of.

## The Example

Two county sheriff's offices in this dataset, both measured as use of force per 100 arrests.

| Year | 2019 | 2020 | 2021 | 2022 | 2023 | 2024 | 2025 | Seven year average |
|---|---|---|---|---|---|---|---|---|
| **Lakeshore County** | 2.84 | 2.27 | 2.43 | 2.57 | 1.93 | 2.28 | 2.20 | **2.36** |
| **Summit County** | 3.62 | 3.72 | 3.14 | 2.58 | 2.23 | 1.67 | 1.66 | **2.66** |

![Two panels. The left panel shows Lakeshore County's yearly rate bouncing between 1.93 and 2.84 with the seven year average of 2.36 drawn as a flat orange line running through the middle of the points. The right panel shows Summit County falling steadily from 3.62 to 1.66, with its seven year average of 2.66 drawn as a flat line that the series crosses once and leaves far behind](Figures/fig_17_stationarity.png)

**Lakeshore County is stationary.** It moves from year to year, sometimes by a lot, but it is always moving around the same place. Every year falls between 1.93 and 2.84, and the average of 2.36 runs right through the middle. "About 2.4 next year" is a defensible forecast, and the recent years are no more informative than the older ones.

**Summit County is not.** Its average of 2.66 is a number the agency passed through on the way down in 2022 and has not been near since. The 2019 and 2020 values of 3.62 and 3.72 describe an agency that no longer exists. Predicting 2.66 for next year would be badly wrong in a completely predictable direction, because the most recent value is 1.66 and the direction has not changed in six years.

**The average is not wrong.** It is a correct summary of seven numbers. It is just not a description of Summit County today, and the difference between those two things is the whole of this module.

## What To Watch For

- **A trend makes a series non stationary.** So does a seasonal pattern, and so does volatility that grows or shrinks over time. See [Topic 7](Topic_07_Trend.md) and [Topic 8](Topic_08_Seasonality.md).
- **Ask what the average is being used for.** As a description of the past, an average is always legitimate. As a prediction of the future, it requires stationarity.
- **The most recent value matters more when a series is moving.** For Lakeshore, the last year and the first year are equally informative. For Summit, the last two years are worth more than all the earlier ones combined.
- **Non stationary is not bad.** Summit County is non stationary because it has improved enormously. That is the best news in the dataset. It just means an average is the wrong summary of it.
- **Monthly data is almost never stationary as it stands,** because of seasonality. Comparing like months, or averaging over twelve, is how that is usually handled. See [Topic 13](Topic_13_Smoothing_And_Moving_Averages.md) and [Topic 18](Topic_18_Year_Over_Year_Comparison.md).

## 💡 The Insight

An average is a fact about the past. It becomes a forecast only if the thing it averages has been holding still, and you have to check that before you use it as one.

## Check Your Understanding

<details>
<summary><b>1.</b> A report states that Summit County's use of force rate over the past seven years averaged 2.66 per 100 arrests. Is that accurate, and is it useful?</summary>

Accurate and close to useless. The seven values do average 2.66. But the agency has fallen from 3.62 to 1.66 without a single reversal, so 2.66 describes neither where Summit County was nor where it is. Anyone using it to set an expectation for next year will be wrong by more than 50 percent. The useful summary is the direction and the current level, not the average.
</details>

<details>
<summary><b>2.</b> Lakeshore County recorded 1.93 in 2023, its lowest value in seven years. Is that evidence the agency is improving?</summary>

Not on its own. Lakeshore is stationary: it has been bouncing between roughly 1.9 and 2.8 for seven years with no direction. A low year in a stationary series is most likely a low draw, and indeed 2024 came back to 2.28. For a stationary series, an unusually low value is a reason to expect a return toward the middle, not the start of a trend.
</details>

<details>
<summary><b>3.</b> Why can a series have strong memory, as in [Topic 16](Topic_16_Autocorrelation.md), and still be stationary?</summary>

Because memory is about whether neighbouring values resemble each other, while stationarity is about whether the level they resemble each other around stays put. Lakeshore's months are related to their neighbours and the whole series still hovers around 2.4 for seven years. Memory describes the short range texture; stationarity describes the long range position. A series can have plenty of the first and still be stable in the second.
</details>

## Key Takeaway

Before using any historical average as an expectation, plot the years and ask whether the average runs through the middle of them or through empty space.

---

| | |
|---|---|
| **Previous** | [Topic 16: Autocorrelation, the Memory of Data](Topic_16_Autocorrelation.md) |
| **Next** | [Topic 18: Year over Year Comparison](Topic_18_Year_Over_Year_Comparison.md) |
| **Builds on** | [Topic 7: Trend](Topic_07_Trend.md), [Topic 9: Cycles and Seasonality](Topic_09_Cycles_And_Seasonality.md), [Topic 16: Autocorrelation](Topic_16_Autocorrelation.md) |
| **Used again in** | [Topic 20: How to Read a Time Series Chart](Topic_20_How_To_Read_A_Chart_Checklist.md) |

*Prepared by Yin Zhang, Center for Interdisciplinary Statistical Education and Research (CISER), Washington State University. Version 1.0, September 2026. Questions, errors, or suggestions: yin.zhang@wsu.edu*

*All examples use synthetic data created for teaching. They do not represent any real jurisdiction, agency, officer, or incident. See [Data/DATA_DICTIONARY.md](../../Data/DATA_DICTIONARY.md).*
