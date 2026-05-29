"""Allowlisted public document corpus for Ira Universe."""

from __future__ import annotations

import re
from pathlib import Path

_REPO_ROOT = Path(__file__).resolve().parents[2]

_STATIC_PUBLIC_FILES = (
    "README.md",
    "SOUL.md",
    "VISION.md",
    "AGENTS.md",
    "docs/ARCHITECTURE.md",
    "docs/IRA_BIRTH_CERTIFICATE.md",
    "docs/IRA_TRIANGULATION.md",
    "docs/PUBLIC_PRIVATE_BOUNDARY.md",
    "docs/DATA_PRIVACY.md",
    "docs/IRA_INSTRUMENT_GUIDE.md",
    "docs/VISITOR_MCP.md",
    "docs/CURSOR_AGENTIC_LOOP.md",
    "docs/CURSOR_WORKFLOWS.md",
    "docs/TIMEOUT_MODEL.md",
    "docs/PIPELINE_AUDIT.md",
    "docs/INDEX.md",
    "docs/IRA_SAMPLE_PROMPTS.md",
    "docs/AGENT_LOOP_STANDARD.md",
    "docs/LONG_RUNNING_HARNESS.md",
    "docs/WHY_IRA.md",
)

_GLOB_PUBLIC_FILES = (
    "data/knowledge/demo_*.md",
    "examples/public_demo/**/*.md",
    "examples/public_demo/**/*.json",
    "examples/sample_*.md",
    "examples/marketing/**/*.md",
)

_MAX_FILE_READ_CHARS = 60_000


def repo_root() -> Path:
    return _REPO_ROOT


def collect_public_corpus_paths() -> list[Path]:
    paths: list[Path] = []
    seen: set[Path] = set()
    for rel_path in _STATIC_PUBLIC_FILES:
        path = (_REPO_ROOT / rel_path).resolve()
        if path.is_file() and path not in seen:
            seen.add(path)
            paths.append(path)
    for pattern in _GLOB_PUBLIC_FILES:
        for path in _REPO_ROOT.glob(pattern):
            resolved = path.resolve()
            if resolved.is_file() and resolved not in seen:
                seen.add(resolved)
                paths.append(resolved)
    return sorted(paths)


def safe_read(rel_path: str, max_chars: int = _MAX_FILE_READ_CHARS) -> str:
    path = _REPO_ROOT / rel_path
    if not path.is_file():
        return ""
    return path.read_text(encoding="utf-8")[: max(1000, min(max_chars, _MAX_FILE_READ_CHARS))]


def search_corpus(query: str, paths: list[Path], max_results: int) -> str:
    term = query.strip()
    if not term:
        return "Provide a non-empty query."
    needle = term.lower()
    ranked: list[tuple[int, str, Path]] = []
    for path in paths:
        text = path.read_text(encoding="utf-8")[:_MAX_FILE_READ_CHARS]
        lowered = text.lower()
        score = lowered.count(needle)
        if score <= 0:
            continue
        excerpt_idx = lowered.find(needle)
        start = max(0, excerpt_idx - 220)
        end = min(len(text), excerpt_idx + max(220, len(term) + 220))
        excerpt = re.sub(r"\s+", " ", text[start:end].replace("\n", " ").strip())
        ranked.append((score, excerpt, path))

    if not ranked:
        return f'No matches in visitor corpus for "{term}".'

    ranked.sort(key=lambda item: item[0], reverse=True)
    lines = [f'Matches for "{term}" ({min(max_results, len(ranked))} shown):']
    for idx, (score, excerpt, path) in enumerate(ranked[:max_results], start=1):
        rel = path.relative_to(_REPO_ROOT)
        lines.append(f"{idx}. {rel} (score={score})")
        lines.append(f"   {excerpt}")
    return "\n".join(lines)


def format_public_assets_index() -> str:
    lines = [
        "Public collateral index (ira-universe repo only).",
        "For full operator pitch decks, use a private Machinecraft clone with local `ira justification/`.",
        "",
    ]
    for path in collect_public_corpus_paths():
        rel = path.relative_to(_REPO_ROOT)
        hint = ""
        name = path.name
        if "demo_" in name or "public_demo" in rel.as_posix():
            hint = " — synthetic demo"
        elif rel.as_posix().endswith("SOUL.md"):
            hint = " — identity / values"
        elif "ARCHITECTURE" in name:
            hint = " — system architecture"
        lines.append(f"- {rel}{hint}")
    return "\n".join(lines)
