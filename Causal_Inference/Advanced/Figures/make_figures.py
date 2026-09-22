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



def _mu0(d):
    """Undo the planted effect, giving each agency month its no program mean."""
    PH = {0: 0.0, 1: 0.25, 2: 0.58, 3: 0.83}
    start = (2023 - 2019) * 12 + 6
    w = np.array([PH.get(k, 1.0) if (a in TREATED and k >= 0) else 0.0
                  for a, k in zip(d["agency_id"], d["t"] - start)])
    return d["n_uof"].values / (0.88 ** w)


def fig_05():
    """Module 5. Poisson and linear two way fixed effects are different estimands."""
    d = panel()
    d["rate"] = 100 * d["n_uof"] / d["n_arrests"]
    d["settled"] = ((d["agency_id"].isin(NO_A007)) & (d["period"] == "after")).astype(float)
    d["phase"] = ((d["agency_id"].isin(NO_A007)) & (d["period"] == "phase")).astype(float)

    zp = smf.glm("n_uof ~ C(agency_id)+C(year_month)+settled+phase", d,
                 family=sm.families.Poisson(), offset=d["lo"]).fit()
    ep, lp, hp = PCT(zp.params["settled"]), *[PCT(v) for v in zp.conf_int().loc["settled"]]
    zo = smf.ols("rate ~ C(agency_id)+C(year_month)+settled+phase", d).fit()
    base = d[(d["agency_id"].isin(NO_A007)) & (d["period"] == "before")]["rate"].mean()
    eo = 100 * zo.params["settled"] / base
    lo_, ho_ = [100 * v / base for v in zo.conf_int().loc["settled"]]

    fig, (a1, a2) = plt.subplots(1, 2, figsize=(13.4, 5.0))

    for yy, (lab, e, lo, hi, c) in enumerate([
            ("linear, on the rate", eo, lo_, ho_, ORANGE),
            ("Poisson, with an offset", ep, lp, hp, AQUA)]):
        a1.plot([lo, hi], [yy, yy], color=c, lw=3.4, solid_capstyle="round", zorder=3)
        a1.scatter([e], [yy], s=110, color=c, zorder=5)
        a1.text(e, yy + 0.16, f"{e:+.1f}%", ha="center", fontsize=11, color=INK,
                weight="bold")
    a1.axvline(-12.0, color=INK, lw=2, ls="--", zorder=6)
    a1.text(-12.4, -0.42, "the truth ", fontsize=9.5, color=INK, ha="right")
    a1.set_yticks([0, 1])
    a1.set_yticklabels(["linear, on the rate", "Poisson, with an offset"], fontsize=10)
    a1.set_xlim(-32, 2)
    a1.set_ylim(-0.55, 1.5)
    a1.set_xlabel("estimated change in the use of force rate")
    style(a1, ygrid=False)
    a1.grid(axis="x", color=GRID, lw=0.8, zorder=0)
    a1.set_axisbelow(True)
    title(a1, "Two estimators, five points apart",
          "Neither is biased. They weight the four agencies differently.")

    post = d[(d["agency_id"].isin(NO_A007)) & (d["period"] == "after")]
    inc = post.groupby("agency_id")["n_uof"].sum()
    inc = 100 * inc / inc.sum()
    mon = post.groupby("agency_id").size()
    mon = 100 * mon / mon.sum()
    xs = np.arange(len(NO_A007))
    wdt = 0.36
    a2.bar(xs - wdt / 2, [inc[a] for a in NO_A007], width=wdt, color=AQUA, zorder=3,
           label="share of incidents, the Poisson weights")
    a2.bar(xs + wdt / 2, [mon[a] for a in NO_A007], width=wdt, color=ORANGE, zorder=3,
           label="share of agency months, the linear weights")
    for x, a in zip(xs, NO_A007):
        a2.text(x - wdt / 2, inc[a] + 1.4, f"{inc[a]:.0f}", ha="center", fontsize=9.5,
                color=INK)
        a2.text(x + wdt / 2, mon[a] + 1.4, f"{mon[a]:.0f}", ha="center", fontsize=9.5,
                color=INK)
    a2.set_xticks(xs)
    a2.set_xticklabels([SHORT[a] for a in NO_A007], fontsize=9.5)
    a2.set_ylim(0, 72)
    a2.set_ylabel("percent")
    a2.legend(fontsize=8.5, frameon=False)
    style(a2)
    title(a2, "Where the difference comes from",
          "Stonewick carries 60 percent of the incidents and a quarter of the months.")

    fig.tight_layout()
    fig.savefig(HERE / "fig_a05_twfe.png", dpi=150)
    plt.close(fig)


