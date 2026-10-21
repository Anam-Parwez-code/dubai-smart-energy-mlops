# Dubai Smart Grid Enterprise MLOps Pipeline ⚡🇦🇪

An enterprise-grade, production-level MLOps pipeline modeled after Dubai's smart grid infrastructure, featuring automated feature engineering, model training, FastAPI inference, data drift monitoring, orchestration, and cloud infrastructure provisioning.

## 🚀 Architecture & Core Components

- **Feature Engineering (`src/feature_engineering.py`):** Simulates Dubai extreme weather conditions (diurnal temperature curves & humidity shifts) to test model robustness and energy demand forecasting.
- **Model Training (`src/train.py`):** Trains a robust energy consumption forecasting model using `scikit-learn` and serializes it into `energy_model.pkl`.
- **FastAPI Inference Server (`src/app.py`):** Production-ready REST API serving real-time energy predictions with interactive Swagger documentation.
- **Evidently AI Monitoring (`src/monitor.py`):** Automated data drift detection tracking temperature anomalies and generating comprehensive audit reports.
- **Apache Airflow Orchestration (`airflow/dags/smart_grid_dag.py`):** Automated daily DAG scheduling model training and drift checks.
- **Infrastructure as Code (`terraform/main.tf`):** Provisions enterprise-grade Azure Kubernetes Service (AKS) clusters for cloud scalability.
- **Containerization (`Dockerfile`, `docker-compose.yml`):** Fully dockerized application ready for multi-environment deployment.

---

## 📂 Project Structure

```text
dubai-smart-energy-mlops/
│
├── airflow/
│   └── dags/
│       └── smart_grid_dag.py    # Airflow orchestration DAG
├── reports/                     # Evidently AI data drift reports
├── src/
│   ├── app.py                   # FastAPI inference server
│   ├── feature_engineering.py   # Dubai weather & feature pipeline
│   ├── monitor.py               # Evidently data drift analysis
│   └── train.py                 # Model training script
├── terraform/
│   └── main.tf                  # Azure AKS infrastructure code
├── Dockerfile                   # Container configuration
├── docker-compose.yml           # Multi-container setup
├── requirements.txt             # Python dependencies
└── README.md                    # Project documentation
