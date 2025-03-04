from pyspark.sql import SparkSession
from pyspark.sql.functions import col
import config.config as cfg

# Initialize Spark Session
spark = SparkSession.builder.appName("ETL-Transformation").getOrCreate()

# Load Raw Data from S3
df = spark.read.csv(f"s3a://{cfg.S3_BUCKET}/raw_data.csv", header=True, inferSchema=True)

# Data Transformation
df_transformed = df.withColumn("amount", col("amount") * 1.1)  # Apply transformation

# Write Transformed Data Back to S3
df_transformed.write.mode("overwrite").parquet(f"s3a://{cfg.S3_BUCKET}/processed_data/")

spark.stop()