def fig_06():
    """Module 6. The event study, and the power of the pre period test."""
    d = panel()
    d["k"] = d["t"] - ((2023 - 2019) * 12 + 6)
    d["ek"] = np.clip(d["k"], -8, 10).astype(int)
    d["trm"] = d["agency_id"].isin(NO_A007)
    d.loc[~d["trm"], "ek"] = -99
    js = [j for j in range(-8, 11) if j != -1]
    terms = " + ".join([f"I(trm&(ek=={j}))" for j in js])
    z = smf.glm("n_uof ~ C(agency_id)+C(year_month)+" + terms, d,
                family=sm.families.Poisson(), offset=d["lo"]).fit()

    est, lo, hi = [], [], []
    for j in js:
        k = [c for c in z.params.index if f"ek == {j}" in c][0]
        l, h = z.conf_int().loc[k]
        est.append(PCT(z.params[k])); lo.append(PCT(l)); hi.append(PCT(h))

    fig, (a1, a2) = plt.subplots(1, 2, figsize=(13.6, 5.0),
                                 gridspec_kw={"width_ratios": [1.4, 1]})
    jf = np.array(js, dtype=float)
    cols = [INK3 if j < 0 else BLUE for j in js]
    a1.errorbar(jf, est, yerr=[np.array(est) - np.array(lo), np.array(hi) - np.array(est)],
                fmt="o", ms=5, color=INK3, ecolor=GRID, elinewidth=2, zorder=4)
    a1.scatter(jf, est, s=45, color=cols, zorder=5)
    frac = np.interp(np.arange(-8, 11), [0, 1, 2, 3, 4], [0, .25, .58, .83, 1.0],
                     left=0, right=1.0)
    a1.plot(np.arange(-8, 11), 100 * (np.exp(np.log(0.88) * frac) - 1), color=ORANGE,
            lw=2.6, zorder=6, label="the effect that is actually there")
    a1.axhline(0, color=GRID, lw=1)
    a1.axvline(-0.5, color=INK3, lw=1.2, ls="--", zorder=3)
    a1.set_xlabel("months since the program started")
    a1.set_ylabel("estimated change in the rate")
    a1.set_ylim(-58, 48)
    a1.legend(fontsize=8.5, frameon=False, loc="lower left")
    style(a1)
    title(a1, "The event study, one coefficient per month",
          "Individually unreadable. The pre period coefficients are the usable output.")

    powers = [(1, 2), (2, 16), (3, 40), (5, 87)]
    a2.bar([p[0] for p in powers], [p[1] for p in powers], color=AQUA, width=0.55,
           zorder=3)
    for x, y in powers:
        a2.text(x, y + 2.2, f"{y}%", ha="center", fontsize=11, color=INK, weight="bold")
    a2.axhline(80, color=ORANGE, lw=2, ls="--", zorder=4)
    a2.text(5.4, 82, "80 percent power", fontsize=9.5, color=ORANGE, ha="right")
    a2.set_xticks([p[0] for p in powers])
    a2.set_xlabel("size of the planted pre trend violation, percent a year")
    a2.set_ylabel("share of simulations where the test rejects")
    a2.set_ylim(0, 100)
    a2.set_xlim(0.3, 5.7)
    style(a2)
    title(a2, "And how often the pre period test finds a violation",
          "The violation that mattered in this dataset was 2.16 percent a year.")

    fig.tight_layout()
    fig.savefig(HERE / "fig_a06_event_study.png", dpi=150)
    plt.close(fig)


def fig_07():
    """Module 7. The staggered adoption bias, decomposed."""
    d = panel()
    d["mu0"] = _mu0(d)
    zp = smf.glm("mu0 ~ C(agency_id)+C(year_month)", d, family=sm.families.Poisson(),
                 offset=d["lo"]).fit()
    d["mu0par"] = zp.fittedvalues

    waves = {"A001": (2021 - 2019) * 12, "A002": (2022 - 2019) * 12,
             "A004": (2023 - 2019) * 12, "A010": (2024 - 2019) * 12}
    d["D"] = 0.0
    for a, g in waves.items():
        d.loc[(d["agency_id"] == a) & (d["t"] >= g), "D"] = 1.0
    nD = {a: int(((d["agency_id"] == a) & (d["t"] >= g)).sum()) for a, g in waves.items()}
    tw = np.array([nD[a] for a in waves], float); tw /= tw.sum()
    het = {"A001": 0.25, "A002": 0.18, "A004": 0.10, "A010": 0.05}
    hom = {a: 0.12 for a in waves}
    true_het = -100 * sum(het[a] * x for a, x in zip(waves, tw))

    rng = np.random.default_rng(17)

    def run(base, effects, reps=150):
        mult = np.ones(len(d))
        for a, g in waves.items():
            mult[((d["agency_id"] == a) & (d["t"] >= g)).values] = 1 - effects[a]
        mu = d[base].values * mult
        out = []
        for _ in range(reps):
            d["y"] = rng.poisson(np.maximum(mu, 0.01))
            z = smf.glm("y ~ C(agency_id)+C(year_month)+D", d,
                        family=sm.families.Poisson(), offset=d["lo"]).fit()
            out.append(PCT(z.params["D"]))
        return np.mean(out)

    cells = [("trends as they are\nin this panel", "mu0"),
             ("trends forced\nparallel", "mu0par")]
    effs = [("constant 12 percent", hom, -12.0), ("heterogeneous by wave", het, true_het)]

    fig, ax = plt.subplots(figsize=(11.2, 5.2))
    xs = np.arange(len(cells))
    wdt = 0.22
    for i, (lab, eff, truth) in enumerate(effs):
        biases = [run(base, eff) - truth for _, base in cells]
        c = ORANGE if i else AQUA
        ax.bar(xs + (i - 0.5) * wdt, biases, width=wdt, color=c, zorder=3, label=lab)
        for x, b in zip(xs + (i - 0.5) * wdt, biases):
            dy = 0.26 if b > 0 else -0.38
            ax.text(x, b + dy, f"{b:+.2f}", ha="center", fontsize=11, color=INK,
                    weight="bold")
    ax.axhline(0, color=INK, lw=2, zorder=5)
    ax.set_xticks(xs)
    ax.set_xticklabels([c[0] for c in cells], fontsize=10)
    ax.set_xlim(-0.45, 1.45)
    ax.set_ylabel("bias of two way fixed effects, percentage points")
    ax.set_ylim(-8.2, 1.6)
    ax.legend(fontsize=9.5, frameon=False, loc="lower left")
    style(ax)
    title(ax, "Staggered adoption: two problems, separately measured",
          "Only the green bar on the right is the textbook case, and only it is unbiased.")
    fig.tight_layout()
    fig.savefig(HERE / "fig_a07_staggered.png", dpi=150)
    plt.close(fig)


