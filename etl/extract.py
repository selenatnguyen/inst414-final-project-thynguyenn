from pathlib import Path

def run_extract():
    base = Path("data/extracted")
    base.mkdir(parents=True, exist_ok=True)
    return {"acs": base / "acs.csv", "rent": base / "rent.csv"}
