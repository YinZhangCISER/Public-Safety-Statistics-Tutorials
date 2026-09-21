"""
Check that the synthetic dataset really contains the patterns it claims to.

Every pattern documented in Data/GROUND_TRUTH.md is recovered here from the
published CSV files alone, using the same tools the tutorials teach, and is
then compared against the value that was deliberately built in. A change to
the generator that quietly breaks a teaching example will show up here as a
FAIL.

A note on method. Use of force counts are small in small agencies, so an
unweighted average of agency level rates is dominated by the noisiest
agencies. Everything below therefore pools counts, or fits a Poisson
regression with the number of arrests as the exposure offset. That choice is
itself one of the lessons of this series.

    python verify_ground_truth.py

Developed by Yin Zhang, PhD, Assistant Professor, Data Analytics Program,
Department of Mathematics and Statistics, Washington State University, for
the Washington Data Exchange for Public Safety (WADEPS) through the Center
for Interdisciplinary Statistical Education and Research (CISER).
"""

from pathlib import Path

import numpy as np
import pandas as pd
import statsmodels.api as sm
import statsmodels.formula.api as smf

HERE = Path(__file__).resolve().parent

# ---- the answer key, copied from the generator ---------------------------
TREATED = ["A001", "A002", "A004", "A007", "A010"]
VIOLATOR = "A007"
PROGRAM_START = "2023-07"
SETTLED_FROM = "2023-11"
TRUE_EFFECT_PCT = -12.0
TRUE_TREND_PCT = 100 * (np.exp(-0.050) - 1)      # about -4.88 percent a year
TRUE_VIOLATOR_TREND_PCT = 100 * (np.exp(-0.130) - 1)   # about -12.19
TRUE_SEASON_AMPLITUDE = 0.20
OUTLIER = ("A002", "2021-06")
GAP = ("A009", ["2022-03", "2022-04", "2022-05"])
DEFCHANGE = ("A003", "2023-01")
PROVISIONAL = {"2026-05": 0.72, "2026-06": 0.45}
SMALL_AGENCY = "A006"

results = []


def check(name, ok, detail):
    results.append(ok)
    print(f"   [{'PASS' if ok else 'FAIL'}] {name}: {detail}")


def poisson(formula, data):
    return smf.glm(formula, data=data, family=sm.families.Poisson(),
                   offset=np.log(data["n_arrests"])).fit()


def pct(x):
    return 100.0 * (np.exp(x) - 1.0)


m = pd.read_csv(HERE / "agency_monthly.csv")
cfs = pd.read_csv(HERE / "cfs_monthly_by_type.csv")
uof = pd.read_csv(HERE / "use_of_force.csv")

m["date"] = pd.PeriodIndex(m["year_month"], freq="M").to_timestamp()
m["month_num"] = m["date"].dt.month
m["t"] = (m["date"].dt.year - 2019) * 12 + m["date"].dt.month - 1
m["treated"] = m["agency_id"].isin(TREATED).astype(int)
m["post"] = (m["year_month"] >= PROGRAM_START).astype(int)

full = m[m["provisional"] == 0].copy()
clean = full[~((full["agency_id"] == OUTLIER[0]) & (full["year_month"] == OUTLIER[1]))].copy()

print("=" * 76)
print("SYNTHETIC WADEPS DATASET, GROUND TRUTH VERIFICATION")
print("=" * 76)

print("\n1. SECULAR TREND")
sub = clean[clean["treated"] == 0]
f = poisson("n_uof ~ t", sub)
est = pct(12 * f.params["t"])
lo, hi = [pct(12 * v) for v in f.conf_int().loc["t"]]
check("control agencies decline at the built in rate",
      lo <= TRUE_TREND_PCT <= hi,
      f"estimate {est:+.2f} percent a year [{lo:+.2f}, {hi:+.2f}], built in {TRUE_TREND_PCT:+.2f}")

print("\n2. SEASONALITY")
pool = sub.groupby("month_num").apply(lambda d: d["n_uof"].sum() / d["n_arrests"].sum())
idx = pool / pool.mean()
print("   month index :", " ".join(f"{v:.2f}" for v in idx.values))
check("July is the peak month", idx.idxmax() == 7, f"peak at month {idx.idxmax()}, value {idx.max():.2f}")
check("amplitude is close to the built in value",
      abs((idx.max() - idx.min()) / 2 - TRUE_SEASON_AMPLITUDE) < 0.12,
      f"half range {(idx.max()-idx.min())/2:.2f}, built in {TRUE_SEASON_AMPLITUDE:.2f}")