def fig_08():
    """Module 8. Synthetic control, and the pre period fit that condemns it."""
    from scipy.optimize import minimize
    d = panel(drop_a007=False)
    piv = d.pivot_table(index="year_month", columns="agency_id",
                        values="uof_per_100_arrests").interpolate()
    pre = piv[piv.index < "2023-07"]
    post = piv[piv.index >= "2023-11"]
    donors = [a for a in piv.columns if a not in TREATED]

    rows = []
    for t in TREATED:
        Y, X = pre[t].values, pre[donors].values
        r = minimize(lambda w: np.mean((Y - X @ w) ** 2),
                     np.repeat(1 / len(donors), len(donors)),
                     bounds=[(0, 1)] * len(donors),
                     constraints=({"type": "eq", "fun": lambda w: w.sum() - 1},))
        rmse = np.sqrt(np.mean((Y - X @ r.x) ** 2))
        eff = 100 * (post[t].mean() / (post[donors].values @ r.x).mean() - 1)
        rows.append((SHORT[t], rmse, rmse / Y.mean(), eff, Y.mean(),
                     pre[donors].mean().max()))

    fig, (a1, a2) = plt.subplots(1, 2, figsize=(13.4, 5.0))
    xs = np.arange(len(rows))
    a1.bar(xs, [r[2] * 100 for r in rows], color=ORANGE, width=0.55, zorder=3)
    for x, r in zip(xs, rows):
        a1.text(x, r[2] * 100 + 1.2, f"{r[2] * 100:.0f}%", ha="center", fontsize=11,
                color=INK, weight="bold")
    a1.axhline(5, color=AQUA, lw=2, ls="--", zorder=4)
    a1.text(4.45, 6.5, "a fit worth using is below about this", fontsize=9,
            color=AQUA, ha="right")
    a1.set_xticks(xs)
    a1.set_xticklabels([r[0] for r in rows], fontsize=9, rotation=18, ha="right")
    a1.set_ylabel("pre period fit error, percent of the agency's own mean")
    a1.set_ylim(0, 58)
    style(a1)
    title(a1, "The diagnostic that comes before the answer",
          "Four of the five sit above every donor. The fifth is inside the range and still fits badly.")

    a2.barh(xs[::-1], [r[3] for r in rows], color=ORANGE, height=0.5, zorder=3)
    for yy, r in zip(xs[::-1], rows):
        off = 0.9 if r[3] > 0 else -0.9
        ha = "left" if r[3] > 0 else "right"
        a2.text(r[3] + off, yy, f"{r[3]:+.1f}%", ha=ha, va="center", fontsize=10.5,
                color=INK, weight="bold")
    a2.axvline(-12.0, color=INK, lw=2, ls="--", zorder=5)
    a2.text(-12.4, -0.72, "the truth ", fontsize=9.5, color=INK, ha="right")
    a2.axvline(0, color=INK3, lw=1.2, zorder=2)
    a2.set_yticks(xs[::-1])
    a2.set_yticklabels([r[0] for r in rows], fontsize=9.5)
    a2.set_xlim(-32, 22)
    a2.set_ylim(-0.95, len(rows) - 0.4)
    a2.set_xlabel("what synthetic control reports")
    style(a2, ygrid=False)
    a2.grid(axis="x", color=GRID, lw=0.8, zorder=0)
    a2.set_axisbelow(True)
    title(a2, "And what it reports when the diagnostic is ignored",
          "Five agencies, one true effect of 12 percent, answers from +11 to -25.")

    fig.tight_layout()
    fig.savefig(HERE / "fig_a08_synthetic_control.png", dpi=150)
    plt.close(fig)


