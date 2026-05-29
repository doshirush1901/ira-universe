# Cursor workflows with Ira

> **Public edition** for ira-universe. Describes how teams use Ira inside Cursor. Full operator rules (`.cursor/rules/`), stable modes, and MCP tiers live in a private `ira-v3` deployment.

**Related:** [IRA_INSTRUMENT_GUIDE.md](IRA_INSTRUMENT_GUIDE.md) · [CURSOR_AGENTIC_LOOP.md](CURSOR_AGENTIC_LOOP.md) · [VISITOR_MCP.md](VISITOR_MCP.md)

---

## Two modes in this repository

| Mode | What you have | Typical use |
|:-----|:--------------|:------------|
| **Visitor (this repo)** | `poetry run ira-universe-mcp` — ~12 tools, allowlisted public docs | Explain Ira, architecture, adoption, synthetic demos |
| **Full operator (private)** | `ira ask`, `ira task`, ~160 MCP tools, Gmail/CRM | Machinecraft day-to-day sales and operations |

---

## Lifecycle (conceptual)

| Workflow | Trigger | What happens |
|:---------|:--------|:-------------|
| **Start visitor MCP** | Clone repo, `poetry install`, enable MCP in Claude Code / Cursor | Read-only architecture and demo corpus |
| **Query (full stack)** | `@Ira`, `ira ask "..."` (private) | 17-step pipeline + agents; show `steps` in JSON when using `--json` |
| **Complex task** | `ira task "..."` (private) | Plan → phases → report under `data/tasks/` |
| **Email** | Search → draft → show in chat → user says **send** (private) | No auto-send; operational mode + explicit approval |
| **Feedback** | "that's wrong" | Correction ledger (Mnemon); overrides stale retrieval |
| **End session** | "end Ira" | Stop routing chat to Ira (session-only; does not stop Docker) |

---

## Cursor agentic loop

Ira in Cursor follows **Explore → Think → Act → Loop → Result**. Each phase has explicit chat blocks (🔍 💭 ▶ ✅) so reasoning is visible.

See [CURSOR_AGENTIC_LOOP.md](CURSOR_AGENTIC_LOOP.md) for tool-level detail (SemanticSearch, Grep, `ira ask`, etc.).

**Execution policy (multi-phase tasks):** one mutating writer at a time; parallel fan-out only for read-only research phases.

---

## Evidence before action (triangulation)

Before calling someone a lead, drafting outbound, or changing CRM stage:

1. **Triangle** — Intent (KB/specs), Relationship (CRM/mail), Identity (company/domain).
2. **Hexagon** (outbound) — add production truth, graph, proof registry, corrections.

Missing legs → state **UNVERIFIED**; do not invent history.

Runbook: [IRA_TRIANGULATION.md](IRA_TRIANGULATION.md).

---

## Stable operator patterns (summary)

These are production habits in the full stack; visitor mode illustrates the ideas only.

| Pattern | Idea |
|:--------|:-----|
| Email reply | Read → draft → revise in chat → send only on explicit instruction |
| Account brief | CRM + mail + KB convergence before prose |
| Draft follow-up | Evidence → bridge → draft; proof URLs from registry only |
| Approval inbox | Human approves drafts; no autonomous send |
| Triangulation / hex | Gaps table before outbound |

---

## MCP quick reference (visitor)

| Tool | Purpose |
|:-----|:--------|
| `who_is_ira` | Identity from SOUL + README |
| `how_ira_is_built` | Architecture summary |
| `explain_triangulation` | Evidence workflow |
| `fork_ira_for_your_factory` | Adoption checklist |
| `search_public_docs` | Search allowlisted corpus |
| `demo_search_knowledge` | Synthetic demos only |
| `build_ira_business_case` | Heuristic ROI / adoption framing |

Full list: [VISITOR_MCP.md](VISITOR_MCP.md).

---

## Suggested visitor prompts

Copy-paste list: [IRA_SAMPLE_PROMPTS.md](IRA_SAMPLE_PROMPTS.md). Try the synthetic journey: [examples/public_demo/journey_acme.md](../examples/public_demo/journey_acme.md).

---

## Daily use vs codebase work

**Use Ira first** for business answers, CRM, mail drafts, and reports when you have the private stack.

**Use Cursor on the repo** for reproducible bugs, missing flags, migrations, and reliability work — not to replace Ira's retrieval on live customer data.

---

## Summary

| Topic | Doc |
|:------|:----|
| Birth certificate / pantheon | [IRA_BIRTH_CERTIFICATE.md](IRA_BIRTH_CERTIFICATE.md) |
| Timeouts | [TIMEOUT_MODEL.md](TIMEOUT_MODEL.md) |
| Pipeline safety ordering | [PIPELINE_AUDIT.md](PIPELINE_AUDIT.md) |
| Agentic phases | [CURSOR_AGENTIC_LOOP.md](CURSOR_AGENTIC_LOOP.md) |
| Public vs private | [PUBLIC_PRIVATE_BOUNDARY.md](PUBLIC_PRIVATE_BOUNDARY.md) |
