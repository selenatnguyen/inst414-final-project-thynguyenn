from pathlib import Path
import logging
import shutil

def run_load(processed_path):
    log = logging.getLogger(__name__)
    final_path = Path("data/processed/final.csv")
    final_path.parent.mkdir(parents=True, exist_ok=True)
    try:
        if processed_path:
            shutil.copy(processed_path, final_path)
        else:
            final_path.touch()
        log.info(f"Final dataset at {final_path}")
    except Exception:
        log.exception("Failed to save final dataset")
    return final_path

