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



def _panel(agencies=None):
    d = F if agencies is None else F[F["agency_id"].isin(agencies)]
    d = d.copy()
    d["lo"] = np.log(d["n_arrests"])
    pi = pd.PeriodIndex(d["year_month"], freq="M")
    d["yr"] = pi.year.values + (pi.month.values - 1) / 12.0
    return d


def fig_05():
    """Module 5. The same 2x2 on two scales."""
    tb, ta = rate(F[F["agency_id"].isin(NO_A007) & (F["period"] == "before")]), \
             rate(F[F["agency_id"].isin(NO_A007) & (F["period"] == "after")])
    cb, ca = rate(F[F["agency_id"].isin(COMPARISON) & (F["period"] == "before")]), \
             rate(F[F["agency_id"].isin(COMPARISON) & (F["period"] == "after")])
    add_pts = (ta - tb) - (ca - cb)
    add_pct = 100 * add_pts / tb
    mult_pct = 100 * ((ta / tb) / (ca / cb) - 1)

    fig, (a1, a2) = plt.subplots(1, 2, figsize=(13.4, 5.0),
                                 gridspec_kw={"width_ratios": [1.2, 1]})

    x = [0, 1]
    a1.plot(x, [tb, ta], color=BLUE, lw=3, marker="o", ms=11, zorder=5,
            label="took the training")
    a1.plot(x, [cb, ca], color=INK3, lw=3, marker="o", ms=11, zorder=5, label="did not")
    a1.plot(x, [tb, tb + (ca - cb)], color=ORANGE, lw=2.6, ls="--", marker="o", ms=9,
            zorder=4, label="Y(0), same change in rate points")
    a1.plot(x, [tb, tb * (ca / cb)], color=AQUA, lw=2.6, ls="--", marker="o", ms=9,
            zorder=4, label="Y(0), same proportional change")
    for v, c in [(tb, BLUE), (cb, INK3)]:
        a1.text(-0.04, v, f"{v:.2f}", ha="right", va="center", fontsize=10, color=c)
    a1.text(1.04, ta, f"{ta:.2f}", va="center", fontsize=10, color=BLUE)
    a1.text(1.04, tb + (ca - cb), f"{tb + (ca - cb):.2f}", va="center", fontsize=10,
            color=ORANGE)
    a1.text(1.04, tb * (ca / cb) - 0.055, f"{tb * (ca / cb):.2f}", va="center",
            fontsize=10, color=AQUA)
    a1.set_xticks(x)
    a1.set_xticklabels(["before the training", "after it was in place"], fontsize=10)
    a1.set_xlim(-0.22, 1.30)
    a1.set_ylim(1.9, 3.95)
    a1.set_ylabel("use of force per 100 arrests")
    a1.legend(fontsize=8.5, frameon=False, loc="lower left")
    style(a1)
    title(a1, "Two counterfactuals from the same comparison group",
          "The comparison group fell 0.52 rate points, and 19.5 percent. Not the same thing.")

    labs = ["same change in\nrate points", "same proportional\nchange"]
    vals = [add_pct, mult_pct]
    cols = [ORANGE, AQUA]
    a2.bar([0, 1], vals, color=cols, width=0.46, zorder=3)
    for xx, v in zip([0, 1], vals):
        a2.text(xx, v - 1.1, f"{v:+.1f}%", ha="center", fontsize=12.5, color=INK,
                weight="bold")
    a2.axhline(-12.0, color=INK, lw=2, ls="--", zorder=5)
    a2.text(1.42, -11.4, "the truth", fontsize=9.5, color=INK, ha="right")
    a2.set_xticks([0, 1])
    a2.set_xticklabels(labs, fontsize=10)
    a2.set_xlim(-0.55, 1.55)
    a2.set_ylim(-18, 1)
    a2.set_ylabel("estimated change in the use of force rate")
    style(a2)
    title(a2, "The scale is a modelling choice",
          "The planted effect acts on the rate, so the proportional version recovers it.")

    fig.tight_layout()
    fig.savefig(HERE / "fig_05_two_by_two.png", dpi=150)
    plt.close(fig)