print("\n3. CAMPUS AGENCY FOLLOWS THE ACADEMIC CALENDAR")
camp = cfs[cfs["agency_id"] == "A010"].groupby("year_month")["n_calls"].sum().reset_index()
camp["month_num"] = pd.PeriodIndex(camp["year_month"], freq="M").month
ci = camp.groupby("month_num")["n_calls"].mean() / camp["n_calls"].mean()
print("   month index :", " ".join(f"{v:.2f}" for v in ci.values))
check("A010 peaks in September and bottoms out in summer",
      ci.idxmax() == 9 and ci.idxmin() in (6, 7),
      f"peak month {ci.idxmax()}, trough month {ci.idxmin()}")

print("\n4. DOCUMENTED OUTLIER")
a2 = full[full["agency_id"] == OUTLIER[0]]
z = (a2["n_uof"] - a2["n_uof"].median()) / a2["n_uof"].std()
check("the largest spike in A002 is the documented unrest month",
      a2.loc[z.idxmax(), "year_month"] == OUTLIER[1] and z.max() > 4,
      f"{a2.loc[z.idxmax(),'year_month']}, n_uof={a2.loc[z.idxmax(),'n_uof']}, z={z.max():.1f}")

print("\n5. REPORTING GAP")
absent = sorted(set(m["year_month"]) - set(m[m["agency_id"] == GAP[0]]["year_month"]))
check("A009 is missing exactly the three migration months", absent == GAP[1], f"{absent}")

print("\n6. CLASSIFICATION DEFINITION CHANGE")
a3 = cfs[cfs["agency_id"] == DEFCHANGE[0]].pivot_table(
    index="year_month", columns="incident_type", values="n_calls", aggfunc="sum")
po = a3["Public Order Offense"] / a3.sum(axis=1)
ot = a3["Other"] / a3.sum(axis=1)
tot = a3.sum(axis=1)
b_po, a_po = po[po.index < DEFCHANGE[1]].mean(), po[po.index >= DEFCHANGE[1]].mean()
b_ot, a_ot = ot[ot.index < DEFCHANGE[1]].mean(), ot[ot.index >= DEFCHANGE[1]].mean()
b_t, a_t = tot[tot.index < DEFCHANGE[1]].mean(), tot[tot.index >= DEFCHANGE[1]].mean()
check("Public Order share jumps at the reclassification date", a_po / b_po > 1.4,
      f"share {b_po:.3f} to {a_po:.3f}, up {100*(a_po-b_po)/b_po:+.1f} percent")
check("the Other category falls by the matching amount", a_ot / b_ot < 0.8,
      f"share {b_ot:.3f} to {a_ot:.3f}, down {100*(a_ot-b_ot)/b_ot:+.1f} percent")
check("total call volume is unaffected", abs(a_t / b_t - 1) < 0.10,
      f"monthly total {b_t:.0f} to {a_t:.0f}")

print("\n7. PROVISIONAL MONTHS")
tt = m.groupby("year_month")["total_cfs"].sum()
base = tt[(tt.index >= "2025-05") & (tt.index <= "2026-04")].mean()
for ym, target in PROVISIONAL.items():
    ratio = tt[ym] / base
    check(f"{ym} is incomplete as designed", abs(ratio - target) < 0.10,
          f"{tt[ym]:,} calls, {100*ratio:.1f} percent of the trailing year, target {100*target:.0f}")

print("\n8. PROGRAM EFFECT")
tr = clean[clean["treated"] == 1]
nb = tr[tr["post"] == 0]["n_uof"].sum() / tr[tr["post"] == 0]["n_arrests"].sum()
na = tr[tr["post"] == 1]["n_uof"].sum() / tr[tr["post"] == 1]["n_arrests"].sum()
naive = 100 * (na - nb) / nb
check("a naive before and after badly overstates the effect", naive < TRUE_EFFECT_PCT - 8,
      f"naive {naive:+.1f} percent against a true {TRUE_EFFECT_PCT:+.1f} percent")

did = clean[clean["agency_id"] != VIOLATOR].copy()
did["settled"] = ((did["treated"] == 1) & (did["year_month"] >= SETTLED_FROM)).astype(int)
did["phasein"] = ((did["treated"] == 1) & (did["year_month"] >= PROGRAM_START)
                  & (did["year_month"] < SETTLED_FROM)).astype(int)
fit = poisson("n_uof ~ C(agency_id) + C(year_month) + settled + phasein", did)
est = pct(fit.params["settled"])
lo, hi = [pct(v) for v in fit.conf_int().loc["settled"]]
check("difference in differences recovers the true effect", lo <= TRUE_EFFECT_PCT <= hi,
      f"estimate {est:+.1f} percent [{lo:+.1f}, {hi:+.1f}], true {TRUE_EFFECT_PCT:+.1f}")
