# day2/databricks_transform.py
# PySpark demo script / notebook cell equivalents
# In Databricks: paste cells or run locally with a Spark session

from pyspark.sql import SparkSession
from pyspark.sql import functions as F
from pyspark.sql.types import StructType, StructField, IntegerType, DateType, DecimalType

spark = SparkSession.builder.appName("DemoDatabricksTransform").getOrCreate()

# Optional: define schema based on MCP context (example)
schema = StructType([
    StructField("sale_id", IntegerType(), True),
    StructField("sale_date", DateType(), True),
    StructField("region_id", IntegerType(), True),
    StructField("product_id", IntegerType(), True),
    StructField("amount", DecimalType(18,2), True)
])

# Replace <path> with your demo CSV path or DBFS mount
csv_path = "/dbfs/FileStore/demo/sales.csv"  # or use mocked DataFrame below

# If you have CSV
# df = spark.read.schema(schema).option("header", True).csv(csv_path)

# For demo, create DataFrame from sample data
data = [
    (1, "2026-05-01", 10, 100, 1200.50),
    (2, "2026-05-02", 20, 101, 980.00),
    (3, "2026-06-01", 10, 100, 700.00),
]
df = spark.createDataFrame(data, ["sale_id", "sale_date", "region_id", "product_id", "amount"])
df = df.withColumn("sale_date", F.to_date("sale_date", "yyyy-MM-dd"))
df = df.withColumn("amount", F.col("amount").cast("double"))

# Add year_month and aggregate
df = df.withColumn("year_month", F.date_format("sale_date", "yyyy-MM"))
agg_df = df.groupBy("region_id", "year_month").agg(
    F.sum("amount").alias("total_sales"),
    F.avg("amount").alias("avg_sale")
).orderBy("year_month", "region_id")

agg_df.show(truncate=False)

# Optionally write to Delta table
# agg_df.write.format("delta").mode("overwrite").save("/mnt/delta/sales_monthly")