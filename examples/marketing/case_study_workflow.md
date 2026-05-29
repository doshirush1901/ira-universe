# Case study workflow (public description)

This document describes how Ira supports **NDA-safe marketing collateral** (LinkedIn carousels, PDF one-pagers) without naming live customers or shipping private assets in public repos.

## What the workflow does

1. Load brand spec from `data/brand/design.md` (colors, typography, slide sizes).
2. Use a **deck brief** under `data/brand/deck_briefs/{slug}.md` (per-account outline, synthetic in public demos).
3. Cadmus (writer agent) drafts copy; operator runs build scripts to export PNG/PDF.
4. Proof claims must come from `data/knowledge/outbound_proof_artifacts.json` (or the public demo registry under `examples/public_demo/`).

## What stays private (Machinecraft operator repo)

- Named customer programs and real installation photos.
- Full case-study PDFs/PPTX in local `ira justification/` (gitignored).
- CRM-linked deck briefs with real domains and contact history.

## Public demo equivalent

See `examples/public_demo/deck_briefs/demo-acme-thermoformer.md` for a **synthetic** thermoformer account (`Acme`) used in visitor mode and training.

## Ira Universe

External users on [ira-universe](https://github.com/doshirush1901/ira-universe) do **not** receive case-study build scripts or named customer collateral — only architecture docs and synthetic examples.
