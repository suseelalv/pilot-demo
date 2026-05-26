# Day 1 – Trainer Notes

## Objectives
- Demonstrate Copilot basics and advanced usage.
- Show prompt engineering, tests, documentation, debugging, and agent-style workflows.

## Setup Checklist
- VS Code signed into GitHub
- Copilot & Copilot Chat enabled
- Python 3.x and pytest installed
- Open repo and run `python main.py` and `pytest` pre-demo

## Demo Flow
1. Intro and agenda
2. Code generation: add search method
3. Refactor summary() via Copilot Chat
4. Generate pytest tests and run them
5. Documentation: docstrings and README snippet
6. Debugging: fix delete_task bug (explain root cause)
7. Advanced: optimization suggestions and multi-file reasoning
8. Agents: plan + implement due_date/persistence across files
9. Wrap-up: best practices and Q&A

## Key Prompts
- “Generate pytest tests for TaskService covering add_task, complete_task, list_tasks, and summary.”
- “There is a bug in delete_task; explain and fix it.”
- “Add due_date across the project; create a short plan first.”

## Troubleshooting
- If Copilot not showing suggestions: confirm extension enabled and VS Code signed into GitHub.
- If tests fail unexpectedly: run tests, show failure trace, ask Copilot to explain the trace.