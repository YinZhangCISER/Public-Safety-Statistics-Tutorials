"""
Build every figure in the Causal Inference Intermediate series.

All figures are drawn from the synthetic WADEPS dataset in Data/. Running this
script overwrites the PNG files that the Markdown topics link to.

    python make_figures.py

Developed by Yin Zhang, PhD, Assistant Professor, Data Analytics Program,
Department of Mathematics and Statistics, Washington State University, for
the Washington Data Exchange for Public Safety (WADEPS) through the Center
for Interdisciplinary Statistical Education and Research (CISER).
"""

import warnings
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

warnings.filterwarnings("ignore")

HERE = Path(__file__).resolve().parent
DATA = HERE.parents[2] / "Data"

BLUE, ORANGE, AQUA = "#2a78d6", "#eb6834", "#1baf7a"
YELLOW = "#eda100"
SURFACE = "#fcfcfb"
INK, INK2, INK3 = "#0b0b0b", "#52514e", "#8a8880"
GRID = "#e8e7e3"

plt.rcParams.update({
    "figure.facecolor": SURFACE, "axes.facecolor": SURFACE,
    "savefig.facecolor": SURFACE, "font.size": 10, "text.color": INK,
    "axes.labelcolor": INK2, "xtick.color": INK2, "ytick.color": INK2,
    "axes.edgecolor": GRID, "axes.linewidth": 0.8,
    "xtick.major.size": 0, "ytick.major.size": 0, "font.family": "DejaVu Sans",
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
        ax.text(0, 1.012, sub, transform=ax.transAxes, fontsize=9, color=INK2,
                va="bottom")


# ---------------------------------------------------------------- the data

TREATED = ["A001", "A002", "A004", "A007", "A010"]

monthly = pd.read_csv(DATA / "agency_monthly.csv")
profile = pd.read_csv(DATA / "agency_profile.csv")
NAME = dict(zip(profile["agency_id"], profile["agency_name"]))
SHORT = {k: v.replace(" Police Department", "").replace(" Sheriff's Office", " Cty")
            .replace("Pinecrest State University Police", "Pinecrest")
            .replace(" Tribal Police", "")
         for k, v in NAME.items()}

F = monthly[monthly["provisional"] == 0].copy()
F = F[~((F["agency_id"] == "A002") & (F["year_month"] == "2021-06"))]
F["trained"] = F["agency_id"].isin(TREATED).astype(int)
F["period"] = np.where(F["year_month"] >= "2023-11", "after",
                       np.where(F["year_month"] < "2023-07", "before", "phase"))
F["dt"] = pd.PeriodIndex(F["year_month"], freq="M").to_timestamp()

FULL = "2023-11-01"          # the month the training was fully in place


def rate(d):
    """Use of force per 100 arrests, pooled over whatever rows are passed in."""
    return 100 * d["n_uof"].sum() / d["n_arrests"].sum()


def group_series(ids, window=12):
    """A smoothed monthly rate for a set of agencies, so the picture is readable."""
    d = F[F["agency_id"].isin(ids)].groupby("dt")[["n_uof", "n_arrests"]].sum()
    s = 100 * d["n_uof"].rolling(window, center=True).sum() \
        / d["n_arrests"].rolling(window, center=True).sum()
    return s.dropna()


NO_A007 = [a for a in TREATED if a != "A007"]
COMPARISON = [a for a in F["agency_id"].unique() if a not in TREATED]


# ---------------------------------------------------------------- figures

def _cf_path():
    """Where the comparison agencies went, as a multiplier."""
    c = F[F["agency_id"].isin(COMPARISON)]
    return rate(c[c["period"] == "after"]) / rate(c[c["period"] == "before"])


def fig_01():
    """Module 1. The claim ladder, with what each rung costs to climb."""
    tr5 = F[F["trained"] == 1]
    b5, a5 = rate(tr5[tr5["period"] == "before"]), rate(tr5[tr5["period"] == "after"])
    t4 = F[F["agency_id"].isin(NO_A007)]
    b4, a4 = rate(t4[t4["period"] == "before"]), rate(t4[t4["period"] == "after"])
    mult = _cf_path()

    rows = [("the rate fell", 100 * (a5 / b5 - 1), "records only", INK3),
            ("it fell more than\nat other agencies", 100 * ((a5 / b5) / mult - 1),
             "records from seven more agencies", ORANGE),
            ("it fell more than at agencies\nthat were moving the same way",
             100 * ((a4 / b4) / mult - 1),
             "the same, plus a pre period check", AQUA)]

    fig, ax = plt.subplots(figsize=(12.6, 4.8))
    ys = np.arange(len(rows))[::-1]
    for (lab, v, cost, c), yy in zip(rows, ys):
        ax.barh(yy, v, color=c, height=0.36, zorder=3)
        ax.text(v - 0.9, yy, f"{v:+.1f}%", ha="right", va="center", fontsize=11.5,
                color=INK, weight="bold")
        ax.text(1.6, yy, cost, fontsize=9, color=INK2, va="center")
    ax.axvline(-12.0, color=INK, lw=2, ls="--", zorder=5)
    ax.text(-12.5, -0.78, "the truth ", fontsize=9.5, color=INK, ha="right")
    ax.set_yticks(ys)
    ax.set_yticklabels([r[0] for r in rows], fontsize=9.5)
    ax.set_xlim(-38, 24)
    ax.set_ylim(-1.0, 2.6)
    ax.set_xlabel("what the sentence is worth, as a number")
    ax.text(1.6, 2.42, "what it takes to say it", fontsize=9.5, color=INK, weight="bold")
    style(ax, ygrid=False)
    ax.grid(axis="x", color=GRID, lw=0.8, zorder=0)
    ax.set_axisbelow(True)
    title(ax, "Three sentences about the same program",
          "Each rung costs one more piece of evidence and moves the number closer.")
    fig.tight_layout()
    fig.savefig(HERE / "fig_01_claim_ladder.png", dpi=150)
    plt.close(fig)


def fig_02():
    """Module 2. Y(1) observed, Y(0) constructed, for each treated agency."""
    mult = _cf_path()
    ids = ["A001", "A002", "A004", "A010"]
    fig, ax = plt.subplots(figsize=(11.8, 5.2))
    xs = np.arange(len(ids))
    y1, y0 = [], []
    for aid in ids:
        g = F[F["agency_id"] == aid]
        b = rate(g[g["period"] == "before"])
        y1.append(rate(g[g["period"] == "after"]))
        y0.append(b * mult)
    w = 0.32
    ax.bar(xs - w / 2, y0, width=w, color=INK3, zorder=3,
           label="Y(0), what the comparison path implies")
    ax.bar(xs + w / 2, y1, width=w, color=BLUE, zorder=3,
           label="Y(1), what was recorded")
    for x, a, b in zip(xs, y0, y1):
        ax.annotate("", xy=(x + w / 2, b + 0.04), xytext=(x - w / 2, a + 0.04),
                    arrowprops=dict(arrowstyle="->", color=ORANGE, lw=1.8))
        ax.text(x, max(a, b) + 0.30, f"{100 * (b / a - 1):+.1f}%", ha="center",
                fontsize=10.5, color=ORANGE, weight="bold")
    ax.set_xticks(xs)
    ax.set_xticklabels([SHORT[a] for a in ids], fontsize=10)
    ax.set_ylim(0, 3.9)
    ax.set_ylabel("use of force per 100 arrests, after the program")
    ax.legend(fontsize=9, frameon=False, loc="lower right")
    style(ax)
    title(ax, "Two potential outcomes per agency, one of them observed",
          "The true effect is 12 percent at all four. The spread between them is noise.")
    fig.tight_layout()
    fig.savefig(HERE / "fig_02_potential_outcomes.png", dpi=150)
    plt.close(fig)


def fig_03():
    """Module 3. One agency, three counterfactuals, three answers."""
    import statsmodels.api as sm
    import statsmodels.formula.api as smf

    g = F[F["agency_id"] == "A001"].copy()
    b, a = rate(g[g["period"] == "before"]), rate(g[g["period"] == "after"])
    mult = _cf_path()

    pre = g[g["period"] == "before"].copy()
    pi = pd.PeriodIndex(pre["year_month"], freq="M")
    pre["yr"] = pi.year.values + (pi.month.values - 1) / 12.0
    z = smf.glm("n_uof ~ yr", pre, family=sm.families.Poisson(),
                offset=np.log(pre["n_arrests"])).fit()
    post = g[g["period"] == "after"].copy()
    pj = pd.PeriodIndex(post["year_month"], freq="M")
    post["yr"] = pj.year.values + (pj.month.values - 1) / 12.0
    trend = 100 * np.exp(z.params["Intercept"] + z.params["yr"] * post["yr"]).mean()

    rows = [("its own past,\nassumed unchanged", b, ORANGE),
            ("its own pre program\ntrend, extrapolated", trend, BLUE),
            ("the comparison\nagencies' path", b * mult, AQUA)]

    fig, ax = plt.subplots(figsize=(11.8, 5.2))
    ys = np.arange(len(rows))[::-1]
    for (lab, y0, c), yy in zip(rows, ys):
        ax.plot([a, y0], [yy, yy], color=c, lw=3.2, solid_capstyle="round", zorder=3)
        ax.scatter([y0], [yy], s=110, color=c, zorder=5)
        ax.text(y0 + 0.035, yy, f"Y(0) = {y0:.2f}", fontsize=10, va="center", color=c)
        ax.text((a + y0) / 2, yy + 0.19, f"{100 * (a / y0 - 1):+.1f}%", ha="center",
                fontsize=10.5, color=INK, weight="bold")
    ax.axvline(a, color=INK, lw=2.4, zorder=6)
    ax.text(a - 0.03, 2.55, f"what was recorded, {a:.2f}  ", fontsize=10, color=INK,
            ha="right")
    ax.set_yticks(ys)
    ax.set_yticklabels([r[0] for r in rows], fontsize=9.5)
    ax.set_xlim(2.35, 3.85)
    ax.set_ylim(-0.6, 2.9)
    ax.set_xlabel("use of force per 100 arrests, after the program")
    style(ax, ygrid=False)
    ax.grid(axis="x", color=GRID, lw=0.8, zorder=0)
    ax.set_axisbelow(True)
    title(ax, "Stonewick alone: same records, three counterfactuals",
          "The true effect is 12 percent. One agency cannot get there from any of these.")
    fig.tight_layout()
    fig.savefig(HERE / "fig_03_three_counterfactuals.png", dpi=150)
    plt.close(fig)


def fig_04():
    """Module 4. Four eligibility rules, and what each one gives."""
    prof = profile.set_index("agency_id")
    pool = [a for a in COMPARISON]
    rules = [("everyone not trained", pool),
             ("municipal police only",
              [a for a in pool if prof.loc[a, "agency_type"] == "Municipal Police"]),
             ("at least 30 sworn officers",
              [a for a in pool if prof.loc[a, "sworn_officers"] >= 30]),
             ("complete call data",
              [a for a in pool if prof.loc[a, "cfs_data_submitted"] == "Yes"])]

    t4 = F[F["agency_id"].isin(NO_A007)]
    tb, ta = rate(t4[t4["period"] == "before"]), rate(t4[t4["period"] == "after"])

    fig, (a1, a2) = plt.subplots(1, 2, figsize=(13.6, 5.0),
                                 gridspec_kw={"width_ratios": [1.15, 1]})

    order = sorted(pool, key=lambda a: -prof.loc[a, "sworn_officers"])
    for j, (lab, keep) in enumerate(rules):
        for i, aid in enumerate(order):
            inc = aid in keep
            a1.scatter([i], [len(rules) - 1 - j], s=170,
                       color=AQUA if inc else "#f0efec",
                       edgecolors=INK3 if not inc else AQUA, lw=1.0, zorder=4)
    a1.set_xticks(range(len(order)))
    a1.set_xticklabels([SHORT[a] for a in order], fontsize=8.5, rotation=32, ha="right")
    a1.set_yticks(range(len(rules)))
    a1.set_yticklabels([r[0] for r in rules][::-1], fontsize=9.5)
    a1.set_xlim(-0.6, len(order) - 0.4)
    a1.set_ylim(-0.6, len(rules) - 0.4)
    style(a1, ygrid=False)
    title(a1, "Four rules, applied to the seven untrained agencies",
          "Filled means the rule admits it.")

    ests = []
    for lab, keep in rules:
        c = F[F["agency_id"].isin(keep)]
        cb, ca = rate(c[c["period"] == "before"]), rate(c[c["period"] == "after"])
        ests.append(100 * ((ta / tb) / (ca / cb) - 1))
    ys = np.arange(len(rules))[::-1]
    a2.barh(ys, ests, color=AQUA, height=0.4, zorder=3)
    for yy, v, (lab, keep) in zip(ys, ests, rules):
        a2.text(v - 0.25, yy, f"{v:+.1f}%", ha="right", va="center", fontsize=11,
                color=INK, weight="bold")
        a2.text(-0.3, yy, f"n = {len(keep)}", ha="left", va="center", fontsize=9,
                color=INK2)
    a2.axvline(-12.0, color=INK, lw=2, ls="--", zorder=5)
    a2.text(-12.3, -0.78, "the truth ", fontsize=9.5, color=INK, ha="right")
    a2.set_yticks(ys)
    a2.set_yticklabels([])
    a2.set_xlim(-16, 3)
    a2.set_ylim(-1.0, 3.55)
    a2.set_xlabel("difference in differences estimate")
    style(a2, ygrid=False)
    a2.grid(axis="x", color=GRID, lw=0.8, zorder=0)
    a2.set_axisbelow(True)
    title(a2, "And what each one gives",
          "A spread of 0.8 points. Report this, rather than assuming it.")

    fig.tight_layout()
    fig.savefig(HERE / "fig_04_building_a_comparison_group.png", dpi=150)
    plt.close(fig)


if __name__ == "__main__":
    for fn in (fig_01, fig_02, fig_03, fig_04):
        fn()
        print("built", fn.__name__)
