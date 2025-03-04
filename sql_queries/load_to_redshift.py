import psycopg2
import config.config as cfg

# Connect to Redshift
conn = psycopg2.connect(
    dbname=cfg.REDSHIFT_DB,
    user=cfg.REDSHIFT_USER,
    password=cfg.REDSHIFT_PASSWORD,
    host=cfg.REDSHIFT_HOST,
    port='5439'
)
cur = conn.cursor()

# Load Data into Redshift Table
query = f"""
COPY sales_data FROM 's3://{cfg.S3_BUCKET}/processed_data/'
IAM_ROLE '{cfg.REDSHIFT_IAM_ROLE}'
FORMAT AS PARQUET;
"""
cur.execute(query)
conn.commit()

cur.close()
conn.close()