def fig_09():
    """Module 9. Four ways of putting an interval on the same estimate."""
    d = panel()
    d["settled"] = ((d["agency_id"].isin(NO_A007)) & (d["period"] == "after")).astype(float)
    d["phase"] = ((d["agency_id"].isin(NO_A007)) & (d["period"] == "phase")).astype(float)
    F0 = "n_uof ~ C(agency_id)+C(year_month)+settled+phase"
    z = smf.glm(F0, d, family=sm.families.Poisson(), offset=d["lo"]).fit()
    real = PCT(z.params["settled"])
    mb = [PCT(v) for v in z.conf_int().loc["settled"]]
    zc = smf.glm(F0, d, family=sm.families.Poisson(), offset=d["lo"]).fit(
        cov_type="cluster", cov_kwds={"groups": d["agency_id"]})
    cr = [PCT(v) for v in zc.conf_int().loc["settled"]]

    rng = np.random.default_rng(21)
    ids = sorted(d["agency_id"].unique())
    boots = []
    for _ in range(400):
        pick = rng.choice(ids, len(ids), replace=True)
        s = pd.concat([d[d["agency_id"] == a].assign(agency_id=f"{a}_{i}")
                       for i, a in enumerate(pick)])
        try:
            zz = smf.glm(F0, s, family=sm.families.Poisson(), offset=s["lo"]).fit()
            boots.append(PCT(zz.params["settled"]))
        except Exception:
            pass
    bs = [np.percentile(boots, 2.5), np.percentile(boots, 97.5)]

    fakes = []
    for _ in range(400):
        pick = list(rng.choice(ids, len(NO_A007), replace=False))
        s = d.copy()
        s["settled"] = ((s["agency_id"].isin(pick)) & (s["period"] == "after")).astype(float)
        s["phase"] = ((s["agency_id"].isin(pick)) & (s["period"] == "phase")).astype(float)
        zz = smf.glm(F0, s, family=sm.families.Poisson(), offset=s["lo"]).fit()
        fakes.append(PCT(zz.params["settled"]))
    fakes = np.array(fakes)
    ri = [np.percentile(fakes, 2.5), np.percentile(fakes, 97.5)]
    pval = np.mean(fakes <= real)

    rows = [("model based", mb, AQUA, ""),
            (f"cluster robust, {d['agency_id'].nunique()} clusters", cr, ORANGE,
             "far below the 40 it needs"),
            ("cluster bootstrap", bs, AQUA, ""),
            ("randomisation, the null", ri, INK3,
             f"the estimate sits at p = {pval:.3f}")]
    fig, ax = plt.subplots(figsize=(12.6, 5.0))
    ys = np.arange(len(rows))[::-1]
    for (lab, iv, c, note), yy in zip(rows, ys):
        ax.plot(iv, [yy, yy], color=c, lw=3.4, solid_capstyle="round", zorder=3)
        ax.text(iv[0] - 0.7, yy, f"{iv[0]:+.1f}", ha="right", va="center", fontsize=9.5,
                color=INK2)
        ax.text(iv[1] + 0.7, yy, f"{iv[1]:+.1f}", ha="left", va="center", fontsize=9.5,
                color=INK2)
        if note:
            ax.text(20.0, yy, note, fontsize=8.5, color=c, va="center")
    ax.axvline(real, color=INK, lw=2.4, zorder=6)
    ax.text(real - 0.6, -0.72, f"the estimate, {real:+.1f}%  ", fontsize=9.5,
            color=INK, ha="right")
    ax.axvline(0, color=INK3, lw=1.2, ls=":", zorder=2)
    ax.set_yticks(ys)
    ax.set_yticklabels([r[0] for r in rows], fontsize=9.5)
    ax.set_xlim(-26, 40)
    ax.set_ylim(-0.95, len(rows) - 0.35)
    ax.set_xlabel("95 percent interval for the change in the use of force rate")
    style(ax, ygrid=False)
    ax.grid(axis="x", color=GRID, lw=0.8, zorder=0)
    ax.set_axisbelow(True)
    title(ax, "Four intervals for one estimate, from eleven agencies",
          "The bootstrap is widest. The cluster robust one is not, which is the warning.")
    fig.tight_layout()
    fig.savefig(HERE / "fig_a09_few_clusters.png", dpi=150)
    plt.close(fig)



def _profile_frame():
    X = profile.set_index("agency_id").copy()
    X = X.loc[sorted(X.index)]
    X["treated"] = [1 if a in TREATED else 0 for a in X.index]
    X["lpop"] = np.log(X["population_served"])
    X["lsworn"] = np.log(X["sworn_officers"])
    return X


def fig_10():
    """Module 10. Separation is mechanical, and the overlap that matters is absent."""
    X = _profile_frame()

    fig, (a1, a2) = plt.subplots(1, 2, figsize=(13.6, 5.0))

    sets = [("one covariate", ["lsworn"]),
            ("two covariates", ["lsworn", "violent_crime_rate_per_1000"]),
            ("four covariates", ["lsworn", "lpop", "violent_crime_rate_per_1000",
                                 "property_crime_rate_per_1000"])]
    for i, (lab, cols) in enumerate(sets):
        Z = sm.add_constant(X[cols].astype(float))
        lg = sm.Logit(X["treated"], Z).fit(disp=False)
        ps = lg.predict(Z)
        for tr, c, off in [(1, BLUE, 0.13), (0, INK3, -0.13)]:
            a1.scatter(ps[X["treated"] == tr], np.full((X["treated"] == tr).sum(), i + off),
                       s=75, color=c, zorder=5, alpha=0.9)
        a1.text(1.06, i, f"pseudo R2 {lg.prsquared:.2f}", fontsize=9, color=INK2,
                va="center")
    a1.set_yticks(range(len(sets)))
    a1.set_yticklabels([s[0] for s in sets], fontsize=10)
    a1.set_xlim(-0.06, 1.42)
    a1.set_ylim(-0.6, len(sets) - 0.4)
    a1.set_xlabel("estimated propensity score")
    a1.text(0.02, len(sets) - 0.55, "treated", fontsize=9.5, color=BLUE)
    a1.text(0.20, len(sets) - 0.55, "not treated", fontsize=9.5, color=INK3)
    style(a1, ygrid=False)
    a1.grid(axis="x", color=GRID, lw=0.8, zorder=0)
    a1.set_axisbelow(True)
    title(a1, "Add covariates to twelve units and separation arrives",
          "Four columns of pure noise separate these groups in 6 percent of draws.")

    for tr, c, lab in [(1, BLUE, "took the training"), (0, INK3, "did not")]:
        v = X[X["treated"] == tr]["pre_program_uof_per_100_arrests"]
        a2.scatter(v, np.full(len(v), tr), s=110, color=c, zorder=5, label=lab)
        for a, x in zip(X[X["treated"] == tr].index, v):
            a2.annotate(SHORT[a], (x, tr), fontsize=8, color=INK2, rotation=40,
                        xytext=(2, 9 if tr else -20), textcoords="offset points")
    a2.axvline(3.159, color=ORANGE, lw=2, ls="--", zorder=4)
    a2.text(3.20, 0.5, "  the only control above\n  the lowest treated agency",
            fontsize=9, color=ORANGE, va="center")
    a2.set_yticks([0, 1])
    a2.set_yticklabels(["not treated", "took the training"], fontsize=10)
    a2.set_ylim(-0.55, 1.75)
    a2.set_xlim(1.9, 4.6)
    a2.set_xlabel("use of force rate before the program")
    style(a2, ygrid=False)
    a2.grid(axis="x", color=GRID, lw=0.8, zorder=0)
    a2.set_axisbelow(True)
    title(a2, "And the variable that decided selection does not overlap",
          "One control agency sits above the lowest treated one. There is nothing to match to.")

    fig.tight_layout()
    fig.savefig(HERE / "fig_a10_propensity.png", dpi=150)
    plt.close(fig)


