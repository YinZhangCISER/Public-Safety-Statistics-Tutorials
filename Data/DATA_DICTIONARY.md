# Data Dictionary

**The Synthetic WADEPS Teaching Dataset**

*Developed by Yin Zhang, PhD, Assistant Professor, Data Analytics Program, Department of Mathematics and Statistics, Washington State University, for the Washington Data Exchange for Public Safety (WADEPS) through the Center for Interdisciplinary Statistical Education and Research (CISER).*

---

## What this dataset is

Five CSV files describing twelve fictional Washington State law enforcement agencies over 90 months, from January 2019 through June 2026. Every tutorial in this repository uses these files and nothing else, so you only ever have to learn one dataset.

**The data are entirely synthetic.** No record describes a real agency, a real officer, or a real person. What is real is the *shape* of the data: field names, category labels, the number of categories, and the marginal distributions are modeled on the Washington Data Exchange for Public Safety (WADEPS) so that code you write here runs unchanged against a real WADEPS extract.

The dataset also contains deliberately planted patterns with known answers. See [GROUND_TRUTH.md](GROUND_TRUTH.md).

## Regenerating the files

```bash
python generate_synthetic_wadeps.py      # rewrites all five CSV files
python verify_ground_truth.py            # confirms the planted patterns survive
```

The random number generator is seeded, so both scripts produce identical results on every machine.

---

## File 1. `agency_profile.csv`

One row per agency. Twelve rows. This is the file you join to when you need agency context.

| Column | Type | Description |
|---|---|---|
| `agency_id` | text | Stable identifier, `A001` through `A012`. The join key for every other file. |
| `agency_name` | text | Fictional agency name. |
| `agency_type` | text | One of `Municipal Police`, `County Sheriff`, `Campus Police`, `Tribal Police`. |
| `sworn_officers` | integer | Number of sworn officers. Ranges from 8 to 902. |
| `population_served` | integer | Residents in the jurisdiction. For the campus agency this is the student population. |
| `region` | text | `West` or `East`, splitting the state at the mountains. |
| `pre_program_uof_per_100_arrests` | float | Average use of force per 100 arrests before July 2023. Computed from the data, not an input. |
| `deescalation_training` | text | `Yes` if the agency adopted the training program, `No` otherwise. |
| `training_start_month` | text | `2023-07` for adopting agencies, empty otherwise. |
| `violent_crime_rate_per_1000` | float | Jurisdiction violent crime rate. |
| `property_crime_rate_per_1000` | float | Jurisdiction property crime rate. |
| `budget_share_public_safety_pct` | float | Share of the local budget going to the police or sheriff office. |
| `county_population` | integer | Population of the surrounding county. |
| `county_budget_millions` | float | Total county budget in millions of dollars. |
| `cfs_data_submitted` | text | `Yes` or `Partial`. Two small agencies have incomplete call for service submission, which mirrors the real coverage gap among smaller and more rural agencies. |

## File 2. `agency_monthly.csv`

One row per agency per month. This is the main table for the time series tutorials.

| Column | Type | Description |
|---|---|---|
| `agency_id` | text | Join key. |
| `agency_name` | text | Convenience copy. |
| `agency_type` | text | Convenience copy. |
| `year_month` | text | `YYYY-MM`. Parse with `pd.PeriodIndex(df["year_month"], freq="M")`. |
| `sworn_officers` | integer | Staffing that month. |
| `total_cfs` | integer | Total calls for service. Equals the sum of `n_calls` in `cfs_monthly.csv` for the same agency and month. |
| `n_arrests` | integer | Arrests. The natural exposure denominator for use of force. |
| `n_uof` | integer | Use of force incidents. Equals the number of rows in `use_of_force.csv` for the same agency and month. |
| `provisional` | 0 or 1 | 1 for the two most recent months, whose records are still being entered. Exclude these before fitting anything. |
| `uof_per_100_arrests` | float | `100 * n_uof / n_arrests`. Blank when there were no arrests. |

Rows are **absent**, not blank, for the three months one agency failed to submit. Reindexing to a complete calendar is the first exercise in the Intermediate series.

## File 3. `cfs_monthly.csv`

One row per agency per month per incident type per incident detail. About 34,000 rows.

| Column | Type | Description |
|---|---|---|
| `agency_id`, `agency_name`, `agency_type` | text | Agency identifiers. |
| `year_month` | text | `YYYY-MM`. |
| `incident_type` | text | One of the eight WADEPS incident types. |
| `incident_detail` | text | One of the 32 WADEPS incident details, always paired with its parent type. |
| `n_calls` | integer | Calls for service in that cell. |

### The WADEPS incident classification

Incident type and incident detail are always assigned as a pair. The 32 details below match the classification established by the Attorney General's Office Advisory Board. Labels are reproduced exactly as WADEPS publishes them, punctuation included, so that code written here transfers without edits.