def fig_06():
    """Module 6. Three specifications, one answer."""
    import statsmodels.api as sm
    import statsmodels.formula.api as smf

    d = _panel(NO_A007 + COMPARISON)
    d["tr"] = d["agency_id"].isin(NO_A007).astype(float)
    d["settled"] = ((d["tr"] == 1) & (d["period"] == "after")).astype(float)
    d["phase"] = ((d["tr"] == 1) & (d["period"] == "phase")).astype(float)
    d["post"] = (d["period"] == "after").astype(float)

    specs = [("group and period\nindicators only", "n_uof ~ tr + post + settled + phase"),
             ("agency fixed\neffects", "n_uof ~ C(agency_id) + post + settled + phase"),
             ("agency and month\nfixed effects",
              "n_uof ~ C(agency_id) + C(year_month) + settled + phase")]
    est, los, his, aics = [], [], [], []
    for _, form in specs:
        z = smf.glm(form, d, family=sm.families.Poisson(), offset=d["lo"]).fit()
        lo, hi = z.conf_int().loc["settled"]
        est.append(100 * (np.exp(z.params["settled"]) - 1))
        los.append(100 * (np.exp(lo) - 1))
        his.append(100 * (np.exp(hi) - 1))
        aics.append(z.aic)

    fig, (a1, a2) = plt.subplots(1, 2, figsize=(13.2, 5.0))
    xs = np.arange(len(specs))
    a1.errorbar(xs, est, yerr=[np.array(est) - np.array(los), np.array(his) - np.array(est)],
                fmt="none", ecolor=AQUA, elinewidth=2.8, capsize=0, zorder=3)
    a1.scatter(xs, est, s=105, color=AQUA, zorder=5)
    for x, e in zip(xs, est):
        a1.text(x + 0.12, e, f"{e:+.1f}%", fontsize=10.5, va="center", color=INK)
    a1.axhline(-12.0, color=INK, lw=2, ls="--", zorder=4)
    a1.text(2.42, -11.3, "the truth", fontsize=9.5, color=INK, ha="right")
    a1.set_xticks(xs)
    a1.set_xticklabels([s[0] for s in specs], fontsize=9)
    a1.set_xlim(-0.4, 2.55)
    a1.set_ylim(-20, -4)
    a1.set_ylabel("estimated change in the use of force rate")
    style(a1)
    title(a1, "Three specifications, one answer",
          "The point estimate moves by 0.1 points and the interval barely at all.")

    a2.bar(xs, aics, color=[INK3, INK3, AQUA], width=0.5, zorder=3)
    for x, v in zip(xs, aics):
        a2.text(x, v + 22, f"{v:,.0f}", ha="center", fontsize=11, color=INK, weight="bold")
    a2.set_xticks(xs)
    a2.set_xticklabels([s[0] for s in specs], fontsize=9)
    a2.set_ylim(4400, 5400)
    a2.set_ylabel("AIC, lower is better")
    style(a2)
    title(a2, "But they are not equally good models",
          "Month effects fit far better without moving the estimate. Both facts matter.")

    fig.tight_layout()
    fig.savefig(HERE / "fig_06_did_as_regression.png", dpi=150)
    plt.close(fig)


def fig_07():
    """Module 7. Every agency's pre program trend, with intervals."""
    import statsmodels.api as sm
    import statsmodels.formula.api as smf

    pre = _panel()
    pre = pre[pre["period"] == "before"]
    rows = []
    for a in sorted(F["agency_id"].unique()):
        s = pre[pre["agency_id"] == a]
        z = smf.glm("n_uof ~ yr", s, family=sm.families.Poisson(),
                    offset=s["lo"]).fit()
        lo, hi = z.conf_int().loc["yr"]
        rows.append((SHORT[a], 100 * (np.exp(z.params["yr"]) - 1),
                     100 * (np.exp(lo) - 1), 100 * (np.exp(hi) - 1), a in TREATED))
    rows.sort(key=lambda r: r[1])

    fig, ax = plt.subplots(figsize=(12.0, 5.6))
    ys = np.arange(len(rows))[::-1]
    for (nm, e, lo, hi, tr), yy in zip(rows, ys):
        c = BLUE if tr else INK3
        if nm.startswith("Summit"):
            c = ORANGE
        ax.plot([lo, hi], [yy, yy], color=c, lw=2.6, solid_capstyle="round", zorder=3)
        ax.scatter([e], [yy], s=75, color=c, zorder=5)
    ax.axvline(-4.46, color=AQUA, lw=2.2, zorder=2)
    ax.text(-4.2, len(rows) - 0.4, " the comparison group's own trend, 4.5% a year",
            fontsize=9, color=AQUA)
    ax.axvline(0, color=INK3, lw=1, ls=":", zorder=2)
    ax.set_yticks(ys)
    ax.set_yticklabels([r[0] for r in rows], fontsize=9.5)
    ax.set_xlim(-22, 34)
    ax.set_ylim(-0.7, len(rows) - 0.1)
    ax.set_xlabel("change in the use of force rate per year, before the program existed")
    ax.text(-21.4, len(rows) - 1.05, "took the training", fontsize=9, color=BLUE)
    ax.text(-21.4, len(rows) - 1.55, "also trained", fontsize=9, color=ORANGE)
    ax.text(-21.4, len(rows) - 2.05, "did not", fontsize=9, color=INK3)
    style(ax, ygrid=False)
    ax.grid(axis="x", color=GRID, lw=0.8, zorder=0)
    ax.set_axisbelow(True)
    title(ax, "Every agency's trend before the program, one at a time",
          "Only three intervals exclude zero. The per agency test is weak, and it still catches Summit County.")
    fig.tight_layout()
    fig.savefig(HERE / "fig_07_parallel_trends.png", dpi=150)
    plt.close(fig)