def fig_11():
    """Module 11. Every candidate instrument, on the two conditions it must meet."""
    X = _profile_frame()
    X["east"] = (X["region"] == "East").astype(int)
    X["sheriff"] = (X["agency_type"] == "County Sheriff").astype(int)
    X["lbudget"] = np.log(X["county_budget_millions"])
    X["lcounty"] = np.log(X["county_population"])
    pre = F[F["period"] == "before"]
    X["pre_rate"] = pre.groupby("agency_id").apply(
        lambda g: 100 * g["n_uof"].sum() / g["n_arrests"].sum())

    cands = [("region is East", "east"), ("is a sheriff's office", "sheriff"),
             ("county budget", "lbudget"), ("county population", "lcounty"),
             ("public safety budget share", "budget_share_public_safety_pct")]
    rows = []
    for lab, c in cands:
        z1 = sm.OLS(X["treated"], sm.add_constant(X[[c]].astype(float))).fit()
        z2 = sm.OLS(X["pre_rate"], sm.add_constant(X[[c]].astype(float))).fit()
        rows.append((lab, z1.fvalue, z2.pvalues.iloc[1]))

    fig, ax = plt.subplots(figsize=(11.8, 5.4))
    ax.axvspan(10, 100, color=AQUA, alpha=0.10, zorder=1)
    for lab, fv, pv in rows:
        c = ORANGE if fv < 10 else AQUA
        ax.scatter([fv], [pv], s=120, color=c, zorder=5)
        ax.annotate(lab, (fv, pv), fontsize=9, color=INK2,
                    xytext=(9, 4), textcoords="offset points")
    ax.axvline(10, color=AQUA, lw=2, ls="--", zorder=4)
    ax.axhline(0.05, color=ORANGE, lw=2, ls="--", zorder=4)
    ax.text(10.6, 0.62, "relevance needs\nF above 10", fontsize=9.5, color=AQUA)
    ax.text(0.09, 0.043, "below this line, the candidate is\nassociated with the outcome before\n"
                         "the program, so exclusion fails",
            fontsize=9, color=ORANGE, va="top")
    ax.set_xscale("log")
    ax.set_xlim(0.0025, 80)
    ax.set_ylim(-0.03, 0.72)
    ax.set_xlabel("F statistic for predicting treatment, log scale")
    ax.set_ylabel("p value for association with the pre program outcome")
    style(ax)
    title(ax, "Five candidate instruments, neither condition met by any of them",
          "A usable instrument would sit in the shaded strip and well above the orange line.")
    fig.tight_layout()
    fig.savefig(HERE / "fig_a11_instrumental_variables.png", dpi=150)
    plt.close(fig)


def fig_12():
    """Module 12. The running variable, and why the cutoff is not sharp."""
    X = _profile_frame()
    v = X["pre_program_uof_per_100_arrests"].sort_values()
    cut = 3.159

    fig, (a1, a2) = plt.subplots(1, 2, figsize=(13.6, 5.0),
                                 gridspec_kw={"width_ratios": [1.35, 1]})

    for a, x in v.items():
        tr = a in TREATED
        wrong = tr != (x > cut)
        c = ORANGE if wrong else (BLUE if tr else INK3)
        a1.scatter([x], [1 if tr else 0], s=150 if wrong else 95, color=c, zorder=5)
        if wrong:
            a1.annotate(SHORT[a], (x, 1 if tr else 0), fontsize=9.5, color=ORANGE,
                        weight="bold", xytext=(-8, 16 if tr else -24),
                        textcoords="offset points", ha="right")
    a1.axvline(cut, color=INK, lw=2.2, zorder=4)
    a1.text(cut, 1.70, " a cutoff at 3.16", fontsize=9.5, color=INK)
    a1.text(2.62, 1.34, "below the cutoff, and treated",
            fontsize=8.5, color=ORANGE, ha="center")
    a1.text(3.20, -0.40, "above the cutoff, and not treated",
            fontsize=8.5, color=ORANGE, ha="center")
    a1.text(4.05, 1.03, "the other four treated", fontsize=8.5, color=BLUE, ha="center")
    a1.text(2.35, 0.19, "the other six controls", fontsize=8.5, color=INK3, ha="center")
    a1.set_yticks([0, 1])
    a1.set_yticklabels(["not treated", "treated"], fontsize=10)
    a1.set_ylim(-0.55, 1.85)
    a1.set_xlim(1.9, 4.5)
    a1.set_xlabel("use of force rate before the program, the running variable")
    style(a1, ygrid=False)
    a1.grid(axis="x", color=GRID, lw=0.8, zorder=0)
    a1.set_axisbelow(True)
    title(a1, "The selection rule was close to a threshold",
          "Two units fall on the wrong side, so the assignment is fuzzy, not sharp.")

    bws = [0.15, 0.30, 0.50, 0.80]
    counts = [int((np.abs(v - cut) < b).sum()) for b in bws]
    a2.bar(range(len(bws)), counts, color=ORANGE, width=0.55, zorder=3)
    for i, c in enumerate(counts):
        a2.text(i, c + 0.22, str(c), ha="center", fontsize=12, color=INK, weight="bold")
    a2.text(0.5, 6.4, "too few to estimate\nanything", fontsize=9, color=ORANGE,
            ha="center")
    a2.text(2.5, 8.6, "no longer local:\nthis is most of the sample", fontsize=9,
            color=ORANGE, ha="center")
    a2.set_xticks(range(len(bws)))
    a2.set_xticklabels([f"{b:.2f}" for b in bws], fontsize=10)
    a2.set_xlabel("bandwidth around the cutoff")
    a2.set_ylabel("agencies inside the bandwidth")
    a2.set_ylim(0, 11)
    style(a2)
    title(a2, "And there is nothing near it to compare",
          "Either the window is local and nearly empty, or it holds the whole panel.")

    fig.tight_layout()
    fig.savefig(HERE / "fig_a12_regression_discontinuity.png", dpi=150)
    plt.close(fig)



