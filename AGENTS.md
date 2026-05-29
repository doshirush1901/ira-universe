# Ira — Agents & pipeline (public edition)

> **ira-universe** ships this excerpt only. Full operator commands, MCP catalog (~160 tools), and `src/ira/` live in a **private** Machinecraft deployment.

Identity: [SOUL.md](SOUL.md) · Direction: [VISION.md](VISION.md) · Architecture: [docs/ARCHITECTURE.md](docs/ARCHITECTURE.md)

## What Ira is

A multi-agent system for manufacturing OEM workflows: **36 specialist agents**, a **17-step request pipeline**, persistent memory, and **human-approved** outbound (draft-only by default). In Cursor, Ira uses **Explore → Think → Act → Loop → Result** with bounded timeouts and parallel sub-agents.

**This repo:** visitor MCP (`poetry run ira-universe-mcp`, ~12 tools, public docs only).  
**Private stack:** `ira ask`, Gmail, CRM, full MCP — not in this repository.

## The Pantheon

| Agent | Role | Domain |
|:------|:-----|:-------|
| **Anu** | AI Recruiter | Resume parsing, candidate scoring |
| **Athena** | Orchestrator | Routes, delegates, synthesizes |
| **Alexandros** | Librarian | Document archive, fallback retrieval |
| **Arachne** | Content Scheduler | Newsletters, content calendar |
| **Artemis** | Lead Hunter | Mailbox patterns, journey mapping |
| **Asclepius** | Quality | Punch lists, FAT/installation |
| **Atlas** | Project Manager | Production schedules, milestones |
| **Cadmus** | CMO / Case Studies | NDA-safe marketing content |
| **Calliope** | Writer | External email and proposals (draft-only) |
| **Chiron** | Sales Trainer | Coaching, outreach patterns |
| **Clio** | Researcher | KB + graph + memory search |
| **Delphi** | Oracle | Email classification, tone |
| **Gapper** | Gap Resolver | Fills missing facts from evidence |
| **Hephaestus** | Production | Machine specs, manufacturing |
| **Hephaestion** | System Auditor | Codebase and ops health (not machine specs) |
| **Hera** | Procurement | Vendors, inventory |
| **Hermes** | Marketing | Campaigns, regional tone |
| **Iris** | External Intel | Web and company intelligence |
| **Mnemon** | Memory Guardian | Corrections override stale KB |
| **Mnemosyne** | Memory | Long-term semantic memory |
| **Nemesis** | Trainer | Adversarial / sleep training |
| **Plutus** | Finance | Pricing, margins, quotes |
| **Populator** | CRM Populator | Lead intake and enrichment |
| **Argus** | Lead scout | Single-domain dossier (Apollo, site, mail, KB) |
| **NA Sales (Hudson)** | NA specialist | US/Canada thermoforming motion |
| **Prometheus** | Sales / CRM | Pipeline, deals, mail history |
| **Quotebuilder** | Quotes | Formal quotes + CRM deals |
| **Sophia** | Reflector | Post-interaction learning |
| **Sphinx** | Gatekeeper | Clarifying questions for vague queries |
| **Themis** | HR | Policies, headcount |
| **Tyche** | Forecasting | Pipeline forecasts |
| **Vera** | Fact Checker | Grounding and hallucination checks |
| **Aegis** | DLP | PII and confidentiality scan |
| **Aletheia** | Provenance | Claim → source tracing |
| **Graphe** | Scribe | Session logging for consolidation |
| **Metis** | Stability | Response quality scoring |

Users talk to **Athena**; specialists run in parallel behind structured **handoffs** (goal, bullets, domain, constraints).

### Collaboration clusters

| Cluster | Agents | Why |
|:--------|:-------|:----|
| Revenue truth | Prometheus, Atlas, Asclepius | Pipeline vs production before “lead” labels |
| Evidence-first outbound | Prometheus, Argus, Clio, Calliope | Brief + proof before prose |
| Grounding | Clio, Vera, Mnemon | Corrections win over thin retrieval |
| Identity gaps | Argus → Gapper | Who they are, then missing specs/dates |

See [docs/IRA_TRIANGULATION.md](docs/IRA_TRIANGULATION.md) for triangle/hexagon evidence rules.

## Request pipeline (17 steps)

Every request flows through a linear pipeline (early exits for greetings, clarify-only, truth hints):

```
 1. PERCEIVE        — identity, channel, warmth
 2. REMEMBER        — conversation, goals
 2.5 FAST PATH      — trivial intents
 2.7 SPHINX        — clarify vague queries
 3–5. ROUTE        — fast → procedural → LLM (Athena)
 5.1 EMAIL SCOPE    — live vs imported mail (private deploy)
 5.5 ENRICH        — style, episodes
 6. EXECUTE         — parallel specialists (bounded)
 6.1a Aletheia      — provenance
 6.1b Aegis         — DLP
 6.2 Mnemon         — corrections
 6.3 Gapper         — missing data
 6.4 Faithfulness   — 4-tier grounding
 6.4b Guardrails    — policy
 7–8. ASSESS/REFLECT
 9. SHAPE           — voice for channel
 9.5–9.6 Graphe/Metis
10. LEARN           — memory, CRM (background)
11. RETURN
```

Details: [docs/PIPELINE_AUDIT.md](docs/PIPELINE_AUDIT.md) · [docs/TIMEOUT_MODEL.md](docs/TIMEOUT_MODEL.md)

## Faithfulness (4-tier)

| Tier | Approach |
|:-----|:---------|
| 0 | Fast grounding API (when configured) |
| 1 | Dual-model LLM verification |
| 2 | Single-model fallback |
| 3 | Keyword overlap heuristic |

The pipeline appends a verification caveat rather than silently inventing CRM or mail history.

## Cursor-native flow

1. **Explore** — docs and codebase  
2. **Think** — plan next step  
3. **Act** — CLI or visitor MCP  
4. **Loop** — until complete  
5. **Result** — answer + sources / UNVERIFIED gaps  

[docs/CURSOR_AGENTIC_LOOP.md](docs/CURSOR_AGENTIC_LOOP.md) · [docs/CURSOR_WORKFLOWS.md](docs/CURSOR_WORKFLOWS.md)

## Synthetic demo account

Public walkthrough (no live CRM): [examples/public_demo/journey_acme.md](examples/public_demo/journey_acme.md) — fictional **Acme Thermoforming** only.

## Private operator stack (not in this repo)

- CLI: `ira ask`, `ira task`, `ira brief "Acme Corp" --contact jane@demo-acme.com`
- Docker: Postgres, Qdrant, Neo4j, Redis
- Full MCP, Gmail send gates, CRM writes

Fork privately; never commit `.env` or customer exports. See [docs/PUBLIC_PRIVATE_BOUNDARY.md](docs/PUBLIC_PRIVATE_BOUNDARY.md).
