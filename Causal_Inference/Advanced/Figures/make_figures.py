"""
Build every figure in the Causal Inference Advanced series.

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

import statsmodels.api as sm
import statsmodels.formula.api as smf

PCT = lambda b: 100 * (np.exp(b) - 1)
BASELINE = profile.set_index("agency_id")["pre_program_uof_per_100_arrests"]


def panel(drop_a007=True):
    d = F[F["agency_id"] != "A007"] if drop_a007 else F
    d = d.copy()
    d["lo"] = np.log(d["n_arrests"])
    pi = pd.PeriodIndex(d["year_month"], freq="M")
    d["yr"] = pi.year.values + (pi.month.values - 1) / 12.0
    d["t"] = (pi.year.values - 2019) * 12 + pi.month.values - 1
    return d


def fit(d, treated, outcome="n_uof", form=None, offset=None):
    s = d.copy()
    s["settled"] = ((s["agency_id"].isin(treated)) & (s["period"] == "after")).astype(float)
    s["phase"] = ((s["agency_id"].isin(treated)) & (s["period"] == "phase")).astype(float)
    fo = form or f"{outcome} ~ C(agency_id)+C(year_month)+settled+phase"
    z = smf.glm(fo, s, family=sm.families.Poisson(),
                offset=s["lo"] if offset is None else offset).fit()
    lo, hi = z.conf_int().loc["settled"]
    return PCT(z.params["settled"]), PCT(lo), PCT(hi), z


def fig_01():
    """Module 1. One design, several estimands."""
    d = panel()
    pooled = fit(d, NO_A007)
    per = []
    for a in NO_A007:
        per.append(fit(d[d["agency_id"].isin([a] + COMPARISON)], [a]))

    fig, ax = plt.subplots(figsize=(12.4, 5.4))
    ys = np.arange(len(per) + 2)[::-1]
    for (e, lo, hi, _), yy, a in zip(per, ys[:len(per)], NO_A007):
        ax.plot([lo, hi], [yy, yy], color=INK3, lw=2.4, solid_capstyle="round", zorder=3)
        ax.scatter([e], [yy], s=75, color=INK3, zorder=5)
        ax.text(hi + 0.9, yy, f"{e:+.1f}%", fontsize=9.5, va="center", color=INK2)
    eq = np.mean([x[0] for x in per])
    ax.scatter([eq], [ys[len(per)]], s=120, color=ORANGE, zorder=6)
    ax.text(eq + 1.2, ys[len(per)], f"{eq:+.1f}%", fontsize=10.5, va="center",
            color=INK, weight="bold")
    e, lo, hi, _ = pooled
    ax.plot([lo, hi], [ys[-1], ys[-1]], color=AQUA, lw=3.4, solid_capstyle="round", zorder=3)
    ax.scatter([e], [ys[-1]], s=120, color=AQUA, zorder=6)
    ax.text(hi + 1.2, ys[-1], f"{e:+.1f}%", fontsize=10.5, va="center", color=INK,
            weight="bold")
    ax.axvline(-12.0, color=INK, lw=2, ls="--", zorder=2)
    ax.text(-12.5, -0.78, "the truth ", fontsize=9.5, color=INK, ha="right")
    ax.set_yticks(ys)
    ax.set_yticklabels([SHORT[a] for a in NO_A007]
                       + ["ATT, agencies weighted equally", "ATT, weighted by incidents"],
                       fontsize=9.5)
    ax.set_xlim(-44, 14)
    ax.set_ylim(-1.0, len(per) + 1.6)
    ax.set_xlabel("estimated change in the use of force rate")
    style(ax, ygrid=False)
    ax.grid(axis="x", color=GRID, lw=0.8, zorder=0)
    ax.set_axisbelow(True)
    title(ax, "Two averages of the same four numbers, three points apart",
          "Both are the ATT. Neither is the ATE, which this design cannot reach.")
    fig.tight_layout()
    fig.savefig(HERE / "fig_a01_estimands.png", dpi=150)
    plt.close(fig)


def _node(ax, xy, w, h, text, fc, ec, fs=9.5):
    from matplotlib.patches import FancyBboxPatch
    x, y = xy
    ax.add_patch(FancyBboxPatch((x - w / 2, y - h / 2), w, h,
                                boxstyle="round,pad=0.02,rounding_size=0.07",
                                fc=fc, ec=ec, lw=1.7, zorder=3))
    ax.text(x, y, text, ha="center", va="center", fontsize=fs, color=INK, zorder=5)


def _edge(ax, a, b, color, curve=0.0, lw=2.0, dashed=False):
    ax.annotate("", xy=b, xytext=a, zorder=4,
                arrowprops=dict(arrowstyle="-|>", color=color, lw=lw,
                                linestyle="--" if dashed else "-",
                                shrinkA=19, shrinkB=19,
                                connectionstyle=f"arc3,rad={curve}"))


def fig_02():
    """Module 2. The DAG for this study, and the two backdoor paths."""
    fig, (a1, a2) = plt.subplots(1, 2, figsize=(14.0, 5.2))
    for ax in (a1, a2):
        ax.set_xlim(0, 10); ax.set_ylim(0, 8); ax.axis("off")

    for ax, blocked in [(a1, set()), (a2, {"U", "S"})]:
        fcU = "#e7f6f0" if "U" in blocked else "#fdeee7"
        ecU = AQUA if "U" in blocked else ORANGE
        fcS = "#e7f6f0" if "S" in blocked else "#fdeee7"
        ecS = AQUA if "S" in blocked else ORANGE
        _node(ax, (2.2, 2.0), 3.0, 1.1, "training\nD", "#eaf1fb", BLUE)
        _node(ax, (7.8, 2.0), 3.0, 1.1, "use of force\nY", "#eaf1fb", BLUE)
        _node(ax, (2.2, 6.2), 3.2, 1.1, "baseline rate\nB", fcS, ecS)
        _node(ax, (7.8, 6.2), 3.4, 1.1, "statewide year\nT", fcU, ecU)
        _edge(ax, (2.2, 2.0), (7.8, 2.0), BLUE, lw=2.6)
        _edge(ax, (2.2, 6.2), (2.2, 2.0), ecS, lw=2.2)
        _edge(ax, (2.2, 6.2), (7.8, 2.0), ecS, curve=-0.16, lw=2.2)
        _edge(ax, (7.8, 6.2), (7.8, 2.0), ecU, lw=2.2)
        _edge(ax, (7.8, 6.2), (2.2, 2.0), ecU, curve=0.16, lw=2.2)
        ax.text(5.0, 1.1, "the effect to be identified", ha="center", fontsize=9,
                color=BLUE)

    title(a1, "Two backdoor paths, both open",
          "D <- B -> Y and D <- T -> Y. Either one carries a spurious association.")
    a1.text(5.0, 7.5, "nothing conditioned on", ha="center", fontsize=10, color=ORANGE,
            weight="bold")
    title(a2, "Agency and month effects close both",
          "Agency effects hold B fixed. Month effects hold T fixed.")
    a2.text(5.0, 7.5, "conditioning on agency and month", ha="center", fontsize=10,
            color=AQUA, weight="bold")
    fig.tight_layout()
    fig.savefig(HERE / "fig_a02_dag.png", dpi=150)
    plt.close(fig)


def fig_03():
    """Module 3. Each adjustment set, and which backdoor path it leaves open."""
    d = panel()
    d["base"] = d["agency_id"].map(BASELINE)
    specs = [
        ("nothing", "n_uof ~ settled + phase", "both paths open"),
        ("baseline rate only", "n_uof ~ base + settled + phase", "T still open"),
        ("month effects only", "n_uof ~ C(year_month) + settled + phase", "B still open"),
        ("baseline rate and month effects",
         "n_uof ~ base + C(year_month) + settled + phase", "both closed"),
        ("agency and month effects",
         "n_uof ~ C(agency_id) + C(year_month) + settled + phase", "both closed"),
    ]
    fig, ax = plt.subplots(figsize=(12.8, 5.2))
    ys = np.arange(len(specs))[::-1]
    for (lab, form, note), yy in zip(specs, ys):
        e, lo, hi, _ = fit(d, NO_A007, form=form)
        c = AQUA if note == "both closed" else ORANGE
        ax.plot([lo, hi], [yy, yy], color=c, lw=3.2, solid_capstyle="round", zorder=3)
        ax.scatter([e], [yy], s=100, color=c, zorder=5)
        ax.text(e, yy + 0.25, f"{e:+.1f}%", ha="center", fontsize=10.5, color=INK,
                weight="bold")
        ax.text(24.0, yy, note, fontsize=9, color=c, va="center")
    ax.axvline(-12.0, color=INK, lw=2, ls="--", zorder=6)
    ax.text(-12.4, -0.76, "the truth ", fontsize=9.5, color=INK, ha="right")
    ax.set_yticks(ys)
    ax.set_yticklabels([s[0] for s in specs], fontsize=9.5)
    ax.set_xlim(-38, 42)
    ax.set_ylim(-0.95, len(specs) - 0.35)
    ax.set_xlabel("estimated change in the use of force rate")
    ax.text(24.0, len(specs) - 0.55, "what is left open", fontsize=9.5, color=INK,
            weight="bold")
    style(ax, ygrid=False)
    ax.grid(axis="x", color=GRID, lw=0.8, zorder=0)
    ax.set_axisbelow(True)
    title(ax, "Five adjustment sets, read off the graph before fitting anything",
          "The two that close both backdoor paths land on the truth. The others do not.")
    fig.tight_layout()
    fig.savefig(HERE / "fig_a03_identification.png", dpi=150)
    plt.close(fig)


def fig_04():
    """Module 4. Three selection rules in a world with no program."""
    g = F.copy()
    g["lo"] = np.log(g["n_arrests"])
    pi = pd.PeriodIndex(g["year_month"], freq="M")
    g["t"] = (pi.year.values - 2019) * 12 + pi.month.values - 1
    g["yr"] = pi.year.values + (pi.month.values - 1) / 12.0

    # strip the planted effect back out, giving a world where nothing happened
    phase_w = {0: 0.0, 1: 0.25, 2: 0.58, 3: 0.83}
    start = (2023 - 2019) * 12 + 6
    w = np.array([phase_w.get(kk, 1.0) if (a in TREATED and kk >= 0) else 0.0
                  for a, kk in zip(g["agency_id"], g["t"] - start)])
    g["mu0"] = g["n_uof"].values / (0.88 ** w)

    ids = sorted(g["agency_id"].unique())
    pre = g[g["period"] == "before"]
    level = {a: 100 * pre[pre["agency_id"] == a]["n_uof"].sum()
                / pre[pre["agency_id"] == a]["n_arrests"].sum() for a in ids}
    slope = {}
    for a in ids:
        s = pre[pre["agency_id"] == a]
        z = smf.glm("n_uof ~ yr", s, family=sm.families.Poisson(),
                    offset=s["lo"]).fit()
        slope[a] = PCT(z.params["yr"])
    lw = g[(g["year_month"] >= "2023-01") & (g["year_month"] < "2023-07")]
    recent = {a: 100 * lw[lw["agency_id"] == a]["n_uof"].sum()
                 / lw[lw["agency_id"] == a]["n_arrests"].sum() for a in ids}

    rng = np.random.default_rng(31)

    def bias(pick, reps=200):
        s = g.copy()
        s["settled"] = ((s["agency_id"].isin(pick)) & (s["period"] == "after")).astype(float)
        s["phase"] = ((s["agency_id"].isin(pick)) & (s["period"] == "phase")).astype(float)
        out = []
        for _ in range(reps):
            s["y"] = rng.poisson(np.maximum(s["mu0"].values, 0.01))
            z = smf.glm("y ~ C(agency_id)+C(year_month)+settled+phase", s,
                        family=sm.families.Poisson(), offset=s["lo"]).fit()
            out.append(PCT(z.params["settled"]))
        return np.array(out)

    rules = [("highest level\nbefore", lambda a: -level[a], ORANGE),
             ("steepest downward\ntrend before", lambda a: slope[a], ORANGE),
             ("worst last six\nmonths before", lambda a: -recent[a], ORANGE),
             ("at random", None, AQUA)]
    draws, labs, cols = [], [], []
    for lab, key, c in rules:
        if key is None:
            vals = []
            for _ in range(60):
                vals.extend(bias(list(rng.choice(ids, 5, replace=False)), reps=6))
            draws.append(np.array(vals))
        else:
            draws.append(bias(sorted(ids, key=key)[:5]))
        labs.append(lab); cols.append(c)

    fig, ax = plt.subplots(figsize=(12.4, 5.2))
    xs = np.arange(len(labs))
    parts = ax.violinplot(draws, positions=xs, widths=0.7, showextrema=False)
    for body, c in zip(parts["bodies"], cols):
        body.set_facecolor(c); body.set_alpha(0.32); body.set_edgecolor(c)
    for x, dr, c in zip(xs, draws, cols):
        ax.scatter([x], [dr.mean()], s=110, color=c, zorder=6)
        dy = 1.9 if abs(dr.mean()) < 1.5 else 0.0
        ax.text(x + 0.17, dr.mean() + dy, f"{dr.mean():+.2f}%", fontsize=10.5,
                va="center", color=INK, weight="bold")
    ax.axhline(0, color=INK, lw=2, ls="--", zorder=5)
    ax.text(-0.72, 1.1, "zero, the true effect in this world", fontsize=9.5,
            color=INK, ha="left")
    ax.set_xticks(xs)
    ax.set_xticklabels(labs, fontsize=9.5)
    ax.set_xlim(-0.78, 3.75)
    ax.set_ylabel("estimated effect of a program that does not exist")
    style(ax)
    title(ax, "Four ways of choosing who gets a program that was never given",
          "Each rule biases the estimator differently, and only one of them by nothing.")
    fig.tight_layout()
    fig.savefig(HERE / "fig_a04_selection.png", dpi=150)
    plt.close(fig)


if __name__ == "__main__":
    for fn in (fig_01, fig_02, fig_03, fig_04):
        fn()
        print("built", fn.__name__)
