from pathlib import Path

def evaluate_model(model, final_path, preds_path):
    metrics = Path("data/outputs/metrics.json")
    metrics.write_text('{"r2": null, "rmse": null}')
    return metrics

