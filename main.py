from etl.extract import run_extract
from etl.transform import run_transform
from etl.load import run_load
from analysis.model import train_model
from analysis.evaluate import evaluate_model
from vis.visualizations import make_figures

def main():
    raw_paths = run_extract()
    processed_path = run_transform(raw_paths)
    final_path = run_load(processed_path)
    model, preds_path = train_model(final_path)
    evaluate_model(model, final_path, preds_path)
    make_figures(final_path, preds_path)
    print("Pipeline staged successfully.")

if __name__ == "__main__":
    main()