def fig_13():
    """Module 13. Two placebo nulls for the same estimate, and only one is right."""
    d = panel()
    real = fit(d, NO_A007)[0]

    one = []
    for a in COMPARISON:
        rest = [x for x in COMPARISON if x != a]
        one.append(fit(d[d["agency_id"].isin([a] + rest)], [a])[0])
    one = np.array(one)

    rng = np.random.default_rng(21)
    ids = sorted(d["agency_id"].unique())
    four = []
    for _ in range(400):
        pick = list(rng.choice(ids, 4, replace=False))
        four.append(fit(d, pick)[0])
    four = np.array(four)

    fig, ax = plt.subplots(figsize=(12.4, 5.2))
    ax.scatter(one, np.full(len(one), 1) + rng.normal(0, 0.035, len(one)),
               s=95, color=ORANGE, zorder=5, label="one agency pretended treated, 7 of them")
    parts = ax.violinplot([four], positions=[0], widths=0.55, showextrema=False,
                          vert=False)
    parts["bodies"][0].set_facecolor(AQUA)
    parts["bodies"][0].set_alpha(0.32)
    parts["bodies"][0].set_edgecolor(AQUA)
    ax.scatter(four, np.full(len(four), 0) + rng.normal(0, 0.05, len(four)),
               s=6, color=AQUA, alpha=0.35, zorder=4)
    ax.axvline(real, color=INK, lw=2.6, zorder=7)
    ax.text(real - 1.2, -0.62, f"the estimate, {real:+.1f}%  ", fontsize=9.5,
            color=INK, ha="right")
    p1 = (np.sum(one <= real) + 1) / (len(one) + 1)
    p4 = np.mean(four <= real)
    ax.text(30, 1, f"p = {p1:.2f}\nthe wrong null", fontsize=10, color=ORANGE,
            va="center")
    ax.text(30, 0, f"p = {p4:.3f}\nthe right null", fontsize=10, color=AQUA,
            va="center")
    ax.set_yticks([0, 1])
    ax.set_yticklabels(["four agencies pretended\ntreated, 400 draws",
                        "one agency pretended\ntreated, 7 of them"], fontsize=9.5)
    ax.set_xlim(-32, 48)
    ax.set_ylim(-0.85, 1.6)
    ax.set_xlabel("estimated effect of a program that was never given")
    style(ax, ygrid=False)
    ax.grid(axis="x", color=GRID, lw=0.8, zorder=0)
    ax.set_axisbelow(True)
    title(ax, "The placebo null depends on how many units you pretend to treat",
          "The treatment went to four agencies, so the four agency null is the reference.")
    fig.tight_layout()
    fig.savefig(HERE / "fig_a13_placebo.png", dpi=150)
    plt.close(fig)


