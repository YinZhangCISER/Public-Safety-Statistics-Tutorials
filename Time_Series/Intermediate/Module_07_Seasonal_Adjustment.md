# Module 7: Seasonal Adjustment

> **Developed by Yin Zhang, PhD**, Assistant Professor, Department of Mathematics and Statistics, Washington State University

**The question this module answers:** *When am I entitled to write "seasonally adjusted" next to a number, and what does the adjustment actually do to it?*

---

## The Question

Beginner [Topic 18](../Beginner/Topic_18_Year_Over_Year_Comparison.md) removed the season by comparing July to July. That works, and it costs eleven twelfths of the data: one usable comparison a year, and no way to say anything about last month.

Seasonal adjustment does the same job differently. It divides the seasonal pattern out so that **every consecutive month becomes comparable**, which is what a monthly report needs.

## The Idea in Plain Language

Take the seasonal factors from [Module 5](Module_05_Decomposition.md) and divide by them.

**adjusted = observed ÷ seasonal factor**

A month whose factor is 1.45 is one where the calendar alone puts the count 45 percent above the level. Dividing by 1.45 asks what that month would have looked like on an ordinary calendar.

What adjustment removes is the **average** seasonal pattern and nothing else. It does not remove the trend, which you usually want to keep, and it does not remove noise, which no adjustment can.

## The Method

```python
stl = STL(np.log(series), period=12, robust=True).fit()
factor = np.exp(stl.seasonal)
adjusted = series / factor
```

The factors belong to **that agency, that series and that estimation window**. They are not transferable, and they change when the window changes.

## Worked Example

Ashfell Police Department.

![Two panels. The left panel shows the reported monthly series in grey and the seasonally adjusted series in blue from 2019 to 2026; the adjusted line is visibly flatter but still moves. The right panel shows month on month percentage change for 2023 as paired bars, reported against adjusted](Figures/fig_m07_seasonal_adjustment.png)

| | Reported | Adjusted |
|---|---|---|
| 2023 range | 50 to 157, a span of **107** | 61 to 113, a span of **51** |
| Month on month change, standard deviation | **28.6** percent | **19.8** percent |

The 2023 range halves and the month to month variability drops by about a third. What is left is real movement, and there is still plenty of it.

### Two months worth looking at

| | Reported change | Adjusted change |
|---|---|---|
| June 2023 against May | **+51%** | **+21%** |
| February 2023 against January | **+28%** | **+46%** |

June is the expected result: a 51 percent alarm turns out to be mostly the calendar.

February is the instructive one. **Adjustment made the rise look larger, not smaller.** January 2023 was unusually low even for a January, so once the calendar is taken out, the climb into February is bigger than it appeared.

That is the correct behaviour and it is worth saying explicitly: **adjustment is not a smoothing device.** It removes one specific, predictable component. Whatever it uncovers is what was underneath.

### Every agency needs its own factors

| Seasonal factor | Jan | Feb | Mar | Apr | May | Jun | Jul | Aug | Sep | Oct | Nov | Dec |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Ashfell | 0.78 | **0.71** | 0.86 | 0.94 | 1.10 | 1.30 | 1.44 | 1.45 | 1.11 | 0.99 | 0.86 | 0.80 |
| Pinecrest State University | 1.11 | 1.15 | 1.07 | 1.05 | 0.73 | **0.55** | 0.57 | 0.90 | 1.44 | 1.36 | 1.14 | 0.93 |

Ashfell's quietest month is February. Pinecrest's is June, when the students leave. Applying a single statewide factor would inflate Pinecrest's summer and deflate its autumn, manufacturing a pattern that is not there.

### The factors themselves get revised

Estimate Ashfell's 2024 factors using data through 2024, then again using data through 2026, and they differ. The largest revisions are in the later months, nearest the end of the shorter series, because loess has data on only one side of them.

An adjusted figure published in January 2025 was therefore provisional in a second sense, beyond the reporting lag of [Module 2](Module_02_Building_An_Honest_Calendar.md): **the adjustment itself was not final.**

## Do It Yourself

