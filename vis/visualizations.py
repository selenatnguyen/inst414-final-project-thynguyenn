from pathlib import Path
import logging
import pandas as pd
import matplotlib.pyplot as plt

def make_figures(final_path, preds_path):
    log = logging.getLogger(__name__)
    try:
        if final_path and Path(final_path).exists():
            df = pd.read_csv(final_path)
            if "rent_to_income_ratio" in df.columns:
                plt.figure()
                df["rent_to_income_ratio"].dropna().hist()
                plt.xlabel("Rent-to-Income Ratio")
                plt.ylabel("Count")
                out = Path("data/outputs/rti_hist.png")
                plt.savefig(out, bbox_inches="tight")
                plt.close()
                log.info(f"Saved {out}")
        return True
    except Exception:
        log.exception("vis.make_figures failed")
        return False


