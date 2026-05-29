# Synthetic operator journey — Acme Thermoforming

PUBLIC DEMO DATA — fully fictional. No real company, mail, CRM, or pricing.

This walkthrough shows how the **private** Ira stack uses evidence before outbound. In **ira-universe** visitor mode, use MCP tools to read the same ideas from public docs and `demo_search_knowledge`.

---

## 1. Account anchor

| Field | Demo value |
|:------|:-----------|
| Company | Acme Thermoforming LLC (synthetic) |
| Domain | demo-acme.com |
| Contact | jane.buyer@demo-acme.com |
| Intent signal | Tray line upgrade; closed-chamber interest |

---

## 2. Triangulation (triangle)

| Leg | Status | Demo evidence |
|:----|:-------|:----------------|
| **Intent** | OK | `data/knowledge/demo_product_specs.md` — PF1-class tray interest |
| **Relationship** | UNVERIFIED in visitor mode | Full stack: CRM + mail search (private only) |
| **Identity** | OK | `examples/sample_customer_context.md` — fictional firmographics |

**Rule:** Missing legs are labeled **UNVERIFIED** — never invent quote history or last email date.

---

## 3. Hexagon (before outbound — private stack)

Add when drafting external mail:

| Leg | Demo note |
|:----|:----------|
| Production truth | Atlas would confirm no conflicting active order |
| Graph | Neo4j related entities (private) |
| Proof | `examples/public_demo/outbound_proof_artifacts.json` — registry IDs only |
| Corrections | Mnemon ledger overrides stale KB |

---

## 4. Draft (never auto-send)

**To:** jane.buyer@demo-acme.com  
**Subject:** Acme — closed-chamber forming review (demo)

Body sketch (plain text):

- Reference allowed claim from proof artifact `demo-acme-pf1-reference` only.
- Bridge to technical review call — no invented EUR/USD figures.
- Sign-off with operator name.

**Policy:** Show draft in Cursor → user says **send** explicitly → only then Gmail send in OPERATIONAL mode (private).

---

## 5. Visitor MCP prompts to try

```
Explain triangulation for Acme Thermoforming using only public demo files.
Search demo knowledge for PF1 tray closed-chamber.
Build a business case for a US thermoformer adopting Ira visitor mode first.
```

---

## Related files

- Deck brief: `examples/public_demo/deck_briefs/demo-acme-thermoformer.md`
- Sample thread: `examples/sample_email_thread.md`
- Triangulation runbook: `docs/IRA_TRIANGULATION.md`
