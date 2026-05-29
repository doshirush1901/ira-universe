# Ira instrument guide (public edition)

*How to think about Ira — visitor repo vs private operator stack.*

Full day-to-day operator manual (CLI, API, Docker, mail, CRM) lives in the **private** `ira-v3` deployment. This excerpt orients evaluators cloning **ira-universe**.

## Part 0 — One idea

Ira is a **system** (pipeline + specialists + memory + approval gates), not a single chat box. Technique matters: triangulate evidence, draft only, send on explicit human approval.

## Part 1 — Unboxing (private stack)

1. Clone **private** repo with `src/ira/`
2. `poetry install` from lockfile
3. `.env` from `.env.example` (never commit)
4. Docker: Postgres, Qdrant, Neo4j, Redis

**This public repo:** `poetry install` → enable **ira-universe** MCP → read docs — no databases required.

## Part 2 — Three consoles

| Console | Public (here) | Private |
|:--------|:----------------|:--------|
| Visitor MCP | `poetry run ira-universe-mcp` | — |
| CLI | — | `ira ask`, `ira task`, `ira brief` |
| API / web UI | — | Optional FastAPI + Next.js |

## Part 3 — Cursor

Use [CURSOR_WORKFLOWS.md](CURSOR_WORKFLOWS.md) and [CURSOR_AGENTIC_LOOP.md](CURSOR_AGENTIC_LOOP.md). Sample prompts: [IRA_SAMPLE_PROMPTS.md](IRA_SAMPLE_PROMPTS.md).

Synthetic end-to-end demo: [examples/public_demo/journey_acme.md](../examples/public_demo/journey_acme.md).

## Further reading

| Topic | Doc |
|:------|:----|
| Birth certificate | [IRA_BIRTH_CERTIFICATE.md](IRA_BIRTH_CERTIFICATE.md) |
| Agents & pipeline | [AGENTS.md](../AGENTS.md) |
| Triangulation | [IRA_TRIANGULATION.md](IRA_TRIANGULATION.md) |
| Doc index | [INDEX.md](INDEX.md) |
