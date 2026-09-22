# Method Selection Guides

*Developed by Yin Zhang, PhD, Assistant Professor, Data Analytics Program, Department of Mathematics and Statistics, Washington State University, for the Washington Data Exchange for Public Safety (WADEPS) through the Center for Interdisciplinary Statistical Education and Research (CISER).*

Two pages for the reader who has a question and does not yet know which method answers it. Each entry points at the module where that method is worked end to end.

| Guide | Use it when the question is |
|---|---|
| [Choosing a Time Series Method](Time_Series_Method_Selection.md) | What did this series do, and what will it do next? |
| [Choosing a Causal Inference Design](Causal_Inference_Method_Selection.md) | Did the program cause the change? |

The boundary between them matters more than it looks. A time series method describes what happened; it does not establish why. Interrupted time series sits on the line and is the design most often read as though it had settled a causal question when it has not.

Both guides carry the same warning in different words: **the check that rules a method out is almost always cheaper than the method itself, and it has to be run first.** In this repository's teaching data, four of seven causal designs should never have been run, and each of the four announces that in one diagnostic requiring no model.

---

*Questions, corrections, or suggestions: yin.zhang@wsu.edu*
