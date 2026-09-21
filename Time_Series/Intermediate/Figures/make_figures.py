"""
Build every figure in the Time Series Intermediate series.

All figures are drawn from the synthetic WADEPS dataset in Data/. Running this
script overwrites the PNG files that the Markdown modules link to.

    python make_figures.py

Colors follow the CISER data visualization palette: categorical slot 1 blue
#2a78d6, slot 2 orange #eb6834, slot 3 aqua #1baf7a, on surface #fcfcfb.

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
YELLOW, MAGENTA = "#eda100", "#e87ba4"
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


uof = pd.read_csv(DATA / "use_of_force.csv")
monthly = pd.read_csv(DATA / "agency_monthly.csv")
profile = pd.read_csv(DATA / "agency_profile.csv")
monthly["year"] = monthly["year_month"].str[:4]
monthly["mon"] = monthly["year_month"].str[5:7].astype(int)

CALENDAR = pd.period_range("2019-01", "2026-06", freq="M").astype(str).tolist()


def short(name):
    return (name.replace(" Police Department", "")
                .replace(" Sheriff's Office", "")
                .replace(" Police", ""))


# ------------------------------------------- 1. records into a series
def fig_01():
    g = uof[(uof["agency_id"] == "A012") & (uof["year_month"].str[:4] == "2023")]
    fig, (a1, a2, a3) = plt.subplots(1, 3, figsize=(13.8, 4.4))

    tot = g.groupby("year_month").size().reindex(
        [f"2023-{m:02d}" for m in range(1, 13)], fill_value=0)
    a1.plot(MONTHS, tot.values, color=BLUE, lw=2.2, marker="o", ms=5,
            mfc=SURFACE, mew=1.6, zorder=3)
    a1.set_ylim(0, 185); a1.set_ylabel("incidents")
    style(a1)
    title(a1, "Grouped by month", "1,136 records become 12 numbers.")

    top4 = g["incident_type"].value_counts().head(4).index.tolist()
    for t, c in zip(top4, [BLUE, ORANGE, AQUA, YELLOW]):
        s = (g[g["incident_type"] == t].groupby("year_month").size()
             .reindex([f"2023-{m:02d}" for m in range(1, 13)], fill_value=0))
        a2.plot(MONTHS, s.values, color=c, lw=1.9, zorder=3, label=t)
    a2.legend(fontsize=7.5, frameon=False, loc="upper left")
    a2.set_ylim(0, 90); a2.set_ylabel("incidents")
    style(a2)
    title(a2, "Grouped by month and incident type", "The same records become four series.")

    inj = (g.groupby(["year_month", "subject_injury"]).size().unstack(fill_value=0)
           .reindex([f"2023-{m:02d}" for m in range(1, 13)], fill_value=0))
    a3.bar(MONTHS, inj["No"], color=BLUE, width=0.66, zorder=3, label="no injury")
    a3.bar(MONTHS, inj["Yes"], bottom=inj["No"], color=ORANGE, width=0.66,
           zorder=3, label="subject injured")
    a3.legend(fontsize=8, frameon=False, loc="upper left")
    a3.set_ylim(0, 185); a3.set_ylabel("incidents")
    style(a3)
    title(a3, "Grouped by month and outcome", "And into a third series again.")

    for a in (a1, a2, a3):
        a.tick_params(labelsize=8.5)
        for lab in a.get_xticklabels()[1::2]:
            lab.set_visible(False)
    fig.tight_layout()
    fig.savefig(HERE / "fig_m01_records_into_a_series.png", dpi=150)
    plt.close(fig)


# ------------------------------------------------ 2. an honest calendar
def fig_02():
    fig, (a1, a2) = plt.subplots(1, 2, figsize=(12.8, 4.5))

    e = uof[uof["agency_id"] == "A006"]
    seen = e.groupby("year_month").size()
    x = pd.PeriodIndex(CALENDAR, freq="M").to_timestamp()
    a1.plot(pd.PeriodIndex(seen.index, freq="M").to_timestamp(), seen.values,
            color=ORANGE, lw=1.6, marker="o", ms=4, zorder=4,
            label="group the event file: 50 points")
    a1.plot(x, [seen.get(c, 0) for c in CALENDAR], color=BLUE, lw=1.3, zorder=3,
            label="reindex to the calendar: 90 points")
    a1.legend(fontsize=8.5, frameon=False, loc="upper right")
    a1.set_ylim(-0.3, 6); a1.set_ylabel("use of force incidents")
    style(a1)
    title(a1, "Elkhorn: 40 months have no incident at all",
          "A group by never creates a row for a month with nothing in it.")

    d = monthly[monthly["agency_id"] == "A009"]
    have = dict(zip(d["year_month"], d["n_uof"]))
    vals = [have.get(c, np.nan) for c in CALENDAR]
    a2.plot(x, vals, color=BLUE, lw=1.4, zorder=3)
    zero = [(i, v) for i, v in enumerate(vals) if v == 0]
    a2.plot([x[i] for i, _ in zero], [0] * len(zero), marker="o", ls="none",
            ms=8, mfc=AQUA, mec=SURFACE, mew=1.3, zorder=5)
    gi = [CALENDAR.index(c) for c in ("2022-03", "2022-04", "2022-05")]
    a2.axvspan(x[gi[0]], x[gi[-1]], color=ORANGE, alpha=0.20, zorder=1)
    a2.text(x[gi[-1]], 9.1, "  never submitted:\n  leave as missing",
            fontsize=8.5, color=INK2, va="top")
    a2.text(0.02, 0.93, "● a reported zero: keep as 0", transform=a2.transAxes,
            fontsize=8.5, color=AQUA)
    a2.set_ylim(-0.4, 10.5); a2.set_ylabel("use of force incidents")
    style(a2)
    title(a2, "Prairie County: zeros and a gap in one series",
          "The event file cannot tell these apart. The reporting roster can.")

    fig.tight_layout()
    fig.savefig(HERE / "fig_m02_honest_calendar.png", dpi=150)
    plt.close(fig)


# ------------------------------------------------- 3. denominators
def fig_03():
    d = (monthly[monthly["year"] == "2023"].groupby("agency_id", as_index=False)
         .agg(uof=("n_uof", "sum"), arr=("n_arrests", "sum"),
              cfs=("total_cfs", "sum"), sworn=("sworn_officers", "max")))
    d = d.merge(profile[["agency_id", "agency_name", "population_served"]], on="agency_id")
    d["short"] = d["agency_name"].map(short)
    cols = {"per 100\narrests": 100 * d["uof"] / d["arr"],
            "per 1,000\ncalls": 1000 * d["uof"] / d["cfs"],
            "per 1,000\nresidents": 1000 * d["uof"] / d["population_served"],
            "per sworn\nofficer": d["uof"] / d["sworn"]}
    ranks = pd.DataFrame({k: v.rank(ascending=False) for k, v in cols.items()})
    ranks.index = d["short"]

    fig, ax = plt.subplots(figsize=(11.5, 5.6))
    xs = np.arange(len(cols))
    for name, row in ranks.iterrows():
        ax.plot(xs, row.values, color=INK3, lw=1.2, alpha=0.45, zorder=2)
        ax.scatter(xs, row.values, s=26, color=INK3, alpha=0.45, zorder=3)
    for name, c in [("Pinecrest State University", ORANGE), ("Elkhorn", BLUE),
                    ("Grandview", AQUA)]:
        row = ranks.loc[name]
        ax.plot(xs, row.values, color=c, lw=2.6, zorder=4)
        ax.scatter(xs, row.values, s=60, color=c, zorder=5)
        ax.text(-0.08, row.values[0], f"{name}  ", ha="right", va="center",
                fontsize=9.5, color=c, weight="bold")
        ax.text(3.08, row.values[-1], f"  {name}", ha="left", va="center",
                fontsize=9.5, color=c, weight="bold")
    ax.set_xticks(xs); ax.set_xticklabels(list(cols.keys()), fontsize=9.5)
    ax.set_xlim(-1.45, 4.45)
    ax.set_yticks(range(1, 13))
    ax.set_yticklabels([f"{i}" for i in range(1, 13)], fontsize=9)
    ax.invert_yaxis()
    ax.set_ylabel("rank, 1 is the highest rate")
    style(ax, ygrid=False)
    ax.grid(axis="y", color=GRID, lw=0.8); ax.set_axisbelow(True)
    title(ax, "The same twelve agencies, 2023, ranked four ways",
          "Each grey line is one agency. The denominator decides the ranking.")
    fig.tight_layout()
    fig.savefig(HERE / "fig_m03_denominators.png", dpi=150)
    plt.close(fig)


# ------------------------------------ 4. why small agencies look volatile
def fig_04():
    f = monthly[(monthly["provisional"] == 0)]
    f = f[~((f["agency_id"] == "A002") & (f["year_month"] == "2021-06"))]
    rows = []
    for aid, g in f.groupby("agency_id"):
        rows.append((short(g["agency_name"].iloc[0]), g["n_uof"].mean(),
                     g["n_uof"].std() / g["n_uof"].mean()))
    v = pd.DataFrame(rows, columns=["name", "mean", "cv"])

    fig, (a1, a2) = plt.subplots(1, 2, figsize=(13, 4.8))

    xs = np.linspace(0.6, 130, 300)
    a1.plot(xs, 1 / np.sqrt(xs), color=ORANGE, lw=2, zorder=3,
            label="what pure counting noise alone would give")
    a1.scatter(v["mean"], v["cv"], s=54, color=BLUE, zorder=4, label="each agency")
    offsets = {"Elkhorn": (10, 6), "Two Rivers Tribal": (10, -16),
               "Grandview": (-10, 14), "Riverbend": (-12, -20)}
    for _, r in v.iterrows():
        if r["name"] in offsets:
            a1.annotate(r["name"], (r["mean"], r["cv"]), textcoords="offset points",
                        xytext=offsets[r["name"]], fontsize=9, color=INK)
    a1.set_xscale("log")
    a1.set_xlabel("average incidents a month")
    a1.set_ylabel("variability: standard deviation as a share of the mean")
    a1.set_ylim(0, 1.35)
    a1.legend(fontsize=8.5, frameon=False, loc="upper right")
    style(a1)
    title(a1, "Small agencies swing more, and it means less",
          "An agency sitting on the orange line is pure noise. Above it is real structure.")

    g23 = (monthly[monthly["year"] == "2023"].groupby("agency_id", as_index=False)
           .agg(uof=("n_uof", "sum"), arr=("n_arrests", "sum")))
    g23 = g23.merge(profile[["agency_id", "agency_name"]], on="agency_id")
    g23["short"] = g23["agency_name"].map(short)
    state = 100 * g23["uof"].sum() / g23["arr"].sum()
    g23["rate"] = 100 * g23["uof"] / g23["arr"]
    n = np.linspace(300, 52000, 400)
    se = 100 * np.sqrt((state / 100) * (1 - state / 100) / n)
    a2.fill_between(n, state - 1.96 * se, state + 1.96 * se, color=BLUE, alpha=0.11,
                    zorder=1, label="where 95 percent of agencies should fall")
    a2.set_xlim(330, 66000)
    a2.axhline(state, color=INK3, lw=1.4, ls=(0, (5, 3)), zorder=2)
    a2.text(64000, state + 0.07, f"state rate {state:.2f}", ha="right",
            fontsize=8.5, color=INK2)
    g23["se"] = 100 * np.sqrt((state / 100) * (1 - state / 100) / g23["arr"])
    out = (g23["rate"] - state).abs() > 1.96 * g23["se"]
    a2.scatter(g23.loc[~out, "arr"], g23.loc[~out, "rate"], s=54, color=BLUE, zorder=4)
    a2.scatter(g23.loc[out, "arr"], g23.loc[out, "rate"], s=64, color=ORANGE, zorder=5)
    off2 = {"Elkhorn": (9, 7), "Two Rivers Tribal": (9, -15),
            "Cedar Falls": (10, 4), "Grandview": (-12, -18),
            "Lakeshore County": (10, -4)}
    for _, r in g23.iterrows():
        if r["short"] in off2:
            a2.annotate(r["short"], (r["arr"], r["rate"]), textcoords="offset points",
                        xytext=off2[r["short"]], fontsize=9, color=INK,
                        ha="right" if r["short"] == "Grandview" else "left")
    a2.set_xscale("log")
    a2.set_xlabel("arrests in 2023, the size of the denominator")
    a2.set_ylabel("use of force per 100 arrests")
    a2.set_ylim(1.2, 4.4)
    a2.legend(fontsize=8.5, frameon=False, loc="upper right")
    style(a2)
    title(a2, "A funnel plot separates unusual from small",
          "Orange agencies are genuinely different. The two smallest are not.")

    fig.tight_layout()
    fig.savefig(HERE / "fig_m04_small_agencies.png", dpi=150)
    plt.close(fig)


# --------------------------------------------------- 5. decomposition
def _series(aid, col="n_uof"):
    d = monthly[(monthly["agency_id"] == aid) & (monthly["provisional"] == 0)].sort_values("year_month")
    return pd.Series(d[col].values,
                     index=pd.PeriodIndex(d["year_month"], freq="M").to_timestamp(),
                     dtype=float)


def _rate(aid):
    d = monthly[(monthly["agency_id"] == aid) & (monthly["provisional"] == 0)].sort_values("year_month")
    return pd.Series((100 * d["n_uof"] / d["n_arrests"]).values,
                     index=pd.PeriodIndex(d["year_month"], freq="M").to_timestamp())


def fig_05():
    from statsmodels.tsa.seasonal import STL
    s = _series("A012")
    st = STL(np.log(s), period=12, robust=True).fit()

    fig = plt.figure(figsize=(13.5, 6.4))
    gs = fig.add_gridspec(4, 2, width_ratios=[1.55, 1], hspace=0.55, wspace=0.22)

    parts = [("what was reported", s, BLUE),
             ("trend", np.exp(st.trend), ORANGE),
             ("season", np.exp(st.seasonal), AQUA),
             ("what is left over", np.exp(st.resid), INK3)]
    for i, (lab, v, c) in enumerate(parts):
        ax = fig.add_subplot(gs[i, 0])
        ax.plot(v.index, v.values, color=c, lw=1.5, zorder=3)
        if i >= 2:
            ax.axhline(1.0, color=INK3, lw=0.9, ls=(0, (4, 3)), zorder=2)
        ax.set_ylabel(lab, fontsize=9)
        ax.tick_params(labelsize=8)
        if i < 3:
            ax.set_xticklabels([])
        style(ax)
    fig.text(0.012, 0.965, "Grandview, monthly use of force, split into three pieces",
             fontsize=11, color=INK)
    fig.text(0.012, 0.932, "Multiply the three lower panels together and the top panel comes back.",
             fontsize=9, color=INK2)

    ax = fig.add_subplot(gs[:, 1])
    for lab, v, c in [("counts", s, BLUE),
                      ("arrests, the denominator", _series("A012", "n_arrests"), AQUA),
                      ("rate per 100 arrests", _rate("A012"), ORANGE)]:
        f = STL(np.log(v), period=12, robust=True).fit()
        idx = np.exp(f.seasonal).groupby(v.index.month).mean()
        ax.plot(MONTHS, idx.values, color=c, lw=2.2, marker="o", ms=4,
                mfc=SURFACE, mew=1.2, zorder=3, label=lab)
    ax.axhline(1.0, color=INK3, lw=1.0, ls=(0, (4, 3)), zorder=2)
    ax.legend(fontsize=8.5, frameon=False, loc="upper left")
    ax.set_ylim(0.6, 1.62)
    ax.set_ylabel("seasonal factor")
    ax.tick_params(labelsize=8.5)
    for lab in ax.get_xticklabels()[1::2]:
        lab.set_visible(False)
    style(ax)
    title(ax, "Which series you decompose changes the answer",
          "Counts peak in August. The rate peaks in July.")
    fig.savefig(HERE / "fig_m05_decomposition.png", dpi=150, bbox_inches="tight")
    plt.close(fig)


# ------------------------------------------------ 6. measuring a trend
def fig_06():
    import statsmodels.formula.api as smf
    r = monthly[(monthly["agency_id"] == "A012") & (monthly["provisional"] == 0)].copy()
    r["rate"] = 100 * r["n_uof"] / r["n_arrests"]
    r["t"] = np.arange(len(r))
    r["mon"] = r["year_month"].str[5:7].astype(int)
    r["date"] = pd.PeriodIndex(r["year_month"], freq="M").to_timestamp()
    whole = r[r["year_month"] <= "2025-12"]

    fig, (a1, a2) = plt.subplots(1, 2, figsize=(13, 4.8))

    fit = smf.ols("np.log(rate) ~ t", data=whole).fit()
    pred = np.exp(fit.predict(whole))
    a1.plot(whole["date"], whole["rate"], color=INK3, lw=1.2, zorder=3, label="monthly rate")
    a1.plot(whole["date"], pred, color=ORANGE, lw=2.6, zorder=4, label="fitted trend")
    a1.set_ylabel("use of force per 100 arrests")
    a1.set_ylim(0, 5.2)
    a1.legend(fontsize=8.5, frameon=False, loc="upper right")
    style(a1)
    title(a1, "Grandview, 2019 to 2025",
          "A straight line on the log scale is a constant percentage per year.")

    def slope(d, formula="np.log(rate) ~ t"):
        o = smf.ols(formula, data=d).fit()
        lo, hi = o.conf_int().loc["t"]
        a = lambda v: 100 * (np.exp(12 * v) - 1)
        return a(o.params["t"]), a(lo), a(hi)

    rows = [
        ("2024 and 2025 only", slope(r[(r["year_month"] >= "2024-01") & (r["year_month"] <= "2025-12")])),
        ("2021 through 2023", slope(r[(r["year_month"] >= "2021-01") & (r["year_month"] <= "2023-12")])),
        ("2019 through 2025", slope(whole)),
        ("2019 through 2025,\nwith month effects", slope(whole, "np.log(rate) ~ t + C(mon)")),
    ]
    ys = np.arange(len(rows))
    for y, (lab, (est, lo, hi)) in zip(ys, rows):
        c = ORANGE if "month effects" in lab else BLUE
        a2.plot([lo, hi], [y, y], color=c, lw=2.6, solid_capstyle="round", zorder=3)
        a2.plot([est], [y], marker="o", ms=9, color=c, zorder=4)
        a2.text(hi + 0.7, y, f"{est:+.2f}%", va="center", fontsize=9, color=INK)
    a2.axvline(100 * (np.exp(-0.05) - 1), color=INK, lw=1.4, ls=(0, (5, 3)), zorder=5)
    a2.text(100 * (np.exp(-0.05) - 1) - 0.9, -0.45,
            "the true trend\nbuilt into the data", ha="right", va="bottom",
            fontsize=8.5, color=INK)
    a2.set_yticks(ys)
    a2.set_yticklabels([r[0] for r in rows], fontsize=9)
    a2.set_ylim(-0.95, len(rows) - 0.25)
    a2.set_xlim(-18, 20)
    a2.set_xlabel("estimated change per year, percent")
    style(a2, ygrid=False)
    a2.grid(axis="x", color=GRID, lw=0.8)
    a2.set_axisbelow(True)
    title(a2, "The same agency, four windows",
          "Every estimate covers the truth. Short windows say almost nothing.")

    fig.tight_layout()
    fig.savefig(HERE / "fig_m06_measuring_the_trend.png", dpi=150)
    plt.close(fig)


# -------------------------------------------- 7. seasonal adjustment
def fig_07():
    from statsmodels.tsa.seasonal import STL
    s = _series("A012")
    st = STL(np.log(s), period=12, robust=True).fit()
    factor = np.exp(st.seasonal)
    adj = s / factor

    fig, (a1, a2) = plt.subplots(1, 2, figsize=(13, 4.6))

    a1.plot(s.index, s.values, color=INK3, lw=1.2, zorder=3, label="as reported")
    a1.plot(adj.index, adj.values, color=BLUE, lw=2, zorder=4, label="seasonally adjusted")
    a1.set_ylim(0, 190)
    a1.set_ylabel("use of force incidents")
    a1.legend(fontsize=8.5, frameon=False, loc="upper right")
    style(a1)
    title(a1, "Grandview, 2019 to 2026",
          "The adjusted line keeps the level and the trend, and drops the calendar.")

    raw = 100 * (s / s.shift(1) - 1)
    adjm = 100 * (adj / adj.shift(1) - 1)
    x = np.arange(12)
    a2.bar(x - 0.2, raw.loc["2023"].values, width=0.38, color=ORANGE,
           zorder=3, label="as reported")
    a2.bar(x + 0.2, adjm.loc["2023"].values, width=0.38, color=BLUE,
           zorder=3, label="seasonally adjusted")
    a2.axhline(0, color=INK2, lw=1.0, zorder=4)
    a2.annotate("June: +51 percent becomes +21", (5.2, 51),
                textcoords="offset points", xytext=(6, 10), fontsize=8.5, color=INK)
    a2.set_xticks(x)
    a2.set_xticklabels(MONTHS, fontsize=8.5)
    for lab in a2.get_xticklabels()[1::2]:
        lab.set_visible(False)
    a2.set_ylim(-48, 72)
    a2.set_ylabel("change on the previous month, percent")
    a2.legend(fontsize=8.5, frameon=False, loc="lower left")
    style(a2)
    title(a2, "Month on month change in 2023",
          "Adjustment removes the calendar, not the noise.")

    fig.tight_layout()
    fig.savefig(HERE / "fig_m07_seasonal_adjustment.png", dpi=150)
    plt.close(fig)


# --------------------------------------------- 8. control limits
def fig_08():
    from statsmodels.tsa.seasonal import STL
    s = _series("A002")
    fig, (a1, a2) = plt.subplots(1, 2, figsize=(13, 4.8))

    base = s[s.index.year <= 2020].mean()
    up = base + 3 * np.sqrt(base)
    lo = max(base - 3 * np.sqrt(base), 0)
    a1.axhspan(lo, up, color=BLUE, alpha=0.10, zorder=1)
    a1.axhline(base, color=INK3, lw=1.3, ls=(0, (5, 3)), zorder=2)
    a1.plot(s.index, s.values, color=BLUE, lw=1.4, zorder=3)
    false_alarm = s[(s > up) & (s < 100)]
    a1.scatter(false_alarm.index, false_alarm.values, s=60, color=ORANGE, zorder=5)
    a1.scatter([pd.Timestamp("2021-06-01")], [s.loc["2021-06-01"]], s=70,
               color=ORANGE, zorder=5)
    for k, v in false_alarm.items():
        a1.annotate("an ordinary summer", xy=(k, v), textcoords="offset points",
                    xytext=(10, 14), fontsize=8.5, color=ORANGE,
                    arrowprops=dict(arrowstyle="->", lw=0.9, color=ORANGE))
    a1.set_ylim(0, 190)
    a1.set_ylabel("use of force incidents")
    style(a1)
    title(a1, "One fixed limit for the whole period",
          "Cedar Falls. The limit ignores the season and the trend.")

    st = STL(np.log(s), period=12, robust=True).fit()
    expected = np.exp(st.trend + st.seasonal)
    keep = ~((s.index.year == 2021) & (s.index.month == 6))
    phi = (((s - expected) ** 2 / expected)[keep]).sum() / (keep.sum() - 1)
    hi = expected + 3 * np.sqrt(phi * expected)
    lo2 = (expected - 3 * np.sqrt(phi * expected)).clip(lower=0)

    a2.fill_between(s.index, lo2, hi, color=BLUE, alpha=0.13, zorder=1)
    a2.plot(expected.index, expected.values, color=INK3, lw=1.3, ls=(0, (5, 3)), zorder=2)
    a2.plot(s.index, s.values, color=BLUE, lw=1.4, zorder=3)
    out = s[s > hi]
    a2.scatter(out.index, out.values, s=64, color=ORANGE, zorder=5)
    a2.annotate(f"June 2021: 176 against a limit of {hi.loc['2021-06-01']:.0f}",
                xy=(pd.Timestamp("2021-06-01"), 176), textcoords="offset points",
                xytext=(18, -6), fontsize=9, color=INK)
    a2.set_ylim(0, 190)
    a2.set_ylabel("use of force incidents")
    style(a2)
    title(a2, "A limit that moves with the trend and the season",
          f"Widened for real spread, dispersion {phi:.2f}. Summer no longer trips it.")

    fig.tight_layout()
    fig.savefig(HERE / "fig_m08_control_limits.png", dpi=150)
    plt.close(fig)


# ----------------------------------------- 9. three ways to present
def fig_09():
    s = _series("A012")
    fig, (a1, a2, a3) = plt.subplots(1, 3, figsize=(14, 4.4))

    a1.plot(s.index, s.values, color=INK3, lw=1.1, zorder=3, label="monthly count")
    a1.plot(s.index, s.rolling(12).mean(), color=BLUE, lw=2.4, zorder=4,
            label="rolling twelve month average")
    a1.set_ylim(0, 190)
    a1.set_ylabel("use of force incidents")
    a1.legend(fontsize=8.5, frameon=False, loc="upper right")
    style(a1)
    title(a1, "Rolling twelve month total",
          "Seasonally neutral by construction, and it updates every month.")

    yoy = 100 * (s / s.shift(12) - 1)
    cols = [ORANGE if v > 0 else BLUE for v in yoy.dropna().values]
    a2.bar(yoy.dropna().index, yoy.dropna().values, width=22, color=cols, zorder=3)
    a2.axhline(0, color=INK2, lw=1.0, zorder=4)
    a2.set_ylim(-60, 60)
    a2.set_ylabel("change on the same month a year earlier, percent")
    style(a2)
    title(a2, "Year over year", "Needs no model, and is noisy month to month.")

    for aid, c in [("A012", BLUE), ("A001", ORANGE), ("A007", AQUA), ("A006", YELLOW)]:
        v = _series(aid)
        base = v.loc["2019"].mean()
        idx = (100 * v / base).rolling(12).mean()
        name = short(monthly[monthly["agency_id"] == aid]["agency_name"].iloc[0])
        a3.plot(idx.index, idx.values, color=c, lw=2, zorder=3, label=name)
    a3.axhline(100, color=INK3, lw=1.1, ls=(0, (4, 3)), zorder=2)
    a3.legend(fontsize=8, frameon=False, loc="lower left")
    a3.set_ylim(30, 145)
    a3.set_ylabel("index, the agency's own 2019 average is 100")
    style(a3)
    title(a3, "Indexed to a base year",
          "Agencies of any size on one chart, each against its own past.")

    fig.tight_layout()
    fig.savefig(HERE / "fig_m09_presentations.png", dpi=150)
    plt.close(fig)


# ------------------------------------------------- 10. autocorrelation
def fig_10():
    from statsmodels.tsa.stattools import acf
    import statsmodels.formula.api as smf
    from statsmodels.stats.diagnostic import acorr_ljungbox

    g = monthly[(monthly["agency_id"] == "A012") & (monthly["provisional"] == 0)].copy()
    g["rate"] = 100 * g["n_uof"] / g["n_arrests"]
    g["t"] = np.arange(len(g))
    g["mon"] = g["year_month"].str[5:7].astype(int)
    g = g[g["year_month"] <= "2025-12"]

    fig, (a1, a2) = plt.subplots(1, 2, figsize=(13, 4.6))
    band = 1.96 / np.sqrt(len(g))

    for ax, formula, name in [
            (a1, "np.log(rate) ~ t", "a trend only"),
            (a2, "np.log(rate) ~ t + C(mon)", "a trend and month terms")]:
        res = smf.ols(formula, data=g).fit().resid
        a = acf(res, nlags=24, fft=False)
        p = acorr_ljungbox(res, lags=[12], return_df=True)["lb_pvalue"].iloc[0]
        outside = np.abs(a[1:]) > band
        cols = [ORANGE if o else BLUE for o in outside]
        ax.bar(range(1, 25), a[1:], width=0.62, color=cols, zorder=3)
        ax.axhspan(-band, band, color=INK3, alpha=0.13, zorder=1)
        ax.axhline(0, color=INK2, lw=1.0, zorder=4)
        ax.set_ylim(-0.85, 0.85)
        ax.set_xlabel("lag, in months")
        ax.set_ylabel("correlation with itself")
        ax.set_xticks([1, 6, 12, 18, 24])
        style(ax)
        title(ax, f"What is left after fitting {name}",
              f"{int(outside.sum())} of 24 lags outside the noise band. "
              f"Ljung Box p = {p:.3f}")
    fig.tight_layout()
    fig.savefig(HERE / "fig_m10_autocorrelation.png", dpi=150)
    plt.close(fig)


# ------------------------------------------------ 11. lead and lag
def _ccf(x, y, maxlag=12):
    n = len(x)
    out = {}
    for k in range(-maxlag, maxlag + 1):
        if k < 0:
            out[k] = float(np.corrcoef(x[-k:], y[:n + k])[0, 1])
        elif k == 0:
            out[k] = float(np.corrcoef(x, y)[0, 1])
        else:
            out[k] = float(np.corrcoef(x[:n - k], y[k:])[0, 1])
    return pd.Series(out)


def fig_11():
    from statsmodels.tsa.seasonal import STL
    resid = lambda s: np.exp(STL(np.log(s), period=12, robust=True).fit().resid)

    cfs, arr, uof = _series("A012", "total_cfs"), _series("A012", "n_arrests"), _series("A012")
    band = 1.96 / np.sqrt(len(uof))

    fig, (a1, a2) = plt.subplots(1, 2, figsize=(13, 4.6))

    raw = _ccf(cfs, uof)
    a1.bar(raw.index, raw.values, width=0.62, color=ORANGE, zorder=3)
    a1.axhspan(-band, band, color=INK3, alpha=0.13, zorder=1)
    a1.axhline(0, color=INK2, lw=1.0, zorder=4)
    a1.annotate(f"lag 12: {raw[12]:+.2f}", xy=(12, raw[12]), textcoords="offset points",
                xytext=(-4, 10), ha="right", fontsize=9, color=INK)
    a1.set_ylim(-0.95, 0.95)
    a1.set_xlabel("months by which calls lead use of force")
    a1.set_ylabel("correlation")
    style(a1)
    title(a1, "Straight off the raw series",
          "A wave, because both series carry the same calendar. None of it is real.")

    for lab, x, c, off in [("calls for service", resid(cfs), INK3, -0.21),
                           ("arrests", resid(arr), BLUE, 0.21)]:
        v = _ccf(x, resid(uof))
        a2.bar(v.index + off, v.values, width=0.4, color=c, zorder=3, label=lab)
    a2.axhspan(-band, band, color=INK3, alpha=0.13, zorder=1)
    a2.axhline(0, color=INK2, lw=1.0, zorder=4)
    a2.annotate("arrests at lag 0: +0.44,\nthe only bar that clears the band",
                xy=(0.21, 0.44), textcoords="offset points", xytext=(16, 6),
                fontsize=8.5, color=INK,
                arrowprops=dict(arrowstyle="->", lw=0.9, color=INK2))
    a2.set_ylim(-0.95, 0.95)
    a2.set_xlabel("months by which the first series leads use of force")
    a2.set_ylabel("correlation")
    a2.legend(fontsize=8.5, frameon=False, loc="lower left")
    style(a2)
    title(a2, "After removing trend and season from both",
          "The wave is gone. What is left is the real link, and it is at lag zero.")

    fig.tight_layout()
    fig.savefig(HERE / "fig_m11_lead_and_lag.png", dpi=150)
    plt.close(fig)


# ------------------------------------------- 12. comparing agencies
NUMERIC = ["sworn_officers", "population_served", "violent_crime_rate_per_1000",
           "property_crime_rate_per_1000", "budget_share_public_safety_pct",
           "county_population"]
CATEGORICAL = ["agency_type", "region"]


def _gower(df):
    P = df.copy()
    for c in ["sworn_officers", "population_served", "county_population"]:
        P[c] = np.log(P[c])
    n = len(P)
    D = np.zeros((n, n))
    for c in NUMERIC:
        v = P[c].astype(float).values
        D += np.abs(v[:, None] - v[None, :]) / (v.max() - v.min())
    for c in CATEGORICAL:
        v = P[c].values
        D += (v[:, None] != v[None, :]).astype(float)
    return D / (len(NUMERIC) + len(CATEGORICAL))


def fig_12():
    from sklearn.manifold import MDS

    y = (monthly[monthly["year_month"].str[:4] == "2023"]
         .groupby("agency_id", as_index=False)
         .agg(uof=("n_uof", "sum"), arr=("n_arrests", "sum")))
    y = y.merge(profile, on="agency_id")
    y["rate"] = 100 * y["uof"] / y["arr"]
    y["short"] = y["agency_name"].map(short)

    D = _gower(y)
    Dd = pd.DataFrame(D, index=y["short"], columns=y["short"])
    xy = MDS(n_components=2, dissimilarity="precomputed",
             random_state=1).fit_transform(D)

    fig, (a1, a2) = plt.subplots(1, 2, figsize=(13.4, 5.4))

    colors = {"Municipal Police": BLUE, "County Sheriff": ORANGE,
              "Campus Police": AQUA, "Tribal Police": YELLOW}
    names = list(y["short"])

    # a thin line from each agency to its single nearest peer
    for i, nm in enumerate(names):
        j = names.index(Dd.loc[nm].drop(nm).idxmin())
        a1.plot([xy[i, 0], xy[j, 0]], [xy[i, 1], xy[j, 1]],
                color=INK3, lw=0.9, alpha=0.55, zorder=2)

    for t, c in colors.items():
        sel = (y["agency_type"] == t).values
        a1.scatter(xy[sel, 0], xy[sel, 1], s=115, color=c, zorder=4,
                   edgecolors=SURFACE, linewidths=1.2, label=t)

    nudge = {"Northgate": (0, 12), "Millgate": (0, -19), "Cedar Falls": (0, -19),
             "Harbor Point": (0, 12), "Grandview": (0, 12), "Riverbend": (0, -19),
             "Summit County": (0, -19), "Lakeshore County": (0, 12)}
    for i, nm in enumerate(names):
        a1.annotate(nm, (xy[i, 0], xy[i, 1]), textcoords="offset points",
                    xytext=nudge.get(nm, (0, 12)), ha="center", fontsize=8, color=INK)

    lonely = {"Grandview": ((0, -30), "center"),
              "Pinecrest State University": ((16, -13), "left")}
    for nm, (off, ha) in lonely.items():
        i = names.index(nm)
        d = Dd.loc[nm].drop(nm).nsmallest(3).mean()
        a1.annotate(f"nearest peers are {d:.2f} away", (xy[i, 0], xy[i, 1]),
                    textcoords="offset points", xytext=off, ha=ha,
                    fontsize=8, color=ORANGE)

    pad = 0.12
    a1.set_xlim(xy[:, 0].min() - pad, xy[:, 0].max() + pad)
    a1.set_ylim(xy[:, 1].min() - pad * 1.6, xy[:, 1].max() + pad)
    a1.set_xticks([]); a1.set_yticks([])
    a1.legend(fontsize=8, frameon=False, loc="upper left",
              bbox_to_anchor=(0.0, 1.0), handletextpad=0.3)
    a1.spines[["top", "right", "left", "bottom"]].set_visible(False)
    title(a1, "Agencies placed by how alike they are",
          "Lines join each agency to its single nearest peer.")

    state = 100 * y["uof"].sum() / y["arr"].sum()
    rows = []
    for i, a in enumerate(y["short"]):
        peers = Dd.loc[a].drop(a).nsmallest(3)
        pm = y[y["short"].isin(peers.index)]
        rows.append((a, y["rate"].iloc[i], 100 * pm["uof"].sum() / pm["arr"].sum()))
    t = pd.DataFrame(rows, columns=["agency", "rate", "peer_rate"]).sort_values("rate")

    ys = np.arange(len(t))
    for yy, (_, r) in zip(ys, t.iterrows()):
        a2.plot([r["peer_rate"], r["rate"]], [yy, yy], color=INK3, lw=1.4, zorder=2)
    a2.scatter(t["peer_rate"], ys, s=52, color=AQUA, zorder=4, label="its three nearest peers")
    a2.scatter(t["rate"], ys, s=52, color=BLUE, zorder=5, label="the agency")
    a2.axvline(state, color=ORANGE, lw=1.6, ls=(0, (5, 3)), zorder=3)
    a2.text(state + 0.03, len(t) - 0.4, f"state {state:.2f}", fontsize=8.5, color=ORANGE)
    a2.set_yticks(ys)
    a2.set_yticklabels(t["agency"], fontsize=9)
    a2.set_xlabel("use of force per 100 arrests, 2023")
    a2.set_xlim(1.7, 3.6)
    a2.legend(fontsize=8.5, frameon=False, loc="lower right")
    style(a2, ygrid=False)
    a2.grid(axis="x", color=GRID, lw=0.8); a2.set_axisbelow(True)
    title(a2, "Against the state, and against its own peers",
          "Some agencies swap sides depending on which comparison is used.")

    fig.tight_layout()
    fig.savefig(HERE / "fig_m12_comparing_agencies.png", dpi=150)
    plt.close(fig)


if __name__ == "__main__":
    for fn in (fig_01, fig_02, fig_03, fig_04,
               fig_05, fig_06, fig_07, fig_08,
               fig_09, fig_10, fig_11, fig_12):
        fn()
        print("built", fn.__name__)
