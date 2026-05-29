#!/usr/bin/env bash
# Lightweight guard for exported ira-universe tree (no PyYAML / full repo required).
set -euo pipefail

ROOT="${1:-.}"
cd "$ROOT"

fail() {
  echo "public_export_guard: $1" >&2
  exit 1
}

if rg -q 'forma3d\.pt|indusind\.com|seed-active-21' . \
  --glob '!poetry.lock' \
  --glob '!scripts/public_export_guard.sh' \
  2>/dev/null; then
  fail "forbidden domain or programme string found"
fi

if rg -qi 'rushabh@|@machinecraft\.(org|in)' . \
  --glob '!poetry.lock' \
  --glob '!scripts/public_export_guard.sh' \
  2>/dev/null; then
  fail "forbidden org email found"
fi

if rg -q 'sk-[a-zA-Z0-9]{20,}' . 2>/dev/null; then
  fail "possible API key pattern found"
fi

echo "public_export_guard: OK"
