# Ira Universe MCP

Public operator guide for the **ira-universe** repository (not full ira-v3).

## Start

```bash
poetry run ira-universe-mcp
```

Claude Code: copy `.mcp.json.example` → `.mcp.json` in the repo root.

## Strict mode

Set `IRA_VISITOR_MCP_STRICT=1` to refuse startup when Gmail/CRM connector environment variables are present.

## Interactive demos (phase 2)

| Tool | Try |
|:-----|:----|
| `demo_account_brief` | Synthetic Acme triangle + UNVERIFIED mail/CRM |
| `demo_draft_email` | Draft-only follow-up using proof registry |
| `walkthrough_pipeline` | Step-by-step pipeline annotations |
| `why_ira` | Narrative from `docs/WHY_IRA.md` |

## Suggested prompts

- Who is Ira vs ChatGPT for a manufacturing OEM?
- Run `demo_account_brief` and explain the UNVERIFIED legs.
- `walkthrough_pipeline` then `demo_draft_email` for Acme.
- Build a business case for thermoforming sales outreach.
