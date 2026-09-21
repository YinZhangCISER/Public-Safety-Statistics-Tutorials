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


if __name__ == "__main__":
    for fn in (fig_01, fig_02, fig_03, fig_04, fig_05, fig_06, fig_07, fig_08):
        fn()
        print("built", fn.__name__)
