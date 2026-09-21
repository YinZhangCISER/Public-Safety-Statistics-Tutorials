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


CAL = pd.period_range("2019-01", "2026-04", freq="M").to_timestamp()


def series(aid, col="n_uof"):
    """Reindexed to a complete calendar, so the gap shows as missing."""
    d = FINAL[FINAL["agency_id"] == aid].sort_values("year_month")
    s = pd.Series(d[col].values, dtype=float,
                  index=pd.PeriodIndex(d["year_month"], freq="M").to_timestamp())
    s = s.reindex(CAL)
    s.index.freq = "MS"
    return s


# ------------------------------------------------ 4. ARIMA end to end
def fig_04():
    from statsmodels.tsa.statespace.sarimax import SARIMAX
    from statsmodels.tsa.stattools import acf, pacf
    from statsmodels.stats.diagnostic import acorr_ljungbox

    s = np.log(series("A004"))                 # Millgate, the weakest season
    train, test = s.loc[:"2024-12"], s.loc["2025-01":"2025-12"]
    d1 = train.diff().dropna()

    fig, axes = plt.subplots(2, 2, figsize=(13.4, 8.2))
    (a1, a2), (a3, a4) = axes

    a1.plot(np.exp(s).index, np.exp(s).values, color=BLUE, lw=1.5, zorder=3)
    a1.set_ylabel("use of force incidents")
    a1.set_ylim(0, 22)
    style(a1)
    title(a1, "Millgate, the least seasonal agency",
          "ADF rejects a unit root and KPSS rejects stationarity: the conflict case.")

    band = 1.96 / np.sqrt(len(d1))
    a_v, p_v = acf(d1, nlags=14, fft=False), pacf(d1, nlags=14)
    x = np.arange(1, 15)
    a2.bar(x - 0.2, a_v[1:15], width=0.38, color=BLUE, zorder=3, label="ACF")
    a2.bar(x + 0.2, p_v[1:15], width=0.38, color=AQUA, zorder=3, label="PACF")
    a2.axhspan(-band, band, color=INK3, alpha=0.13, zorder=1)
    a2.axhline(0, color=INK2, lw=1, zorder=4)
    a2.annotate("one big spike in the ACF,\na decaying PACF: a moving\naverage term of order one",
                (1, a_v[1]), textcoords="offset points", xytext=(28, -14),
                fontsize=8.5, color=INK,
                arrowprops=dict(arrowstyle="->", lw=0.9, color=INK2))
    a2.set_ylim(-0.75, 0.45)
    a2.set_xlabel("lag, in months")
    a2.legend(fontsize=8.5, frameon=False, loc="lower right")
    style(a2)
    title(a2, "After one difference, the order is readable",
          "This is what identification means: the picture names the model.")

    orders = [(0, 0, 0), (1, 0, 0), (2, 0, 0), (1, 0, 1), (1, 1, 0), (1, 1, 1), (0, 1, 1)]
    rows = []
    for o in orders:
        r = SARIMAX(train, order=o, seasonal_order=(0, 0, 0, 0),
                    trend="c" if o[1] == 0 else "n",
                    enforce_stationarity=False, enforce_invertibility=False).fit(disp=False)
        rows.append({"order": str(o), "AIC": r.aic,
                     "MAE": float(np.mean(np.abs(np.exp(test.values)
                                                 - np.exp(r.forecast(12).values))))})
    sel = pd.DataFrame(rows)

    a3.scatter(sel["AIC"], sel["MAE"], s=64, color=BLUE, zorder=4)
    nudge = {"(1, 0, 1)": (7, -13), "(0, 0, 0)": (7, 4), "(2, 0, 0)": (-7, 6),
             "(1, 1, 0)": (-8, 4)}
    for _, r in sel.iterrows():
        off = nudge.get(r["order"], (7, 4))
        a3.annotate(r["order"], (r["AIC"], r["MAE"]), textcoords="offset points",
                    xytext=off, fontsize=8.5, color=INK,
                    ha="right" if off[0] < 0 else "left")
    best_aic = sel.loc[sel["AIC"].idxmin()]
    best_mae = sel.loc[sel["MAE"].idxmin()]
    a3.scatter([best_aic["AIC"]], [best_aic["MAE"]], s=150, facecolors="none",
               edgecolors=ORANGE, linewidths=2, zorder=5)
    a3.scatter([best_mae["AIC"]], [best_mae["MAE"]], s=150, facecolors="none",
               edgecolors=AQUA, linewidths=2, zorder=5)
    a3.axhline(4.08, color=INK3, lw=1.3, ls=(0, (5, 3)), zorder=2)
    a3.text(100.2, 4.14, "the seasonal naive baseline", ha="left", fontsize=8.5, color=INK2)
    a3.set_xlabel("AIC, lower is better")
    a3.set_ylabel("forecast error in 2025, incidents a month")
    a3.set_ylim(2.0, 4.6)
    style(a3)
    title(a3, "The best fit is not the best forecast",
          "Orange ring: lowest AIC. Green ring: lowest forecast error.")

    ash = np.log(series("A012")).loc[:"2024-12"]
    checks = []
    for lab, o, so in [("ARIMA(1,1,1)", (1, 1, 1), (0, 0, 0, 0)),
                       ("ARIMA(2,1,2)", (2, 1, 2), (0, 0, 0, 0)),
                       ("SARIMA(0,1,1)(0,1,1)", (0, 1, 1), (0, 1, 1, 12))]:
        r = SARIMAX(ash, order=o, seasonal_order=so, enforce_stationarity=False,
                    enforce_invertibility=False).fit(disp=False)
        res = r.resid[13:]
        checks.append((lab,
                       acorr_ljungbox(res, lags=[12], return_df=True)["lb_pvalue"].iloc[0],
                       acorr_ljungbox(res, lags=[24], return_df=True)["lb_pvalue"].iloc[0]))
    ys = np.arange(len(checks))
    a4.barh(ys - 0.19, [c[1] for c in checks], height=0.36, color=BLUE, zorder=3,
            label="Ljung Box at lag 12")
    a4.barh(ys + 0.19, [c[2] for c in checks], height=0.36, color=AQUA, zorder=3,
            label="Ljung Box at lag 24")
    a4.axvline(0.05, color=ORANGE, lw=1.6, ls=(0, (5, 3)), zorder=5)
    a4.text(0.07, -0.62, "below this the model is not finished", fontsize=8.5, color=ORANGE)
    a4.set_yticks(ys); a4.set_yticklabels([c[0] for c in checks], fontsize=9)
    a4.set_ylim(-0.9, len(checks) - 0.4)
    a4.set_xlim(0, 1)
    a4.set_xlabel("p value")
    a4.legend(fontsize=8.5, frameon=False, loc="lower right")
    style(a4, ygrid=False)
    a4.grid(axis="x", color=GRID, lw=0.8); a4.set_axisbelow(True)
    title(a4, "Ashfell: what a missing seasonal term looks like",
          "No amount of non seasonal complexity rescues it.")

    fig.tight_layout()
    fig.savefig(HERE / "fig_a04_arima.png", dpi=150)
    plt.close(fig)


