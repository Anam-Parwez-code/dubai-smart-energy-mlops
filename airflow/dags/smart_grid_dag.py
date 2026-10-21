from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.bash import BashOperator

default_args = {
    'owner': 'anam-mlops-engineer',
    'depends_on_past': False,
    'email_on_failure': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

with DAG(
    'dubai_smart_grid_mlops_pipeline',
    default_args=default_args,
    description='Automated MLOps Pipeline for Dubai Smart Grid Energy Forecasting',
    schedule_interval='@daily',
    start_date=datetime(2026, 1, 1),
    catchup=False,
) as dag:

    # Task 1: Model Train karna
    train_model_task = BashOperator(
        task_id='train_energy_model',
        bash_command='cd /home/anam/dubai-smart-energy-mlops && PYTHONPATH=. python src/train.py',
    )

    # Task 2: Evidently AI se Data Drift check karna
    drift_check_task = BashOperator(
        task_id='run_data_drift_check',
        bash_command='cd /home/anam/dubai-smart-energy-mlops && PYTHONPATH=. python src/monitor.py',
    )

    # Pipeline Flow: Pehle Model Train hoga, fir Data Drift check chalega
    train_model_task >> drift_check_task
