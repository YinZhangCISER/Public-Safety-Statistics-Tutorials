"""
Build every figure in the Time Series Beginner series.

All figures are drawn from the synthetic WADEPS dataset in Data/. Running this
script overwrites the PNG files that the Markdown modules link to.

    python make_figures.py

Colors follow the CISER data visualization palette: categorical slot 1 blue
#2a78d6, slot 2 orange #eb6834, slot 3 aqua #1baf7a, on surface #fcfcfb. Series
are always direct labeled or listed in a legend, never identified by color
alone, and every number shown here also appears in a table in the module text.

Prepared by Yin Zhang, Center for Interdisciplinary Statistical Education
and Research (CISER), Washington State University.
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
    title(ax, "Grandview Police Department, 2023",
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
    colors = [ORANGE if s == "Cedar Falls" else BLUE for s in bc["short"]]
    a1.barh(bc["short"], bc["uof"], color=colors, height=0.68, zorder=3)
    for y, v in enumerate(bc["uof"]):
        a1.text(v + 18, y, f"{v:,}", va="center", fontsize=9, color=INK2)
    a1.set_xlim(0, 1330)
    a1.set_xlabel("use of force incidents in 2023")
    style(a1, ygrid=False)
    a1.grid(axis="x", color=GRID, lw=0.8)
    a1.set_axisbelow(True)
    title(a1, "By count", "Grandview has by far the most. Cedar Falls is third.")

    rc = d.sort_values("rate")
    colors = [ORANGE if s == "Cedar Falls" else BLUE for s in rc["short"]]
    a2.barh(rc["short"], rc["rate"], color=colors, height=0.68, zorder=3)
    for y, v in enumerate(rc["rate"]):
        a2.text(v + 0.05, y, f"{v:.2f}", va="center", fontsize=9, color=INK2)
    a2.set_xlim(0, 3.9)
    a2.set_xlabel("use of force per 100 arrests in 2023")
    style(a2, ygrid=False)
    a2.grid(axis="x", color=GRID, lw=0.8)
    a2.set_axisbelow(True)
    title(a2, "By rate", "Cedar Falls is the highest in the state. Grandview is below average.")

    fig.tight_layout()
    fig.savefig(HERE / "fig_05_counts_and_rates.png", dpi=150)
    plt.close(fig)


if __name__ == "__main__":
    for fn in (fig_01, fig_02, fig_03, fig_04, fig_05):
        fn()
        print("built", fn.__name__)
