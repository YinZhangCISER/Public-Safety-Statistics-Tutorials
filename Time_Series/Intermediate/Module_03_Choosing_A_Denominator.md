# Module 3: Choosing a Denominator

> **Developed by Yin Zhang, PhD**, Assistant Professor, Department of Mathematics and Statistics, Washington State University

**The question this module answers:** *Per resident, per call, per arrest, or per officer? They give different answers, so which one is right?*

---

## The Question

Beginner [Topic 5](../Beginner/Topic_05_Counts_And_Rates.md) established that a count has to be divided by something. It did not say by what.

That turns out to be the harder question. There are four defensible denominators for use of force, they rank agencies differently, and the choice is not technical. It is a choice about what is being asked.

## The Idea in Plain Language

A denominator is an **exposure**: the amount of opportunity there was for the thing to happen. Different denominators describe different opportunities.

| Rate | The question it answers | Who it is for |
|---|---|---|
| per 100 arrests | when officers take someone into custody, how often is force involved | oversight of officer decisions |
| per 1,000 calls for service | across everything officers are sent to, how often does force result | operational review |
| per 1,000 residents | how much force does this community experience | community and council |
| per sworn officer | how much force does the average officer apply | staffing and workload |

Each is correct for its own question and misleading for the others.

## The Method

```python
rate = numerator / exposure * scale
```

The scale is cosmetic: per 100, per 1,000, per 100,000. Choose whatever makes the typical value a readable number and state it.

Two properties matter when choosing the exposure.

**Does it measure the right opportunity?** Force happens during police contact, so contacts are the natural exposure. Residents are an exposure for *community burden*, which is a different and equally legitimate question.

**Can the agency move it?** An agency chooses how many arrests to make. If it arrests fewer people but behaves identically in the situations it does encounter, its rate per arrest rises with no change in conduct. Calls for service are generated mostly by the public, so they are harder for an agency to influence. Neither denominator is clean, which is why reporting two is the honest default.

## Worked Example

The twelve agencies in 2023, ranked four ways.

![A bump chart. Each of the twelve agencies is a line running across four columns, one per denominator, with the vertical position showing its rank. Most lines stay roughly level. Pinecrest State University falls from fifth to eleventh between arrests and residents, and Elkhorn rises from fourth to first](Figures/fig_m03_denominators.png)

| Agency | per 100 arrests | rank | per 1,000 residents | rank |
|---|---|---|---|---|
| Cedar Falls | 3.34 | 1 | 3.57 | 2 |
| Riverbend | 2.96 | 2 | 3.27 | 3 |
| Millgate | 2.94 | 3 | 3.04 | 4 |
| **Elkhorn** | 2.89 | **4** | 3.59 | **1** |
| **Pinecrest State University** | 2.83 | **5** | 1.31 | **11** |
| Two Rivers Tribal | 2.81 | 6 | 1.76 | 8 |
| Harbor Point | 2.79 | 7 | 2.85 | 6 |
| Northgate | 2.70 | 8 | 2.97 | 5 |
| Grandview | 2.32 | 9 | 2.37 | 7 |
| Prairie County | 2.24 | 10 | 1.62 | 9 |
| Summit County | 2.23 | 11 | 1.33 | 10 |
| Lakeshore County | 1.93 | 12 | 1.22 | 12 |

Most agencies move a place or two. Two move a long way, and for instructive reasons.

**Pinecrest State University falls from fifth to eleventh.** Its 29,000 residents are students, most of whom leave in June, and the campus also serves visitors who are in nobody's population count. The denominator does not mean the same thing for a campus force that it means for a city. Ranking a campus agency per resident is close to meaningless.

**Elkhorn rises from fourth to first.** It is an eight officer department with 3,900 residents and fourteen incidents in the entire year. A small denominator and a tiny numerator produce a rate that looks alarming and carries almost no information. Whether that number can support a ranking at all is [Module 4](Module_04_Why_Small_Agencies_Look_Volatile.md).

