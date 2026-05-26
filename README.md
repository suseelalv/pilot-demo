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

# DemoCopilotAgents

This repository contains a small Python demo project used to showcase:

- GitHub Copilot fundamentals
- prompt-based development workflows
- refactoring and unit test generation
- debugging with Copilot
- agent-style multi-file enhancements

The application is intentionally simple so it can be used easily in live demos and workshops.

## Project Overview

The project is a lightweight task manager that demonstrates:

- adding tasks
- listing tasks
- completing tasks
- deleting tasks
- generating summaries
- extending features with GitHub Copilot

## Project Structure

```text
DemoCopilotAgents/
├── README.md
├── requirements.txt
├── dev-requirements.txt
├── run_demo.sh
├── run_demo.ps1
├── PROMPTS.md
├── AGENDA.md
├── main.py
├── models.py
├── service.py
├── storage.py
├── tests/
│   └── test_service.py
└── demo_notes/
    ├── day1_notes.md
    ├── day2_notes.md
    └── day3_notes.md


Step 1: clone
Step 2: python -m venv .venv
.venv\Scripts\activate.bat
Step 3: Step 3: Install Dependencies 
pip install -r requirements.txt
or 
python -m pip install --upgrade pip
Step 4: Run the Application
python main.py
Step 5: Run the Tests
pytest
or pytest -v
To run a single test file:

bash

pytest tests/test_service.py
Step 6: Run Using Demo Scripts
Windows PowerShell
powershell

Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
.\run_demo.ps1

///Phython version ///
python3 --version
pytest not found
Install again:

bash

pip install -r requirements.txt
PowerShell blocks script execution
Run:

powershell

Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
Then retry:

powershell

.\run_demo.ps1