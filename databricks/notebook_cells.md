# Databricks Genie Code Demo — Notebook cells (paste into a Databricks notebook)

## Cell 1 (Markdown)
# Databricks Genie Code Demo
Objective: Demonstrate AI-assisted PySpark, SQL, and pipeline scaffolding for a simple sales aggregation use case.

## Cell 2 (Markdown)
Prereqs: Databricks workspace & cluster, sample sales data in DBFS or mount.

## Cell 3 (Python)
from pyspark.sql import functions as F

data = [
    ("2026-05-01", "East", "ProductA", 1200.50),
    ("2026-05-02", "West", "ProductB", 980.00),
    ("2026-05-10", "East", "ProductC", 450.75),
    ("2026-06-01", "North", "ProductA", 700.00),
    ("2026-06-05", "West", "ProductA", 1300.20),
    ("2026-06-12", "East", "ProductB", 640.00),
]

columns = ["sale_date", "region", "product", "amount"]
df = spark.createDataFrame(data, columns)
display(df)

## Cell 4 (Markdown)
Prompt to Genie Code:
"Given DataFrame `df`, generate PySpark code to parse sale_date as date, create year_month, aggregate total sales by region and month, and return DataFrame `agg_df`."

## Cell 5 (Python)
transformed_df = (
    df.withColumn("sale_date", F.to_date("sale_date"))
      .withColumn("year_month", F.date_format("sale_date", "yyyy-MM"))
)

agg_df = (
    transformed_df.groupBy("region", "year_month")
    .agg(F.sum("amount").alias("total_sales"))
    .orderBy("year_month", "region")
)

display(agg_df)

## Cell 6 (Markdown)
SQL prompt example:
"Generate Snowflake-compatible SQL to join fact_sales with dim_region and return total sales per region for last 6 months; include simple optimization suggestions."

## Cell 7 (SQL)
-- Example SQL (replace table names)
WITH recent_sales AS (
  SELECT *
  FROM fact_sales
  WHERE sale_date >= DATEADD(month, -6, CURRENT_DATE())
)
SELECT r.region_name, SUM(s.amount) AS total_sales
FROM recent_sales s
JOIN dim_region r ON s.region_id = r.region_id
GROUP BY r.region_name;

## Cell 8 (Python)
output_table = "default.sales_monthly_summary_demo"
agg_df.write.mode("overwrite").format("delta").saveAsTable(output_table)
print(f"Saved output to table: {output_table}")

## Cell 9 (SQL)
SELECT * FROM default.sales_monthly_summary_demo ORDER BY year_month, region;