# ---------------------------------------------------------- 5. SARIMA
def fig_05():
    from statsmodels.tsa.statespace.sarimax import SARIMAX
    from statsmodels.tsa.stattools import acf, pacf
    from statsmodels.stats.diagnostic import acorr_ljungbox

    s = np.log(series("A012"))
    train = s.loc[:"2024-12"]
    D12 = train.diff(12).dropna()

    fig, (a1, a2, a3) = plt.subplots(1, 3, figsize=(14.4, 4.9))

    band = 1.96 / np.sqrt(len(D12))
    a_v, p_v = acf(D12, nlags=26, fft=False), pacf(D12, nlags=26)
    x = np.arange(1, 27)
    a1.bar(x - 0.2, a_v[1:27], width=0.38, color=BLUE, zorder=3, label="ACF")
    a1.bar(x + 0.2, p_v[1:27], width=0.38, color=AQUA, zorder=3, label="PACF")
    a1.axhspan(-band, band, color=INK3, alpha=0.13, zorder=1)
    a1.axhline(0, color=INK2, lw=1, zorder=4)
    for lag in (12, 24):
        a1.axvline(lag, color=ORANGE, lw=1, ls=(0, (3, 3)), zorder=2)
    a1.text(12.4, 0.30, "lag 12", fontsize=8.5, color=ORANGE)
    a1.set_xlabel("lag, in months")
    a1.set_ylim(-0.55, 0.4)
    a1.legend(fontsize=8.5, frameon=False, loc="lower right")
    style(a1)
    title(a1, "Look at the seasonal lags, not just the first few",
          "Ashfell after one seasonal difference. Something is left at 12.")

    cands = [((0, 1, 1), (0, 1, 1, 12)), ((1, 1, 1), (0, 1, 1, 12)),
             ((0, 1, 1), (1, 1, 1, 12)), ((0, 1, 1), (2, 1, 0, 12)),
             ((0, 1, 1), (0, 1, 2, 12)), ((0, 1, 1), (1, 1, 0, 12))]
    rows = []
    for o, so in cands:
        r = SARIMAX(train, order=o, seasonal_order=so, enforce_stationarity=False,
                    enforce_invertibility=False).fit(disp=False)
        res = r.resid[13:]
        rows.append({"order": f"{o}\n{so[:3]} at 12", "AIC": r.aic,
                     "p": acorr_ljungbox(res, lags=[24], return_df=True)["lb_pvalue"].iloc[0],
                     "k": len(r.params)})
    sel = pd.DataFrame(rows).sort_values("AIC")

    ys = np.arange(len(sel))
    cols = [AQUA if i == 0 else BLUE for i in range(len(sel))]
    a2.barh(ys, sel["AIC"], color=cols, height=0.6, zorder=3)
    for y, (_, r) in zip(ys, sel.iterrows()):
        mark = "" if r["p"] > 0.05 else "   fails Ljung Box"
        a2.text(r["AIC"] - 0.4, y, f"{r['AIC']:.1f}{mark}", va="center", ha="right",
                fontsize=8.5, color=INK)
    a2.set_yticks(ys); a2.set_yticklabels(sel["order"], fontsize=8)
    a2.invert_yaxis()
    a2.set_xlim(-15.5, 1)
    a2.set_xlabel("AIC, lower is better")
    style(a2, ygrid=False)
    a2.grid(axis="x", color=GRID, lw=0.8); a2.set_axisbelow(True)
    title(a2, "Six seasonal orders", "The simplest one wins on fit and on diagnostics.")

    labels = ["chosen by reading\nthe ACF and PACF", "chosen by\nauto_arima"]
    aics = [-12.2, -8.5]
    a3.bar(labels, aics, color=[AQUA, ORANGE], width=0.5, zorder=3)
    for i, v in enumerate(aics):
        a3.text(i, v - 0.6, f"{v}", ha="center", fontsize=11, color=INK, weight="bold")
    a3.axhline(0, color=INK2, lw=1, zorder=4)
    a3.set_ylim(-16, 2)
    a3.set_ylabel("AIC, lower is better")
    a3.tick_params(labelsize=9)
    style(a3)
    title(a3, "Automatic selection is not always better",
          "A stepwise search settled for a worse model than the manual read.")

    fig.tight_layout()
    fig.savefig(HERE / "fig_a05_sarima.png", dpi=150)
    plt.close(fig)


