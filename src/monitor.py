import pandas as pd
from evidently import Report
from evidently.presets import DataDriftPreset
from src.feature_engineering import FeatureEngineer

def check_data_drift():
    print("Running Evidently AI Data Drift Analysis for Dubai Smart Grid...")
    
    # 1. Reference Data
    reference_dates = pd.date_range(start="2026-01-01", periods=100, freq="h")
    ref_df = pd.DataFrame(index=reference_dates)
    fe = FeatureEngineer(country="US", mode="train")
    reference_data = fe.transform(ref_df)
    
    # 2. Current / Production Data
    current_dates = pd.date_range(start="2026-06-01", periods=100, freq="h")
    curr_df = pd.DataFrame(index=current_dates)
    current_data = fe.transform(curr_df)
    
    if 'temperature_celsius' in current_data.columns:
        current_data['temperature_celsius'] += 5.0
    else:
        raise KeyError("Column 'temperature_celsius' missing after feature transformation!")

    # 3. Generate Report
    drift_report = Report(metrics=[
        DataDriftPreset(),
    ])
    
    drift_report.run(reference_data=reference_data, current_data=current_data)
    
    # Print available methods to see exact save function name in v0.7.23
    methods = [m for m in dir(drift_report) if 'save' in m or 'html' in m or 'export' in m]
    print("Available export/save methods:", methods)
    
    # Try saving using the first matching method found
    if hasattr(drift_report, "save_html"):
        drift_report.save_html("reports/data_drift_report.html")
    elif hasattr(drift_report, "save"):
        drift_report.save("reports/data_drift_report.html")
    elif hasattr(drift_report, "export_html"):
        drift_report.export_html("reports/data_drift_report.html")
    else:
        print("Report generated successfully in memory!")

    print("Success! Data Drift monitoring completed.")

if __name__ == "__main__":
    import os
    os.makedirs("reports", exist_ok=True)
    check_data_drift()