def fig_08():
    """Module 8. Four responses to a failed parallel trends test."""
    import statsmodels.api as sm
    import statsmodels.formula.api as smf

    d = _panel()
    d["tr"] = d["agency_id"].isin(TREATED).astype(float)
    d["settled"] = ((d["tr"] == 1) & (d["period"] == "after")).astype(float)
    d["phase"] = ((d["tr"] == 1) & (d["period"] == "phase")).astype(float)
    base = "n_uof ~ C(agency_id)+C(year_month)+settled+phase"
    trends = "n_uof ~ C(agency_id)+C(year_month)+C(agency_id):yr+settled+phase"
    opts = [("do nothing, keep Summit County", base, d, ORANGE),
            ("drop Summit County", base, d[d["agency_id"] != "A007"], AQUA),
            ("agency specific linear trends", trends, d, ORANGE),
            ("both", trends, d[d["agency_id"] != "A007"], ORANGE)]

    fig, ax = plt.subplots(figsize=(12.4, 5.0))
    ys = np.arange(len(opts))[::-1]
    for (lab, form, data, c), yy in zip(opts, ys):
        z = smf.glm(form, data, family=sm.families.Poisson(), offset=data["lo"]).fit()
        lo, hi = z.conf_int().loc["settled"]
        e = 100 * (np.exp(z.params["settled"]) - 1)
        lo, hi = 100 * (np.exp(lo) - 1), 100 * (np.exp(hi) - 1)
        ax.plot([lo, hi], [yy, yy], color=c, lw=3.2, solid_capstyle="round", zorder=3)
        ax.scatter([e], [yy], s=105, color=c, zorder=5)
        ax.text(e - 1.6, yy + 0.26, f"{e:+.1f}%", ha="center", fontsize=10.5, color=INK,
                weight="bold")
        if lo < 0 < hi:
            ax.text(hi + 0.9, yy, "interval includes zero", fontsize=8.5, color=ORANGE,
                    va="center")
    ax.axvline(-12.0, color=INK, lw=2, ls="--", zorder=6)
    ax.text(-12.4, -0.72, "the truth ", fontsize=9.5, color=INK, ha="right")
    ax.axvline(0, color=INK3, lw=1.2, zorder=2)
    ax.set_yticks(ys)
    ax.set_yticklabels([o[0] for o in opts], fontsize=9.5)
    ax.set_xlim(-25, 17)
    ax.set_ylim(-0.95, 3.55)
    ax.set_xlabel("estimated change in the use of force rate")
    style(ax, ygrid=False)
    ax.grid(axis="x", color=GRID, lw=0.8, zorder=0)
    ax.set_axisbelow(True)
    title(ax, "Four responses to one failed assumption",
          "The simple fix works. The sophisticated one doubles the interval and loses the effect.")
    fig.tight_layout()
    fig.savefig(HERE / "fig_08_when_parallel_trends_fails.png", dpi=150)
    plt.close(fig)



def _win(ids, lo_ym, hi_ym):
    d = F[F["agency_id"].isin(ids) & (F["year_month"] >= lo_ym) & (F["year_month"] < hi_ym)]
    return 100 * d["n_uof"].sum() / d["n_arrests"].sum()


def fig_09():
    """Module 9. Regression to the mean, and how much of it is real."""
    import statsmodels.api as sm

    early = {a: _win([a], "2019-01", "2020-07") for a in COMPARISON}
    late = {a: _win([a], "2022-07", "2023-07") for a in COMPARISON}
    h1 = {a: _win([a], "2019-01", "2021-04") for a in COMPARISON}
    h2 = {a: _win([a], "2021-04", "2023-07") for a in COMPARISON}

    fig, (a1, a2) = plt.subplots(1, 2, figsize=(13.4, 5.0))

    x = np.array([early[a] for a in COMPARISON])
    y = np.array([100 * (late[a] / early[a] - 1) for a in COMPARISON])
    z = sm.OLS(y, sm.add_constant(x)).fit()
    a1.scatter(x, y, s=95, color=BLUE, zorder=5)
    for a, xi, yi in zip(COMPARISON, x, y):
        a1.annotate(SHORT[a], (xi, yi), fontsize=8.5, color=INK2,
                    xytext=(7, -3), textcoords="offset points")
    xs = np.linspace(x.min() - 0.15, x.max() + 0.15, 20)
    a1.plot(xs, z.params[0] + z.params[1] * xs, color=ORANGE, lw=2.2, zorder=4)
    a1.axhline(0, color=INK3, lw=1.2, zorder=3)
    a1.text(2.05, 22,
            f"slope {z.params[1]:.1f} points per unit\np = {z.pvalues[1]:.2f}, "
            f"R squared {z.rsquared:.2f}", fontsize=9.5, color=ORANGE)
    a1.set_xlabel("use of force rate, 2019 to mid 2020")
    a1.set_ylabel("percent change by 2022 to mid 2023")
    a1.set_xlim(1.95, 3.85)
    a1.set_ylim(-22, 30)
    style(a1)
    title(a1, "Agencies that started higher fell further",
          "Seven agencies, none of which received any program.")

    u = np.array([h1[a] for a in COMPARISON])
    v = np.array([h2[a] for a in COMPARISON])
    a2.scatter(u, v, s=95, color=AQUA, zorder=5)
    for a, ui, vi in zip(COMPARISON, u, v):
        a2.annotate(SHORT[a], (ui, vi), fontsize=8.5, color=INK2,
                    xytext=(7, -3), textcoords="offset points")
    lim = [1.9, 3.6]
    a2.plot(lim, lim, color=INK3, lw=1.4, ls="--", zorder=3)
    a2.text(2.0, 3.35, f"correlation {np.corrcoef(u, v)[0, 1]:.2f}",
            fontsize=11, color=AQUA, weight="bold")
    a2.set_xlim(*lim)
    a2.set_ylim(*lim)
    a2.set_xlabel("rate in the first half of the pre period")
    a2.set_ylabel("rate in the second half")
    style(a2)
    title(a2, "And yet the level differences are almost entirely real",
          "An agency high in one half is high in the other. Little of the ranking is luck.")

    fig.tight_layout()
    fig.savefig(HERE / "fig_09_regression_to_mean.png", dpi=150)
    plt.close(fig)


