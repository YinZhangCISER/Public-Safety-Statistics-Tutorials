# Public Safety Statistics Tutorials

### Time Series and Causal Inference, from no background to working analyst

> **Developed by Yin Zhang, PhD**
> Assistant Professor, Data Analytics Program, Department of Mathematics and Statistics, Washington State University
>
> Developed for the [Washington Data Exchange for Public Safety (WADEPS)](https://wadeps.org) through the [Center for Interdisciplinary Statistical Education and Research (CISER)](https://ciser.wsu.edu) at Washington State University.
> Contact: [yin.zhang@wsu.edu](mailto:yin.zhang@wsu.edu)

---

## What this is

Two tutorial series, each in three levels, that teach the statistics behind public safety data using public safety questions.

The material is written for people who need to read what their data is telling them, not for people training to become statisticians. It starts with a reader who has never taken a statistics course and ends with methods an agency analyst or a graduate researcher can defend in a report.

Every example uses one synthetic dataset built to look exactly like WADEPS. Code you write here runs unchanged against a real extract.

## Start here

| If you are | Start at | What you will be able to do |
|---|---|---|
| A commander, an administrator, a reporter, or a member of the public | [Time Series, Beginner](Time_Series/Beginner/) | Read any chart of incidents over time and say what is real in it |
| An officer, an agency staff member, or an undergraduate student | [Time Series, Intermediate](Time_Series/Intermediate/) | Build the series yourself, measure a trend, adjust for season, make a forecast |
| An agency data analyst, a graduate student, or an early career researcher | [Time Series, Advanced](Time_Series/Advanced/) | Fit and defend a model, and know when not to |
| Anyone asking whether a program worked | [Causal Inference](Causal_Inference/) | Tell the effect of a policy apart from everything else that was happening |

Not sure which method your question calls for? See the [method selection guides](Shared/Method_Selection_Guides/).

---

## The two series

### 📈 Time Series

| Level | Modules | For | Code | Status |
|---|---|---|---|---|
| [Beginner](Time_Series/Beginner/) | 20 | No statistics background at all | None | **Complete** |
| [Intermediate](Time_Series/Intermediate/) | 16 | Some background, wants to do it | Jupyter notebooks, gentle | **Complete** |
| [Advanced](Time_Series/Advanced/) | 14 | Fits models and reports results | Jupyter notebooks, complete | Planned |

### 🎯 Causal Inference

| Level | Modules | For | Code | Status |
|---|---|---|---|---|
| [Beginner](Causal_Inference/Beginner/) | 20 | No statistics background at all | None | Planned |
| [Intermediate](Causal_Inference/Intermediate/) | 16 | Some background, wants to do it | Jupyter notebooks, gentle | Planned |
| [Advanced](Causal_Inference/Advanced/) | 16 | Fits models and reports results | Jupyter notebooks, complete | Planned |

---

## The teaching dataset

Twelve fictional Washington agencies, 90 months, from January 2019 through June 2026. Field names, category labels and marginal distributions are modeled on WADEPS: eight incident types, 32 incident details, the reportable use of force fields, and agency context variables.

**The data are entirely synthetic.** No record describes a real agency, officer, or person.

What makes it useful for teaching is that the answers are known. Eleven patterns were deliberately built in, each with a known size, a known date, and a known cause:

- a secular decline of about 5 percent a year in every agency
- an annual July peak of about 20 percent
- one agency that follows the academic calendar instead
- one documented outlier month caused by civil unrest
- one three month reporting gap
- one classification definition change that moves no calls but breaks a category
- two provisional months at the end of the series
- one agency whose rate was already falling faster than everyone else's
- **a de escalation training program with a true effect of exactly 12 percent, phased in over four months, at five agencies that were not chosen at random**
- two agencies too small for their monthly rates to mean anything
- two agencies with incomplete call for service coverage

So every method can be graded. A naive before and after comparison of the training program returns about a 30 percent reduction. The truth is 12 percent. Difference in differences recovers it. That contrast, with real numbers, is the spine of the whole repository.

| | |
|---|---|
| **Files and fields** | [Data/DATA_DICTIONARY.md](Data/DATA_DICTIONARY.md) |
| **The answer key** | [Data/GROUND_TRUTH.md](Data/GROUND_TRUTH.md) |
| **Rebuild the data** | `python Data/generate_synthetic_wadeps.py` |
| **Check it still works** | `python Data/verify_ground_truth.py` |

---

## Running the code

Every notebook opens in Google Colab and runs top to bottom with no setup. Nothing to install, nothing to download.

To run locally instead:

```bash
git clone <this repository>
cd Public-Safety-Statistics-Tutorials
pip install -r requirements.txt
jupyter lab
```

Notebooks are written to work with both pandas 1.4 and pandas 2.x.

---

## Repository layout

```
Public-Safety-Statistics-Tutorials/
├── Time_Series/
│   ├── Beginner/        20 modules, no code
│   ├── Intermediate/    16 modules + notebooks
│   └── Advanced/        14 modules + notebooks
├── Causal_Inference/    the same three levels
├── Data/                the synthetic dataset, its dictionary, its answer key
├── Shared/              glossary, method selection guides, module template
├── PDF/                 printable versions of each level
└── requirements.txt
```

---

## 📹 CISER video tutorials

CISER is producing a companion series of foundational statistics videos led by subject matter experts across several disciplines, together with short animated explainers on the WADEPS variables themselves. They will be linked here as they are released.

---

## Who this is for

| Audience | How to use it |
|---|---|
| **Public safety professionals** | Read modules on demand. Keep the Beginner Topic 20 checklist in your briefing materials. |
| **Agency data analysts** | Work the Intermediate series through, then take the Advanced modules your questions require. |
| **Policymakers and legislative staff** | Beginner Topics 5, 11, 12, 18 and 19 cover the ways public safety numbers are most often misread. |
| **Journalists** | The same five, plus the Causal Inference Beginner series before writing that a program worked. |
| **Students and instructors** | The dataset has known answers, so the exercises grade themselves. Everything is CC BY 4.0. |
| **Researchers** | Advanced modules, and the reproducibility practices in Advanced Module 14. |

---

## License and citation

Written tutorials: **CC BY 4.0**. Code: **MIT**. Data: public domain. See [LICENSE_TEXT.md](LICENSE_TEXT.md) and [LICENSE](LICENSE).

> Zhang, Y. (2026). *Public Safety Statistics Tutorials: Time Series and Causal Inference.* Washington State University. Developed for the Washington Data Exchange for Public Safety (WADEPS).

GitHub will generate a formatted citation from [CITATION.cff](CITATION.cff) in the sidebar.

---

## Feedback

This is a living document. Corrections, disagreements, and requests for topics are all welcome.

**Yin Zhang, PhD**
Assistant Professor, Data Analytics Program
Department of Mathematics and Statistics
Washington State University
[yin.zhang@wsu.edu](mailto:yin.zhang@wsu.edu)

*All examples use synthetic data created for teaching. They do not represent any real jurisdiction, agency, officer, or incident.*
