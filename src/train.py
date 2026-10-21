from pathlib import Path
import joblib 
import pandas as pd
from sklearn.metrics import mean_absolute_error, mean_squared_error, root_mean_squared_error

from src.data_loader import EnergyDataLoader
from src.feature_engineering import FeatureEngineer
from src.models import get_models


def train_and_evaluate(data_path: Path):
    loader = EnergyDataLoader(data_path)
    df = loader.load_and_preprocess()

    fe = FeatureEngineer(country="US", mode="train")
    df = fe.transform(df)

    X = df.drop(columns=["load"])
    y = df["load"]

    split_date = "2000-01-01"
    X_train = X[X.index < split_date]
    X_test = X[X.index >= split_date]
    y_train = y[y.index < split_date]
    y_test = y[y.index >= split_date]

    results = {}
    best_model = None 
    best_rmse = float("inf") 
    best_model_name = None 

    for name, model in get_models().items():
        model.fit(X_train, y_train)
        preds = model.predict(X_test)

        mae = mean_absolute_error(y_test, preds)
        # rmse = mean_squared_error(y_test, preds, squared=False)
        rmse = root_mean_squared_error(y_test, preds)

        results[name] = {
            "MAE": mae,
            "RMSE": rmse,
        }

        print(f"{name} -> MAE: {mae:.2f}, RMSE: {rmse:.2f}")

        if rmse < best_rmse:
            best_rmse = rmse
            best_model = model
            best_model_name = name

    model_dir = Path("models")
    model_dir.mkdir(exist_ok=True)
    model_path = model_dir / "energy_model.pkl"

    joblib.dump(best_model, model_path)
    print(f"Best model ({best_model_name}) saved to {model_path}")

    return results


if __name__ == "__main__":
    train_and_evaluate(
        Path("data/raw/PJM_Load_hourly.csv")
    )