> 📓 **Notebook:** [Module_07_Seasonal_Adjustment.ipynb](Notebooks/Module_07_Seasonal_Adjustment.ipynb)
> [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/YinZhangCISER/Public-Safety-Statistics-Tutorials/blob/main/Time_Series/Intermediate/Notebooks/Module_07_Seasonal_Adjustment.ipynb)
> About 15 minutes.

The notebook builds the factors, adjusts the series, reproduces both tables, compares Ashfell against Pinecrest, demonstrates the revision problem directly, and ends with an exercise on what adjustment does to the Tarnbridge unrest month.

## When you may write "seasonally adjusted"

| Condition | Why |
|---|---|
| At least three full years, preferably five | each factor is an average across years |
| Factors estimated from this agency and this series | seasonality differs by agency type and by numerator |
| The estimation window stated | factors change when the window changes |
| Provisional months excluded | they drag the recent factors |
| The unadjusted series published alongside | readers must be able to see what was done |

## Pitfalls

| What goes wrong | What it looks like | What to do |
|---|---|---|
| Borrowing factors from another agency | a manufactured pattern, backwards for a campus force | estimate per agency |
| Adjusting the count and talking about behaviour | a July claim from an August peak | adjust the series the question is about |
| Expecting adjustment to remove spikes | a one off event still visible and called a failure | it is not outlier removal, and should not be |
| Treating the latest adjusted point as final | a figure that quietly changes next month | flag recent adjusted values as subject to revision |
| Publishing only the adjusted series | nobody can check the adjustment | show both |
| Adjusting, then comparing year over year | the seasonal correction applied twice | pick one method, not both |

## Check Your Understanding

<details>
<summary><b>1.</b> Adjustment turned June's +51 percent into +21 percent but turned February's +28 percent into +46 percent. Is something wrong?</summary>

No, and the asymmetry is the point. Adjustment divides each month by its own factor. June's factor is high, so dividing shrinks the apparent jump. January's factor is very low, so January 2023's already low count of 50 becomes an even lower adjusted figure, which makes the climb into February look steeper. Adjustment corrects for the calendar in whichever direction the calendar points; it is not a device for making numbers smaller.
</details>

<details>
<summary><b>2.</b> An agency has two years of data and wants to publish a seasonally adjusted series. What should it do instead?</summary>

Publish the unadjusted series with a year over year column. Two years gives two observations per calendar month, so each factor is essentially an average of two numbers and will move substantially when the third year arrives. Adjusting on that basis produces a series whose history changes every time it is updated. Year over year comparison needs no estimated factors and is honest with short data.
</details>

<details>
<summary><b>3.</b> Why are the most recent adjusted values the least reliable, and what should a monthly report do about it?</summary>

Because loess estimates each point using data on both sides of it, and at the end of the series there is no right hand side, so those factors rest on less information and get revised as months arrive. A monthly report should mark the most recent two or three adjusted points as subject to revision, publish the unadjusted values next to them, and avoid making a decision that turns on the newest adjusted figure alone.
</details>

## Key Takeaway

Divide by factors estimated from that agency's own series, publish the unadjusted values alongside, and remember that adjustment removes the calendar and nothing else.

---

| | |
|---|---|
| **Previous** | [Module 6: Measuring the Trend](Module_06_Measuring_The_Trend.md) |
| **Next** | [Module 8: Rolling Statistics and Control Limits](Module_08_Rolling_Statistics_And_Control_Limits.md) |
| **Builds on** | [Beginner Topic 18](../Beginner/Topic_18_Year_Over_Year_Comparison.md), [Module 5](Module_05_Decomposition.md) |
| **Used again in** | [Module 8](Module_08_Rolling_Statistics_And_Control_Limits.md), [Module 9](Module_09_Year_Over_Year_And_Indexing.md) |

*This module is part of a series developed for the Washington Data Exchange for Public Safety (WADEPS) through the Center for Interdisciplinary Statistical Education and Research (CISER) at Washington State University. Version 1.0, September 2026. Questions, errors, or suggestions: yin.zhang@wsu.edu*

*All examples use synthetic data created for teaching. They do not represent any real jurisdiction, agency, officer, or incident. See [Data/DATA_DICTIONARY.md](../../Data/DATA_DICTIONARY.md).*
