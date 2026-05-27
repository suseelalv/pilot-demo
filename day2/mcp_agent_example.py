# day2/mcp_agent_example.py
# Simulated agent: fetches context from mock MCP, prints a plan, and optionally applies a small local change.
# Usage:
#   1) Run mock_mcp_server.py
#   2) python day2/mcp_agent_example.py --simulate
# Requires: requests (pip install requests)

import requests
import json
import argparse
from pathlib import Path

MCP_URL = "[http://localhost:9000/context/job_sales"](http://localhost:9000/context/job_sales")
REPO_ROOT = Path(__file__).parents[1]

def fetch_context():
    print("Fetching context from MCP mock server:", MCP_URL)
    r = requests.get(MCP_URL)
    r.raise_for_status()
    return r.json()

def create_plan(context):
    plan = [
        "1) Validate schema fact_sales and dim_region (files: day2/snowflake_schema_and_queries.sql)",
        "2) Generate Databricks PySpark transform based on schema (files: day2/databricks_transform.py)",
        "3) Create ADF pipeline template to copy CSV to Azure SQL (files: day2/adf_pipeline_template.json)",
        "4) Produce SQL queries and optimization notes (files: day2/snowflake_schema_and_queries.sql)",
        "5) Update README / demo notes with instructions and sample prompts"
    ]
    return plan

def show_prompts_for_copilot(context):
    # Build an example prompt to paste into Copilot Chat or Genie
    prompt = f"""
    We have the following MCP context (schema + samples):
    {json.dumps(context, indent=2)}

    Please:
    1) Generate a PySpark transformation that reads fact_sales CSV, enforces schema types, creates a year_month column, and aggregates total_sales by region and month.
    2) Keep code readable and include brief comments.
    3) Suggest any Snowflake optimization for the aggregation query.
    """
    print("=== Copy the following prompt into Copilot Chat or Genie Code ===\n")
    print(prompt)
    print("\n=== End of prompt ===\n")

def apply_local_change_example():
    # Example: append a small note to day2/README.md to record that the plan was executed
    target = REPO_ROOT / "day2" / "README.md"
    target.parent.mkdir(exist_ok=True)
    note = "\nPlan executed by simulated agent: add databricks transform & queries.\n"
    with open(target, "a", encoding="utf-8") as f:
        f.write(note)
    print(f"Appended plan note to {target}")

def main(simulate=False):
    ctx = fetch_context()
    plan = create_plan(ctx)
    print("Agent Plan:")
    for step in plan:
        print("-", step)
    show_prompts_for_copilot(ctx)
    if simulate:
        apply_local_change_example()
        print("Simulation step applied a local change. Open day2/README.md to see note.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--simulate", action="store_true", help="Apply a small local change to simulate execution")
    args = parser.parse_args()
    main(simulate=args.simulate)