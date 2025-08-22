from pathlib import Path
import logging
import pandas as pd

def run_transform(paths):
    log = logging.getLogger(__name__)
    out = Path("data/processed/clean.csv")
    out.parent.mkdir(parents=True, exist_ok=True)

    acs = paths.get("acs")
    rent = paths.get("rent")

    df = pd.DataFrame()
    if acs and Path(acs).exists():
        df = pd.read_csv(acs)
    if rent and Path(rent).exists():
        rent_df = pd.read_csv(rent).rename(columns={"rent": "rent_dept"})
        df = df.merge(rent_df, on="neighborhood_id", how="left") if not df.empty else rent_df

    if df.empty:
        log.warning("No data available in transform; writing empty clean.csv")
        df.to_csv(out, index=False)
        return out

    df = df.drop_duplicates()
    for col in ["median_income", "household_size", "renters_pct", "rent"]:
        if col not in df.columns:
            df[col] = pd.NA

    df["rent_to_income_ratio"] = (df["rent"] / df["median_income"]).round(4)
    df.to_csv(out, index=False)

    eda_out = Path("data/outputs/eda_summary.csv")
    eda_out.parent.mkdir(parents=True, exist_ok=True)
    df.describe(include="all").to_csv(eda_out)
    log.info(f"Wrote {out} and {eda_out}")
    return out