def fig_14():
    """Module 14. Three sensitivity analyses with three different verdicts."""
    d = panel()
    d["tr"] = d["agency_id"].isin(NO_A007).astype(float)
    d["yrc"] = d["yr"] - d["yr"].min()

    deltas = np.arange(0.0, -6.1, -0.5)
    est = []
    for delta in deltas:
        dd = d.copy()
        dd["adj"] = np.log(dd["n_arrests"]) + np.log(1 + delta / 100) * dd["tr"] * dd["yrc"]
        est.append(fit(dd, NO_A007, offset=dd["adj"])[0])
    pre = d[d["period"] == "before"]
    z = smf.glm("n_uof ~ C(agency_id) + yr + tr:yr", pre,
                family=sm.families.Poisson(), offset=pre["lo"]).fit()
    k = [x for x in z.params.index if "yr" in x and "tr" in x][0]
    olo = PCT(z.conf_int().loc[k][0])

    tr = d[d["agency_id"].isin(NO_A007)]
    y1 = rate(tr[tr["period"] == "after"])
    before = rate(tr[tr["period"] == "before"])
    after_c = [rate(d[(d["agency_id"] == a) & (d["period"] == "after")])
               for a in COMPARISON]

    d["settled"] = ((d["agency_id"].isin(NO_A007)) & (d["period"] == "after")).astype(float)
    d["phase"] = ((d["agency_id"].isin(NO_A007)) & (d["period"] == "phase")).astype(float)
    short = smf.glm("n_uof ~ settled+phase", d, family=sm.families.Poisson(),
                    offset=d["lo"]).fit()
    full = smf.glm("n_uof ~ C(agency_id)+C(year_month)+settled+phase", d,
                   family=sm.families.Poisson(), offset=d["lo"]).fit()
    bs, bf = PCT(short.params["settled"]), PCT(full.params["settled"])
    delta_o = abs((0 - bf) / (bf - bs))

    fig, (a1, a2) = plt.subplots(1, 2, figsize=(13.6, 5.0),
                                 gridspec_kw={"width_ratios": [1.25, 1]})
    a1.axvspan(olo, 0.6, color=AQUA, alpha=0.13, zorder=1)
    a1.plot(deltas, est, color=BLUE, lw=2.8, zorder=5)
    a1.axhline(0, color=INK, lw=1.8, zorder=4)
    cross = np.interp(0, est, deltas)
    a1.scatter([cross], [0], s=130, color=ORANGE, zorder=7)
    a1.annotate(f"{abs(cross):.1f}% a year would\nerase the estimate",
                xy=(cross, 0), xytext=(cross - 0.2, -12), fontsize=9.5, color=ORANGE,
                ha="center", arrowprops=dict(arrowstyle="->", color=ORANGE, lw=1.7))
    a1.text(-1.7, 14, "the shaded band is what\nthe pre period cannot rule out",
            fontsize=9, color=AQUA, ha="center")
    a1.set_xlim(0.6, -6.2)
    a1.set_ylim(-20, 18)
    a1.set_xlabel("hidden trend favouring the treated, percent a year")
    a1.set_ylabel("estimated change in the rate")
    style(a1)
    title(a1, "Sensitivity to an unmeasured trend",
          "The breakdown point sits just inside what the pre period allows.")

    rows = [("no assumption at all:\nY(0) anywhere the untreated span",
             100 * (y1 / max(after_c) - 1), 100 * (y1 / min(after_c) - 1), ORANGE),
            ("Y(0) did not rise above the\ntreated group's own before value",
             100 * (y1 / before - 1), 100 * (y1 / min(after_c) - 1), INK3)]
    ys = [1, 0]
    for (lab, lo, hi, c), yy in zip(rows, ys):
        a2.plot([lo, hi], [yy, yy], color=c, lw=3.4, solid_capstyle="round", zorder=3)
        if lo > -10:
            a2.text(lo, yy + 0.16, f"{lo:+.1f}", ha="center", va="bottom",
                    fontsize=9.5, color=INK2)
        else:
            a2.text(lo - 2.5, yy, f"{lo:+.1f}", ha="right", va="center",
                    fontsize=9.5, color=INK2)
        a2.text(hi + 2.5, yy, f"{hi:+.1f}", ha="left", va="center", fontsize=9.5,
                color=INK2)
    a2.axvline(-12.0, color=INK, lw=2.2, ls="--", zorder=6)
    a2.text(-12.5, -0.62, "the truth ", fontsize=9.5, color=INK, ha="right")
    a2.axvline(0, color=INK3, lw=1, ls=":", zorder=2)
    a2.text(70, 1, "excludes the truth", fontsize=9, color=ORANGE, va="center")
    a2.text(70, 0, "contains it, and is\n75 points wide", fontsize=9, color=INK3,
            va="center")
    a2.set_yticks(ys)
    a2.set_yticklabels([r[0] for r in rows], fontsize=9)
    a2.set_xlim(-46, 132)
    a2.set_ylim(-0.8, 1.5)
    a2.set_xlabel("bounds on the effect")
    style(a2, ygrid=False)
    a2.grid(axis="x", color=GRID, lw=0.8, zorder=0)
    a2.set_axisbelow(True)
    title(a2, "And bounds that assume almost nothing",
          f"An unobservable would need {delta_o:.1f} times the pull of the observed controls.")

    fig.tight_layout()
    fig.savefig(HERE / "fig_a14_sensitivity.png", dpi=150)
    plt.close(fig)


def fig_15():
    """Module 15. Four estimates of one common effect, and the test that says so."""
    import scipy.stats as st
    d = panel()
    for a in NO_A007:
        d[f"s_{a}"] = ((d["agency_id"] == a) & (d["period"] == "after")).astype(float)
    d["phase"] = ((d["agency_id"].isin(NO_A007)) & (d["period"] == "phase")).astype(float)
    terms = " + ".join(f"s_{a}" for a in NO_A007)
    zh = smf.glm("n_uof ~ C(agency_id)+C(year_month)+phase+" + terms, d,
                 family=sm.families.Poisson(), offset=d["lo"]).fit()
    d["settled"] = ((d["agency_id"].isin(NO_A007)) & (d["period"] == "after")).astype(float)
    z0 = smf.glm("n_uof ~ C(agency_id)+C(year_month)+settled+phase", d,
                 family=sm.families.Poisson(), offset=d["lo"]).fit()
    lr = 2 * (zh.llf - z0.llf)
    pv = 1 - st.chi2.cdf(lr, len(NO_A007) - 1)

    fig, ax = plt.subplots(figsize=(12.4, 5.2))
    ys = np.arange(len(NO_A007) + 1)[::-1]
    for a, yy in zip(NO_A007, ys[:-1]):
        e = PCT(zh.params[f"s_{a}"])
        lo, hi = [PCT(v) for v in zh.conf_int().loc[f"s_{a}"]]
        ax.plot([lo, hi], [yy, yy], color=INK3, lw=2.8, solid_capstyle="round", zorder=3)
        ax.scatter([e], [yy], s=85, color=INK3, zorder=5)
        ax.text(hi + 1.2, yy, f"{e:+.1f}%", fontsize=9.5, va="center", color=INK2)
    e = PCT(z0.params["settled"])
    lo, hi = [PCT(v) for v in z0.conf_int().loc["settled"]]
    ax.plot([lo, hi], [ys[-1], ys[-1]], color=AQUA, lw=3.6, solid_capstyle="round",
            zorder=3)
    ax.scatter([e], [ys[-1]], s=120, color=AQUA, zorder=5)
    ax.text(hi + 1.2, ys[-1], f"{e:+.1f}%", fontsize=10.5, va="center", color=INK,
            weight="bold")
    ax.axvline(-12.0, color=INK, lw=2, ls="--", zorder=6)
    ax.text(-12.5, -0.78, "the truth, common to all four ", fontsize=9.5, color=INK,
            ha="right")
    ax.text(18, 1.7, f"test of a common effect\nchi squared {lr:.2f} on 3 df, p = {pv:.3f}",
            fontsize=10, color=AQUA)
    ax.set_yticks(ys)
    ax.set_yticklabels([SHORT[a] for a in NO_A007] + ["pooled, one common effect"],
                       fontsize=9.5)
    ax.set_xlim(-46, 40)
    ax.set_ylim(-1.0, len(NO_A007) + 0.6)
    ax.set_xlabel("estimated change in the use of force rate")
    style(ax, ygrid=False)
    ax.grid(axis="x", color=GRID, lw=0.8, zorder=0)
    ax.set_axisbelow(True)
    title(ax, "Four estimates spanning 12 points, of one identical effect",
          "The spread is what four noisy estimates of the same number look like.")
    fig.tight_layout()
    fig.savefig(HERE / "fig_a15_heterogeneous.png", dpi=150)
    plt.close(fig)


