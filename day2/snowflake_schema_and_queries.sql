-- day2/snowflake_schema_and_queries.sql

-- Example schema DDL (for demo only)
CREATE TABLE IF NOT EXISTS dim_region (
  region_id INTEGER PRIMARY KEY,
  region_name VARCHAR(100)
);

CREATE TABLE IF NOT EXISTS fact_sales (
  sale_id INTEGER PRIMARY KEY,
  sale_date DATE,
  region_id INTEGER,
  product_id INTEGER,
  amount NUMBER(18,2)
);

-- Example optimized SQL to compute last 6 months sales by region
WITH recent_sales AS (
  SELECT sale_date, region_id, amount
  FROM fact_sales
  WHERE sale_date >= DATEADD(month, -6, CURRENT_DATE())
)
SELECT r.region_name,
       DATE_TRUNC('month', s.sale_date) AS month,
       SUM(s.amount) AS total_sales,
       COUNT(*) AS sale_count
FROM recent_sales s
JOIN dim_region r ON s.region_id = r.region_id
GROUP BY r.region_name, DATE_TRUNC('month', s.sale_date)
ORDER BY month DESC, total_sales DESC;

-- Optimization suggestions (to narrate)
-- 1) Ensure fact_sales has a clustering/cluster key on (sale_date) or (region_id, sale_date) for frequent range scans.
-- 2) Use micro-partition pruning (Snowflake clustering) if this becomes large.
-- 3) Materialize monthly aggregates in a summary table if queries are frequent.