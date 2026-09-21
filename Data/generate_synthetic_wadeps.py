"""
Synthetic WADEPS style public safety data generator.

This script produces the teaching dataset used by every tutorial in this
repository. The data are entirely synthetic. No record describes a real
agency, a real officer, or a real person. The field names, category labels
and category counts are modeled on the Washington Data Exchange for Public
Safety (WADEPS) so that a reader who learns a method here can apply the
same code to real WADEPS extracts without renaming anything.

The dataset has known ground truth deliberately built into it: a fixed
trend, a fixed seasonal shape, one documented outlier month, one reporting
gap, one classification definition change, one policy intervention with a
known effect size and a known lag, and two provisional months at the end of
the series. Every tutorial can therefore check whether a method recovers the
answer that was put there on purpose. The answer key lives in
Data/GROUND_TRUTH.md.

Running this script reproduces the CSV files exactly, because the random
number generator is seeded.

    python generate_synthetic_wadeps.py

Developed by Yin Zhang, PhD, Assistant Professor, Data Analytics Program,
Department of Mathematics and Statistics, Washington State University, for
the Washington Data Exchange for Public Safety (WADEPS) through the Center
for Interdisciplinary Statistical Education and Research (CISER).
Contact: yin.zhang@wsu.edu
"""

import argparse
from pathlib import Path

import numpy as np
import pandas as pd

SEED = 1
START_MONTH = "2019-01"
END_MONTH = "2026-06"

# ---------------------------------------------------------------------------
# 1. Agencies
# ---------------------------------------------------------------------------
# Twelve fictional agencies spanning the range of sizes and agency types
# found in Washington State. "uof_base" is the baseline probability that an
# arrest involves a reportable use of force, before trend, season, program
# effect and random variation are applied.

AGENCIES = [
    # agency_id, name, type, sworn, population, uof_base, annual_trend, region
    ("A001", "Riverbend Police Department",        "Municipal Police", 412, 210000, 0.038, -0.050, "West"),
    ("A002", "Cedar Falls Police Department",      "Municipal Police", 188,  96000, 0.041, -0.050, "West"),
    ("A003", "Harbor Point Police Department",     "Municipal Police",  95,  48000, 0.029, -0.050, "West"),
    ("A004", "Millgate Police Department",         "Municipal Police",  54,  27000, 0.040, -0.050, "East"),
    ("A005", "Northgate Police Department",        "Municipal Police",  31,  15500, 0.027, -0.050, "East"),
    ("A006", "Elkhorn Police Department",          "Municipal Police",   8,   3900, 0.026, -0.050, "East"),
    ("A007", "Summit County Sheriff's Office",     "County Sheriff",   268, 175000, 0.037, -0.130, "West"),
    ("A008", "Lakeshore County Sheriff's Office",  "County Sheriff",   141,  92000, 0.028, -0.050, "West"),
    ("A009", "Prairie County Sheriff's Office",    "County Sheriff",    38,  21000, 0.025, -0.050, "East"),
    ("A010", "Pinecrest State University Police",  "Campus Police",     46,  29000, 0.039, -0.050, "West"),
    ("A011", "Two Rivers Tribal Police",           "Tribal Police",     18,   7400, 0.030, -0.050, "East"),
    ("A012", "Grandview Police Department",        "Municipal Police", 902, 480000, 0.030, -0.050, "West"),
]

# The agency whose use of force rate was already falling faster than
# everyone else before the program began. Including it in a difference in
# differences comparison violates the parallel trends assumption.
PRE_TREND_VIOLATOR = "A007"

# Agencies that adopted the de escalation training program, and the month
# the program started. Selection was not random: the five agencies with the
# highest baseline use of force rates were chosen. That is what makes a
# naive before and after comparison misleading.
TREATED = ["A001", "A002", "A004", "A007", "A010"]
PROGRAM_START = "2023-07"
PROGRAM_TRUE_EFFECT = 0.12          # 12 percent reduction once fully in place
PROGRAM_PHASE_IN = [0.00, 0.25, 0.58, 0.83, 1.00]   # months 0 to 4 after start

# Documented one time event: civil unrest in Cedar Falls.
OUTLIER_AGENCY, OUTLIER_MONTH = "A002", "2021-06"
OUTLIER_UOF_MULTIPLIER = 4.0
OUTLIER_CFS_MULTIPLIER = 2.5