# ------------------------------------------ 6. regression with ARMA errors
def fig_06():
    from statsmodels.tsa.statespace.sarimax import SARIMAX
    from statsmodels.tsa.stattools import acf
    from statsmodels.stats.diagnostic import acorr_ljungbox
    import statsmodels.formula.api as smf

    g = FINAL[(FINAL["agency_id"] == "A001") & (FINAL["year_month"] <= "2025-12")].sort_values("year_month")
    y = pd.Series(np.log(g["n_uof"].values),
                  index=pd.PeriodIndex(g["year_month"], freq="M").to_timestamp())
    y.index.freq = "MS"
    X = pd.DataFrame({"log_arrests": np.log(g["n_arrests"].values),
                      "programme": (g["year_month"] >= "2023-11").astype(float).values},
                     index=y.index)

    ols = smf.ols("y ~ log_arrests + programme", data=X.assign(y=y.values)).fit()
    arma = SARIMAX(y, exog=X, order=(0, 0, 1), seasonal_order=(0, 1, 1, 12)).fit(disp=False)

    fig, (a1, a2, a3) = plt.subplots(1, 3, figsize=(14.4, 4.9))

    band = 1.96 / np.sqrt(len(y))
    for ax, res, name, p in [(a1, ols.resid, "ordinary least squares",
                              acorr_ljungbox(ols.resid, lags=[12], return_df=True)["lb_pvalue"].iloc[0]),
                             (a2, arma.resid[13:], "regression with ARMA errors",
                              acorr_ljungbox(arma.resid[13:], lags=[12], return_df=True)["lb_pvalue"].iloc[0])]:
        a_v = acf(res, nlags=24, fft=False)
        ax.bar(range(1, 25), a_v[1:],
               color=[ORANGE if abs(v) > band else BLUE for v in a_v[1:]],
               width=0.6, zorder=3)
        ax.axhspan(-band, band, color=INK3, alpha=0.13, zorder=1)
        ax.axhline(0, color=INK2, lw=1, zorder=4)
        ax.set_ylim(-0.6, 0.6)
        ax.set_xlabel("lag, in months")
        ax.set_ylabel("residual autocorrelation")
        style(ax)
        title(ax, name, f"Ljung Box at lag 12 gives p = {p:.4f}")

    ests = [("ordinary least squares", ols, ORANGE),
            ("regression with ARMA errors", arma, BLUE)]
    ys = np.arange(len(ests))
    for yv, (lab, mod, c) in zip(ys, ests):
        b = mod.params["programme"]
        lo, hi = mod.conf_int().loc["programme"]
        pc = lambda v: 100 * (np.exp(v) - 1)
        a3.plot([pc(lo), pc(hi)], [yv, yv], color=c, lw=3, solid_capstyle="round", zorder=3)
        a3.plot([pc(b)], [yv], marker="o", ms=10, color=c, zorder=4)
        a3.text(pc(hi) + 1.2, yv, f"{pc(b):+.1f}%", va="center", fontsize=9.5, color=INK)
        a3.text(-34, yv + 0.30, f"{lab}, exposure coefficient {mod.params['log_arrests']:+.2f}",
                va="bottom", ha="left", fontsize=8.5, color=INK2)
    a3.axvline(-12.0, color=INK, lw=1.6, ls=(0, (5, 3)), zorder=5)
    a3.text(-12.5, -0.75, "the true effect", ha="right", va="bottom", fontsize=8.5, color=INK)
    a3.axvline(0, color=INK2, lw=1, zorder=2)
    a3.set_yticks([])
    a3.set_ylim(-1.05, len(ests) - 0.35)
    a3.set_xlim(-35, 14)
    a3.set_xlabel("estimated programme effect, percent")
    style(a3, ygrid=False)
    a3.grid(axis="x", color=GRID, lw=0.8); a3.set_axisbelow(True)
    title(a3, "Same data, same regressors, different errors",
          "Ignoring the correlation gives a confident answer that is twice the truth.")

    fig.tight_layout()
    fig.savefig(HERE / "fig_a06_arma_errors.png", dpi=150)
    plt.close(fig)


