from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from datetime import datetime
import subprocess

# Define default args
default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2024, 10, 1),
    'retries': 1,
}

# Define DAG
dag = DAG(
    'enterprise_etl_pipeline',
    default_args=default_args,
    description='ETL pipeline using Airflow, Spark, and Redshift',
    schedule_interval='@daily',
)

# Task 1: Run Spark Transformation Job
def run_spark_job():
    subprocess.run(["spark-submit", "/opt/airflow/spark_jobs/transform_data.py"], check=True)

spark_task = PythonOperator(
    task_id='run_spark_job',
    python_callable=run_spark_job,
    dag=dag,
)

# Task 2: Load Processed Data into Redshift
def load_to_redshift():
    subprocess.run(["python3", "/opt/airflow/sql_queries/load_to_redshift.py"], check=True)

redshift_task = PythonOperator(
    task_id='load_to_redshift',
    python_callable=load_to_redshift,
    dag=dag,
)

# Define Task Dependencies
spark_task >> redshift_task