**The coverage trap.** Prairie County submitted only nine months of 2022. Its 2022 **rate** is fine, because incidents and arrests are both short by the same three months and the ratio is unaffected. Its 2022 **count** is not comparable to any other agency's. Rates tolerate coverage gaps; counts do not.

## Do It Yourself

> 📓 **Notebook:** [Module_03_Choosing_A_Denominator.ipynb](Notebooks/Module_03_Choosing_A_Denominator.ipynb)
> [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/OWNER/REPO/blob/main/Time_Series/Intermediate/Notebooks/Module_03_Choosing_A_Denominator.ipynb)
> Opens in Google Colab, runs top to bottom, about 15 minutes.

The notebook builds all four rates, produces the rank comparison, demonstrates the coverage trap, and ends with a reusable `agency_rates` function that reports the number of months behind each figure.

## Pitfalls

| What goes wrong | What it looks like | What to do |
|---|---|---|
| The denominator goes unnamed | "the rate rose 12 percent" with no way to check it | name it and the scale, every time |
| Numerator and denominator cover different periods | a rate that jumps when an agency has a reporting gap | count the months on both sides and report them |
| Comparing a count to a rate | a large agency always looks worst | compare like with like |
| A denominator the agency controls | a rate that moves when arrest policy changes | report per call as well as per arrest |
| Population used for a non residential agency | campus, transit and tribal forces ranked nonsensically | use contacts, not residents, for those agencies |
| A denominator near zero | enormous rates from tiny agencies | suppress or flag below a minimum exposure, and see Module 4 |

## Check Your Understanding

<details>
<summary><b>1.</b> A department reduces arrests by 20 percent and its use of force count falls by 10 percent. What happens to its rate per arrest, and what should be concluded?</summary>

The rate rises by about 12 percent, because the denominator fell faster than the numerator. Whether that is bad depends entirely on why arrests fell. If the department stopped making low risk arrests, the remaining ones are on average more confrontational and a higher rate per arrest is expected with no change in conduct. This is why the rate per call for service, which the department controls less, belongs in the same table.
</details>

<details>
<summary><b>2.</b> Why is ranking Pinecrest State University per 1,000 residents a bad idea, while ranking it per 100 arrests is reasonable?</summary>

Because its resident count does not describe who is exposed to its policing. The student population empties out in summer, and the campus serves visitors and staff who are counted somewhere else. Arrests, by contrast, are actual police contacts made by that agency, so they measure exposure in the same way for Pinecrest as for anyone else. The general rule is to prefer a denominator built from the agency's own activity when the population base is not comparable.
</details>

<details>
<summary><b>3.</b> An agency has nine months of data in a year. Which of its 2022 figures can be compared with a twelve month agency, and which cannot?</summary>

Rates can, counts cannot. A rate is a ratio in which both parts cover the same nine months, so the missing quarter cancels. A count is a total over a shorter period and is understated by roughly a quarter. If a count has to be shown, either annualise it and label the estimate, or restrict every agency to the same nine months.
</details>

## Key Takeaway

Say which denominator you used, report at least two, and check that both sides of the ratio cover the same months.

---

| | |
|---|---|
| **Previous** | [Module 2: Building an Honest Calendar](Module_02_Building_An_Honest_Calendar.md) |
| **Next** | [Module 4: Why Small Agencies Look Volatile](Module_04_Why_Small_Agencies_Look_Volatile.md) |
| **Builds on** | [Beginner Topic 5](../Beginner/Topic_05_Counts_And_Rates.md), [Module 2](Module_02_Building_An_Honest_Calendar.md) |
| **Used again in** | [Module 12: Comparing Agencies Fairly](Module_12_Comparing_Agencies_Fairly.md) |

*This module is part of a series developed for the Washington Data Exchange for Public Safety (WADEPS) through the Center for Interdisciplinary Statistical Education and Research (CISER) at Washington State University. Version 1.0, September 2026. Questions, errors, or suggestions: yin.zhang@wsu.edu*

*All examples use synthetic data created for teaching. They do not represent any real jurisdiction, agency, officer, or incident. See [Data/DATA_DICTIONARY.md](../../Data/DATA_DICTIONARY.md).*
