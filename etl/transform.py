from pathlib import Path

def run_transform(paths):
    out = Path("data/processed/clean.csv")
    out.parent.mkdir(parents=True, exist_ok=True)
    out.touch()
    return out