def _did(t_ids, c_ids):
    tb = rate(F[F["agency_id"].isin(t_ids) & (F["period"] == "before")])
    ta = rate(F[F["agency_id"].isin(t_ids) & (F["period"] == "after")])
    cb = rate(F[F["agency_id"].isin(c_ids) & (F["period"] == "before")])
    ca = rate(F[F["agency_id"].isin(c_ids) & (F["period"] == "after")])
    return 100 * ((ta / tb) / (ca / cb) - 1)


def fig_10():
    """Module 10. Selection on the outcome, isolated."""
    base = profile.set_index("agency_id")["pre_program_uof_per_100_arrests"]
    ranked = sorted(COMPARISON, key=lambda a: -base[a])
    worst, best = ranked[:3], ranked[-3:]

    tb = rate(F[F["agency_id"].isin(NO_A007) & (F["period"] == "before")])
    ta = rate(F[F["agency_id"].isin(NO_A007) & (F["period"] == "after")])

    rows = [
        ("the real program,\nbefore and after only", 100 * (ta / tb - 1), -12.0, ORANGE),
        ("the real program,\ndifference in differences", _did(NO_A007, COMPARISON),
         -12.0, AQUA),
        ("no program at all,\ngiven to the worst three",
         _did(worst, [a for a in COMPARISON if a not in worst]), 0.0, ORANGE),
        ("no program at all,\ngiven to the best three",
         _did(best, [a for a in COMPARISON if a not in best]), 0.0, ORANGE),
    ]

    fig, ax = plt.subplots(figsize=(12.6, 5.2))
    ys = np.arange(len(rows))[::-1]
    for (lab, est, truth, c), yy in zip(rows, ys):
        ax.barh(yy, est, color=c, height=0.36, zorder=3)
        off = -0.6 if est < 0 else 0.6
        ha = "right" if est < 0 else "left"
        ax.text(est + off, yy, f"{est:+.1f}%", ha=ha, va="center", fontsize=11,
                color=INK, weight="bold")
        ax.scatter([truth], [yy], s=150, marker="|", color=INK, zorder=6, linewidths=2.4)
        ax.text(truth, yy + 0.30, f"truth {truth:+.0f}%", ha="center", fontsize=8.5,
                color=INK)
    ax.axvline(0, color=INK3, lw=1.2, zorder=2)
    ax.set_yticks(ys)
    ax.set_yticklabels([r[0] for r in rows], fontsize=9.5)
    ax.set_xlim(-34, 17)
    ax.set_ylim(-0.7, 3.65)
    ax.set_xlabel("what a difference in differences reports")
    style(ax, ygrid=False)
    ax.grid(axis="x", color=GRID, lw=0.8, zorder=0)
    ax.set_axisbelow(True)
    title(ax, "Selecting on the outcome manufactures an effect of its own",
          "The bottom two rows use agencies that received nothing. The truth for them is zero.")
    fig.tight_layout()
    fig.savefig(HERE / "fig_10_selection_on_outcome.png", dpi=150)
    plt.close(fig)


def _box(ax, xy, w, h, text, fc, ec, fs=9.5):
    from matplotlib.patches import FancyBboxPatch
    x, y = xy
    ax.add_patch(FancyBboxPatch((x - w / 2, y - h / 2), w, h,
                                boxstyle="round,pad=0.02,rounding_size=0.06",
                                fc=fc, ec=ec, lw=1.6, zorder=3))
    ax.text(x, y, text, ha="center", va="center", fontsize=fs, color=INK, zorder=5)


def _arrow(ax, a, b, color, curve=0.0, lw=2.0):
    ax.annotate("", xy=b, xytext=a, zorder=4,
                arrowprops=dict(arrowstyle="-|>", color=color, lw=lw,
                                shrinkA=17, shrinkB=17,
                                connectionstyle=f"arc3,rad={curve}"))


