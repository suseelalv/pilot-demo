---

## `PROMPTS.md`

```md
# GitHub Copilot Demo Prompt Library

This file contains prompts used during the workshop.

## Day 1 – Session 1: Copilot Basics

### Code Generation

Create a method in TaskService that searches tasks by keyword in the title.

Requirements:
- case insensitive
- return matching tasks only
- keep the implementation simple
- add a short docstring

### Refactoring

Refactor the summary method in TaskService to improve readability.

Constraints:
- do not change behavior
- keep it beginner friendly
- explain what changed before suggesting code

### Unit Test Generation

Generate pytest unit tests for TaskService.

Cover:
- add_task
- complete_task
- list_tasks
- summary

Keep the tests independent and easy to read.

### Documentation

Add concise Python docstrings to all public methods in TaskService.

Then draft a short README usage section that explains:
- how to run the project
- how to run tests

## Day 1 – Session 2: Advanced Copilot Usage

### Debugging

There is a bug in delete_task in service.py.

Please:
1. explain the root cause
2. propose a minimal fix
3. generate a pytest test that would catch the issue
4. keep the explanation simple and practical

### Optimization

Review TaskService for possible performance improvements if the number of tasks becomes large.

Please:
- explain trade-offs first
- do not rewrite the whole design immediately
- suggest a simple improvement path

### Multi-file Understanding

Review main.py, models.py, service.py, and storage.py.

Please:
- explain how data flows through the application
- identify what is missing for persistent storage
- suggest the minimum required changes

## Day 1 – Session 3: Agents

### Agent-Oriented Feature Prompt

Add due_date support across the project.

Please:
1. review the current codebase
2. create a short implementation plan
3. update the model
4. update the service
5. update tests
6. update README
7. summarize the changes

Keep the design simple and beginner-friendly.

### Agent-Oriented Persistence Prompt

Implement JSON persistence for the project.

Requirements:
- load tasks at startup
- save tasks after add, complete, and delete
- keep the changes minimal
- update tests accordingly
- explain assumptions before suggesting edits

## Day 2 – MCP + Azure Data Stack + Agents

### MCP Fundamentals Prompt

Explain how MCP improves Copilot suggestions when connected to enterprise systems such as Azure Data Factory, Databricks, and Snowflake.

Please include:
- architecture summary
- developer value
- governance value

### Azure Data Factory Prompt

Generate a reusable ADF pipeline pattern for ingesting CSV files from blob storage into Azure SQL.

Please include:
- parameterized source path
- logging consideration
- error handling consideration
- reusable design

### Databricks Prompt

Generate a PySpark transformation that:
- reads raw sales data
- converts types
- aggregates total sales by region and month
- keeps the code readable
- includes brief comments

### Snowflake Prompt

Generate a schema-aware SQL query for a sales analytics use case.

Please:
- join fact_sales with dimension tables
- aggregate total sales by region
- suggest simple optimization considerations

### MCP + Agents Prompt

Explain how an agent becomes more useful when it has MCP-provided schema, metadata, and standards context.

Please include:
- multi-step execution
- planning
- enterprise automation example

## Day 3 – Databricks Genie Code Enablement

### Genie Code Foundations Prompt

Explain what Genie Code is and how it differs from broader Genie experiences used for business interaction and AI/BI use cases.

Keep the explanation practical and customer-friendly.

### Role-Based Value Prompt

Summarize how Genie Code helps:
- Data Engineers
- Analytics Engineers
- ML Engineers
- Architects

Keep it concise and role-oriented.

### Adoption Prompt

Provide a practical readiness checklist for teams getting started with Genie Code in a Databricks workspace.

Include:
- access
- data readiness
- governance
- onboarding