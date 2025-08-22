from pathlib import Path
import logging
import json
import pandas as pd
from sklearn.metrics import r2_score, mean_squared_error
import matplotlib.pyplot as plt

def evaluate_model(model, final_path, preds_path):
    log = logging.getLogger(__name__)
    metrics_path = Path("data/outputs/metrics.json")
    figs = []

    r2, rmse = None, None
    try:
        if preds_path and Path(preds_path).exists():
            df = pd.read_csv(preds_path)
            if {"rent", "predicted_rent"}.issubset(df.columns) and df["rent"].notna().any():
                r2 = float(r2_score(df["rent"], df["predicted_rent"]))
                rmse = float(mean_squared_error(df["rent"], df["predicted_rent"], squared=False))
    except Exception:
        log.exception("Metric computation failed")

    metrics_path.write_text(json.dumps({"r2": r2, "rmse": rmse}, indent=2))
    log.info(f"Metrics saved to {metrics_path}")

    # Predicted vs Actual scatter
    try:
        if preds_path and Path(preds_path).exists():
            df = pd.read_csv(preds_path)
            if {"rent", "predicted_rent"}.issubset(df.columns):
                plt.figure()
                plt.scatter(df["rent"], df["predicted_rent"])
                plt.xlabel("Actual Rent")
                plt.ylabel("Predicted Rent")
                fig_path = Path("data/outputs/pred_vs_actual.png")
                plt.savefig(fig_path, bbox_inches="tight")
                plt.close()
                figs.append(fig_path)
                log.info(f"Saved {fig_path}")
    except Exception:
        log.exception("Evaluation plot failed")

    return metrics_path, figs
