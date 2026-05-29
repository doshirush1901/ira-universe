# Contributing to ira-universe (public repo)

Thank you for helping keep the public visitor repo safe and useful.

## What belongs in the public export

- Architecture and adoption docs (`docs/*_PUBLIC.md` sources in ira-v3)
- Synthetic demos under `examples/public_demo/` and `data/knowledge/demo_*.md`
- `src/ira_universe/` visitor MCP package
- Tests that do not require live API keys

## What never belongs

- Customer names, real domains, quotes, or mailbox text
- `.env`, tokens, CRM exports, `data/imports/`
- Full `src/ira/` operator stack
- `machinecraft.org` emails or campaign-specific strings (see `scripts/public_repo_guard.py` in ira-v3)

## How maintainers publish

From **ira-v3** root:

```bash
bash scripts/republish_ira_universe.sh
```

This exports to `../ira-universe-export`, runs tests, commits if changed, and pushes `main`.

Manual export only:

```bash
python3 scripts/export_ira_universe_repo.py -o ../ira-universe-export
```

## PR checklist

- [ ] No secrets or real customer data
- [ ] Demo files marked synthetic at the top
- [ ] `poetry run pytest tests/test_ira_universe_mcp.py` passes
- [ ] Corpus allowlist updated in `src/ira_universe/corpus.py` if adding docs
