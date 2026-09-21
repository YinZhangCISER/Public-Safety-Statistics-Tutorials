"""
Build every figure in the Time Series Beginner series.

All figures are drawn from the synthetic WADEPS dataset in Data/. Running this
script overwrites the PNG files that the Markdown modules link to.

    python make_figures.py

Colors follow the CISER data visualization palette: categorical slot 1 blue
#2a78d6, slot 2 orange #eb6834, slot 3 aqua #1baf7a, on surface #fcfcfb. Series
are always direct labeled or listed in a legend, never identified by color
alone, and every number shown here also appears in a table in the module text.

Developed by Yin Zhang, PhD, Assistant Professor, Data Analytics Program,
Department of Mathematics and Statistics, Washington State University, for
the Washington Data Exchange for Public Safety (WADEPS) through the Center
for Interdisciplinary Statistical Education and Research (CISER).
"""

from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

HERE = Path(__file__).resolve().parent
DATA = HERE.parents[2] / "Data"

BLUE, ORANGE, AQUA = "#2a78d6", "#eb6834", "#1baf7a"
SURFACE = "#fcfcfb"
INK, INK2, INK3 = "#0b0b0b", "#52514e", "#8a8880"
GRID = "#e8e7e3"
MONTHS = ["Jan", "Feb", "Mar", "Apr", "May", "Jun",
          "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]

plt.rcParams.update({
    "figure.facecolor": SURFACE, "axes.facecolor": SURFACE,
    "savefig.facecolor": SURFACE,
    "font.size": 10, "text.color": INK,
    "axes.labelcolor": INK2, "xtick.color": INK2, "ytick.color": INK2,
    "axes.edgecolor": GRID, "axes.linewidth": 0.8,
    "xtick.major.size": 0, "ytick.major.size": 0,
    "font.family": "DejaVu Sans",
})


def style(ax, ygrid=True):
    ax.spines[["top", "right"]].set_visible(False)
    ax.spines[["left", "bottom"]].set_color(GRID)
    if ygrid:
        ax.grid(axis="y", color=GRID, lw=0.8, zorder=0)
        ax.set_axisbelow(True)
    return ax


def title(ax, main, sub=None):
    ax.set_title(main, loc="left", fontsize=11, color=INK, pad=26 if sub else 8)
    if sub:
        ax.text(0, 1.012, sub, transform=ax.transAxes, fontsize=9,
                color=INK2, va="bottom")


# ---------------------------------------------------------------- load data
m = pd.read_csv(DATA / "agency_monthly.csv")
u = pd.read_csv(DATA / "use_of_force.csv")
m["year"] = m["year_month"].str[:4]
m["mon"] = m["year_month"].str[5:7].astype(int)

g23 = m[(m["agency_id"] == "A012") & (m["year"] == "2023")].sort_values("mon")
GRANDVIEW = g23["n_uof"].tolist()


# ------------------------------------------------- 1. what is a time series
def fig_01():
    fig, ax = plt.subplots(figsize=(9, 4.4))
    avg = np.mean(GRANDVIEW)
    ax.axhline(avg, color=INK3, lw=1.2, ls=(0, (4, 3)), zorder=1)
    ax.text(11.35, avg + 4, f"the one number answer: {avg:.0f} a month",
            fontsize=9, color=INK2, ha="right")
    ax.plot(MONTHS, GRANDVIEW, color=BLUE, lw=2, marker="o", ms=5,
            mfc=SURFACE, mew=1.6, zorder=3)
    for i, lab in [(0, "January\n50"), (6, "July\n157"), (11, "December\n78")]:
        ax.annotate(lab, (i, GRANDVIEW[i]), textcoords="offset points",
                    xytext=(0, 14 if i == 6 else -30), ha="center",
                    fontsize=9, color=INK, weight="bold")
    ax.set_ylim(0, 185)
    ax.set_ylabel("use of force incidents")
    style(ax)
    title(ax, "Ashfell Police Department, 2023",
          "1,136 incidents for the year. The timing is the part the total hides.")
    fig.tight_layout()
    fig.savefig(HERE / "fig_01_what_is_a_time_series.png", dpi=150)
    plt.close(fig)


# --------------------------------------------- 2. snapshot against a movie
def fig_02():
    years = [str(y) for y in range(2019, 2026)]
    rate = {}
    for aid in ["A007", "A008"]:
        d = m[(m["agency_id"] == aid) & (m["year"].isin(years))]
        rate[aid] = [100 * d[d["year"] == y]["n_uof"].sum() / d[d["year"] == y]["n_arrests"].sum()
                     for y in years]

    fig, (a1, a2) = plt.subplots(1, 2, figsize=(11, 4.4),
                                 gridspec_kw={"width_ratios": [1, 1.9]})

    i23 = years.index("2023")
    vals = [rate["A007"][i23], rate["A008"][i23]]
    bars = a1.bar(["Summit\nCounty", "Lakeshore\nCounty"], vals,
                  color=[BLUE, ORANGE], width=0.55, zorder=3)
    for b, v in zip(bars, vals):
        a1.text(b.get_x() + b.get_width() / 2, v + 0.06, f"{v:.2f}",
                ha="center", fontsize=10, color=INK, weight="bold")
    a1.set_ylim(0, 3.0)
    a1.set_ylabel("use of force per 100 arrests")
    style(a1)
    title(a1, "The snapshot: 2023 only", "Summit County looks worse.")

    for aid, color, lab in [("A007", BLUE, "Summit County"), ("A008", ORANGE, "Lakeshore County")]:
        a2.plot(years, rate[aid], color=color, lw=2, marker="o", ms=5,
                mfc=SURFACE, mew=1.6, zorder=3, label=lab)
        a2.text(6.12, rate[aid][-1], f" {lab}\n {rate[aid][-1]:.2f}",
                color=INK, fontsize=9, va="center")
    a2.axvspan(i23 - 0.25, i23 + 0.25, color=INK3, alpha=0.13, zorder=1)
    a2.text(i23, 0.18, "the snapshot\nyear", ha="center", fontsize=8.5, color=INK2)
    a2.set_xlim(-0.3, 8.6)
    a2.set_ylim(0, 4.4)
    a2.set_ylabel("use of force per 100 arrests")
    style(a2)
    title(a2, "The movie: 2019 through 2025",
          "Summit County was far worse, and is now improving fastest.")
    fig.tight_layout()
    fig.savefig(HERE / "fig_02_snapshot_and_movie.png", dpi=150)
    plt.close(fig)


# ------------------------------------------------- 3. reading a line plot
def fig_03():
    fig, (a1, a2, a3) = plt.subplots(1, 3, figsize=(13.5, 4.2))

    a1.plot(MONTHS, GRANDVIEW, color=BLUE, lw=2, zorder=3)
    a1.set_ylim(0, 185)
    a1.set_ylabel("use of force incidents")
    style(a1)
    title(a1, "Right: the axis starts at zero", "The summer rise is real and is shown at its real size.")

    a2.plot(MONTHS, GRANDVIEW, color=ORANGE, lw=2, zorder=3)
    a2.set_ylim(45, 160)
    a2.set_ylabel("use of force incidents")
    style(a2)
    title(a2, "Wrong: the axis is cut off", "Same numbers. January now looks like nothing.")

    six = ["A001", "A002", "A003", "A007", "A008", "A012"]
    for aid, c in zip(six, [BLUE, ORANGE, AQUA, "#eda100", "#e87ba4", "#4a3aa7"]):
        d = m[(m["agency_id"] == aid) & (m["year"] == "2023")].sort_values("mon")
        a3.plot(MONTHS, d["n_uof"].tolist(), color=c, lw=1.6, zorder=3,
                label=d["agency_name"].iloc[0].split()[0])
    a3.legend(fontsize=7.5, frameon=False, ncol=2, loc="upper left")
    a3.set_ylim(0, 185)
    a3.set_ylabel("use of force incidents")
    style(a3)
    title(a3, "Wrong: too many lines", "Six agencies at once. No one can follow a single line.")

    for a in (a1, a2, a3):
        a.tick_params(labelsize=8.5)
        for lab in a.get_xticklabels()[1::2]:
            lab.set_visible(False)
    fig.tight_layout()
    fig.savefig(HERE / "fig_03_reading_a_line_plot.png", dpi=150)
    plt.close(fig)


# --------------------------------------------------- 4. three frequencies
def fig_04():
    fig, (a1, a2, a3) = plt.subplots(1, 3, figsize=(13.5, 4.2))

    jul = u[(u["agency_id"] == "A012") & (u["year_month"] == "2023-07")]
    days = pd.date_range("2023-07-01", "2023-07-31")
    counts = [int((jul["incident_date"] == d.strftime("%Y-%m-%d")).sum()) for d in days]
    a1.plot(range(1, 32), counts, color=BLUE, lw=1.4, zorder=3)
    a1.set_ylim(0, 12)
    a1.set_xlabel("day of July 2023")
    a1.set_ylabel("use of force incidents")
    style(a1)
    title(a1, "Daily: static", "Every quiet day looks like success. No pattern survives.")

    a2.plot(MONTHS, GRANDVIEW, color=BLUE, lw=2, marker="o", ms=4,
            mfc=SURFACE, mew=1.4, zorder=3)
    a2.set_ylim(0, 185)
    a2.set_ylabel("use of force incidents")
    style(a2)
    title(a2, "Monthly: the pattern appears", "A winter low, a July peak, a return. This is the useful view.")
    a2.tick_params(labelsize=8.5)
    for lab in a2.get_xticklabels()[1::2]:
        lab.set_visible(False)

    years = [str(y) for y in range(2019, 2026)]
    tot = [m[(m["agency_id"] == "A012") & (m["year"] == y)]["n_uof"].sum() for y in years]
    a3.bar(years, tot, color=BLUE, width=0.6, zorder=3)
    for i, v in enumerate(tot):
        a3.text(i, v + 20, f"{v:,}", ha="center", fontsize=8.5, color=INK2)
    a3.set_ylim(0, 1650)
    a3.set_ylabel("use of force incidents")
    style(a3)
    title(a3, "Yearly: the slow drift", "A gentle decline, and no sign that July is different from January.")
    a3.tick_params(labelsize=8.5)

    fig.tight_layout()
    fig.savefig(HERE / "fig_04_three_frequencies.png", dpi=150)
    plt.close(fig)


# ---------------------------------------------------- 5. counts and rates
def fig_05():
    d = (m[m["year"] == "2023"]
         .groupby(["agency_id", "agency_name"], as_index=False)
         .agg(uof=("n_uof", "sum"), arr=("n_arrests", "sum")))
    d["rate"] = 100 * d["uof"] / d["arr"]
    d["short"] = d["agency_name"].str.replace(" Police Department", "", regex=False) \
                                 .str.replace(" Sheriff's Office", "", regex=False) \
                                 .str.replace(" Police", "", regex=False)

    fig, (a1, a2) = plt.subplots(1, 2, figsize=(12.5, 5.2))

    bc = d.sort_values("uof")
    colors = [ORANGE if s == "Tarnbridge" else BLUE for s in bc["short"]]
    a1.barh(bc["short"], bc["uof"], color=colors, height=0.68, zorder=3)
    for y, v in enumerate(bc["uof"]):
        a1.text(v + 18, y, f"{v:,}", va="center", fontsize=9, color=INK2)
    a1.set_xlim(0, 1330)
    a1.set_xlabel("use of force incidents in 2023")
    style(a1, ygrid=False)
    a1.grid(axis="x", color=GRID, lw=0.8)
    a1.set_axisbelow(True)
    title(a1, "By count", "Ashfell has by far the most. Tarnbridge is third.")

    rc = d.sort_values("rate")
    colors = [ORANGE if s == "Tarnbridge" else BLUE for s in rc["short"]]
    a2.barh(rc["short"], rc["rate"], color=colors, height=0.68, zorder=3)
    for y, v in enumerate(rc["rate"]):
        a2.text(v + 0.05, y, f"{v:.2f}", va="center", fontsize=9, color=INK2)
    a2.set_xlim(0, 3.9)
    a2.set_xlabel("use of force per 100 arrests in 2023")
    style(a2, ygrid=False)
    a2.grid(axis="x", color=GRID, lw=0.8)
    a2.set_axisbelow(True)
    title(a2, "By rate", "Tarnbridge is the highest in the state. Ashfell is below average.")

    fig.tight_layout()
    fig.savefig(HERE / "fig_05_counts_and_rates.png", dpi=150)
    plt.close(fig)


# ------------------------------------------------ 6. missing and zero
def fig_06():
    fig, (a1, a2, a3) = plt.subplots(1, 3, figsize=(13.5, 4.3))

    d = m[(m["agency_id"] == "A009") & (m["year_month"] >= "2021-07")
          & (m["year_month"] <= "2022-12")]
    cal = pd.period_range("2021-07", "2022-12", freq="M").astype(str)
    have = dict(zip(d["year_month"], d["total_cfs"]))
    joined = [have.get(c, np.nan) for c in cal]
    ticks = [i for i, c in enumerate(cal) if c[5:] in ("07", "01")]
    labs = [c for c in cal if c[5:] in ("07", "01")]

    naive = pd.Series(joined).interpolate().tolist()
    a1.plot(range(len(cal)), naive, color=ORANGE, lw=2, zorder=3)
    a1.set_xticks(ticks); a1.set_xticklabels(labs, fontsize=8.5)
    a1.set_ylim(1100, 1900); a1.set_ylabel("calls for service")
    style(a1)
    title(a1, "Wrong: the line runs straight through",
          "Three months are absent. The chart quietly invents them.")

    a2.plot(range(len(cal)), joined, color=BLUE, lw=2, zorder=3)
    gi = [i for i, c in enumerate(cal) if c in ("2022-03", "2022-04", "2022-05")]
    a2.axvspan(gi[0] - 0.5, gi[-1] + 0.5, color=INK3, alpha=0.16, zorder=1)
    a2.text((gi[0] + gi[-1]) / 2, 1160, "never\nsubmitted", ha="center",
            fontsize=8.5, color=INK2)
    a2.set_xticks(ticks); a2.set_xticklabels(labs, fontsize=8.5)
    a2.set_ylim(1100, 1900); a2.set_ylabel("calls for service")
    style(a2)
    title(a2, "Right: the gap is left open",
          "The reader can see there is nothing to know here.")

    e = m[(m["agency_id"] == "A006") & (m["year"] == "2023")].sort_values("mon")
    vals = e["n_uof"].tolist()
    a3.bar(MONTHS, vals, color=BLUE, width=0.62, zorder=3)
    zeros = [i for i, v in enumerate(vals) if v == 0]
    a3.plot(zeros, [0] * len(zeros), marker="o", ls="none", ms=9,
            mfc=ORANGE, mec=SURFACE, mew=1.4, zorder=5)
    a3.text(0.02, 0.93, "● a reported zero", transform=a3.transAxes,
            fontsize=9, color=ORANGE)
    a3.set_ylim(-0.25, 5); a3.set_yticks(range(6))
    a3.set_ylabel("use of force incidents")
    style(a3)
    title(a3, "A zero is not a gap",
          "Orrindale, 2023. Four months reported a true zero.")
    a3.tick_params(labelsize=8.5)
    for lab in a3.get_xticklabels()[1::2]:
        lab.set_visible(False)

    fig.tight_layout()
    fig.savefig(HERE / "fig_06_missing_and_zero.png", dpi=150)
    plt.close(fig)


# ----------------------------------------------------------- 7. trend
def fig_07():
    fig, (a1, a2) = plt.subplots(1, 2, figsize=(12, 4.4))

    d = m[(m["agency_id"] == "A001") & (m["year"] == "2023")].sort_values("mon")
    v = d["n_uof"].tolist()
    a1.plot(MONTHS, v, color=BLUE, lw=2, marker="o", ms=5, mfc=SURFACE, mew=1.6, zorder=3)
    a1.plot([5], [v[5]], marker="o", ms=13, mfc="none", mec=ORANGE, mew=2.2, zorder=4)
    a1.annotate("June: 79\nthe highest month\nof the year",
                (5, v[5]), textcoords="offset points", xytext=(4, 20),
                fontsize=9, color=INK, ha="center")
    a1.set_ylim(0, 110); a1.set_ylabel("use of force incidents")
    style(a1)
    title(a1, "One year on its own", "Stonewick, 2023. June looks like the story.")
    a1.tick_params(labelsize=8.5)
    for lab in a1.get_xticklabels()[1::2]:
        lab.set_visible(False)

    years = [str(y) for y in range(2019, 2026)]
    d2 = m[(m["agency_id"] == "A001") & (m["year"].isin(years))]
    rate = [100 * d2[d2["year"] == y]["n_uof"].sum() / d2[d2["year"] == y]["n_arrests"].sum()
            for y in years]
    fit = np.poly1d(np.polyfit(range(7), rate, 1))
    a2.plot(years, [fit(i) for i in range(7)], color=INK3, lw=1.3, ls=(0, (4, 3)), zorder=2)
    a2.plot(years, rate, color=BLUE, lw=2, marker="o", ms=6, mfc=SURFACE, mew=1.8, zorder=3)
    for i in (0, 6):
        a2.annotate(f"{rate[i]:.2f}", (i, rate[i]), textcoords="offset points",
                    xytext=(0, 12), ha="center", fontsize=9.5, color=INK, weight="bold")
    a2.set_ylim(0, 4.8); a2.set_ylabel("use of force per 100 arrests")
    style(a2)
    title(a2, "The same agency over seven years",
          "Down every single year. June 2023 sits inside a long decline.")

    fig.tight_layout()
    fig.savefig(HERE / "fig_07_trend.png", dpi=150)
    plt.close(fig)


# ----------------------------------------------------- 8. seasonality
def fig_08():
    fig, (a1, a2, a3) = plt.subplots(1, 3, figsize=(13.8, 4.4))

    d = m[(m["provisional"] == 0) & (m["agency_id"] != "A010")]
    idx = d.groupby("mon").apply(lambda x: 100 * x["n_uof"].sum() / x["n_arrests"].sum())
    idx = idx / idx.mean()
    cols = [ORANGE if v >= 1.15 else BLUE for v in idx.values]
    a1.bar(MONTHS, idx.values, color=cols, width=0.66, zorder=3)
    a1.axhline(1.0, color=INK3, lw=1.1, ls=(0, (4, 3)), zorder=4)
    a1.text(0, 1.03, "annual average", ha="left", fontsize=8.5, color=INK2)
    a1.set_ylim(0, 1.45); a1.set_ylabel("share of the annual average rate")
    style(a1)
    title(a1, "Every agency pooled, 2019 to 2026",
          "June and July run about 25 percent above average.")
    a1.tick_params(labelsize=8.5)
    for lab in a1.get_xticklabels()[1::2]:
        lab.set_visible(False)

    years = [str(y) for y in range(2019, 2026)]
    jan = [int(m[(m["agency_id"] == "A012") & (m["year"] == y) & (m["mon"] == 1)]["n_uof"].iloc[0])
           for y in years]
    jul = [int(m[(m["agency_id"] == "A012") & (m["year"] == y) & (m["mon"] == 7)]["n_uof"].iloc[0])
           for y in years]
    x = np.arange(7)
    a2.bar(x - 0.2, jan, width=0.38, color=BLUE, label="January", zorder=3)
    a2.bar(x + 0.2, jul, width=0.38, color=ORANGE, label="July", zorder=3)
    a2.set_xticks(x); a2.set_xticklabels(years, fontsize=8.5)
    a2.legend(fontsize=8.5, frameon=False, loc="upper right")
    a2.set_ylim(0, 205); a2.set_ylabel("use of force incidents")
    style(a2)
    title(a2, "Ashfell, July against January",
          "July wins in all seven years. That is what predictable means.")

    c = pd.read_csv(DATA / "cfs_monthly_by_type.csv")
    a = c[c["agency_id"] == "A010"].groupby("year_month", as_index=False)["n_calls"].sum()
    a["mon"] = a["year_month"].str[5:7].astype(int)
    camp = a.groupby("mon")["n_calls"].mean()
    camp = camp / camp.mean()
    cols = [ORANGE if v >= 1.25 else BLUE for v in camp.values]
    a3.bar(MONTHS, camp.values, color=cols, width=0.66, zorder=3)
    a3.axhline(1.0, color=INK3, lw=1.1, ls=(0, (4, 3)), zorder=4)
    a3.set_ylim(0, 1.45); a3.set_ylabel("share of the annual average calls")
    style(a3)
    title(a3, "The campus agency disagrees",
          "Pinecrest peaks in September and empties out in June.")
    a3.tick_params(labelsize=8.5)
    for lab in a3.get_xticklabels()[1::2]:
        lab.set_visible(False)

    fig.tight_layout()
    fig.savefig(HERE / "fig_08_seasonality.png", dpi=150)
    plt.close(fig)


# ------------------------------------------ 9. cycles and seasonality
def fig_09():
    fig, (a1, a2) = plt.subplots(1, 2, figsize=(12.5, 4.4))

    d = m[(m["agency_id"] == "A012") & (m["provisional"] == 0)].sort_values("year_month")
    x = pd.PeriodIndex(d["year_month"], freq="M").to_timestamp()
    a1.plot(x, d["n_uof"], color=BLUE, lw=1.4, zorder=3)
    yr = d[d["year"] <= "2025"].groupby("year")["n_uof"].mean()
    a1.plot([pd.Timestamp(f"{y}-07-01") for y in yr.index], yr.values,
            color=ORANGE, lw=2.2, zorder=4)
    a1.text(pd.Timestamp("2024-09-01"), 26, "yearly average", color=ORANGE, fontsize=9)
    a1.text(pd.Timestamp("2019-03-01"), 172, "each spike is July", color=INK2, fontsize=9)
    a1.set_ylim(0, 195); a1.set_ylabel("use of force incidents")
    style(a1)
    title(a1, "What is in this dataset: season plus trend",
          "A peak every twelve months, on a level that drifts slowly down.")

    t = np.linspace(0, 7, 400)
    cyc = 100 + 26 * np.sin(2 * np.pi * t / 4.7 - 0.8)
    a2.plot(2019 + t, cyc, color=INK3, lw=2.2, zorder=3)
    a2.set_xlim(2019, 2026); a2.set_ylim(0, 195)
    a2.set_ylabel("illustrative level")
    a2.set_xticks(range(2019, 2027))
    a2.set_xticklabels([str(y) for y in range(2019, 2027)], fontsize=8.5)
    a2.text(2019.25, 172, "ILLUSTRATION ONLY", fontsize=9, color=ORANGE, weight="bold")
    a2.text(2019.25, 158, "not from this dataset", fontsize=8.5, color=INK2)
    a2.annotate("", xy=(2020.1, 40), xytext=(2024.8, 40),
                arrowprops=dict(arrowstyle="<->", color=INK2, lw=1))
    a2.text(2022.4, 30, "one full swing: close to five years",
            ha="center", fontsize=8.5, color=INK2)
    style(a2)
    title(a2, "What a cycle would look like",
          "No fixed length, no fixed month. Years between turns.")

    fig.tight_layout()
    fig.savefig(HERE / "fig_09_cycles_and_seasonality.png", dpi=150)
    plt.close(fig)


# ----------------------------------------------------------- 10. noise
def fig_10():
    fig, (a1, a2, a3) = plt.subplots(1, 3, figsize=(13.8, 4.3))

    d = m[(m["agency_id"] == "A008") & (m["year"] == "2023")].sort_values("mon")
    v = d["n_uof"].tolist()
    a1.plot(MONTHS, v, color=BLUE, lw=2, marker="o", ms=5, mfc=SURFACE, mew=1.6, zorder=3)
    a1.annotate("14", (9, v[9]), textcoords="offset points", xytext=(0, 11),
                ha="center", fontsize=9.5, color=INK, weight="bold")
    a1.annotate("4", (10, v[10]), textcoords="offset points", xytext=(0, -20),
                ha="center", fontsize=9.5, color=INK, weight="bold")
    a1.set_ylim(0, 19); a1.set_ylabel("use of force incidents")
    style(a1)
    title(a1, "Lakeshore County, 2023",
          "October 14, November 4. A 71 percent drop, and nothing caused it.")
    a1.tick_params(labelsize=8.5)
    for lab in a1.get_xticklabels()[1::2]:
        lab.set_visible(False)

    years = [str(y) for y in range(2019, 2026)]
    d2 = m[(m["agency_id"] == "A008") & (m["year"].isin(years))]
    rate = [100 * d2[d2["year"] == y]["n_uof"].sum() / d2[d2["year"] == y]["n_arrests"].sum()
            for y in years]
    a2.plot(years, rate, color=BLUE, lw=2, marker="o", ms=6, mfc=SURFACE, mew=1.8, zorder=3)
    a2.axhline(np.mean(rate), color=INK3, lw=1.2, ls=(0, (4, 3)), zorder=2)
    a2.text(6.35, np.mean(rate), f" average\n {np.mean(rate):.2f}", fontsize=9, color=INK2, va="center")
    a2.set_xlim(-0.35, 7.8); a2.set_ylim(0, 3.6)
    a2.tick_params(labelsize=8.5)
    a2.set_ylabel("use of force per 100 arrests")
    style(a2)
    title(a2, "The same agency, seven years",
          "No direction at all. The monthly swings were noise around this line.")

    e = m[(m["agency_id"] == "A006") & (m["year"] == "2023")].sort_values("mon")
    vals = e["n_uof"].tolist()
    a3.bar(MONTHS, vals, color=BLUE, width=0.62, zorder=3)
    zeros = [i for i, v in enumerate(vals) if v == 0]
    a3.plot(zeros, [0] * len(zeros), marker="o", ls="none", ms=9,
            mfc=ORANGE, mec=SURFACE, mew=1.4, zorder=5)
    a3.annotate("0 in June,\n4 in July", (6, 4), textcoords="offset points",
                xytext=(0, 12), ha="center", fontsize=9, color=INK)
    a3.set_ylim(-0.3, 6); a3.set_yticks(range(7))
    a3.set_ylabel("use of force incidents")
    style(a3)
    title(a3, "Orrindale, eight officers",
          "Small numbers make every month a headline.")
    a3.tick_params(labelsize=8.5)
    for lab in a3.get_xticklabels()[1::2]:
        lab.set_visible(False)

    fig.tight_layout()
    fig.savefig(HERE / "fig_10_noise.png", dpi=150)
    plt.close(fig)


# -------------------------------------------------------- 11. outliers
def fig_11():
    fig, (a1, a2) = plt.subplots(1, 2, figsize=(12.5, 4.4))

    d = m[(m["agency_id"] == "A002") & (m["year"] == "2021")].sort_values("mon")
    v = d["n_uof"].tolist()
    a1.plot(MONTHS, v, color=BLUE, lw=2, marker="o", ms=5, mfc=SURFACE, mew=1.6, zorder=3)
    a1.plot([5], [v[5]], marker="o", ms=9, mfc=ORANGE, mec=SURFACE, mew=1.6, zorder=5)
    a1.annotate("June 2021: 176\na week of civil unrest", (5, v[5]),
                textcoords="offset points", xytext=(18, -6), fontsize=9, color=INK)
    a1.axhline(np.median(v), color=INK3, lw=1.2, ls=(0, (4, 3)), zorder=2)
    a1.text(11.4, np.median(v) + 6, "typical month: 31", ha="right", fontsize=8.5, color=INK2)
    a1.set_ylim(0, 195); a1.set_ylabel("use of force incidents")
    style(a1)
    title(a1, "Tarnbridge, 2021", "One month is nearly six times the typical month.")
    a1.tick_params(labelsize=8.5)
    for lab in a1.get_xticklabels()[1::2]:
        lab.set_visible(False)

    years = [str(y) for y in range(2019, 2026)]
    dd = m[(m["agency_id"] == "A002") & (m["year"].isin(years))]
    with_o = [dd[dd["year"] == y]["n_uof"].mean() for y in years]
    keep = dd[~((dd["year"] == "2021") & (dd["mon"] == 6))]
    without = [keep[keep["year"] == y]["n_uof"].mean() for y in years]
    x = np.arange(7)
    a2.bar(x - 0.2, with_o, width=0.38, color=ORANGE, label="June 2021 included", zorder=3)
    a2.bar(x + 0.2, without, width=0.38, color=BLUE, label="June 2021 set aside", zorder=3)
    a2.annotate("43.0", (1.8, 43.0), textcoords="offset points", xytext=(0, 5),
                ha="center", fontsize=9, color=INK, weight="bold")
    a2.annotate("30.9", (2.2, 30.9), textcoords="offset points", xytext=(0, 5),
                ha="center", fontsize=9, color=INK, weight="bold")
    a2.set_xticks(x); a2.set_xticklabels(years, fontsize=8.5)
    a2.legend(fontsize=8.5, frameon=False, loc="upper right")
    a2.set_ylim(0, 54); a2.set_ylabel("average incidents a month")
    style(a2)
    title(a2, "What that one month does to every yearly average",
          "It invents a bad year in 2021 that the agency did not have.")

    fig.tight_layout()
    fig.savefig(HERE / "fig_11_outliers.png", dpi=150)
    plt.close(fig)


# ----------------------------------------- 12. short term, long term
def fig_12():
    fig, (a1, a2, a3) = plt.subplots(1, 3, figsize=(13.8, 4.3))
    d = m[(m["agency_id"] == "A012") & (m["year"] == "2023")].sort_values("mon")
    v = d["n_uof"].tolist()

    a1.plot(MONTHS[:6], v[:6], color=ORANGE, lw=2.2, marker="o", ms=5,
            mfc=SURFACE, mew=1.6, zorder=3)
    a1.set_ylim(0, 185); a1.set_ylabel("use of force incidents")
    style(a1)
    title(a1, "Six months: up 156 percent", "January 50 to June 128. A department in trouble.")

    a2.plot(MONTHS[5:], v[5:], color=AQUA, lw=2.2, marker="o", ms=5,
            mfc=SURFACE, mew=1.6, zorder=3)
    a2.set_ylim(0, 185); a2.set_ylabel("use of force incidents")
    style(a2)
    title(a2, "The next six: down 39 percent", "June 128 to December 78. A turnaround.")

    years = [str(y) for y in range(2019, 2026)]
    tot = [m[(m["agency_id"] == "A012") & (m["year"] == y)]["n_uof"].sum() for y in years]
    a3.plot(years, tot, color=BLUE, lw=2.2, marker="o", ms=6, mfc=SURFACE, mew=1.8, zorder=3)
    a3.set_ylim(0, 1650); a3.set_ylabel("use of force incidents a year")
    a3.tick_params(labelsize=8.5)
    style(a3)
    title(a3, "Seven years: down 25 percent", "1,405 to 1,058. Neither of the above happened.")

    for a in (a1, a2):
        a.tick_params(labelsize=8.5)
    fig.tight_layout()
    fig.savefig(HERE / "fig_12_windows.png", dpi=150)
    plt.close(fig)


# ------------------------------------------------------- 13. smoothing
def fig_13():
    fig, (a1, a2) = plt.subplots(1, 2, figsize=(12.5, 4.4))

    d = m[(m["agency_id"] == "A008") & (m["year"] == "2023")].sort_values("mon")
    raw = pd.Series(d["n_uof"].tolist())
    ma = raw.rolling(3).mean()
    a1.plot(MONTHS, raw, color=INK3, lw=1.4, marker="o", ms=4, mfc=SURFACE,
            mew=1.2, zorder=3, label="what was reported")
    a1.plot(MONTHS, ma, color=BLUE, lw=2.4, zorder=4, label="three month average")
    a1.set_ylim(0, 19); a1.set_ylabel("use of force incidents")
    a1.legend(fontsize=8.5, frameon=False, loc="lower left")
    style(a1)
    title(a1, "Lakeshore County, 2023",
          "The 14 to 4 drop becomes 9.7 to 8.3 once the noise is averaged out.")
    a1.tick_params(labelsize=8.5)
    for lab in a1.get_xticklabels()[1::2]:
        lab.set_visible(False)

    g = m[(m["agency_id"] == "A012") & (m["provisional"] == 0)].sort_values("year_month")
    x = pd.PeriodIndex(g["year_month"], freq="M").to_timestamp()
    raw = pd.Series(g["n_uof"].tolist())
    a2.plot(x, raw, color=INK3, lw=1.1, zorder=3, label="what was reported")
    a2.plot(x, raw.rolling(12).mean(), color=BLUE, lw=2.6, zorder=4,
            label="twelve month average")
    a2.set_ylim(0, 195); a2.set_ylabel("use of force incidents")
    a2.legend(fontsize=8.5, frameon=False, loc="lower left")
    style(a2)
    title(a2, "Ashfell, 2019 to 2026",
          "A twelve month average erases the summer entirely, leaving the trend.")

    fig.tight_layout()
    fig.savefig(HERE / "fig_13_smoothing.png", dpi=150)
    plt.close(fig)


# ------------------------------------------------ 14. comparison group
def fig_14():
    fig, (a1, a2) = plt.subplots(1, 2, figsize=(12.8, 4.6))

    trio = [("A002", "Tarnbridge", ORANGE), ("A012", "Ashfell", BLUE),
            ("A008", "Lakeshore County", AQUA)]
    for aid, lab, c in trio:
        d = m[(m["agency_id"] == aid) & (m["year"] == "2021")].sort_values("mon")
        v = np.array(d["n_uof"].tolist(), dtype=float) / d["n_uof"].median()
        a1.plot(MONTHS, v, color=c, lw=2, marker="o", ms=4, mfc=SURFACE,
                mew=1.2, zorder=3, label=lab)
    a1.axhline(1.0, color=INK3, lw=1.1, ls=(0, (4, 3)), zorder=2)
    a1.legend(fontsize=8.5, frameon=False, loc="upper left")
    a1.set_ylim(0, 6.4); a1.set_ylabel("times the agency's own typical month")
    style(a1)
    title(a1, "The same twelve months, three agencies",
          "Each drawn against its own normal, so the sizes can be compared.")
    a1.tick_params(labelsize=8.5)
    for lab in a1.get_xticklabels()[1::2]:
        lab.set_visible(False)

    rows = []
    for aid in sorted(m["agency_id"].unique()):
        d = m[(m["agency_id"] == aid) & (m["year"] == "2021")]
        med = max(d["n_uof"].median(), 0.5)
        rows.append((d["agency_name"].iloc[0].replace(" Police Department", "")
                     .replace(" Sheriff's Office", "").replace(" Police", ""),
                     float(d[d["mon"] == 6]["n_uof"].iloc[0]) / med))
    rows.sort(key=lambda r: r[1])
    names = [r[0] for r in rows]; vals = [r[1] for r in rows]
    cols = [ORANGE if n == "Tarnbridge" else BLUE for n in names]
    a2.barh(names, vals, color=cols, height=0.68, zorder=3)
    for y, v in enumerate(vals):
        a2.text(v + 0.08, y, f"{v:.1f}", va="center", fontsize=9, color=INK2)
    a2.axvline(1.0, color=INK3, lw=1.1, ls=(0, (4, 3)), zorder=4)
    a2.set_xlim(0, 6.6)
    a2.set_xlabel("June 2021, as times that agency's own typical month")
    style(a2, ygrid=False)
    a2.grid(axis="x", color=GRID, lw=0.8); a2.set_axisbelow(True)
    title(a2, "Every agency in June 2021",
          "Eleven agencies had an ordinary June. One did not.")

    fig.tight_layout()
    fig.savefig(HERE / "fig_14_comparison_group.png", dpi=150)
    plt.close(fig)


# ---------------------------------------------------------- 15. lag
def fig_15():
    TRAINED = ["A001", "A002", "A004", "A007", "A010"]
    d = m[(m["provisional"] == 0)].copy()
    d = d[~((d["agency_id"] == "A002") & (d["year_month"] == "2021-06"))]
    d["grp"] = np.where(d["agency_id"].isin(TRAINED), "trained", "control")
    g = (d.groupby(["grp", "year_month"])[["n_uof", "n_arrests"]].sum()
           .reset_index())

    fig, (a1, a2) = plt.subplots(1, 2, figsize=(12.8, 4.5))

    for grp, c, lab in [("trained", ORANGE, "agencies that adopted the training"),
                        ("control", BLUE, "agencies that did not")]:
        s = g[g["grp"] == grp].sort_values("year_month")
        x = pd.PeriodIndex(s["year_month"], freq="M").to_timestamp()
        roll = (100 * s["n_uof"].rolling(12).sum() / s["n_arrests"].rolling(12).sum())
        a1.plot(x, roll, color=c, lw=2.2, zorder=3, label=lab)
    a1.axvline(pd.Timestamp("2023-07-01"), color=INK, lw=1.1, ls=(0, (4, 3)), zorder=4)
    a1.text(pd.Timestamp("2023-07-20"), 3.82, "training begins", fontsize=8.5, color=INK2)
    sep = g[(g["grp"] == "trained")].sort_values("year_month").reset_index(drop=True)
    i = list(sep["year_month"]).index("2023-09")
    ysep = 100 * sep["n_uof"].iloc[i - 11:i + 1].sum() / sep["n_arrests"].iloc[i - 11:i + 1].sum()
    a1.plot([pd.Timestamp("2023-09-01")], [ysep], marker="o", ms=10, mfc="none",
            mec=INK, mew=1.8, zorder=6)
    a1.annotate("two months in, a report\nwritten here calls it a failure",
                xy=(pd.Timestamp("2023-09-20"), ysep),
                xytext=(pd.Timestamp("2024-03-01"), 3.62), fontsize=8.5, color=INK,
                arrowprops=dict(arrowstyle="->", lw=0.9, color=INK2))
    a1.set_ylim(1.5, 4.1); a1.set_ylabel("use of force per 100 arrests")
    a1.legend(fontsize=8.5, frameon=False, loc="lower left", bbox_to_anchor=(0.01, 0.0))
    style(a1)
    title(a1, "Twelve month trailing rate",
          "Two months in, the trained group had not moved at all.")

    labs = ["12 months\nbefore", "first 3 months\nafter launch", "fully in place\nNov 2023 onward"]
    gaps = [20.9, 17.2, 8.3]
    cols = [INK3, INK3, ORANGE]
    b = a2.bar(labs, gaps, color=cols, width=0.55, zorder=3)
    for bb, v in zip(b, gaps):
        a2.text(bb.get_x() + bb.get_width() / 2, v + 0.6, f"{v:.1f}%",
                ha="center", fontsize=10.5, color=INK, weight="bold")
    a2.set_ylim(0, 26)
    a2.set_ylabel("how far the trained group sits above the others")
    a2.tick_params(labelsize=9)
    style(a2)
    title(a2, "The gap between the two groups",
          "Barely moved at three months. Cut by more than half once in place.")

    fig.tight_layout()
    fig.savefig(HERE / "fig_15_lagged_effects.png", dpi=150)
    plt.close(fig)


# ------------------------------------------------- 16. autocorrelation
def fig_16():
    import itertools
    fig, (a1, a2, a3) = plt.subplots(1, 3, figsize=(13.8, 4.3))

    d = m[(m["agency_id"] == "A012") & (m["year"] == "2023")].sort_values("mon")
    v = d["n_uof"].tolist()
    a1.plot(MONTHS, v, color=BLUE, lw=2, marker="o", ms=5, mfc=SURFACE, mew=1.6, zorder=3)
    for i in range(11):
        a1.plot([i, i + 1], [v[i], v[i + 1]], color=ORANGE, lw=3.2, alpha=0.30, zorder=2)
    cons = np.mean([abs(v[i + 1] - v[i]) for i in range(11)])
    rand = np.mean([abs(a - b) for a, b in itertools.combinations(v, 2)])
    a1.text(0.03, 0.93, f"one month to the next: {cons:.0f} apart on average\n"
                        f"any two months of the year: {rand:.0f} apart",
            transform=a1.transAxes, fontsize=9, color=INK, va="top")
    a1.set_ylim(0, 205); a1.set_ylabel("use of force incidents")
    style(a1)
    title(a1, "Ashfell, 2023", "Neighbouring months stay close to each other.")
    a1.tick_params(labelsize=8.5)
    for lab in a1.get_xticklabels()[1::2]:
        lab.set_visible(False)

    for ax, aid, lab, lim in [(a2, "A012", "Ashfell, 902 officers", 205),
                              (a3, "A006", "Orrindale, 8 officers", 6)]:
        d = m[(m["agency_id"] == aid) & (m["provisional"] == 0)].sort_values("year_month")
        y = d["n_uof"].tolist()
        jit = 0.10 if aid == "A006" else 0.0
        rng = np.random.default_rng(7)
        xs = np.array(y[:-1], dtype=float) + rng.normal(0, jit, len(y) - 1)
        ys = np.array(y[1:], dtype=float) + rng.normal(0, jit, len(y) - 1)
        ax.scatter(xs, ys, s=26, color=BLUE, alpha=0.62, edgecolors="none", zorder=3)
        ax.plot([0, lim], [0, lim], color=INK3, lw=1.1, ls=(0, (4, 3)), zorder=2,
                label="next month exactly equals this month")
        ax.legend(fontsize=8, frameon=False, loc="lower right")
        ax.set_xlim(0, lim); ax.set_ylim(0, lim)
        ax.set_xlabel("this month"); ax.set_ylabel("the month after")
        style(ax)
    title(a2, "Ashfell: memory", "Each dot is a pair of neighbouring months. They line up.")
    title(a3, "Orrindale: no memory", "The same picture for a tiny agency is a cloud.")

    fig.tight_layout()
    fig.savefig(HERE / "fig_16_autocorrelation.png", dpi=150)
    plt.close(fig)


# -------------------------------------------------- 17. stationarity
def fig_17():
    years = [str(y) for y in range(2019, 2026)]
    fig, (a1, a2) = plt.subplots(1, 2, figsize=(12.5, 4.4))

    for ax, aid, name, note in [
            (a1, "A008", "Lakeshore County", "Steady. The average is a usable forecast."),
            (a2, "A007", "Summit County", "Falling. The average is a forecast of nothing.")]:
        d = m[(m["agency_id"] == aid) & (m["year"].isin(years))]
        r = [100 * d[d["year"] == y]["n_uof"].sum() / d[d["year"] == y]["n_arrests"].sum()
             for y in years]
        avg = np.mean(r)
        ax.axhline(avg, color=ORANGE, lw=2, ls=(0, (5, 3)), zorder=2)
        ax.text(6.3, avg, f" seven year\n average {avg:.2f}", fontsize=9, color=ORANGE, va="center")
        ax.plot(years, r, color=BLUE, lw=2.2, marker="o", ms=6, mfc=SURFACE, mew=1.8, zorder=3)
        for i in (0, 6):
            ax.annotate(f"{r[i]:.2f}", (i, r[i]), textcoords="offset points",
                        xytext=(0, 12), ha="center", fontsize=9.5, color=INK, weight="bold")
        ax.set_xlim(-0.35, 8.4); ax.set_ylim(0, 4.4)
        ax.set_ylabel("use of force per 100 arrests")
        ax.tick_params(labelsize=8.5)
        style(ax)
        title(ax, name, note)

    fig.tight_layout()
    fig.savefig(HERE / "fig_17_stationarity.png", dpi=150)
    plt.close(fig)


# ---------------------------------------------- 18. year over year
def fig_18():
    fig, (a1, a2) = plt.subplots(1, 2, figsize=(12.8, 4.5))

    d = m[(m["agency_id"] == "A012") & (m["year"].isin(["2022", "2023"]))]
    p = d.pivot_table(index="mon", columns="year", values="n_uof")
    a1.plot(MONTHS, p["2022"], color=INK3, lw=2, marker="o", ms=4, mfc=SURFACE,
            mew=1.2, zorder=3, label="2022")
    a1.plot(MONTHS, p["2023"], color=BLUE, lw=2.2, marker="o", ms=5, mfc=SURFACE,
            mew=1.6, zorder=4, label="2023")
    a1.legend(fontsize=9, frameon=False, loc="upper left")
    a1.set_ylim(0, 185); a1.set_ylabel("use of force incidents")
    style(a1)
    title(a1, "Ashfell, the same months two years running",
          "Both years have the same shape. 2023 sits a little lower.")
    a1.tick_params(labelsize=8.5)
    for lab in a1.get_xticklabels()[1::2]:
        lab.set_visible(False)

    yoy = (100 * (p["2023"] / p["2022"] - 1)).tolist()
    mom = (100 * (p["2023"] / p["2023"].shift(1) - 1)).tolist()
    x = np.arange(12)
    a2.bar(x - 0.2, mom, width=0.38, color=ORANGE, label="against last month", zorder=3)
    a2.bar(x + 0.2, yoy, width=0.38, color=BLUE, label="against the same month last year", zorder=3)
    a2.axhline(0, color=INK2, lw=1.0, zorder=4)
    a2.annotate("June: up 51 percent\non last month,\nup 3 percent on last June",
                (5.2, 51), textcoords="offset points", xytext=(6, 8),
                fontsize=8.5, color=INK)
    a2.set_xticks(x); a2.set_xticklabels(MONTHS, fontsize=8.5)
    for lab in a2.get_xticklabels()[1::2]:
        lab.set_visible(False)
    a2.legend(fontsize=8.5, frameon=False, loc="lower left")
    a2.set_ylim(-60, 95); a2.set_ylabel("percent change")
    style(a2)
    title(a2, "Two ways to report the same twelve months",
          "One measures the calendar. The other measures the agency.")

    fig.tight_layout()
    fig.savefig(HERE / "fig_18_year_over_year.png", dpi=150)
    plt.close(fig)


# ---------------------------------------------- 19. data quality
def fig_19():
    fig, (a1, a2) = plt.subplots(1, 2, figsize=(12.8, 4.5))

    c = pd.read_csv(DATA / "cfs_monthly_by_type.csv")
    h = c[c["agency_id"] == "A003"].pivot_table(index="year_month", columns="incident_type",
                                                values="n_calls", aggfunc="sum")
    h = h.loc["2021-07":"2024-06"]
    base = h.loc["2022-01":"2022-12"]
    x = pd.PeriodIndex(h.index, freq="M").to_timestamp()
    a1.plot(x, h["Public Order Offense"] / base["Public Order Offense"].mean(),
            color=ORANGE, lw=2.2, zorder=4, label="public order calls")
    a1.plot(x, h.sum(axis=1) / base.sum(axis=1).mean(),
            color=BLUE, lw=2.2, zorder=3, label="all calls for service")
    a1.axvline(pd.Timestamp("2023-01-01"), color=INK, lw=1.1, ls=(0, (4, 3)), zorder=5)
    a1.text(pd.Timestamp("2023-01-20"), 0.42, "the agency changed\nhow it labels calls",
            fontsize=8.5, color=INK2)
    a1.axhline(1.0, color=INK3, lw=1.0, zorder=2)
    a1.legend(fontsize=8.5, frameon=False, loc="upper left")
    a1.set_ylim(0.3, 2.0); a1.set_ylabel("times the 2022 average")
    a1.set_xticks([pd.Timestamp(f"{y}-01-01") for y in (2022, 2023, 2024)])
    a1.set_xticklabels(["2022", "2023", "2024"], fontsize=9)
    style(a1)
    title(a1, "Havenbrook: a category jumps, the total does not",
          "Public order calls rise 54 percent. Total calls rise 3 percent.")

    tot = m.groupby("year_month")[["total_cfs"]].sum().loc["2024-11":"2026-06"]
    xs = pd.PeriodIndex(tot.index, freq="M").to_timestamp()
    cols = [ORANGE if i in ("2026-05", "2026-06") else BLUE for i in tot.index]
    a2.bar(xs, tot["total_cfs"], width=22, color=cols, zorder=3)
    a2.text(pd.Timestamp("2026-06-20"), 84000, "still being\nentered",
            fontsize=9, color=ORANGE, ha="right")
    a2.set_ylim(0, 132000); a2.set_ylabel("calls for service, every agency")
    a2.set_xticks([pd.Timestamp(f"{y}-01-01") for y in (2025, 2026)])
    a2.set_xticklabels(["2025", "2026"], fontsize=9)
    a2.set_yticks([0, 25000, 50000, 75000, 100000, 125000])
    a2.set_yticklabels(["0", "25,000", "50,000", "75,000", "100,000", "125,000"], fontsize=8.5)
    style(a2)
    title(a2, "The most recent months are never finished",
          "Nothing happened in May 2026. The records have not arrived yet.")

    fig.tight_layout()
    fig.savefig(HERE / "fig_19_data_quality.png", dpi=150)
    plt.close(fig)


# ------------------------------------------------------ 20. checklist
def fig_20():
    fig, ax = plt.subplots(figsize=(13, 5.0))
    d = m[m["agency_id"] == "A002"].sort_values("year_month")
    x = pd.PeriodIndex(d["year_month"], freq="M").to_timestamp()
    final = d[d["provisional"] == 0]
    prov = d[d["provisional"] == 1]
    ax.plot(x, d["n_uof"], color=BLUE, lw=1.6, zorder=3)
    ax.plot(pd.PeriodIndex(prov["year_month"], freq="M").to_timestamp(),
            prov["n_uof"], color=ORANGE, lw=2.6, zorder=4)
    yr = final[final["year"] <= "2025"].groupby("year")["n_uof"].mean()
    ax.plot([pd.Timestamp(f"{y}-07-01") for y in yr.index], yr.values,
            color=INK3, lw=2.2, ls=(0, (5, 3)), zorder=5)

    notes = [
        ("2021-06-01", 176, "3  one documented outlier,\n    a week of civil unrest", (14, -4)),
        ("2020-07-01", 62, "2  ordinary variation,\n    roughly 15 to 45 a month", (10, 30)),
        ("2024-01-01", 40, "4  the level drifts down\n    year after year", (16, 26)),
        ("2026-05-01", 11, "5  the last two months\n    are incomplete", (-118, 34)),
    ]
    for dt, yv, txt, off in notes:
        ax.annotate(txt, xy=(pd.Timestamp(dt), yv), textcoords="offset points",
                    xytext=off, fontsize=9, color=INK,
                    arrowprops=dict(arrowstyle="->", lw=0.9, color=INK2))
    ax.text(0.012, 0.95, "1  the axis starts at zero", transform=ax.transAxes,
            fontsize=9, color=INK)
    ax.set_ylim(0, 195)
    ax.set_ylabel("use of force incidents")
    style(ax)
    title(ax, "Tarnbridge Police Department, every month from 2019 to 2026",
          "Five of the twelve checklist questions can be answered from this one chart.")
    fig.tight_layout()
    fig.savefig(HERE / "fig_20_reading_a_chart.png", dpi=150)
    plt.close(fig)


if __name__ == "__main__":
    for fn in (fig_01, fig_02, fig_03, fig_04, fig_05,
               fig_06, fig_07, fig_08, fig_09, fig_10,
               fig_11, fig_12, fig_13, fig_14, fig_15,
               fig_16, fig_17, fig_18, fig_19, fig_20):
        fn()
        print("built", fn.__name__)
