# day2/mock_mcp_server.py
# Simple MCP mock server to serve schema, sample rows and metadata for demo purposes.
# Run: python day2/mock_mcp_server.py
# Requires: pip install flask

from flask import Flask, jsonify
app = Flask(__name__)

@app.route("/context/job_sales")
def job_sales():
    # Example context: simple schema + sample rows + naming conventions
    context = {
        "source": "blob://demo/sales/",
        "target": {
            "type": "azure_sql",
            "table": "dbo.fact_sales"
        },
        "schema": {
            "fact_sales": {
                "columns": [
                    {"name": "sale_id", "type": "INTEGER", "desc": "unique sale id"},
                    {"name": "sale_date", "type": "DATE"},
                    {"name": "region_id", "type": "INTEGER"},
                    {"name": "product_id", "type": "INTEGER"},
                    {"name": "amount", "type": "DECIMAL(18,2)"}
                ],
                "primary_key": ["sale_id"]
            },
            "dim_region": {
                "columns": [
                    {"name": "region_id", "type": "INTEGER"},
                    {"name": "region_name", "type": "VARCHAR(100)"}
                ]
            }
        },
        "sample_rows": {
            "fact_sales": [
                {"sale_id": 1, "sale_date": "2026-05-01", "region_id": 10, "product_id": 100, "amount": 1200.50},
                {"sale_id": 2, "sale_date": "2026-05-02", "region_id": 20, "product_id": 101, "amount": 980.00},
            ]
        },
        "naming_conventions": {
            "pipeline": "org_project_env_pipeline",
            "dataset": "org_project_env_dataset"
        },
        "policies": {
            "masking": ["customer_name"],
            "max_parallelism": 4
        }
    }
    return jsonify(context)

if __name__ == "__main__":
    app.run(port=9000, debug=True)