# Agent loop standard (public note)

Multi-phase work in the **full private Ira stack** uses `plan_task` → `execute_phase` → `generate_report` with validation contracts and per-phase assertions.

**ira-universe** does not ship the task orchestrator or MCP agent-loop tools. This repo is architecture + visitor MCP only.

For the full contract, use the private operator repository (`docs/AGENT_LOOP_STANDARD.md` there).
