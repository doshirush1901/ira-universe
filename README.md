# Ira Universe

Public-safe **visitor MCP** for Claude Code and Cursor — explain what Ira is, how it is built, and how to adopt a factory-specific fork **without** Machinecraft CRM, Gmail, or customer data.

Full operator stack lives in private **ira-v3**. This repo is intentionally small.

## Recommended reading order

See [docs/INDEX.md](docs/INDEX.md) for the full map. Short path:

1. [IRA_BIRTH_CERTIFICATE.md](docs/IRA_BIRTH_CERTIFICATE.md) — identity, pipeline, body metaphor
2. [ARCHITECTURE.md](docs/ARCHITECTURE.md) — technical map
3. [AGENTS.md](AGENTS.md) — pantheon + 17 steps (public excerpt)
4. [PIPELINE_AUDIT.md](docs/PIPELINE_AUDIT.md) — safety ordering (executive summary)
5. [CURSOR_AGENTIC_LOOP.md](docs/CURSOR_AGENTIC_LOOP.md) + [CURSOR_WORKFLOWS.md](docs/CURSOR_WORKFLOWS.md)
6. [IRA_TRIANGULATION.md](docs/IRA_TRIANGULATION.md) — evidence before outbound
7. **Demo:** [examples/public_demo/journey_acme.md](examples/public_demo/journey_acme.md) — synthetic Acme walkthrough
8. [IRA_SAMPLE_PROMPTS.md](docs/IRA_SAMPLE_PROMPTS.md) — copy-paste MCP prompts

## Quick start (Claude Code)

```bash
git clone https://github.com/doshirush1901/ira-universe.git
cd ira-universe
poetry install
```

Add `.mcp.json` from `.mcp.json.example`, then enable **`ira-universe`** in your MCP settings.

Start manually (optional):

```bash
poetry run ira-universe-mcp
```

## MCP tools (16)

| Tool | Purpose |
|:-----|:--------|
| `who_is_ira` | Identity from SOUL + README |
| `why_ira` | Narrative — why Ira vs a chat box |
| `how_ira_is_built` | Architecture summary |
| `list_pantheon_agents` | Agent table excerpt |
| `walkthrough_pipeline` | Annotated 17-step pipeline |
| `explain_triangulation` | Evidence workflow (triangle/hex) |
| `fork_ira_for_your_factory` | Adoption checklist |
| `demo_account_brief` | Synthetic Acme brief (JSON optional) |
| `demo_draft_email` | Proof-safe demo follow-up (draft only) |
| `list_public_corpus` | Allowlisted files |
| `search_public_docs` | Search public docs |
| `demo_search_knowledge` | Synthetic demo only |
| `universe_mcp_status` | Safety posture |
| `list_ira_justification_assets` | Public collateral index |
| `read_ira_justification_text` | Read one public doc by path |
| `build_ira_business_case` | Heuristic ROI / adoption case |

## What is NOT in this repo

- `PSG_Case_Study/` and other named-customer marketing builds (private operator repo)
- Full `ira mcp` (~160 tools), web UI, Docker operator stack
- Gmail / CRM connectors or send paths

See `examples/marketing/case_study_workflow.md` for how case studies work in the private stack.

## Safety

- No secrets in Git — use your own `.env` only on a **private** fork if you expand beyond visitor mode.
- Optional: `IRA_VISITOR_MCP_STRICT=1` blocks startup when Gmail/CRM env vars are set.

## License

Proprietary — see `LICENSE`. Fork for evaluation; contact Machinecraft for redistribution terms.
