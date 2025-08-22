from pathlib import Path

def run_load(processed_path):
    final_path = Path("data/processed/final.csv")
    final_path.touch()
    return final_path
