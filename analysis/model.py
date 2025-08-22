from pathlib import Path
import logging
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

def train_model(final_path):
    log = logging.getLogger(__name__)
    preds = Path("data/outputs/predictions.csv")
    preds.parent.mkdir(parents=True, exist_ok=True)

    df = pd.read_csv(final_path) if final_path and Path(final_path).exists() else pd.DataFrame()
    if df.empty:
        log.warning("Final dataset empty; writing empty predictions.")
        preds.write_text("")
        return None, preds

    features = ["median_income", "household_size", "renters_pct"]
    for f in features:
        if f not in df.columns:
            df[f] = 0
    df = df.dropna(subset=["rent"])
    X, y = df[features], df["rent"]

    if len(df) < 2:
        log.warning("Not enough rows to train; writing baseline predictions.")
        df["predicted_rent"] = y if not y.empty else 0
        df[["neighborhood_id", "rent", "predicted_rent"]].to_csv(preds, index=False)
        return None, preds

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)
    model = LinearRegression()
    model.fit(X_train, y_train)
    df["predicted_rent"] = model.predict(X)
    df[["neighborhood_id", "rent", "predicted_rent"]].to_csv(preds, index=False)
    log.info(f"Predictions saved to {preds}")
    return model, preds
