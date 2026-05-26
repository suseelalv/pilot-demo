# Day 2 – Trainer Notes

## Objectives
- Explain MCP and its role in improving AI suggestions
- Demonstrate example prompts for ADF, Databricks, and Snowflake
- Show how MCP improves agent workflows in enterprise settings

## Setup Checklist
- Slide with MCP architecture ready
- Sample schema snippets (text) ready
- Optional connectivity demos pre-recorded if live connectors are unavailable

## Demo Flow
1. MCP fundamentals and architecture (Copilot → MCP → Systems)
2. ADF prompt: generate pipeline template (parameterized CSV ingestion)
3. Databricks prompt: PySpark transform with schema
4. Snowflake prompt: schema-aware SQL
5. MCP + Agents: planning and orchestration example
6. Q&A: governance, data access, policy enforcement

## Key Prompts
- “Generate a reusable ADF pipeline for CSV ingestion to Azure SQL with parameterized paths, logging, and error handling.”
- “Given schema X, generate PySpark code to aggregate sales by month.”
- “Generate SQL to join fact_sales with dim_region and aggregate last 6 months.”