# --------------------------------------------- 7. state space and gaps
def fig_07():
    from statsmodels.tsa.statespace.sarimax import SARIMAX
    from statsmodels.tsa.holtwinters import ExponentialSmoothing
    from statsmodels.tsa.seasonal import STL

    p = series("A009")                      # Prairie County, three months missing
    lp = np.log(p + 0.5)
    lp.index.freq = "MS"
    gap = lp.index[lp.isna()]

    ss = SARIMAX(lp, order=(0, 1, 1), seasonal_order=(0, 1, 1, 12)).fit(disp=False)
    ss_fit = np.exp(ss.get_prediction().predicted_mean) - 0.5

    hw = ExponentialSmoothing(lp, trend="add", seasonal="add", seasonal_periods=12,
                              initialization_method="estimated").fit()
    hw_fit = pd.Series(np.exp(np.asarray(hw.fittedvalues)) - 0.5, index=lp.index)

    stl = STL(lp, period=12, robust=True).fit()
    stl_trend = pd.Series(np.asarray(stl.trend), index=lp.index)

    fig, (a1, a2) = plt.subplots(1, 2, figsize=(13.4, 4.9))

    a1.axvspan(gap[0], gap[-1], color=ORANGE, alpha=0.18, zorder=1)
    a1.plot(p.index, p.values, color=INK3, lw=1.5, zorder=3, label="what was reported")
    a1.plot(ss_fit.index, ss_fit.values, color=BLUE, lw=2, zorder=4,
            label="state space, fitted through the gap")
    a1.scatter(gap, ss_fit.loc[gap], s=60, color=BLUE, zorder=6)
    a1.text(gap[-1], 9.6, "  three months\n  never submitted", fontsize=8.5,
            color=INK2, va="top")
    a1.set_ylim(-0.3, 10.5)
    a1.set_ylabel("use of force incidents")
    a1.legend(fontsize=8.5, frameon=False, loc="upper left")
    style(a1)
    title(a1, "Prairie County: the Kalman filter simply skips them",
          "It estimates the missing months instead of refusing to run.")

    usable = {
        "state space\n(SARIMAX)": 100 * (1 - float(np.isnan(np.asarray(ss_fit)).mean())),
        "Holt Winters": 100 * (1 - float(np.isnan(np.asarray(hw_fit)).mean())),
        "STL": 100 * (1 - float(np.isnan(np.asarray(stl_trend)).mean())),
    }
    cols = [AQUA if v > 99 else ORANGE for v in usable.values()]
    a2.bar(list(usable), list(usable.values()), color=cols, width=0.55, zorder=3)
    for i, (k, v) in enumerate(usable.items()):
        note = "" if v > 99 else "  fails silently"
        a2.text(i, v + 2.5, f"{v:.0f}%{note}", ha="center", fontsize=10, color=INK,
                weight="bold")
    a2.set_ylim(0, 118)
    a2.set_yticks([0, 25, 50, 75, 100])
    a2.set_ylabel("percent of months with a usable fitted value")
    a2.tick_params(labelsize=9)
    style(a2)
    title(a2, "The same gapped series, three methods",
          "Two return no error and no usable output.")

    fig.tight_layout()
    fig.savefig(HERE / "fig_a07_state_space.png", dpi=150)
    plt.close(fig)


if __name__ == "__main__":
    for fn in (fig_01, fig_02, fig_03, fig_04, fig_05, fig_06, fig_07):
        fn()
        print("built", fn.__name__)
