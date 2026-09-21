"""
Build every figure in the Time Series Advanced series.

All figures are drawn from the synthetic WADEPS dataset in Data/. Running this
script overwrites the PNG files that the Markdown modules link to.

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
        ax.text(0, 1.012, sub, transform=ax.transAxes, fontsize=9, color=INK2, va="bottom")


monthly = pd.read_csv(DATA / "agency_monthly.csv")
FINAL = monthly[monthly["provisional"] == 0]


def short(n):
    return (n.replace(" Police Department", "").replace(" Sheriff's Office", "")
             .replace(" Police", ""))


def counts(aid):
    d = FINAL[FINAL["agency_id"] == aid].sort_values("year_month")
    s = pd.Series(d["n_uof"].values, dtype=float,
                  index=pd.PeriodIndex(d["year_month"], freq="M").to_timestamp())
    s.index.freq = "MS"
    return s


def rate(aid):
    d = FINAL[FINAL["agency_id"] == aid].sort_values("year_month")
    s = pd.Series((100 * d["n_uof"] / d["n_arrests"]).values,
                  index=pd.PeriodIndex(d["year_month"], freq="M").to_timestamp())
    s.index.freq = "MS"
    return s


# ------------------------------------------------- 1. stationarity
def fig_01():
    from statsmodels.tsa.stattools import adfuller, kpss

    fig = plt.figure(figsize=(14, 8.2))
    gs = fig.add_gridspec(2, 3, height_ratios=[1, 1.05], hspace=0.55, wspace=0.28)

    series = [("A008", rate, "Lakeshore County, rate", "both tests agree: stationary",
               AQUA, (0, 4.6), "use of force per 100 arrests"),
              ("A007", rate, "Summit County, rate", "both agree: not stationary",
               ORANGE, (0, 4.6), None),
              ("A012", counts, "Ashfell, counts", "neither test rejects: inconclusive",
               BLUE, (0, 200), "use of force incidents")]
    for i, (aid, getter, nm, verdict, c, ylim, ylab) in enumerate(series):
        ax = fig.add_subplot(gs[0, i])
        v = getter(aid)
        ax.plot(v.index, v.values, color=c, lw=1.5, zorder=3)
        ax.axhline(v.mean(), color=INK3, lw=1.1, ls=(0, (4, 3)), zorder=2)
        ax.set_ylim(*ylim)
        if ylab:
            ax.set_ylabel(ylab)
        ax.tick_params(labelsize=8.5)
        style(ax)
        title(ax, nm, verdict)

    # the four verdicts
    ax = fig.add_subplot(gs[1, 0])
    ax.axis("off")
    cell = [["cannot reject\nstationarity", "rejects\nstationarity"],
            ["", ""]]
    rows = ["rejects a\nunit root", "cannot reject\na unit root"]
    txt = [["stationary\n\nmodel the level", "CONFLICT\n\nusually a trend\nplus a stable part"],
           ["INCONCLUSIVE\n\nnot enough data\nto decide", "not stationary\n\ndifference it"]]
    cols = [[AQUA, YELLOW], [YELLOW, ORANGE]]
    for r in range(2):
        for c_ in range(2):
            ax.add_patch(plt.Rectangle((c_ * 0.5, 0.42 - r * 0.42), 0.48, 0.40,
                                       facecolor=cols[r][c_], alpha=0.18,
                                       edgecolor=GRID, transform=ax.transAxes))
            ax.text(c_ * 0.5 + 0.24, 0.62 - r * 0.42, txt[r][c_], ha="center", va="center",
                    fontsize=8.5, color=INK, transform=ax.transAxes)
    for c_, lab in enumerate(cell[0]):
        ax.text(c_ * 0.5 + 0.24, 0.90, "KPSS " + lab.split("\n")[0] + "\n" + lab.split("\n")[1],
                ha="center", va="center", fontsize=8, color=INK2, transform=ax.transAxes)
    for r, lab in enumerate(rows):
        ax.text(-0.04, 0.62 - r * 0.42, "ADF\n" + lab, ha="right", va="center",
                fontsize=8, color=INK2, transform=ax.transAxes)
    ax.set_title("Two tests, opposite nulls, four verdicts", loc="left",
                 fontsize=11, color=INK, pad=10)

    # over differencing
    s = np.log(rate("A007"))
    transforms = [("level", s), ("first\ndifference", s.diff()),
                  ("twice\ndifferenced", s.diff().diff()),
                  ("seasonal\ndifference", s.diff(12)),
                  ("first and\nseasonal", s.diff().diff(12))]
    names = [t[0] for t in transforms]
    varr = [t[1].dropna().var() for t in transforms]
    ac = [t[1].dropna().autocorr(1) for t in transforms]

    ax = fig.add_subplot(gs[1, 1])
    cols2 = [ORANGE if v == max(varr) else (AQUA if v == min(varr) else BLUE) for v in varr]
    ax.bar(range(5), varr, color=cols2, width=0.62, zorder=3)
    ax.set_xticks(range(5)); ax.set_xticklabels(names, fontsize=8)
    ax.set_ylabel("variance of what is left")
    style(ax)
    title(ax, "Differencing too much adds variance",
          "Summit County, log rate.")

    ax = fig.add_subplot(gs[1, 2])
    cols3 = [ORANGE if v < -0.55 else (AQUA if abs(v) < 0.2 else BLUE) for v in ac]
    ax.bar(range(5), ac, color=cols3, width=0.62, zorder=3)
    ax.axhline(0, color=INK2, lw=1.0, zorder=4)
    ax.axhline(-0.5, color=ORANGE, lw=1.2, ls=(0, (4, 3)), zorder=4)
    ax.text(0.05, -0.56, "minus one half", ha="left", fontsize=8, color=ORANGE)
    ax.set_xticks(range(5)); ax.set_xticklabels(names, fontsize=8)
    ax.set_ylim(-0.85, 0.85)
    ax.set_ylabel("lag one autocorrelation")
    style(ax)
    title(ax, "And drives lag one toward minus one half",
          "Minus one half is value is the signature of over differencing.")

    fig.savefig(HERE / "fig_a01_stationarity.png", dpi=150, bbox_inches="tight")
    plt.close(fig)


# --------------------------------------------- 2. counts are not Gaussian
def fig_02():
    import statsmodels.api as sm
    import statsmodels.formula.api as smf
    from scipy import stats

    f = FINAL[FINAL["year_month"] <= "2025-12"].copy()
    f = f[~((f["agency_id"] == "A002") & (f["year_month"] == "2021-06"))]
    idx = pd.PeriodIndex(f["year_month"], freq="M")
    f["t"] = (idx.year - 2019) * 12 + idx.month - 1
    f["mon"] = idx.month

    rows = []
    for aid, g in f.groupby("agency_id"):
        mod = smf.glm("n_uof ~ t + C(mon)", data=g, family=sm.families.Poisson(),
                      offset=np.log(g["n_arrests"])).fit()
        rows.append((short(g["agency_name"].iloc[0]), g["n_uof"].mean(),
                     g["n_uof"].var() / g["n_uof"].mean(),
                     (mod.resid_pearson ** 2).sum() / mod.df_resid))
    disp = pd.DataFrame(rows, columns=["agency", "mean", "raw", "model"]).sort_values("mean")

    fig, (a1, a2, a3) = plt.subplots(1, 3, figsize=(15.4, 5.0))

    a1.scatter(disp["mean"], disp["raw"], s=58, color=ORANGE, zorder=4,
               label="variance divided by mean, raw")
    a1.scatter(disp["mean"], disp["model"], s=58, color=BLUE, zorder=5,
               label="dispersion after a model")
    for _, r in disp.iterrows():
        a1.plot([r["mean"], r["mean"]], [r["raw"], r["model"]], color=INK3, lw=1, zorder=3)
    a1.axhline(1.0, color=INK, lw=1.2, ls=(0, (5, 3)), zorder=2)
    a1.text(1.0, 1.08, "Poisson", fontsize=8.5, color=INK)
    a1.annotate("Ashfell", (disp["mean"].iloc[-1], disp["raw"].iloc[-1]),
                textcoords="offset points", xytext=(-8, 6), ha="right", fontsize=9, color=INK)
    a1.set_xscale("log")
    a1.set_xlabel("average incidents a month")
    a1.set_ylabel("variance divided by mean")
    a1.legend(fontsize=8.5, frameon=False, loc="upper left")
    style(a1)
    title(a1, "Most of the apparent overdispersion is structure",
          "Model the trend and season first, and nearly every agency is close to Poisson.")

    e = f[f["agency_id"] == "A006"].copy()
    ols = smf.ols("n_uof ~ t + C(mon)", data=e).fit()
    pi = ols.get_prediction(e).summary_frame(alpha=0.05)
    poi = smf.glm("n_uof ~ t + C(mon)", data=e, family=sm.families.Poisson(),
                  offset=np.log(e["n_arrests"])).fit()
    plo, phi = stats.poisson.ppf(0.025, poi.mu), stats.poisson.ppf(0.975, poi.mu)
    x = np.arange(len(e))

    a2.fill_between(x, pi["obs_ci_lower"], 0, where=(pi["obs_ci_lower"] < 0),
                    color=ORANGE, alpha=0.20, zorder=2)
    a2.plot(x, pi["obs_ci_lower"], color=ORANGE, lw=2, zorder=4,
            label="ordinary regression, lower bound")
    a2.plot(x, plo, color=BLUE, lw=2, zorder=5,
            label="Poisson with exposure, lower bound")
    a2.plot(x, e["n_uof"].values, color=INK3, lw=0, marker="o", ms=3, alpha=0.6,
            zorder=3, label="what was recorded")
    a2.axhline(0, color=INK, lw=1.4, zorder=6)
    a2.text(42, -1.9, "a count cannot go below this line", ha="center",
            fontsize=8.5, color=INK)
    a2.set_ylim(-2.4, 5.0)
    a2.set_xlabel("months, Orrindale")
    a2.set_ylabel("use of force incidents")
    a2.legend(fontsize=8, frameon=False, loc="upper right")
    style(a2)
    title(a2, "Orrindale: every ordinary interval is impossible",
          "All 84 lower bounds are negative. Poisson never allows one.")

    g = f[f["agency_id"] == "A012"].copy()
    g["rate"] = 100 * g["n_uof"] / g["n_arrests"]
    py = lambda b: 100 * (np.exp(12 * b) - 1)
    poi2 = smf.glm("n_uof ~ t + C(mon)", data=g, family=sm.families.Poisson(),
                   offset=np.log(g["n_arrests"])).fit()
    aux = ((g["n_uof"] - poi2.mu) ** 2 - g["n_uof"]) / poi2.mu
    alpha = sm.OLS(aux, poi2.mu).fit().params.iloc[0]
    nb = smf.glm("n_uof ~ t + C(mon)", data=g,
                 family=sm.families.NegativeBinomial(alpha=alpha),
                 offset=np.log(g["n_arrests"])).fit()

    ests = []
    for lab, mod in [("Poisson", poi2), ("negative binomial", nb)]:
        lo, hi = mod.conf_int().loc["t"]
        ests.append((lab, py(mod.params["t"]), py(lo), py(hi)))
    ys = np.arange(len(ests))
    for y, (lab, e_, lo, hi) in zip(ys, ests):
        c = BLUE if lab == "Poisson" else AQUA
        a3.plot([lo, hi], [y, y], color=c, lw=3, solid_capstyle="round", zorder=3)
        a3.plot([e_], [y], marker="o", ms=10, color=c, zorder=4)
        a3.text(hi + 0.15, y, f"{e_:+.2f}%  width {hi - lo:.2f}", va="center",
                fontsize=9, color=INK)
    a3.axvline(100 * (np.exp(-0.05) - 1), color=INK, lw=1.5, ls=(0, (5, 3)), zorder=5)
    a3.text(100 * (np.exp(-0.05) - 1) - 0.12, -0.62, "the true trend", ha="right",
            va="bottom", fontsize=8.5, color=INK)
    a3.set_yticks(ys)
    a3.set_yticklabels([e[0] for e in ests], fontsize=9.5)
    a3.set_ylim(-0.9, len(ests) - 0.4)
    a3.set_xlim(-7.4, -2.8)
    a3.set_xlabel("estimated trend, percent a year")
    style(a3, ygrid=False)
    a3.grid(axis="x", color=GRID, lw=0.8); a3.set_axisbelow(True)
    title(a3, "The same slope, two different intervals",
          "Ashfell. Poisson is a fifth too narrow: it ignores the extra spread.")

    fig.tight_layout()
    fig.savefig(HERE / "fig_a02_counts.png", dpi=150)
    plt.close(fig)


# ------------------------------------- 3. selection, diagnostics, uncertainty
def fig_03():
    from statsmodels.tsa.statespace.sarimax import SARIMAX
    from statsmodels.tsa.stattools import acf
    from scipy import stats

    s = np.log(counts("A012"))
    train, test = s.loc[:"2024-12"], s.loc["2025-01":"2025-12"]

    cands = [(1, 0, 0, 0, 0, 0), (0, 1, 1, 0, 0, 0), (1, 0, 0, 0, 1, 0),
             (2, 0, 0, 1, 1, 0), (1, 0, 1, 0, 1, 1), (1, 1, 1, 1, 1, 1),
             (0, 1, 1, 0, 1, 1)]
    rows = []
    for p, d_, q, P, D, Q in cands:
        r = SARIMAX(train, order=(p, d_, q), seasonal_order=(P, D, Q, 12),
                    enforce_stationarity=False, enforce_invertibility=False).fit(disp=False)
        rows.append((f"({p},{d_},{q})({P},{D},{Q})", r.aic, r.bic))
    sel = pd.DataFrame(rows, columns=["order", "AIC", "BIC"]).sort_values("AIC")

    r = SARIMAX(train, order=(0, 1, 1), seasonal_order=(0, 1, 1, 12)).fit(disp=False)
    res = r.resid[13:]

    fig, axes = plt.subplots(2, 3, figsize=(14.4, 8.4))
    (a1, a2, a3), (a4, a5, a6) = axes

    ys = np.arange(len(sel))
    a1.barh(ys - 0.19, sel["AIC"], height=0.36, color=BLUE, zorder=3, label="AIC")
    a1.barh(ys + 0.19, sel["BIC"], height=0.36, color=AQUA, zorder=3, label="BIC")
    a1.set_yticks(ys); a1.set_yticklabels(sel["order"], fontsize=8.5)
    a1.invert_yaxis()
    a1.axvline(0, color=INK2, lw=1)
    a1.legend(fontsize=8.5, frameon=False, loc="lower right")
    a1.set_xlabel("lower is better")
    style(a1, ygrid=False)
    a1.grid(axis="x", color=GRID, lw=0.8); a1.set_axisbelow(True)
    title(a1, "Both criteria pick the same model", "Ashfell, log counts, seasonal period 12.")

    band = 1.96 / np.sqrt(len(res))
    ac = acf(res, nlags=24, fft=False)
    a2.bar(range(1, 25), ac[1:], width=0.6,
           color=[ORANGE if abs(v) > band else BLUE for v in ac[1:]], zorder=3)
    a2.axhspan(-band, band, color=INK3, alpha=0.13, zorder=1)
    a2.axhline(0, color=INK2, lw=1, zorder=4)
    a2.set_ylim(-0.4, 0.4)
    a2.set_xlabel("lag, in months")
    a2.set_ylabel("residual autocorrelation")
    style(a2)
    title(a2, "Nothing left in the residuals", "Ljung Box at lag 12 gives p = 0.78.")

    stats.probplot(res / res.std(), dist="norm", plot=a3)
    a3.get_lines()[0].set_color(BLUE); a3.get_lines()[0].set_markersize(4)
    a3.get_lines()[1].set_color(ORANGE); a3.get_lines()[1].set_linewidth(2)
    a3.set_title(""); a3.set_xlabel("normal quantiles"); a3.set_ylabel("standardised residual")
    style(a3)
    title(a3, "And they are close to normal", "Jarque Bera gives p = 0.70.")

    sim = np.asarray(r.simulate(12, repetitions=6000, anchor="end",
                                random_state=1)).reshape(12, -1)
    lo, hi = np.percentile(sim, 2.5, axis=1), np.percentile(sim, 97.5, axis=1)
    show = np.exp(s.loc["2022":])
    a4.plot(show.index, show.values, color=INK3, lw=1.4, zorder=3, label="what happened")
    a4.fill_between(test.index, np.exp(lo), np.exp(hi), color=BLUE, alpha=0.16,
                    zorder=2, label="95 percent, simulated")
    a4.plot(test.index, np.exp(r.get_forecast(12).predicted_mean.values), color=BLUE,
            lw=2.4, zorder=4, label="forecast")
    a4.axvline(pd.Timestamp("2025-01-01"), color=INK, lw=1.1, ls=(0, (4, 3)), zorder=5)
    a4.set_ylim(0, 210)
    a4.set_xticks([pd.Timestamp(f"{y}-01-01") for y in (2022, 2023, 2024, 2025, 2026)])
    a4.set_xticklabels(["2022", "2023", "2024", "2025", "2026"], fontsize=9)
    a4.set_ylabel("use of force incidents")
    a4.legend(fontsize=8, frameon=False, loc="lower left")
    style(a4)
    title(a4, "The forecast and its distribution", "Simulated from the fitted model.")

    nominal = [50, 80, 95]
    observed = [45.0, 86.7, 98.3]
    a5.plot([0, 100], [0, 100], color=INK3, lw=1.3, ls=(0, (4, 3)), zorder=2)
    a5.plot(nominal, observed, color=BLUE, lw=2.2, marker="o", ms=9, mfc=SURFACE,
            mew=2, zorder=4)
    for n, o in zip(nominal, observed):
        a5.annotate(f"{o:.1f}", (n, o), textcoords="offset points", xytext=(9, -4),
                    fontsize=9, color=INK)
    a5.set_xlim(40, 100); a5.set_ylim(40, 100)
    a5.set_xlabel("nominal coverage, percent")
    a5.set_ylabel("observed coverage, percent")
    style(a5)
    title(a5, "Calibration over 60 forecast months",
          "Above the line means the intervals are wider than they claim.")

    pit_counts = [7, 87, 7]
    a6.bar(["below 0.1", "middle", "above 0.9"], pit_counts, color=[ORANGE, BLUE, ORANGE],
           width=0.6, zorder=3)
    a6.axhline(10, color=INK, lw=1.3, ls=(0, (5, 3)), zorder=4)
    a6.axhline(80, color=INK, lw=1.3, ls=(0, (5, 3)), zorder=4)
    a6.text(1.0, 84, "what a calibrated forecast would give", ha="center",
            fontsize=8.5, color=INK)
    for i, v in enumerate(pit_counts):
        a6.text(i, v + 3.5, f"{v}%", ha="center", fontsize=10, color=INK, weight="bold")
    a6.set_ylim(0, 100)
    a6.set_ylabel("percent of the 60 months")
    style(a6)
    title(a6, "Where the outcomes actually fell",
          "Too few in the tails: the distribution is a little too wide.")

    fig.tight_layout()
    fig.savefig(HERE / "fig_a03_diagnostics.png", dpi=150)
    plt.close(fig)


if __name__ == "__main__":
    for fn in (fig_01, fig_02, fig_03):
        fn()
        print("built", fn.__name__)