def fig_11():
    """Module 11. Three shapes, three different instructions."""
    fig, axes = plt.subplots(1, 3, figsize=(14.4, 4.4))
    specs = [
        ("Confounder", "control for it", AQUA,
         "the statewide decline", 4.9, [(4.9, 2.0, 0.18), (4.9, 8.0, -0.18)]),
        ("Mediator", "do NOT control for it", ORANGE,
         "how officers handle a call", 4.9, None),
        ("Collider", "do NOT control for it", ORANGE,
         "the agency gets reviewed", 1.2, None),
    ]
    for ax, (name, rule, col, mid, _, _) in zip(axes, specs):
        ax.set_xlim(0, 10); ax.set_ylim(0.6, 6.6); ax.axis("off")
        title(ax, name, rule)
        _box(ax, (2.2, 2.0), 3.2, 1.0, "took the\ntraining", "#eaf1fb", BLUE)
        _box(ax, (7.8, 2.0), 3.2, 1.0, "use of force\nfell", "#eaf1fb", BLUE)
        _arrow(ax, (2.2, 2.0), (7.8, 2.0), INK3, lw=1.6)
        if name == "Confounder":
            _box(ax, (5.0, 5.0), 4.4, 1.0, mid, "#e7f6f0", AQUA)
            _arrow(ax, (5.0, 5.0), (2.2, 2.0), AQUA, curve=0.18)
            _arrow(ax, (5.0, 5.0), (7.8, 2.0), AQUA, curve=-0.18)
            ax.text(5.0, 1.15, "both arrows point out of it", ha="center",
                    fontsize=8.5, color=AQUA)
        elif name == "Mediator":
            _box(ax, (5.0, 5.0), 4.4, 1.0, mid, "#fdeee7", ORANGE)
            _arrow(ax, (2.2, 2.0), (5.0, 5.0), ORANGE, curve=-0.18)
            _arrow(ax, (5.0, 5.0), (7.8, 2.0), ORANGE, curve=-0.18)
            ax.text(5.0, 1.15, "it sits on the path you are measuring",
                    ha="center", fontsize=8.5, color=ORANGE)
        else:
            _box(ax, (5.0, 5.0), 4.4, 1.0, mid, "#fdeee7", ORANGE)
            _arrow(ax, (2.2, 2.0), (5.0, 5.0), ORANGE, curve=-0.18)
            _arrow(ax, (7.8, 2.0), (5.0, 5.0), ORANGE, curve=0.18)
            ax.text(5.0, 1.15, "both arrows point into it", ha="center",
                    fontsize=8.5, color=ORANGE)
    fig.tight_layout()
    fig.savefig(HERE / "fig_11_confounders_mediators_colliders.png", dpi=150)
    plt.close(fig)