# Records management system migration: three months of data never submitted.
GAP_AGENCY = "A009"
GAP_MONTHS = ["2022-03", "2022-04", "2022-05"]

# Classification definition change: from this month the agency began routing
# calls that used to be labeled Other into Public Order Offense.
DEFCHANGE_AGENCY, DEFCHANGE_MONTH = "A003", "2023-01"
DEFCHANGE_SHARE_MOVED = 0.30

# Reporting lag: the two most recent months are incomplete.
PROVISIONAL = {"2026-05": 0.72, "2026-06": 0.45}

# ---------------------------------------------------------------------------
# 2. The WADEPS incident classification
# ---------------------------------------------------------------------------
# Eight incident types and thirty two incident details, matching the pairing
# established by the Attorney General's Office Advisory Board. The labels are
# reproduced exactly as WADEPS publishes them so that code written against
# this dataset also runs against real extracts.

TAXONOMY = {
    "Offense Against Person": [
        "Assault", "Homicide", "Rape", "Robbery",
        "Civil order violation", "Offense Against Person - Other",
    ],
    "Property Offense": [
        "Arson", "Burglary", "Theft", "Mischief",
        "Trespassing", "Vehicle theft/prowl", "Property Offense - Other",
    ],
    "Public Order Offense": [
        "Public disturbance", "Drug related", "Sex related",
        "Weapon related", "Transit related", "Public Order Offense - Other",
    ],
    "Vehicle Stop": [
        "DUI", "Accident", "Moving violation",
        "Non-moving violation", "Vehicle Stop - Other",
    ],
    "Pedestrian Stop": ["Pedestrian Stop"],
    "Civil Caretaking": [
        "Mental health / wellness check", "Civil infraction",
        "Eviction order enforcement", "Domestic order enforcement",
        "Civil Caretaking - Other",
    ],
    "Warrant": ["Warrant"],
    "Other": ["Other"],
}

# Within a type, how calls split across details. The generalized "Other"
# details carry heavy weight, reproducing the real WADEPS finding that
# catch all labels account for close to half of all calls for service.
DETAIL_WEIGHTS = {
    "Offense Against Person": [0.34, 0.01, 0.03, 0.06, 0.11, 0.45],
    "Property Offense": [0.02, 0.13, 0.26, 0.09, 0.09, 0.11, 0.30],
    "Public Order Offense": [0.27, 0.13, 0.04, 0.07, 0.05, 0.44],
    "Vehicle Stop": [0.07, 0.19, 0.42, 0.13, 0.19],
    "Pedestrian Stop": [1.00],
    "Civil Caretaking": [0.22, 0.14, 0.05, 0.10, 0.49],
    "Warrant": [1.00],
    "Other": [1.00],
}

# Share of an agency's calls falling in each incident type, by agency type.
# The Municipal Police column reproduces the statewide WADEPS distribution.
TYPE_SHARE = {
    "Municipal Police": {
        "Offense Against Person": 0.061, "Property Offense": 0.101,
        "Public Order Offense": 0.142, "Vehicle Stop": 0.195,
        "Pedestrian Stop": 0.027, "Civil Caretaking": 0.205,
        "Warrant": 0.019, "Other": 0.250,
    },
    "County Sheriff": {
        "Offense Against Person": 0.048, "Property Offense": 0.118,
        "Public Order Offense": 0.101, "Vehicle Stop": 0.262,
        "Pedestrian Stop": 0.012, "Civil Caretaking": 0.196,
        "Warrant": 0.023, "Other": 0.240,
    },
    "Campus Police": {
        "Offense Against Person": 0.031, "Property Offense": 0.147,
        "Public Order Offense": 0.121, "Vehicle Stop": 0.083,
        "Pedestrian Stop": 0.041, "Civil Caretaking": 0.288,
        "Warrant": 0.009, "Other": 0.280,
    },
    "Tribal Police": {
        "Offense Against Person": 0.072, "Property Offense": 0.094,
        "Public Order Offense": 0.131, "Vehicle Stop": 0.178,
        "Pedestrian Stop": 0.017, "Civil Caretaking": 0.258,
        "Warrant": 0.020, "Other": 0.230,
    },
}