def fig_16():
    """Module 16. Every design this series tried, and what survived."""
    d = panel()
    dall = panel(drop_a007=False)
    tb = rate(F[F["agency_id"].isin(TREATED) & (F["period"] == "before")])
    ta = rate(F[F["agency_id"].isin(TREATED) & (F["period"] == "after")])

    rows = [
        ("before and after", 100 * (ta / tb - 1), ORANGE, "no comparison group"),
        ("regression discontinuity", None, ORANGE, "two agencies near the cutoff"),
        ("instrumental variables", None, ORANGE, "strongest first stage F is 1.6"),
        ("synthetic control", None, ORANGE, "pre period fit error 25 to 48 percent"),
        ("propensity score", None, ORANGE, "four percent overlap, two units survive trimming"),
        ("difference in differences,\nall five treated", _did_all(dall), ORANGE,
         "one agency on its own pre trend"),
        ("difference in differences,\nchecked", fit(d, NO_A007)[0], AQUA,
         "reported, with its interval and its caveats"),
    ]
    # the regression discontinuity jump, converted to a proportional statement
    CUT = 3.159
    X = _profile_frame()
    X["above"] = (X["pre_program_uof_per_100_arrests"] > CUT).astype(int)
    X["post_rate"] = F[F["period"] == "after"].groupby("agency_id").apply(
        lambda g: 100 * g["n_uof"].sum() / g["n_arrests"].sum())
    ins = X[np.abs(X["pre_program_uof_per_100_arrests"] - CUT) < 0.80]
    zr = sm.OLS(ins["post_rate"],
                sm.add_constant(ins[["above",
                                     "pre_program_uof_per_100_arrests"]])).fit()
    rd = 100 * zr.params["above"] / CUT
    stand = {"regression discontinuity": rd, "instrumental variables": -22.8,
             "synthetic control": -25.1, "propensity score": None}

    fig, ax = plt.subplots(figsize=(13.0, 5.6))
    ys = np.arange(len(rows))[::-1]
    for (lab, e, c, note), yy in zip(rows, ys):
        if e is None:
            e = stand.get(lab)
        if e is None:
            ax.text(-1.5, yy, "no estimate is defensible", fontsize=9.5,
                    color=INK3, style="italic", ha="right", va="center")
        else:
            ax.barh(yy, e, color=c, height=0.34, zorder=3)
            off = -0.9 if e < 0 else 0.9
            ha = "right" if e < 0 else "left"
            ax.text(e + off, yy, f"{e:+.1f}%", ha=ha, va="center", fontsize=10.5,
                    color=INK, weight="bold")
        ax.text(42, yy, note, fontsize=8.5, color=INK2, va="center")
    ax.axvline(-12.0, color=INK, lw=2, ls="--", zorder=6)
    ax.text(-12.4, -0.82, "the truth ", fontsize=9.5, color=INK, ha="right")
    ax.axvline(0, color=INK3, lw=1.2, zorder=2)
    ax.set_yticks(ys)
    ax.set_yticklabels([r[0] for r in rows], fontsize=9.5)
    ax.set_xlim(-47, 92)
    ax.set_ylim(-1.05, len(rows) - 0.3)
    ax.set_xticks([-40, -20, 0, 20, 40])
    ax.set_xlabel("what each design reported")
    style(ax, ygrid=False)
    ax.grid(axis="x", color=GRID, lw=0.8, zorder=0)
    ax.set_axisbelow(True)
    title(ax, "Seven designs, one 12 percent effect, one defensible answer",
          "Four of the seven had no business being run, and each says so in one diagnostic.")
    fig.tight_layout()
    fig.savefig(HERE / "fig_a16_the_causal_claim.png", dpi=150)
    plt.close(fig)


def _did_all(dall):
    return fit(dall, TREATED)[0]


if __name__ == "__main__":
    for fn in (fig_01, fig_02, fig_03, fig_04,
               fig_05, fig_06, fig_07, fig_08, fig_09,
               fig_10, fig_11, fig_12,
               fig_13, fig_14, fig_15, fig_16):
        fn()
        print("built", fn.__name__)
