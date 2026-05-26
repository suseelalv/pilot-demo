# pilot-demo
---

## PROMPTS.md

```md
# GitHub Copilot Demo Prompt Library

## Day 1 – Copilot Basics

### Code Generation
Create a method in TaskService that searches tasks by keyword in the title.
- Requirements: case insensitive, return matching tasks only, add a short docstring.

### Refactoring
Refactor the summary method in TaskService to improve readability.
- Constraints: do not change behavior; explain the improvement.

### Unit Tests
Generate pytest tests for TaskService covering:
- add_task, complete_task, list_tasks, delete_task, summary.
Keep tests independent and readable.

### Documentation
Add docstrings to public methods in TaskService. Draft a README usage section.

## Day 1 – Advanced Usage

### Debugging
There is a bug in delete_task in service.py.
- Explain root cause, propose minimal fix, and generate a pytest test.

### Optimization
Review TaskService for performance if tasks scale to thousands.
- Explain trade-offs before code changes.

### Multi-file Understanding
Review main.py, models.py, service.py, and storage.py.
- Explain data flow and suggest minimal changes to add persistence.

## Day 1 – Agents

### Agent Feature
Add due_date support across the project:
- Update model, service, tests, and README.
- Provide a plan first, then implement step-by-step.

### Agent Persistence
Implement JSON persistence:
- load tasks at startup
- save on add/complete/delete
- use tmp_path in tests
- provide a step plan first

## Day 2 – MCP + Azure Data Stack

### MCP Fundamentals
Explain how MCP improves Copilot suggestions for ADF, Databricks, and Snowflake.
- Include architecture summary, developer benefits, and governance value.

### ADF Prompt
Generate a reusable ADF pipeline template (CSV -> Azure SQL) with parameterization, logging, and error handling.

### Databricks Prompt
Generate PySpark transformations: parse dates, cast amount, aggregate total sales by region & month — keep code readable.

### Snowflake Prompt
Generate schema-aware SQL joining fact_sales and dims, aggregating last 6 months by region; include optimization notes.

### MCP + Agents
Explain how agents are strengthened when MCP supplies schema, metadata, and organizational patterns.

## Day 3 – Databricks Genie Code

### Genie Foundations
Explain Genie Code vs Genie ecosystem; highlight core capabilities and positioning.

### Role-Based Value
Summarize value for Data Engineers, Analytics Engineers, ML Engineers, and Architects.

### Adoption
Provide workspace readiness checklist: access, data, governance, cluster setup, and training.