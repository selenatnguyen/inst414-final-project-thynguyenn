import logging
from etl.extract import run_extract
from etl.transform import run_transform
from etl.load import run_load
from analysis.model import train_model
from analysis.evaluate import evaluate_model
from vis.visualizations import make_figures

logging.basicConfig(
    filename="project.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def main():
    logging.info("Pipeline start")
    try:
        raw_paths = run_extract()
        logging.info(f"Extracted: {raw_paths}")
    except Exception:
        logging.exception("Extract failed")
        raw_paths = {}

    try:
        processed_path = run_transform(raw_paths)
        logging.info(f"Processed: {processed_path}")
    except Exception:
        logging.exception("Transform failed")
        processed_path = None

    try:
        final_path = run_load(processed_path)
        logging.info(f"Loaded: {final_path}")
    except Exception:
        logging.exception("Load failed")
        final_path = None

    try:
        model, preds_path = train_model(final_path)
        logging.info(f"Model OK. Predictions: {preds_path}")
    except Exception:
        logging.exception("Model training failed")
        model, preds_path = None, None

    try:
        metrics_path, figs = evaluate_model(model, final_path, preds_path)
        logging.info(f"Metrics: {metrics_path}; Eval figs: {figs}")
    except Exception:
        logging.exception("Evaluation failed")

    try:
        make_figures(final_path, preds_path)
    except Exception:
        logging.exception("Visualization failed")

    logging.info("Pipeline end")

if __name__ == "__main__":
    main()