check("the phase in months show a smaller partial effect",
      TRUE_EFFECT_PCT < pct(fit.params["phasein"]) < 0,
      f"phase in estimate {pct(fit.params['phasein']):+.1f} percent")

bad = clean.copy()
bad["settled"] = ((bad["treated"] == 1) & (bad["year_month"] >= SETTLED_FROM)).astype(int)
bad["phasein"] = ((bad["treated"] == 1) & (bad["year_month"] >= PROGRAM_START)
                  & (bad["year_month"] < SETTLED_FROM)).astype(int)
fb = poisson("n_uof ~ C(agency_id) + C(year_month) + settled + phasein", bad)
check("keeping the pre trend violator in biases the estimate away from the truth",
      pct(fb.params["settled"]) < est - 1.0,
      f"with A007 included {pct(fb.params['settled']):+.1f} percent against {est:+.1f} without it")

print("\n9. PARALLEL TRENDS")
pre = clean[clean["post"] == 0]
ok_group = [a for a in TREATED if a not in (VIOLATOR, "A010")]
f_tr = poisson("n_uof ~ t", pre[pre["agency_id"].isin(ok_group)])
f_ct = poisson("n_uof ~ t", pre[pre["treated"] == 0])
d_tr, d_ct = pct(12 * f_tr.params["t"]), pct(12 * f_ct.params["t"])
check("treated and control pre period trends are close",
      abs(d_tr - d_ct) < 2.5, f"treated {d_tr:+.2f}, control {d_ct:+.2f} percent a year")
f_v = poisson("n_uof ~ t", pre[pre["agency_id"] == VIOLATOR])
lo, hi = [pct(12 * v) for v in f_v.conf_int().loc["t"]]
check("A007 was already declining much faster before the program",
      hi < d_ct,
      f"A007 {pct(12*f_v.params['t']):+.2f} [{lo:+.2f}, {hi:+.2f}] excludes the control trend "
      f"of {d_ct:+.2f}, built in {TRUE_VIOLATOR_TREND_PCT:+.2f}")
print(f"   note: A010 has only {pre[pre['agency_id']=='A010']['n_uof'].sum()} pre period events, "
      f"too few for a reliable agency level slope. That is deliberate.")

print("\n10. SMALL AGENCY VOLATILITY")
a6 = full[full["agency_id"] == SMALL_AGENCY]["n_uof"]
check("A006 monthly counts are dominated by sampling noise",
      a6.mean() < 2.0 and (a6 == 0).mean() > 0.25,
      f"mean {a6.mean():.2f}, max {a6.max()}, {100*(a6==0).mean():.0f} percent of months at zero")

print("\n11. INTERNAL CONSISTENCY")
ev = uof.groupby(["agency_id", "year_month"]).size().rename("events").reset_index()
chk = m.merge(ev, on=["agency_id", "year_month"], how="left").fillna({"events": 0})
check("the event file and the monthly file agree everywhere",
      (chk["n_uof"] != chk["events"]).sum() == 0,
      f"{(chk['n_uof'] != chk['events']).sum()} disagreeing rows")
roll = cfs.groupby(["agency_id", "year_month"])["n_calls"].sum().rename("cfs").reset_index()
chk2 = m.merge(roll, on=["agency_id", "year_month"], how="left")
check("the call file rolls up to the monthly totals",
      (chk2["total_cfs"] != chk2["cfs"]).sum() == 0,
      f"{(chk2['total_cfs'] != chk2['cfs']).sum()} disagreeing rows")
check("every incident detail in the taxonomy appears",
      pd.read_csv(HERE / "cfs_monthly.csv")["incident_detail"].nunique() == 32,
      f"{pd.read_csv(HERE / 'cfs_monthly.csv')['incident_detail'].nunique()} distinct details")

print("\n12. EVENT ATTRIBUTES MATCH THE PUBLISHED WADEPS BASELINE")
for col, value, target in [("subject_race", "White", 39.6), ("subject_sex", "Male", 86.9),
                           ("subject_resistance", "Active Resistance", 44.6),
                           ("contact_reason", "Public Request for Service", 54.0),
                           ("subject_perceived_armed", "Yes", 40.0)]:
    got = 100 * (uof[col] == value).mean()
    check(f"{col} equal to {value}", abs(got - target) < 2.0,
          f"{got:.1f} percent against a target of {target:.1f}")

print("\n" + "=" * 76)
print(f"{sum(results)} of {len(results)} checks passed")
print("=" * 76)
