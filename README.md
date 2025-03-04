# Enterprise Data Warehouse & ETL Pipeline

## Overview
This project is a scalable ETL pipeline using Apache Airflow, Apache Spark, AWS Redshift, Python, and SQL.

## Features
- **Automated ETL** using **Airflow DAGs**.
- **Data Transformation** with **Apache Spark**.
- **Data Warehouse Storage** in **AWS Redshift**.
- **AWS S3 for Staging Data**.

## Installation

### 1️⃣ Install Dependencies
```sh
pip install apache-airflow pyspark psycopg2-binary boto3
```

### 2️⃣ Start Docker Services
```sh
docker-compose up -d
```

### 3️⃣ Run Airflow Scheduler & Webserver
```sh
airflow scheduler & airflow webserver
```

### 4️⃣ Trigger ETL Pipeline
```sh
airflow dags trigger enterprise_etl_pipeline
```

## API Endpoints
- **Airflow DAG** → Automates ETL process.
- **Spark Job** → Reads, processes, and writes data to S3.
- **Redshift Loader** → Loads transformed data into AWS Redshift.

## Technologies Used
- **Apache Airflow** → Workflow orchestration.
- **Apache Spark** → Big data processing.
- **AWS Redshift** → Cloud data warehousing.
- **AWS S3** → Cloud storage for staging.
- **Docker** → Containerized services.

## Author
Shantanu Fuke