def fig_12():
    """Module 12. Placebo tests: fake dates and fake outcomes."""
    import statsmodels.api as sm
    import statsmodels.formula.api as smf

    d = F[F["agency_id"].isin(NO_A007 + COMPARISON)].copy()
    d["lo"] = np.log(d["n_arrests"])
    d["tr"] = d["agency_id"].isin(NO_A007).astype(float)
    d["settled"] = ((d["tr"] == 1) & (d["period"] == "after")).astype(float)
    d["phase"] = ((d["tr"] == 1) & (d["period"] == "phase")).astype(float)
    pre = d[d["period"] == "before"].copy()
    pf = lambda b: 100 * (np.exp(b) - 1)

    fig, (a1, a2) = plt.subplots(1, 2, figsize=(13.6, 5.0))

    cuts = ["2020-07", "2021-01", "2021-07", "2022-01", "2022-07"]
    est, los, his = [], [], []
    for cut in cuts:
        s = pre.copy()
        s["fake"] = ((s["tr"] == 1) & (s["year_month"] >= cut)).astype(float)
        z = smf.glm("n_uof ~ C(agency_id) + C(year_month) + fake", s,
                    family=sm.families.Poisson(), offset=s["lo"]).fit()
        lo, hi = z.conf_int().loc["fake"]
        est.append(pf(z.params["fake"])); los.append(pf(lo)); his.append(pf(hi))
    xs = np.arange(len(cuts))
    a1.errorbar(xs, est, yerr=[np.array(est) - np.array(los), np.array(his) - np.array(est)],
                fmt="none", ecolor=AQUA, elinewidth=2.8, capsize=0, zorder=3)
    a1.scatter(xs, est, s=95, color=AQUA, zorder=5)
    for x, e in zip(xs, est):
        a1.text(x + 0.13, e, f"{e:+.1f}%", fontsize=9.5, va="center", color=INK)
    a1.axhline(0, color=INK, lw=2, ls="--", zorder=4)
    a1.text(4.42, 0.9, "what a placebo should find", fontsize=9, color=INK, ha="right")
    a1.set_xticks(xs)
    a1.set_xticklabels([c for c in cuts], fontsize=9.5, rotation=20)
    a1.set_xlim(-0.4, 4.6)
    a1.set_ylim(-15, 9)
    a1.set_ylabel("estimated effect of a program that did not exist")
    a1.set_xlabel("fake intervention date, all inside the pre period")
    style(a1)
    title(a1, "Five dates, no program on any of them",
          "Every interval covers zero, and the drift is the residual pre trend gap.")

    outcomes = [("use of force\nthe real outcome", "n_uof", d["lo"], BLUE),
                ("arrests", "n_arrests", None, AQUA),
                ("calls for service", "total_cfs", None, ORANGE)]
    labs, e2, l2, h2 = [], [], [], []
    for lab, col, off, c in outcomes:
        z = smf.glm(f"{col} ~ C(agency_id) + C(year_month) + settled + phase", d,
                    family=sm.families.Poisson(),
                    offset=off if off is not None else None).fit()
        lo, hi = z.conf_int().loc["settled"]
        labs.append(lab); e2.append(pf(z.params["settled"]))
        l2.append(pf(lo)); h2.append(pf(hi))
    ys = np.arange(len(labs))[::-1]
    for yy, lab, e, lo, hi, (_, _, _, c) in zip(ys, labs, e2, l2, h2, outcomes):
        a2.plot([lo, hi], [yy, yy], color=c, lw=3.2, solid_capstyle="round", zorder=3)
        a2.scatter([e], [yy], s=100, color=c, zorder=5)
        a2.text(3.0, yy, f"{e:+.2f}%  [{lo:+.2f}, {hi:+.2f}]", ha="left", va="center",
                fontsize=9.5, color=INK, weight="bold")
    a2.axvline(0, color=INK, lw=2, ls="--", zorder=4)
    a2.set_yticks(ys)
    a2.set_yticklabels(labs, fontsize=9.5)
    a2.set_xlim(-21, 22)
    a2.set_ylim(-0.6, 2.6)
    a2.set_xlabel("estimated effect of the real program")
    style(a2, ygrid=False)
    a2.grid(axis="x", color=GRID, lw=0.8, zorder=0)
    a2.set_axisbelow(True)
    title(a2, "Three outcomes, only one the program should touch",
          "Arrests are untouched. Calls move 0.42 percent, which is detectable and meaningless.")

    fig.tight_layout()
    fig.savefig(HERE / "fig_12_placebo_tests.png", dpi=150)
    plt.close(fig)



def _frame(drop_a007=True):
    d = F[F["agency_id"] != "A007"] if drop_a007 else F
    d = d.copy()
    d["lo"] = np.log(d["n_arrests"])
    pi = pd.PeriodIndex(d["year_month"], freq="M")
    d["yr"] = pi.year.values + (pi.month.values - 1) / 12.0
    return d


def _fit(d, treated_ids, outcome="n_uof", offset=None):
    import statsmodels.api as sm
    import statsmodels.formula.api as smf
    d = d.copy()
    d["settled"] = ((d["agency_id"].isin(treated_ids))
                    & (d["period"] == "after")).astype(float)
    d["phase"] = ((d["agency_id"].isin(treated_ids))
                  & (d["period"] == "phase")).astype(float)
    off = d["lo"] if offset is None else offset
    z = smf.glm(f"{outcome} ~ C(agency_id)+C(year_month)+settled+phase", d,
                family=sm.families.Poisson(), offset=off).fit()
    lo, hi = z.conf_int().loc["settled"]
    f_ = lambda b: 100 * (np.exp(b) - 1)
    return f_(z.params["settled"]), f_(lo), f_(hi), z.bse["settled"]


def fig_13():
    """Module 13. Contamination, by agency size and by dose."""
    d = _frame()
    prof = profile.set_index("agency_id")
    clean = _fit(d, NO_A007)[0]

    order = sorted(COMPARISON, key=lambda a: -prof.loc[a, "sworn_officers"])
    lost = [abs(_fit(d, NO_A007 + [a])[0] - clean) for a in order]
    sizes = [prof.loc[a, "sworn_officers"] for a in order]

    fig, (a1, a2) = plt.subplots(1, 2, figsize=(13.4, 5.0))

    a1.scatter(sizes, lost, s=110, color=ORANGE, zorder=5)
    for s, l, a in zip(sizes, lost, order):
        a1.annotate(SHORT[a], (s, l), fontsize=8.5, color=INK2,
                    xytext=(8, -3), textcoords="offset points")
    a1.set_xscale("log")
    a1.set_xlabel("sworn officers at the contaminated agency (log scale)")
    a1.set_ylabel("percentage points of the effect lost")
    a1.set_xlim(6, 2400)
    a1.set_ylim(-0.3, 5.0)
    style(a1)
    title(a1, "One comparison agency secretly trained",
          "The damage tracks the agency's size, not its similarity.")

    rng = np.random.default_rng(5)
    fracs = [0.0, 0.25, 0.5, 1.0]
    ests = []
    for fr in fracs:
        dd = d.copy()
        mult = np.where((dd["agency_id"] == "A012") & (dd["period"] == "after"),
                        0.88 ** fr, 1.0)
        dd["y"] = rng.binomial(dd["n_uof"].values.astype(int), np.minimum(mult, 1.0))
        ests.append(_fit(dd, NO_A007, outcome="y")[0])
    a2.plot([100 * x for x in fracs], ests, color=ORANGE, lw=2.6, marker="o", ms=9,
            zorder=5)
    for x, e in zip([100 * x for x in fracs], ests):
        a2.text(x, e + 0.55, f"{e:+.1f}%", ha="center", fontsize=10, color=INK,
                weight="bold")
    a2.axhline(-12.0, color=INK, lw=2, ls="--", zorder=4)
    a2.text(100, -11.4, "the truth  ", fontsize=9.5, color=INK, ha="right")
    a2.axhline(0, color=INK3, lw=1.2, zorder=3)
    a2.set_xlabel("share of the program's effect that leaks to Ashfell")
    a2.set_ylabel("estimated change in the use of force rate")
    a2.set_xlim(-6, 108)
    a2.set_ylim(-16, 3)
    style(a2)
    title(a2, "And it does not need to be all or nothing",
          "A quarter of the effect leaking costs two points.")

    fig.tight_layout()
    fig.savefig(HERE / "fig_13_spillover.png", dpi=150)
    plt.close(fig)