| Response category | Incident type | Incident details |
|---|---|---|
| Crime Control | Offense Against Person | Assault; Homicide; Rape; Robbery; Civil order violation; Offense Against Person - Other |
| Crime Control | Property Offense | Arson; Burglary; Theft; Mischief; Trespassing; Vehicle theft/prowl; Property Offense - Other |
| Order Maintenance | Public Order Offense | Public disturbance; Drug related; Sex related; Weapon related; Transit related; Public Order Offense - Other |
| Order Maintenance | Vehicle Stop | DUI; Accident; Moving violation; Non-moving violation; Vehicle Stop - Other |
| Order Maintenance | Pedestrian Stop | Pedestrian Stop |
| Public Service | Civil Caretaking | Mental health / wellness check; Civil infraction; Eviction order enforcement; Domestic order enforcement; Civil Caretaking - Other |
| Public Service | Warrant | Warrant |
| Other | Other | Other |

As in the real system, the generalized labels carry heavy weight. Categories ending in "Other", plus Civil Caretaking, account for close to half of all calls. That is a known limitation of the 32 category system, not an artifact of this dataset, and it is the subject of a data quality discussion in several modules.

## File 4. `cfs_monthly_by_type.csv`

The same information rolled up to incident type, for tutorials that do not need the detail level. Columns: `agency_id`, `year_month`, `incident_type`, `n_calls`.

## File 5. `use_of_force.csv`

One row per use of force incident. About 22,000 rows. Use this file when a tutorial needs individual records rather than monthly counts.

| Column | Type | Description |
|---|---|---|
| `incident_id` | text | Unique, `UOF######`. |
| `subject_id` | text | Subject identifier. A small share of subjects appear more than once, so de duplicate on this field before counting people rather than events. |
| `agency_id`, `agency_name`, `agency_type` | text | Agency identifiers. |
| `incident_date` | text | `YYYY-MM-DD`. |
| `year_month` | text | `YYYY-MM`, for joining to the monthly files. |
| `incident_type` | text | The WADEPS incident type that brought the officer into contact. |
| `contact_reason` | text | `Public Request for Service`, `Individual Officer/Unit Initiated`, `Agency Request for Service`, `Planned Activities`, `Unknown`. |
| `incident_location` | text | `City`, `Unincorporated Area`, `State Highway`, `Interstate Highway`. |
| `subject_race` | text | Nine categories including `Unknown`. |
| `subject_sex` | text | `Male`, `Female`, `Unknown`. |
| `subject_age_group` | text | Six bands from `Under 18` to `55 and over`. |
| `subject_perceived_armed` | text | `Yes` or `No`. |
| `subject_weapon` | text | Weapon found or used, or `Not Applicable` when the subject was not perceived as armed. |
| `subject_perceived_impaired` | text | `Yes` or `No`. Alcohol, drugs, or altered mental health status. |
| `subject_resistance` | text | `None`, `Passive Resistance`, `Active Resistance`, `Assaultive`, `Threat of Deadly Force`. |
| `type_of_force` | text | Highest level of force applied: `Physical Control`, `Chemical Agent`, `ECW`, `Impact Weapon`, `K9`, `Less Lethal Projectile`, `Firearm Discharge`, `Vehicle Intervention`. |
| `subject_injury` | text | `Yes` or `No`. |
| `officer_injury` | text | `Yes` or `No`. |
| `officer_race` | text | Eight categories including `Unknown`. |
| `officer_sex` | text | `Male` or `Female`. |

Marginal distributions of the subject, officer, resistance, force, contact and location fields follow the published WADEPS reportable use of force baseline to within about two percentage points. The fields are drawn with realistic conditional structure: the level of force depends on the level of resistance, and the chance of injury depends on the level of force.

---

## Two calibration choices worth knowing

**Use of force is more common here than reportable force is in reality.** Incidents run at roughly 3 percent of arrests, which matches the rate used throughout the Beginner series and leaves mid sized agencies with enough monthly events to analyze. WADEPS defines *reportable* force more narrowly, and real counts are far rarer. What changes when counts are that rare is the subject of Advanced Module 9.

**Call volume is calibrated to the real thing.** Officers generate roughly 550 calls for service per year each, which is what the statewide WADEPS totals imply.

---

## Loading the data

```python
import pandas as pd

BASE = "https://raw.githubusercontent.com/<owner>/<repo>/main/Data/"

monthly = pd.read_csv(BASE + "agency_monthly.csv")
monthly["date"] = pd.PeriodIndex(monthly["year_month"], freq="M").to_timestamp()

# Always drop the provisional months before fitting anything.
monthly = monthly[monthly["provisional"] == 0]
```

---

*Questions, corrections, or suggestions: yin.zhang@wsu.edu*
