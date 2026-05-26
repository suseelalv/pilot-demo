# Speaker Cheat Sheet & Q&A

## Key messages (one-liners)
- Copilot accelerates drafting and repetitive tasks; humans retain responsibility.
- Strong prompts + context = better results.
- Tests and reviews are required for safety and correctness.
- MCP supplies enterprise context, improving suggestion quality and compliance.
- Genie Code accelerates data engineering workflows in Databricks.

## Likely Questions & Ideal Answers

Q: Will Copilot replace developers?
A: No. It speeds up drafting and repetitive work, but developers still define requirements, validate logic, and ensure security.

Q: How do we ensure output quality?
A: Use tests, code reviews, linters, security scans, and governance processes. Treat AI output like any PR.

Q: What is MCP?
A: Model Context Protocol — a way to provide structured schema, metadata, and enterprise context to AI tools to produce more relevant results.

Q: When should we use agents?
A: When tasks span multiple steps/files and benefit from planning and coordinated execution (feature additions, refactors, tests, docs).

Q: How should pilots be structured?
A: Start small: a single team, defined success metrics (time-to-first-draft, PR cycle time), and governance guardrails.

Q: What are the risks?
A: Over-reliance, hallucinations, exposure of sensitive data. Mitigate with review, testing, and access policies.

Q: How to measure success?
A: Time-to-first-draft, PR turnaround, test coverage, defect escape rate, and developer satisfaction.