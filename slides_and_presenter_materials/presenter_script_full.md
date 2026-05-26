# Presenter script — Word-for-word (Days 1–3)

## Day 1 — Full Script (2 hours)
Opening (0:00–0:05)
"Welcome everyone. Today we’ll start with GitHub Copilot basics in VS Code and progress to agent-style workflows. The goal is to learn how to collaborate with Copilot effectively while maintaining human review and engineering judgment."

Agenda and Outcomes (0:05–0:10)
"The agenda is three sessions: Copilot Basics, Advanced Copilot Usage, and Introduction to Copilot Agents. By the end, you'll know when to use simple prompts and when to ask for agent-like multi-step help."

Session 1: Copilot Basics (0:10–0:40)
"Copilot is an AI coding assistant integrated into VS Code. It suggests code, explains snippets, helps write tests, and creates documentation. It’s most effective when we provide context and constraints."
(Perform code generation, refactor, test generation, docs demos as described in AGENDA.md and PROMPTS.md, reading prompts aloud and narrating acceptance/rejection of suggestions.)

Prompt engineering basics:
"Good prompts include intent, context, constraints, and desired output. 'Write tests' is weak; 'Generate pytest tests for TaskService covering add_task, complete_task, list_tasks, and summary; keep tests independent' is strong."

Session 2: Advanced Copilot Usage (0:40–1:15)
"Advanced use is about better context and intent. Ask for explanations and trade-offs, not just code." (Perform debugging demo on delete_task, optimization discussion, multi-file reasoning.)

Session 3: Introduction to Copilot Agents (1:15–1:50)
"Prompt-based interaction gives a response. Agent-style interaction aims for an outcome. Agents plan, execute across multiple steps, and coordinate changes across files."
(Execute the agent-style plan: ask for a plan to add due_date/persistence, then implement step-by-step, run tests, update docs.)

Wrap-up (1:50–2:00)
"Key takeaways: Copilot accelerates drafting; strong prompts reduce rework; context improves outcomes; agents bring planning and multi-step execution. Ensure review and testing for all AI changes."

## Day 2 — Full Script (2 hours)
Opening (0:00–0:05)
"Welcome to Day 2. Today we discuss MCP—Model Context Protocol—and how context from Azure Data Engineering and Snowflake improves AI coding and agent workflows."

MCP Fundamentals (0:10–0:35)
"MCP supplies structured context—schemas, sample rows, metadata, templates—to AI tools. The high-level architecture is Copilot → MCP → ADF/Databricks/Snowflake. This makes suggestions more accurate, reduces guesswork, and helps enforce standards."

MCP with Azure Data Engineering (0:35–1:20)
(ADF Demo, Databricks Demo, Snowflake Demo — read prompt patterns and show example outputs. Emphasize how schema and metadata improve the generated code or pipeline.)

MCP + Agents (1:20–1:50)
"When agents use MCP-provided metadata and templates, they can plan end-to-end flows, validate schema changes and produce deployable artifacts aligned with enterprise standards."

Wrap-up (1:50–2:00)
"Context is the multiplier. MCP + agents help scale reliable automation."

## Day 3 — Full Script (1 hour)
Opening (0:00–0:03)
"Today we focus on Databricks Genie Code: what it is, how it helps engineers, and how to get started."

Demo (0:10–0:25)
(Paste notebook cells into Databricks, read the Genie prompts aloud, run generated cells, show outputs.)

Role-based value (0:25–0:35)
"Genie Code helps data engineers, analytics engineers, ML engineers, and architects: faster transformations, quicker SQL, faster feature engineering, and rapid reference designs."

Adoption (0:35–0:45)
"Adoption needs workspace readiness: access, governance, cluster setup, sample data, and training."

Wrap-up & Q&A (0:45–1:00)
"Genie Code is a multiplier when teams use it with real context and disciplined review. Happy to take questions."