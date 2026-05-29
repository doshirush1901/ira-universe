PUBLIC DEMO DATA — fully synthetic. This file does not contain Machinecraft customer, pricing, quote, invoice, CRM, Gmail, or email data.

# Demo email workflow (human-in-the-loop)

1. **Search** — optional Gmail connector (local credentials only).
2. **Draft** — Calliope-style writer proposes `To` / `Subject` / `Body` using **synthetic proof registry** under `examples/public_demo/`.
3. **Review** — human edits in Cursor (or your UI).
4. **Send** — only when `IRA_EMAIL_MODE=OPERATIONAL` and the operator explicitly confirms.

No auto-send in public demo defaults.