def fig_14():
    """Module 14. What the design could have detected."""
    d = _frame()
    mde = lambda se: 100 * (1 - np.exp(-2.80 * se))

    fig, (a1, a2) = plt.subplots(1, 2, figsize=(13.4, 5.0))

    pts = [("8", "2024-06"), ("14", "2024-12"), ("20", "2025-06"),
           ("26", "2025-12"), ("30", "2026-04")]
    xs, ys = [], []
    for lab, end in pts:
        se = _fit(d[d["year_month"] <= end], NO_A007)[3]
        xs.append(int(lab)); ys.append(mde(se))
    a1.plot(xs, ys, color=BLUE, lw=2.6, marker="o", ms=9, zorder=5)
    for x, y in zip(xs, ys):
        dy = -0.62 if abs(y - 12.0) < 1.3 else 0.35
        a1.text(x, y + dy, f"{y:.1f}%", ha="center", fontsize=10, color=INK,
                weight="bold")
    a1.axhline(12.0, color=ORANGE, lw=2.2, ls="--", zorder=4)
    a1.text(30, 12.45, "the effect that was actually there  ", fontsize=9.5,
            color=ORANGE, ha="right")
    a1.set_xlabel("months of follow up")
    a1.set_ylabel("smallest effect detectable at 80 percent power")
    a1.set_xlim(5, 33)
    a1.set_ylim(7, 16)
    style(a1)
    title(a1, "How long the study had to run",
          "Below the dashed line the design can see a 12 percent effect.")

    ks, ms = [], []
    for k in [1, 2, 3, 4]:
        se = _fit(d, NO_A007[:k])[3]
        ks.append(k); ms.append(mde(se))
    a2.bar(ks, ms, color=AQUA, width=0.5, zorder=3)
    for k, v in zip(ks, ms):
        a2.text(k, v + 0.2, f"{v:.1f}%", ha="center", fontsize=11, color=INK,
                weight="bold")
    a2.axhline(12.0, color=ORANGE, lw=2.2, ls="--", zorder=4)
    a2.text(4.45, 12.4, "the real effect", fontsize=9.5, color=ORANGE, ha="right")
    a2.set_xticks(ks)
    a2.set_xlabel("number of agencies given the program")
    a2.set_ylabel("smallest effect detectable at 80 percent power")
    a2.set_xlim(0.4, 4.6)
    a2.set_ylim(0, 14)
    style(a2)
    title(a2, "And how many agencies it needed",
          "Quadrupling the treated group buys one point. The comparison group is the constraint.")

    fig.tight_layout()
    fig.savefig(HERE / "fig_14_detectable_effect.png", dpi=150)
    plt.close(fig)


