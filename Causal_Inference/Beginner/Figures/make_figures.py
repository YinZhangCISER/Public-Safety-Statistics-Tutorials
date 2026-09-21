"""
Build every figure in the Causal Inference Beginner series.

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

def fig_01():
    """Topic 1. Two stories that fit the same line."""
    s = group_series(NO_A007)
    fig, ax = plt.subplots(figsize=(10.4, 4.7))
    ax.plot(s.index, s.values, color=INK3, lw=2.4, zorder=4)
    ax.axvline(pd.Timestamp(FULL), color=ORANGE, lw=2, zorder=3)
    ax.text(pd.Timestamp(FULL), 3.95, "  training in place", fontsize=9.5, color=ORANGE)
    ax.annotate("story one:\nthe training worked",
                xy=(pd.Timestamp("2025-03-01"), 2.45), xytext=(pd.Timestamp("2024-04-01"), 3.5),
                fontsize=9.5, color=BLUE,
                arrowprops=dict(arrowstyle="->", color=BLUE, lw=1.6))
    ax.annotate("story two:\nit was already falling",
                xy=(pd.Timestamp("2021-01-01"), 3.4), xytext=(pd.Timestamp("2019-06-01"), 1.9),
                fontsize=9.5, color=AQUA,
                arrowprops=dict(arrowstyle="->", color=AQUA, lw=1.6))
    ax.set_ylabel("use of force per 100 arrests")
    ax.set_ylim(1.5, 4.3)
    style(ax)
    title(ax, "The four agencies that took the training",
          "One line. Two explanations. Nothing on this chart can separate them.")
    fig.tight_layout()
    fig.savefig(HERE / "fig_01_what_caused_means.png", dpi=150)
    plt.close(fig)


def fig_02():
    """Topic 2. The question is about a comparison, not a change."""
    fig, ax = plt.subplots(figsize=(10.4, 4.7))
    s = group_series(NO_A007)
    obs = s[s.index >= pd.Timestamp(FULL)]
    ax.plot(s.index, s.values, color=INK3, lw=2.4, zorder=4, label="what was recorded")
    start = obs.iloc[0]
    n = len(obs)
    hyp = start * np.linspace(1, 1.0, n)
    ax.plot(obs.index, hyp, color=BLUE, lw=2.2, ls="--", zorder=5,
            label="one guess at what would have happened")
    ax.plot(obs.index, start * np.linspace(1, 0.88, n), color=AQUA, lw=2.2, ls="--",
            zorder=5, label="another guess")
    ax.fill_between(obs.index, obs.values, hyp, color=ORANGE, alpha=0.18, zorder=2)
    ax.axvline(pd.Timestamp(FULL), color=ORANGE, lw=2, zorder=3)
    ax.text(pd.Timestamp("2024-02-01"), 2.05,
            "the gap is the effect,\nand it depends entirely\non which dashed line is right",
            fontsize=9.5, color=INK2)
    ax.set_ylabel("use of force per 100 arrests")
    ax.set_ylim(1.5, 4.3)
    ax.legend(fontsize=8.5, frameon=False, loc="upper right")
    style(ax)
    title(ax, "The effect is a gap against something that never happened",
          "The recorded line is a fact. Both dashed lines are guesses.")
    fig.tight_layout()
    fig.savefig(HERE / "fig_02_the_question.png", dpi=150)
    plt.close(fig)


def fig_03():
    """Topic 3. Two worlds, one of which you get to see."""
    fig, ax = plt.subplots(figsize=(10.4, 4.9))
    s = group_series(NO_A007)
    cut = pd.Timestamp(FULL)
    pre = s[s.index <= cut]
    post = s[s.index >= cut]
    ax.plot(pre.index, pre.values, color=INK3, lw=2.6, zorder=4)
    ax.plot(post.index, post.values, color=BLUE, lw=2.8, zorder=5,
            label="the world that happened: they took the training")
    n = len(post)
    ghost = post.iloc[0] * np.exp(np.log(1 - 0.049) * np.arange(n) / 12.0)
    ax.plot(post.index, ghost, color=INK3, lw=2.6, ls=(0, (2, 2)), zorder=5,
            label="the world that did not: the same agencies, no training")
    ax.fill_between(post.index, post.values, ghost, color=ORANGE, alpha=0.2, zorder=2)
    ax.axvline(cut, color=ORANGE, lw=2, zorder=3)
    mid = post.index[len(post) // 2]
    ax.annotate("the effect", xy=(mid, 2.55), xytext=(pd.Timestamp("2024-03-01"), 1.85),
                fontsize=10, color=ORANGE, weight="bold",
                arrowprops=dict(arrowstyle="->", color=ORANGE, lw=1.8))
    ax.set_ylabel("use of force per 100 arrests")
    ax.set_ylim(1.5, 4.3)
    ax.legend(fontsize=9, frameon=False, loc="upper right")
    style(ax)
    title(ax, "Every causal question compares two worlds",
          "Only one of them leaves records. The other has to be constructed.")
    fig.tight_layout()
    fig.savefig(HERE / "fig_03_world_you_cannot_see.png", dpi=150)
    plt.close(fig)


def fig_04():
    """Topic 4. Before and after, against the truth."""
    tr = F[F["agency_id"].isin(TREATED)]
    b, a = rate(tr[tr["period"] == "before"]), rate(tr[tr["period"] == "after"])
    fig, (a1, a2) = plt.subplots(1, 2, figsize=(12.6, 4.9),
                                 gridspec_kw={"width_ratios": [1, 1.25]})

    a1.bar([0, 1], [b, a], color=[INK3, BLUE], width=0.52, zorder=3)
    for x, v in [(0, b), (1, a)]:
        a1.text(x, v + 0.08, f"{v:.2f}", ha="center", fontsize=11, color=INK, weight="bold")
    a1.annotate("", xy=(1, a + 0.34), xytext=(0, b + 0.34),
                arrowprops=dict(arrowstyle="->", color=ORANGE, lw=2))
    a1.text(0.5, b + 0.46, f"{100 * (a / b - 1):+.1f}%", ha="center", fontsize=12,
            color=ORANGE, weight="bold")
    a1.set_xticks([0, 1])
    a1.set_xticklabels(["before the training", "after it was in place"], fontsize=9.5)
    a1.set_ylabel("use of force per 100 arrests")
    a1.set_ylim(0, 4.6)
    style(a1)
    title(a1, "What the agencies' own records show", "Before against after, nothing else.")

    labels = ["before and after,\nthe trained agencies", "what the training\nactually did"]
    vals = [100 * (a / b - 1), -12.0]
    cols = [ORANGE, AQUA]
    a2.barh([1, 0], vals, color=cols, height=0.3, zorder=3)
    for y, v in zip([1, 0], vals):
        a2.text(v - 1.2, y, f"{v:+.1f}%", ha="right", va="center", fontsize=12,
                color=INK, weight="bold")
    a2.set_yticks([1, 0])
    a2.set_yticklabels(labels, fontsize=9.5)
    a2.set_xlim(-40, 3)
    a2.set_ylim(-0.75, 1.75)
    a2.axvline(0, color=INK3, lw=1)
    a2.set_xlabel("change in the use of force rate")
    style(a2, ygrid=False)
    a2.grid(axis="x", color=GRID, lw=0.8, zorder=0)
    a2.set_axisbelow(True)
    title(a2, "The same agencies, against the real answer",
          "The before and after number is nearly three times too big.")

    fig.tight_layout()
    fig.savefig(HERE / "fig_04_before_and_after.png", dpi=150)
    plt.close(fig)


def fig_05():
    """Topic 5. Everyone was already falling."""
    rows = []
    pre = F[F["period"] == "before"]
    for aid, g in pre.groupby("agency_id"):
        e = g[g["year_month"] < "2020-07"]
        l = g[g["year_month"] >= "2022-07"]
        rows.append((SHORT[aid], 100 * (rate(l) / rate(e) - 1), aid in TREATED))
    rows.sort(key=lambda r: r[1])

    fig, ax = plt.subplots(figsize=(11.4, 5.0))
    ys = np.arange(len(rows))
    cols = [BLUE if r[2] else INK3 for r in rows]
    ax.barh(ys, [r[1] for r in rows], color=cols, height=0.6, zorder=3)
    for y, r in zip(ys, rows):
        off = -0.8 if r[1] < 0 else 0.8
        ha = "right" if r[1] < 0 else "left"
        ax.text(r[1] + off, y, f"{r[1]:+.1f}%", ha=ha, va="center", fontsize=9.5, color=INK)
    ax.axvline(0, color=INK2, lw=1.2, zorder=4)
    ax.set_yticks(ys)
    ax.set_yticklabels([r[0] for r in rows], fontsize=9.5)
    ax.set_xlim(-42, 27)
    ax.set_xlabel("change in the use of force rate, 2019 against 2022, before any training")
    handles = [plt.Rectangle((0, 0), 1, 1, color=BLUE),
               plt.Rectangle((0, 0), 1, 1, color=INK3)]
    ax.legend(handles, ["later took the training", "never took it"],
              fontsize=9, frameon=False, loc="lower right")
    style(ax, ygrid=False)
    ax.grid(axis="x", color=GRID, lw=0.8, zorder=0)
    ax.set_axisbelow(True)
    title(ax, "Every one of these changes happened before the training existed",
          "Ten of the twelve were already falling. The program had not started.")
    fig.tight_layout()
    fig.savefig(HERE / "fig_05_already_changing.png", dpi=150)
    plt.close(fig)


def fig_06():
    """Topic 6. Put the comparison group on the same chart."""
    t = group_series(NO_A007)
    c = group_series(COMPARISON)
    fig, ax = plt.subplots(figsize=(10.8, 4.9))
    ax.plot(t.index, t.values, color=BLUE, lw=2.6, zorder=5, label="took the training")
    ax.plot(c.index, c.values, color=INK3, lw=2.6, zorder=4, label="did not")
    ax.axvline(pd.Timestamp(FULL), color=ORANGE, lw=2, zorder=3)
    ax.text(pd.Timestamp(FULL), 4.0, "  training in place", fontsize=9.5, color=ORANGE)
    ax.set_ylabel("use of force per 100 arrests")
    ax.set_ylim(1.5, 4.3)
    ax.legend(fontsize=9.5, frameon=False, loc="lower left")
    style(ax)
    title(ax, "The same chart, with somebody to compare against",
          "Both lines fall. Only the gap between them is about the training.")
    fig.tight_layout()
    fig.savefig(HERE / "fig_06_comparison_group.png", dpi=150)
    plt.close(fig)


def fig_07():
    """Topic 7. What makes a comparison group good or bad."""
    fig, (a1, a2) = plt.subplots(1, 2, figsize=(13.0, 4.9))

    t = group_series(TREATED)
    good = group_series(COMPARISON)
    bad = group_series(["A006"])
    for ax, other, lab, ok, note in [
            (a1, good, "all seven comparison agencies", True,
             "seven agencies, moving steadily, so the gap after means something"),
            (a2, bad, "Orrindale on its own", False,
             "eight officers, so the line swings for reasons nobody can name")]:
        ax.plot(t.index, t.values, color=BLUE, lw=2.6, zorder=5, label="took the training")
        ax.plot(other.index, other.values, color=AQUA if ok else ORANGE, lw=2.6,
                zorder=4, label=lab)
        ax.axvline(pd.Timestamp(FULL), color=INK3, lw=1.6, ls="--", zorder=3)
        ax.set_ylim(1.2, 4.6)
        ax.set_ylabel("use of force per 100 arrests")
        ax.legend(fontsize=9, frameon=False, loc="lower left")
        style(ax)
        title(ax, "A comparison you can use" if ok else "A comparison you cannot", note)
    fig.tight_layout()
    fig.savefig(HERE / "fig_07_good_comparison.png", dpi=150)
    plt.close(fig)


def fig_08():
    """Topic 8. The two by two, drawn."""
    tr = F[F["agency_id"].isin(TREATED)]
    ct = F[F["agency_id"].isin(COMPARISON)]
    tb, ta = rate(tr[tr["period"] == "before"]), rate(tr[tr["period"] == "after"])
    cb, ca = rate(ct[ct["period"] == "before"]), rate(ct[ct["period"] == "after"])

    fig, ax = plt.subplots(figsize=(10.8, 5.2))
    x = [0, 1]
    ax.plot(x, [tb, ta], color=BLUE, lw=3, marker="o", ms=11, zorder=5,
            label="took the training")
    ax.plot(x, [cb, ca], color=INK3, lw=3, marker="o", ms=11, zorder=5, label="did not")
    expected = tb * (ca / cb)
    ax.plot(x, [tb, expected], color=AQUA, lw=3, ls="--", marker="o", ms=10, zorder=4,
            label="where the trained agencies would have landed")
    ax.annotate("", xy=(1.0, ta), xytext=(1.0, expected),
                arrowprops=dict(arrowstyle="<->", color=ORANGE, lw=2.4))
    ax.text(1.04, (ta + expected) / 2,
            f"the effect\n{100 * (ta / expected - 1):+.1f}%",
            fontsize=11, color=ORANGE, weight="bold", va="center")
    for v, c in [(tb, BLUE), (cb, INK3)]:
        ax.text(-0.04, v, f"{v:.2f}", ha="right", va="center", fontsize=10, color=c)
    for v, c, dy in [(ta, BLUE, -0.115), (ca, INK3, -0.115), (expected, AQUA, 0.09)]:
        ax.text(1.0, v + dy, f"{v:.2f}", ha="center", va="center", fontsize=10, color=c)
    ax.set_xticks(x)
    ax.set_xticklabels(["before the training", "after it was in place"], fontsize=10)
    ax.set_xlim(-0.22, 1.42)
    ax.set_ylim(1.7, 3.9)
    ax.set_ylabel("use of force per 100 arrests")
    ax.legend(fontsize=9, frameon=False, loc="lower left")
    style(ax)
    title(ax, "Two differences: what changed, minus what would have changed anyway",
          "Much closer than 33 percent, and still not right. Topic 9 finds the reason.")
    fig.tight_layout()
    fig.savefig(HERE / "fig_08_two_differences.png", dpi=150)
    plt.close(fig)



def _did(trained_ids, comparison_ids):
    t = F[F["agency_id"].isin(trained_ids)]
    c = F[F["agency_id"].isin(comparison_ids)]
    tb, ta = rate(t[t["period"] == "before"]), rate(t[t["period"] == "after"])
    cb, ca = rate(c[c["period"] == "before"]), rate(c[c["period"] == "after"])
    return 100 * ((ta / tb) / (ca / cb) - 1)


def fig_09():
    """Topic 9. One agency was not moving with the others, before anything happened."""
    fig, (a1, a2) = plt.subplots(1, 2, figsize=(13.4, 5.0),
                                 gridspec_kw={"width_ratios": [1.35, 1]})

    pre_end = pd.Timestamp("2023-07-01")
    for ids, col, lab, lw in [(NO_A007, BLUE, "the other four that took the training", 2.6),
                              (COMPARISON, INK3, "the seven that did not", 2.6),
                              (["A007"], ORANGE, "Summit County, which also took it", 2.8)]:
        s = group_series(ids)
        s = s[s.index <= pre_end]
        a1.plot(s.index, s.values, color=col, lw=lw, zorder=5 if col == ORANGE else 4,
                label=lab)
    a1.text(pd.Timestamp("2019-08-01"), 2.14,
            "Summit County is already pulling away,\nand the training does not exist yet",
            fontsize=9.5, color=ORANGE)
    a1.set_ylabel("use of force per 100 arrests")
    a1.set_ylim(2.0, 4.3)
    a1.legend(fontsize=8.5, frameon=False, loc="upper right")
    style(a1)
    title(a1, "The years before the program started",
          "Two of the three lines move together. One does not.")

    steps = [("before and after,\nthe trained agencies", -33.1, ORANGE),
             ("minus what happened\nto everybody else", _did(TREATED, COMPARISON), ORANGE),
             ("minus the agency that\nwas not moving with them",
              _did(NO_A007, COMPARISON), AQUA)]
    ys = np.arange(len(steps))[::-1]
    for (lab, v, c), yy in zip(steps, ys):
        a2.barh(yy, v, color=c, height=0.42, zorder=3)
        a2.text(v - 1.0, yy, f"{v:+.1f}%", ha="right", va="center", fontsize=11,
                color=INK, weight="bold")
    a2.axvline(-12.0, color=INK, lw=2, ls="--", zorder=5)
    a2.text(-12.6, -0.72, "the truth ", fontsize=9.5, color=INK, ha="right")
    a2.set_yticks(ys)
    a2.set_yticklabels([s[0] for s in steps], fontsize=9)
    a2.set_xlim(-40, 2)
    a2.set_ylim(-1.0, 2.55)
    a2.set_xlabel("estimated change in the use of force rate")
    style(a2, ygrid=False)
    a2.grid(axis="x", color=GRID, lw=0.8, zorder=0)
    a2.set_axisbelow(True)
    title(a2, "Two corrections, in order",
          "Each one removes something that was not the training.")

    fig.tight_layout()
    fig.savefig(HERE / "fig_09_moving_together.png", dpi=150)
    plt.close(fig)


def fig_10():
    """Topic 10. A comparison agency that was quietly treated too."""
    correct = _did(NO_A007, [a for a in COMPARISON])
    rows = [("nobody in the comparison\ngroup was trained", correct, AQUA, "")]
    for aid in ["A003", "A008", "A012"]:
        rest = [a for a in COMPARISON if a != aid]
        rows.append((f"{SHORT[aid]} was trained too,\nand nobody recorded it",
                     _did(NO_A007 + [aid], rest), ORANGE,
                     f"{profile.loc[profile.agency_id == aid, 'sworn_officers'].iloc[0]:.0f} officers"))

    fig, ax = plt.subplots(figsize=(11.6, 5.0))
    ys = np.arange(len(rows))[::-1]
    for (lab, v, c, note), yy in zip(rows, ys):
        ax.barh(yy, v, color=c, height=0.44, zorder=3)
        ax.text(v - 0.45, yy, f"{v:+.1f}%", ha="right", va="center", fontsize=11,
                color=INK, weight="bold")
        if note:
            ax.text(0.6, yy, note, ha="left", va="center", fontsize=9, color=INK2)
    ax.axvline(-12.0, color=INK, lw=2, ls="--", zorder=5)
    ax.text(-12.4, -0.78, "the truth ", fontsize=9.5, color=INK, ha="right")
    ax.set_yticks(ys)
    ax.set_yticklabels([r[0] for r in rows], fontsize=9.5)
    ax.set_xlim(-17, 6)
    ax.set_ylim(-1.05, 3.55)
    ax.set_xlabel("estimated change in the use of force rate")
    style(ax, ygrid=False)
    ax.grid(axis="x", color=GRID, lw=0.8, zorder=0)
    ax.set_axisbelow(True)
    title(ax, "What one contaminated comparison agency costs",
          "The bigger the agency that leaks, the more of the effect disappears.")
    fig.tight_layout()
    fig.savefig(HERE / "fig_10_contamination.png", dpi=150)
    plt.close(fig)


def _early_late():
    """For the seven untrained agencies: rate in 2019 to mid 2020, and in 2022 to mid 2023."""
    out = {}
    for aid in COMPARISON:
        g = F[F["agency_id"] == aid]
        e = g[g["year_month"] < "2020-07"]
        l = g[(g["year_month"] >= "2022-07") & (g["year_month"] < "2023-07")]
        out[aid] = (rate(e), rate(l))
    return out


def fig_11():
    """Topic 11. Regression to the mean, among agencies that received nothing."""
    d = _early_late()
    order = sorted(d, key=lambda a: -d[a][0])
    fig, (a1, a2) = plt.subplots(1, 2, figsize=(13.4, 5.0),
                                 gridspec_kw={"width_ratios": [1.25, 1]})

    for i, aid in enumerate(order):
        e, l = d[aid]
        c = ORANGE if i < 3 else (BLUE if i >= len(order) - 3 else INK3)
        a1.plot([0, 1], [e, l], color=c, lw=2.4, marker="o", ms=8, zorder=4)
        dy = 0.0
        for other in order[:i]:
            if abs(d[other][0] - e) < 0.045:
                dy = -0.05
        a1.text(-0.04, e + dy, SHORT[aid], ha="right", va="center", fontsize=9, color=c)
    a1.set_xticks([0, 1])
    a1.set_xticklabels(["2019 to mid 2020", "2022 to mid 2023"], fontsize=10)
    a1.set_xlim(-0.62, 1.12)
    a1.set_ylabel("use of force per 100 arrests")
    a1.text(1.02, 3.2, "the three that\nstarted highest", fontsize=9, color=ORANGE)
    a1.text(1.02, 1.93, "the three that\nstarted lowest", fontsize=9, color=BLUE)
    style(a1)
    title(a1, "Seven agencies, none of which took any program",
          "The ones at the top came down. The ones at the bottom did not.")

    hi = np.mean([100 * (d[a][1] / d[a][0] - 1) for a in order[:3]])
    lo = np.mean([100 * (d[a][1] / d[a][0] - 1) for a in order[-3:]])
    a2.bar([0, 1], [hi, lo], color=[ORANGE, BLUE], width=0.5, zorder=3)
    for x, v in [(0, hi), (1, lo)]:
        a2.text(x, v + (0.9 if v > 0 else -1.6), f"{v:+.1f}%", ha="center",
                fontsize=12, color=INK, weight="bold")
    a2.axhline(0, color=INK2, lw=1.2, zorder=4)
    a2.set_xticks([0, 1])
    a2.set_xticklabels(["started highest", "started lowest"], fontsize=10)
    a2.set_ylim(-17, 12)
    a2.set_ylabel("change in the use of force rate")
    style(a2)
    title(a2, f"A gap of {abs(hi - lo):.0f} points, with no program anywhere",
          "Being at the top is itself a reason to improve.")

    fig.tight_layout()
    fig.savefig(HERE / "fig_11_regression_to_mean.png", dpi=150)
    plt.close(fig)


def fig_12():
    """Topic 12. The two groups match on everything except the thing that matters."""
    p = profile.copy()
    p["grp"] = np.where(p["agency_id"].isin(TREATED), "trained", "not")
    rows = [("sworn officers", "sworn_officers"),
            ("population served", "population_served"),
            ("violent crime rate", "violent_crime_rate_per_1000"),
            ("property crime rate", "property_crime_rate_per_1000"),
            ("public safety budget share", "budget_share_public_safety_pct"),
            ("use of force rate before the program", "pre_program_uof_per_100_arrests")]
    ratios, labs = [], []
    for lab, col in rows:
        a = p[p["grp"] == "trained"][col].mean()
        b = p[p["grp"] == "not"][col].mean()
        ratios.append(a / b)
        labs.append(lab)

    fig, ax = plt.subplots(figsize=(11.8, 4.8))
    ys = np.arange(len(labs))[::-1]
    for r, yy, lab in zip(ratios, ys, labs):
        far = abs(r - 1) > 0.25
        c = ORANGE if far else INK3
        ax.plot([1, r], [yy, yy], color=c, lw=2.4, zorder=3)
        ax.scatter([r], [yy], s=110, color=c, zorder=5)
        ax.text(r + 0.022, yy, f"{r:.2f}", va="center", fontsize=10,
                color=INK, weight="bold" if far else "normal")
    ax.axvline(1.0, color=INK2, lw=1.6, zorder=4)
    ax.text(1.0, -0.78, "identical on average", fontsize=9.5, color=INK2, ha="center")
    ax.set_yticks(ys)
    ax.set_yticklabels(labs, fontsize=10)
    ax.set_xlim(0.72, 1.58)
    ax.set_ylim(-1.05, 5.5)
    ax.set_xlabel("trained agencies divided by agencies that were not trained")
    style(ax, ygrid=False)
    ax.grid(axis="x", color=GRID, lw=0.8, zorder=0)
    ax.set_axisbelow(True)
    title(ax, "The two groups, compared on everything in the file",
          "Alike on every characteristic anyone would check, except one.")
    fig.tight_layout()
    fig.savefig(HERE / "fig_12_who_participated.png", dpi=150)
    plt.close(fig)


def fig_13():
    """Topic 13. A program that does not exist, evaluated two ways."""
    base = profile.set_index("agency_id")["pre_program_uof_per_100_arrests"]
    ranked = sorted(COMPARISON, key=lambda a: -base[a])
    worst, best = ranked[:3], ranked[-3:]

    rows = []
    for lab, pick, c in [("the three worst performers", worst, ORANGE),
                         ("the three best performers", best, BLUE)]:
        rest = [a for a in COMPARISON if a not in pick]
        rows.append((lab, _did(pick, rest), c, ", ".join(SHORT[a] for a in pick)))

    fig, ax = plt.subplots(figsize=(11.8, 4.7))
    ys = [1, 0]
    for (lab, v, c, who), yy in zip(rows, ys):
        ax.barh(yy, v, color=c, height=0.36, zorder=3)
        off = -0.45 if v < 0 else 0.45
        ha = "right" if v < 0 else "left"
        ax.text(v + off, yy, f"{v:+.1f}%", ha=ha, va="center", fontsize=12,
                color=INK, weight="bold")
        ax.text(-13.4, yy - 0.32, who, fontsize=8.5, color=INK2, va="center")
    ax.axvline(0, color=INK, lw=2, ls="--", zorder=5)
    ax.text(0.25, -0.62, "the true effect of a program nobody received",
            fontsize=9.5, color=INK)
    ax.set_yticks(ys)
    ax.set_yticklabels([r[0] for r in rows], fontsize=10.5)
    ax.set_xlim(-14, 14)
    ax.set_ylim(-0.85, 1.6)
    ax.set_xlabel("what a difference in differences reports")
    style(ax, ygrid=False)
    ax.grid(axis="x", color=GRID, lw=0.8, zorder=0)
    ax.set_axisbelow(True)
    title(ax, "Choose the worst performers and you manufacture an effect",
          "None of these seven agencies received anything. Choose the best and the sign flips.")
    fig.tight_layout()
    fig.savefig(HERE / "fig_13_picking_winners.png", dpi=150)
    plt.close(fig)


def fig_14():
    """Topic 14. Splitting the observed change into its two parts, in rate units."""
    t = F[F["agency_id"].isin(NO_A007)]
    c = F[F["agency_id"].isin(COMPARISON)]
    tb, ta = rate(t[t["period"] == "before"]), rate(t[t["period"] == "after"])
    cb, ca = rate(c[c["period"] == "before"]), rate(c[c["period"] == "after"])
    mid = tb * (ca / cb)                      # where the statewide decline alone lands them

    fig, ax = plt.subplots(figsize=(11.4, 5.0))
    vals = [tb, mid, ta]
    cols = [INK3, ORANGE, AQUA]
    labs = ["before the training",
            "where the statewide\ndecline alone puts them",
            "where they actually\nended up"]
    ax.bar([0, 1, 2], vals, color=cols, width=0.5, zorder=3)
    for x, v in zip([0, 1, 2], vals):
        ax.text(x, v + 0.20, f"{v:.2f}", ha="center", fontsize=12, color=INK,
                weight="bold")

    ax.annotate("", xy=(1, mid + 0.02), xytext=(0.5, tb + 0.02),
                arrowprops=dict(arrowstyle="->", color=ORANGE, lw=2.2))
    ax.text(0.52, tb + 0.30,
            f"everything that happened\nto every agency: {100 * (ca / cb - 1):+.1f}%",
            fontsize=9.5, color=ORANGE)
    ax.annotate("", xy=(2, ta + 0.02), xytext=(1.5, mid + 0.02),
                arrowprops=dict(arrowstyle="->", color=AQUA, lw=2.2))
    ax.text(1.52, mid + 0.30,
            f"what is left for the\ntraining: {100 * (ta / mid - 1):+.1f}%",
            fontsize=9.5, color=AQUA)

    ax.set_xticks([0, 1, 2])
    ax.set_xticklabels(labs, fontsize=10)
    ax.set_ylim(0, 4.6)
    ax.set_ylabel("use of force per 100 arrests")
    style(ax)
    title(ax, "One observed change, two causes",
          f"The whole fall is {100 * (ta / tb - 1):+.1f}%. Most of it is not the training.")
    fig.tight_layout()
    fig.savefig(HERE / "fig_14_confounding.png", dpi=150)
    plt.close(fig)


if __name__ == "__main__":
    for fn in (fig_01, fig_02, fig_03, fig_04, fig_05, fig_06, fig_07, fig_08,
               fig_09, fig_10, fig_11, fig_12, fig_13, fig_14):
        fn()
        print("built", fn.__name__)