# Calls per sworn officer per month, by agency type.
CALLS_PER_OFFICER = {
    "Municipal Police": 46.0, "County Sheriff": 38.0,
    "Campus Police": 28.0, "Tribal Police": 26.0,
}

# Seasonal amplitude and peak month for each incident type. A value of 0.18
# means calls run about 18 percent above the annual average at the peak and
# about 18 percent below it six months later.
SEASON = {
    "Offense Against Person": (0.22, 7), "Property Offense": (0.14, 8),
    "Public Order Offense": (0.20, 7), "Vehicle Stop": (0.10, 8),
    "Pedestrian Stop": (0.16, 7), "Civil Caretaking": (0.09, 1),
    "Warrant": (0.06, 5), "Other": (0.07, 7),
}

# Overdispersion of the count draws. Larger means closer to Poisson, that is,
# less month to month volatility on top of the deliberate patterns.
DISPERSION_CFS = 300.0
DISPERSION_ARRESTS = 250.0
DISPERSION_UOF = 150.0

# Campus police follow the academic calendar instead of the weather. Index 0
# is January. Quiet summers, busy September and October.
CAMPUS_SEASON = np.array(
    [1.05, 1.12, 1.02, 0.98, 0.72, 0.55, 0.52, 0.86, 1.34, 1.28, 1.10, 0.86]
)

# ---------------------------------------------------------------------------
# 3. Use of force event attributes
# ---------------------------------------------------------------------------
# Marginal distributions follow the published WADEPS reportable use of force
# baseline as closely as a synthetic dataset can.

SUBJECT_RACE = {
    "White": 0.396, "Unknown": 0.218, "Black or African American": 0.162,
    "Hispanic or Latino": 0.131, "Multiple Races/Ethnicities": 0.043,
    "American Indian or Alaska Native": 0.019, "Asian": 0.018,
    "Hawaiian or Pacific Islander": 0.011, "Middle Eastern or North African": 0.002,
}
SUBJECT_SEX = {"Male": 0.869, "Female": 0.126, "Unknown": 0.005}
SUBJECT_AGE = {
    "Under 18": 0.041, "18 to 24": 0.174, "25 to 34": 0.289,
    "35 to 44": 0.323, "45 to 54": 0.112, "55 and over": 0.061,
}
OFFICER_RACE = {
    "White": 0.448, "Unknown": 0.249, "Hispanic or Latino": 0.112,
    "Black or African American": 0.071, "Asian": 0.062,
    "American Indian or Alaska Native": 0.031,
    "Hawaiian or Pacific Islander": 0.018, "Multiple Races/Ethnicities": 0.009,
}
UOF_INCIDENT_TYPE = {
    "Offense Against Person": 0.386, "Property Offense": 0.213,
    "Vehicle Stop": 0.150, "Warrant": 0.088, "Public Order Offense": 0.075,
    "Civil Caretaking": 0.043, "Other": 0.032, "Pedestrian Stop": 0.012,
}
CONTACT_REASON = {
    "Public Request for Service": 0.540, "Individual Officer/Unit Initiated": 0.261,
    "Agency Request for Service": 0.131, "Planned Activities": 0.045,
    "Unknown": 0.023,
}
LOCATION = {
    "City": 0.753, "Unincorporated Area": 0.210,
    "State Highway": 0.024, "Interstate Highway": 0.013,
}
RESISTANCE = {
    "Active Resistance": 0.446, "Passive Resistance": 0.221,
    "Assaultive": 0.208, "Threat of Deadly Force": 0.041, "None": 0.084,
}
# Probability of each force type given the highest level of resistance.
FORCE_GIVEN_RESISTANCE = {
    "None":                  {"Physical Control": 0.82, "Chemical Agent": 0.03, "ECW": 0.05, "Impact Weapon": 0.02, "K9": 0.02, "Less Lethal Projectile": 0.02, "Firearm Discharge": 0.00, "Vehicle Intervention": 0.04},
    "Passive Resistance":    {"Physical Control": 0.86, "Chemical Agent": 0.04, "ECW": 0.04, "Impact Weapon": 0.02, "K9": 0.01, "Less Lethal Projectile": 0.01, "Firearm Discharge": 0.00, "Vehicle Intervention": 0.02},
    "Active Resistance":     {"Physical Control": 0.68, "Chemical Agent": 0.07, "ECW": 0.13, "Impact Weapon": 0.04, "K9": 0.03, "Less Lethal Projectile": 0.02, "Firearm Discharge": 0.01, "Vehicle Intervention": 0.02},
    "Assaultive":            {"Physical Control": 0.44, "Chemical Agent": 0.06, "ECW": 0.22, "Impact Weapon": 0.09, "K9": 0.06, "Less Lethal Projectile": 0.06, "Firearm Discharge": 0.05, "Vehicle Intervention": 0.02},
    "Threat of Deadly Force":{"Physical Control": 0.16, "Chemical Agent": 0.02, "ECW": 0.14, "Impact Weapon": 0.05, "K9": 0.07, "Less Lethal Projectile": 0.11, "Firearm Discharge": 0.42, "Vehicle Intervention": 0.03},
}
SUBJECT_INJURY_GIVEN_FORCE = {
    "Physical Control": 0.21, "Chemical Agent": 0.14, "ECW": 0.33,
    "Impact Weapon": 0.52, "K9": 0.78, "Less Lethal Projectile": 0.49,
    "Firearm Discharge": 0.71, "Vehicle Intervention": 0.44,
}
WEAPON_IF_ARMED = {
    "Firearm": 0.421, "Edged Object": 0.299, "Blunt Object": 0.103,
    "Vehicle": 0.024, "Projectile": 0.019, "Chemical Explosive": 0.018,
    "ECW": 0.004, "None Found": 0.112,
}


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def pick(rng, mapping, size):
    """Draw from a dictionary of category to probability."""
    keys = list(mapping.keys())
    probs = np.array(list(mapping.values()), dtype=float)
    probs = probs / probs.sum()
    return rng.choice(keys, size=size, p=probs)


