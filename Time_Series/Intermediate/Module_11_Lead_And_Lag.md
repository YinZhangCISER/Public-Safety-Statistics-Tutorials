# Module 11: Lead and Lag Between Two Series

> **Developed by Yin Zhang, PhD**, Assistant Professor, Department of Mathematics and Statistics, Washington State University

**The question this module answers:** *Does call volume move before use of force does, and how would I tell?*

---

## The Question

It is a reasonable operational question. If calls for service rose two months before use of force did, that would be an early warning worth having.

It is also an easy question to answer wrongly, because two public safety series almost always correlate. Both rise in summer and both drift with the same long run forces. Correlating them as they stand measures the calendar they share.

## The Idea in Plain Language

The **cross correlation function** shifts one series against the other and reports the correlation at each shift. A peak at a negative lag means the first series leads.

Before computing it, remove from **both** series everything they are known to share: the trend and the season. What survives is the month to month movement that each series has of its own, and a correlation between those is evidence of a genuine link.

## The Method

```python
clean_x = np.exp(STL(np.log(x), period=12, robust=True).fit().resid)
clean_y = np.exp(STL(np.log(y), period=12, robust=True).fit().resid)
c = ccf(clean_x, clean_y)
```

Then judge against a noise band of about ±1.96/√n, and remember you are looking at 25 values at once.

## Worked Example

Ashfell Police Department, three series: calls for service, arrests, and use of force. The noise band is **±0.21**.

### Straight off the raw series

![Two panels of cross correlation bars. The left panel, computed on raw series, oscillates in a wave from about plus 0.6 at lag 12 to about minus 0.8 at lag 6. The right panel, computed after removing trend and season from both series, is flat and inside the noise band except for a single tall bar for arrests at lag zero](Figures/fig_m11_lead_and_lag.png)

| Lag | −12 | −6 | −1 | 0 | +1 | +6 | +12 |
|---|---|---|---|---|---|---|---|
| **Correlation** | +0.61 | −0.74 | +0.54 | +0.57 | +0.37 | −0.78 | **+0.62** |

The largest value is at **lag 12**. Read literally, that says calls for service twelve months ago predict use of force today better than calls this month do.

That is nonsense, and the shape gives it away. The values oscillate with a twelve month period, because shifting one seasonal series by six months lines its summer up against the other's winter. **A cross correlation on raw seasonal series measures the calendar.**

### After removing trend and season from both

| | Lag 0 | Anything outside the band |
|---|---|---|
| Calls for service to use of force | **+0.12** | scattered marginal values, consistent with testing 25 lags |
| Arrests to use of force | **+0.44** | **lag 0 only** |

**Calls for service tell you almost nothing.** At lag 0 the correlation sits inside the noise band.

**Arrests tell you a great deal, at lag 0 and nowhere else.** The +0.44 is the only value in the entire function that clears the band.

The pair of results together is what makes this convincing. The method found nothing where there is nothing, and one clean thing where there is one. **A method that flags something everywhere is not detecting, it is decorating.**

### Why calls do not reach through

| Link | Correlation at lag 0 |
|---|---|
| Calls to arrests | +0.37 |
| Arrests to use of force | +0.44 |
| Calls to use of force | **+0.12** |

Each link is real and moderate; the two together are weak. Every step adds its own variation, so by the time you get from calls to use of force two layers of noise sit between them. That is an ordinary feature of chained relationships, and a good reason to measure the step you care about rather than the one whose data is easiest to obtain.

## Do It Yourself

> 📓 **Notebook:** [Module_11_Lead_And_Lag.ipynb](Notebooks/Module_11_Lead_And_Lag.ipynb)
> [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/YinZhangCISER/Public-Safety-Statistics-Tutorials/blob/main/Time_Series/Intermediate/Notebooks/Module_11_Lead_And_Lag.ipynb)
> About 20 minutes.

The notebook builds the cross correlation from scratch, reproduces both panels, traces the chain, and ends with an exercise running the same analysis on Tarnbridge, where the identical built in relationship turns out to be undetectable.

## Pitfalls

| What goes wrong | What it looks like | What to do |
|---|---|---|
| Correlating raw seasonal series | a wave, and a spurious peak at lag 12 | remove trend and season from both first |
| Removing the season from only one series | a correlation driven by the one that still has it | treat both sides identically |
| Reading a peak as a cause | "calls drive force" from a lag alone | a lead is consistent with a shared driver too |
| Testing 25 lags and reporting the biggest | about one false positive per analysis | decide which lags are plausible in advance |
| Concluding "no relationship" from a flat function | a real effect that the agency is too small to reveal | it means not detectable here, never not there |
| Measuring the convenient link rather than the relevant one | calls used as a proxy for contacts | measure the step the question is about |

## Check Your Understanding

<details>
<summary><b>1.</b> The raw cross correlation peaks at lag 12 with +0.62. What is actually being measured?</summary>

The shared seasonal cycle. Both series are high in summer and low in winter, so shifting one by exactly twelve months lines summers up with summers again and produces a high correlation. The same mechanism produces the large negative value at lag 6, where summer meets winter. None of it involves one series influencing the other, and the oscillating shape of the whole function is the signature to recognise.
</details>

<details>
<summary><b>2.</b> Why does the arrests result at lag 0 with nothing elsewhere make the analysis more credible than a single strong finding would?</summary>

Because it works as a control. The same procedure applied to calls for service returned nothing, which shows the method is capable of returning nothing. A procedure that produces a significant result on every pair of series it is given has no diagnostic value, because you cannot tell a real finding from its normal output. Having both outcomes from the same method on the same data is what makes either of them worth believing.
</details>

<details>
<summary><b>3.</b> An analyst finds calls for service lead use of force by two months and proposes using call volume as an early warning. What should be checked first?</summary>

Whether the season was removed from both series, since a two month lag is exactly the kind of artifact a shared seasonal cycle produces. Then whether two months was specified in advance or chosen because it was the largest of 25 values. Then whether the relationship holds in other agencies and other periods. And finally, even if all of that survives, whether a lead is useful: a correlation of 0.3 at two months will not support a forecast anyone can act on.
</details>

## Key Takeaway

Remove trend and season from both series before correlating them, judge against the noise band while remembering how many lags you tested, and treat a flat result as a statement about the evidence rather than about the world.

---

| | |
|---|---|
| **Previous** | [Module 10: Reading ACF and PACF as Pictures](Module_10_Reading_Autocorrelation.md) |
| **Next** | [Module 12: Building a Peer Benchmark Series](Module_12_Building_A_Peer_Benchmark_Series.md) |
| **Builds on** | [Module 5](Module_05_Decomposition.md), [Module 10](Module_10_Reading_Autocorrelation.md) |
| **Used again in** | Advanced Modules 6 and 13 |

*This module is part of a series developed for the Washington Data Exchange for Public Safety (WADEPS) through the Center for Interdisciplinary Statistical Education and Research (CISER) at Washington State University. Version 1.0, September 2026. Questions, errors, or suggestions: yin.zhang@wsu.edu*

*All examples use synthetic data created for teaching. They do not represent any real jurisdiction, agency, officer, or incident. See [Data/DATA_DICTIONARY.md](../../Data/DATA_DICTIONARY.md).*