def fig_15():
    """Module 15. How wrong the assumption would have to be."""
    import statsmodels.api as sm
    import statsmodels.formula.api as smf

    d = _frame()
    d["tr"] = d["agency_id"].isin(NO_A007).astype(float)
    d["yrc"] = d["yr"] - d["yr"].min()

    deltas = np.arange(0.0, -6.5, -0.5)
    est, los, his = [], [], []
    for delta in deltas:
        dd = d.copy()
        dd["adj"] = np.log(dd["n_arrests"]) + np.log(1 + delta / 100) * dd["tr"] * dd["yrc"]
        e, lo, hi, _ = _fit(dd, NO_A007, offset=dd["adj"])
        est.append(e); los.append(lo); his.append(hi)

    pre = d[d["period"] == "before"]
    z = smf.glm("n_uof ~ C(agency_id) + yr + tr:yr", pre,
                family=sm.families.Poisson(), offset=pre["lo"]).fit()
    k = [x for x in z.params.index if "yr" in x and "tr" in x][0]
    obs = 100 * (np.exp(z.params[k]) - 1)
    olo, ohi = [100 * (np.exp(v) - 1) for v in z.conf_int().loc[k]]

    fig, ax = plt.subplots(figsize=(12.2, 5.4))
    ax.axvspan(ohi, olo, color=AQUA, alpha=0.13, zorder=1)
    ax.fill_between(deltas, los, his, color=BLUE, alpha=0.16, zorder=2)
    ax.plot(deltas, est, color=BLUE, lw=2.8, zorder=5)
    ax.axhline(0, color=INK, lw=1.8, zorder=4)
    ax.axvline(obs, color=AQUA, lw=2.4, zorder=5)
    ax.text(obs - 0.12, -19.5, "what the pre period\nactually shows, 0.70%  ",
            fontsize=9.5, color=AQUA, ha="right")
    ax.text(-1.55, 13.2, "the shaded green band is the range\nthe pre period cannot rule out",
            fontsize=9, color=AQUA, ha="center")
    cross = np.interp(0, est, deltas)
    ax.scatter([cross], [0], s=130, color=ORANGE, zorder=7)
    ax.annotate(f"a hidden trend of {abs(cross):.1f}% a year\nwould wipe the estimate out",
                xy=(cross, 0), xytext=(cross - 0.15, -13),
                fontsize=9.5, color=ORANGE, ha="center",
                arrowprops=dict(arrowstyle="->", color=ORANGE, lw=1.8))
    ax.set_xlabel("size of an unmeasured trend difference favouring the treated agencies, percent a year")
    ax.set_ylabel("estimated change in the use of force rate")
    ax.set_xlim(0.6, -6.4)
    ax.set_ylim(-22, 16)
    style(ax)
    title(ax, "How wrong the parallel trends assumption would have to be",
          "The shaded band is what the pre period leaves open. It reaches most of the way.")
    fig.tight_layout()
    fig.savefig(HERE / "fig_15_sensitivity.png", dpi=150)
    plt.close(fig)


def fig_16():
    """Module 16. Everything this series produced, and what survived."""
    d = _frame()
    dall = _frame(drop_a007=False)
    tb = rate(F[F["agency_id"].isin(TREATED) & (F["period"] == "before")])
    ta = rate(F[F["agency_id"].isin(TREATED) & (F["period"] == "after")])

    rows = [
        ("before and after, five trained agencies", 100 * (ta / tb - 1), ORANGE,
         "no comparison group"),
        ("difference in differences, all five", _fit(dall, TREATED)[0], ORANGE,
         "one agency on its own pre trend"),
        ("agency effects but no time term", None, ORANGE, "nothing absorbs the decline"),
        ("difference in differences, checked", _fit(d, NO_A007)[0], AQUA,
         "reported as the result"),
    ]
    import statsmodels.api as sm
    import statsmodels.formula.api as smf
    dd = d.copy()
    dd["settled"] = ((dd["agency_id"].isin(NO_A007)) & (dd["period"] == "after")).astype(float)
    dd["phase"] = ((dd["agency_id"].isin(NO_A007)) & (dd["period"] == "phase")).astype(float)
    zb = smf.glm("n_uof ~ C(agency_id) + settled + phase", dd,
                 family=sm.families.Poisson(), offset=dd["lo"]).fit()
    rows[2] = (rows[2][0], 100 * (np.exp(zb.params["settled"]) - 1), ORANGE, rows[2][3])

    fig, ax = plt.subplots(figsize=(12.8, 5.0))
    ys = np.arange(len(rows))[::-1]
    for (lab, e, c, note), yy in zip(rows, ys):
        ax.barh(yy, e, color=c, height=0.36, zorder=3)
        ax.text(e - 0.8, yy, f"{e:+.1f}%", ha="right", va="center", fontsize=11,
                color=INK, weight="bold")
        ax.text(1.4, yy, note, fontsize=9, color=INK2, va="center")
    ax.axvline(-12.0, color=INK, lw=2, ls="--", zorder=5)
    ax.text(-12.4, -0.74, "the truth ", fontsize=9.5, color=INK, ha="right")
    ax.set_yticks(ys)
    ax.set_yticklabels([r[0] for r in rows], fontsize=9.5)
    ax.set_xlim(-36, 26)
    ax.set_ylim(-0.95, 3.6)
    ax.set_xlabel("estimated change in the use of force rate")
    style(ax, ygrid=False)
    ax.grid(axis="x", color=GRID, lw=0.8, zorder=0)
    ax.set_axisbelow(True)
    title(ax, "Every estimate this series produced of one 12 percent effect",
          "All computed correctly. The bottom row is the one the checks let you report.")
    fig.tight_layout()
    fig.savefig(HERE / "fig_16_writing_up.png", dpi=150)
    plt.close(fig)


if __name__ == "__main__":
    for fn in (fig_01, fig_02, fig_03, fig_04,
               fig_05, fig_06, fig_07, fig_08,
               fig_09, fig_10, fig_11, fig_12,
               fig_13, fig_14, fig_15, fig_16):
        fn()
        print("built", fn.__name__)