def negbin(rng, mean, dispersion=6.0):
    """Negative binomial draw parameterized by its mean.

    Larger dispersion means the counts behave more like a Poisson variable.
    Smaller dispersion means more month to month volatility.
    """
    mean = np.maximum(mean, 1e-9)
    p = dispersion / (dispersion + mean)
    return rng.negative_binomial(dispersion, p)


def program_multiplier(agency_id, month_index, program_index):
    """Effect of the de escalation training program in a given month."""
    if agency_id not in TREATED:
        return 1.0
    elapsed = month_index - program_index
    if elapsed < 0:
        return 1.0
    phase = PROGRAM_PHASE_IN[min(elapsed, len(PROGRAM_PHASE_IN) - 1)]
    return 1.0 - PROGRAM_TRUE_EFFECT * phase


def build(outdir: Path):
    rng = np.random.default_rng(SEED)

    months = pd.period_range(START_MONTH, END_MONTH, freq="M")
    month_labels = [str(m) for m in months]
    n_months = len(months)
    program_index = month_labels.index(PROGRAM_START)

    profile = pd.DataFrame(
        AGENCIES,
        columns=["agency_id", "agency_name", "agency_type", "sworn_officers",
                 "population_served", "_uof_base", "_annual_trend", "region"],
    )

    cfs_rows = []
    monthly_rows = []
    uof_rows = []
    uof_counter = 0

    for _, ag in profile.iterrows():
        aid = ag["agency_id"]
        atype = ag["agency_type"]
        sworn = int(ag["sworn_officers"])
        uof_base = float(ag["_uof_base"])
        annual_trend = float(ag["_annual_trend"])

        # A stable agency level offset so that agencies are not identical
        # once the deliberate patterns are removed.
        agency_noise = rng.normal(0.0, 0.06)

        for t, ym in enumerate(month_labels):
            if aid == GAP_AGENCY and ym in GAP_MONTHS:
                continue

            month_num = int(ym[5:7])
            years_elapsed = t / 12.0
            trend = np.exp(annual_trend * years_elapsed + agency_noise)

            # ---- calls for service, by incident type and detail ----
            total_expected = sworn * CALLS_PER_OFFICER[atype] * (1.0 + 0.10 * years_elapsed / 7.0)
            type_counts = {}

            for itype, share in TYPE_SHARE[atype].items():
                amp, peak = SEASON[itype]
                if atype == "Campus Police":
                    seasonal = CAMPUS_SEASON[month_num - 1]
                else:
                    seasonal = 1.0 + amp * np.cos(2 * np.pi * (month_num - peak) / 12.0)

                mu = total_expected * share * seasonal
                if aid == OUTLIER_AGENCY and ym == OUTLIER_MONTH and itype == "Public Order Offense":
                    mu *= OUTLIER_CFS_MULTIPLIER
                type_counts[itype] = int(negbin(rng, mu, dispersion=DISPERSION_CFS))

            # Definition change: calls that used to be labeled Other are
            # relabeled Public Order Offense from a known month onward.
            if aid == DEFCHANGE_AGENCY and ym >= DEFCHANGE_MONTH:
                moved = int(round(type_counts["Other"] * DEFCHANGE_SHARE_MOVED))
                type_counts["Other"] -= moved
                type_counts["Public Order Offense"] += moved

            # Reporting lag on the most recent months.
            prov_factor = PROVISIONAL.get(ym, 1.0)
            if prov_factor < 1.0:
                for itype in type_counts:
                    type_counts[itype] = int(rng.binomial(type_counts[itype], prov_factor))

            for itype, count in type_counts.items():
                details = TAXONOMY[itype]
                weights = np.array(DETAIL_WEIGHTS[itype], dtype=float)
                weights = weights / weights.sum()
                split = rng.multinomial(count, weights)
                for detail, n in zip(details, split):
                    cfs_rows.append((aid, ag["agency_name"], atype, ym, itype, detail, int(n)))

            total_cfs = int(sum(type_counts.values()))

            # ---- arrests ----
            arrest_share = {"Municipal Police": 0.092, "County Sheriff": 0.081,
                            "Campus Police": 0.090, "Tribal Police": 0.076}[atype]
            n_arrests = int(negbin(rng, total_cfs * arrest_share, dispersion=DISPERSION_ARRESTS))

            # ---- reportable use of force ----
            uof_seasonal = 1.0 + 0.20 * np.cos(2 * np.pi * (month_num - 7) / 12.0)
            rate = uof_base * trend * uof_seasonal
            rate *= program_multiplier(aid, t, program_index)
            mu_uof = n_arrests * rate
            if aid == OUTLIER_AGENCY and ym == OUTLIER_MONTH:
                mu_uof *= OUTLIER_UOF_MULTIPLIER
            n_uof = int(negbin(rng, mu_uof, dispersion=DISPERSION_UOF))
            if prov_factor < 1.0:
                n_uof = int(rng.binomial(n_uof, prov_factor))

            monthly_rows.append(
                (aid, ag["agency_name"], atype, ym, sworn, total_cfs, n_arrests,
                 n_uof, int(prov_factor < 1.0))
            )

            # ---- one row per use of force event ----
            days_in_month = pd.Period(ym, freq="M").days_in_month
            for _ in range(n_uof):
                uof_counter += 1
                day = int(rng.integers(1, days_in_month + 1))
                resistance = pick(rng, RESISTANCE, 1)[0]
                force = pick(rng, FORCE_GIVEN_RESISTANCE[resistance], 1)[0]
                armed = bool(rng.random() < 0.40)
                weapon = pick(rng, WEAPON_IF_ARMED, 1)[0] if armed else "Not Applicable"
                injured = bool(rng.random() < SUBJECT_INJURY_GIVEN_FORCE[force])
                off_injured = bool(rng.random() < (0.24 if resistance == "Assaultive" else 0.09))
                uof_rows.append((
                    f"UOF{uof_counter:06d}",
                    f"S{int(rng.integers(1, 90000)):05d}",
                    aid, ag["agency_name"], atype,
                    f"{ym}-{day:02d}", ym,
                    pick(rng, UOF_INCIDENT_TYPE, 1)[0],
                    pick(rng, CONTACT_REASON, 1)[0],
                    pick(rng, LOCATION, 1)[0],
                    pick(rng, SUBJECT_RACE, 1)[0],
                    pick(rng, SUBJECT_SEX, 1)[0],
                    pick(rng, SUBJECT_AGE, 1)[0],
                    "Yes" if armed else "No",
                    weapon,
                    "Yes" if rng.random() < 0.75 else "No",
                    resistance, force,
                    "Yes" if injured else "No",
                    "Yes" if off_injured else "No",
                    pick(rng, OFFICER_RACE, 1)[0],
                    "Male" if rng.random() < 0.931 else "Female",
                ))

    # ---- assemble frames ----
    cfs = pd.DataFrame(cfs_rows, columns=[
        "agency_id", "agency_name", "agency_type", "year_month",
        "incident_type", "incident_detail", "n_calls"])

    monthly = pd.DataFrame(monthly_rows, columns=[
        "agency_id", "agency_name", "agency_type", "year_month",
        "sworn_officers", "total_cfs", "n_arrests", "n_uof", "provisional"])
    monthly["uof_per_100_arrests"] = (
        100.0 * monthly["n_uof"] / monthly["n_arrests"].replace(0, np.nan)).round(3)

    uof = pd.DataFrame(uof_rows, columns=[
        "incident_id", "subject_id", "agency_id", "agency_name", "agency_type",
        "incident_date", "year_month", "incident_type", "contact_reason",
        "incident_location", "subject_race", "subject_sex", "subject_age_group",
        "subject_perceived_armed", "subject_weapon", "subject_perceived_impaired",
        "subject_resistance", "type_of_force", "subject_injury",
        "officer_injury", "officer_race", "officer_sex"])

    # ---- agency profile with context variables ----
    prof = profile.drop(columns=["_uof_base", "_annual_trend"]).copy()
    pre = monthly[monthly["year_month"] < PROGRAM_START]
    pre_rate = (pre.groupby("agency_id")
                  .apply(lambda d: 100.0 * d["n_uof"].sum() / max(d["n_arrests"].sum(), 1))
                  .round(3))
    prof["pre_program_uof_per_100_arrests"] = prof["agency_id"].map(pre_rate)
    prof["deescalation_training"] = np.where(prof["agency_id"].isin(TREATED), "Yes", "No")
    prof["training_start_month"] = np.where(prof["agency_id"].isin(TREATED), PROGRAM_START, "")

    rng2 = np.random.default_rng(SEED + 1)
    prof["violent_crime_rate_per_1000"] = np.round(
        2.1 + 4.4 * (prof["population_served"] / 480000) + rng2.normal(0, 0.45, len(prof)), 2).clip(0.4)
    prof["property_crime_rate_per_1000"] = np.round(
        12.0 + 21.0 * (prof["population_served"] / 480000) + rng2.normal(0, 2.2, len(prof)), 2).clip(3.0)
    prof["budget_share_public_safety_pct"] = np.round(
        np.where(prof["agency_type"] == "Municipal Police", 29.0, 21.0)
        + rng2.normal(0, 3.1, len(prof)), 1).clip(8.0, 46.0)
    prof["county_population"] = (prof["population_served"] * rng2.uniform(1.8, 4.6, len(prof))).astype(int)
    prof["county_budget_millions"] = np.round(prof["county_population"] * rng2.uniform(0.0016, 0.0031, len(prof)), 1)
    prof["cfs_data_submitted"] = np.where(prof["agency_id"].isin(["A006", "A009"]), "Partial", "Yes")

    # ---- write ----
    outdir.mkdir(parents=True, exist_ok=True)
    cfs.to_csv(outdir / "cfs_monthly.csv", index=False)
    monthly.to_csv(outdir / "agency_monthly.csv", index=False)
    uof.to_csv(outdir / "use_of_force.csv", index=False)
    prof.to_csv(outdir / "agency_profile.csv", index=False)

    rollup = (cfs.groupby(["agency_id", "year_month", "incident_type"], as_index=False)["n_calls"]
                 .sum())
    rollup.to_csv(outdir / "cfs_monthly_by_type.csv", index=False)

    print(f"months            : {n_months} ({month_labels[0]} to {month_labels[-1]})")
    print(f"agencies          : {len(prof)}")
    print(f"agency_monthly    : {len(monthly):,} rows")
    print(f"cfs_monthly       : {len(cfs):,} rows")
    print(f"cfs_monthly_by_type: {len(rollup):,} rows")
    print(f"use_of_force      : {len(uof):,} rows")
    print(f"total calls       : {cfs['n_calls'].sum():,}")
    print(f"written to        : {outdir}")


if __name__ == "__main__":
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--outdir", default=str(Path(__file__).resolve().parent),
                    help="directory to write the CSV files into")
    args = ap.parse_args()
    build(Path(args.outdir))
