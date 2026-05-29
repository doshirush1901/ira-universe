# Why Ira?

*From "AI as a Tool" to "AI as Infrastructure."*

> **Public edition** for ira-universe. Examples below are **synthetic** unless marked otherwise.

---

Imagine your company is a body: sales talks, production builds, finance digests cash, and the founder is the brain — except the brain needs sleep, forgets context, and stress appears when sales promises what production cannot ship.

For years we used AI like a genius in a box: slide a question in, get an answer out. The box does not know your CRM, your last quote, or whether the machine is actually on the production schedule.

**Ira is different.** It is a multi-agent operating system — a **pantheon** of specialists orchestrated by **Athena**, with memory, evidence gates, and **human-approved** outbound. You can start in **visitor mode** (this repo, read-only docs + demo MCP) or run the full private stack from your IDE.

---

## The IDE as command center

Cursor (and Claude Code) can run tools via **MCP**. Instead of yet another dashboard, Ira meets you where you already work:

- **Visitor:** `poetry run ira-universe-mcp` — architecture, triangulation, synthetic Acme demos.
- **Private stack:** Docker + `ira ask` / `ira task` — CRM, mail, full agent graph.

No tab circus. You explore, think, act, and loop until the answer is grounded.

---

## Synthetic dialogue (demo only)

```
You:     Who is Acme Thermoforming in the public demo?

Ira:     [Synthetic brief — demo_account_brief]
         Acme Thermoforming LLC (demo-acme.com)
         Intent: verified from demo_product_specs (PF1-class tray interest)
         Relationship: UNVERIFIED in visitor mode (no live Gmail/CRM here)
         Identity: verified from sample_customer_context.md (fictional)

You:     Draft a follow-up for the demo

Ira:     [demo_draft_email — DRAFT ONLY, proof-registry claims only]
         No invented EUR/USD figures or delivery dates.
```

In production, each leg is sourced; gaps are labeled **UNVERIFIED**; send requires explicit human approval.

---

## Use case 1 — Stop being the human email router

A discount question touches pricing, production load, and margin. You become the router between departments.

**With Ira (private stack):** classification → memory → finance check → **Calliope** drafts. You edit and approve. Visitor mode shows the *pattern* via `demo_draft_email` without touching real mail.

---

## Use case 2 — Multi-phase work (agent loop)

"Prepare a quarterly review" is a project, not a one-shot prompt. The private stack can **plan → execute phases → observe → compile** (see `docs/AGENT_LOOP_STANDARD.md` stub; full contract in operator repo).

---

## Use case 3 — Board-style debate

Strategic questions can route multiple agents (sales, production, finance) and synthesize minutes — bounded time, named contributors, no calendar scheduling.

---

## Use case 4 — Dream (consolidation)

Off-hours cycles prune memory, surface knowledge gaps, and promote procedures — operational maturity, not just chat logs.

---

## The big picture

We are moving from **AI as a tool** to **AI as infrastructure**: wired into evidence, approvals, and specialist boundaries — not a single model improvising your company.

Start here:

1. [IRA_BIRTH_CERTIFICATE.md](IRA_BIRTH_CERTIFICATE.md)
2. [examples/public_demo/journey_acme.md](../examples/public_demo/journey_acme.md)
3. [IRA_SAMPLE_PROMPTS.md](IRA_SAMPLE_PROMPTS.md)
4. [VISITOR_MCP.md](VISITOR_MCP.md) — try `demo_account_brief`, `walkthrough_pipeline`, `demo_draft_email`

Full operator manual: private **ira-v3** deployment only. See [PUBLIC_PRIVATE_BOUNDARY.md](PUBLIC_PRIVATE_BOUNDARY.md).
