"""Ira Universe — public-safe MCP server (standalone package)."""

from __future__ import annotations

import json
import logging
import os
import sys
from pathlib import Path

from mcp.server.fastmcp import FastMCP

from ira_universe import business_case, corpus, demos

logger = logging.getLogger(__name__)

_MAX_SNIPPET_CHARS = 12_000
_DEFAULT_SEARCH_RESULTS = 5
_MAX_SEARCH_RESULTS = 12
_STRICT_ENV_FLAG = "IRA_VISITOR_MCP_STRICT"
_STRICT_BLOCKLIST_ENV = "IRA_VISITOR_MCP_BLOCK_ENV_KEYS"
_DEFAULT_SENSITIVE_CONNECTOR_ENV_KEYS = (
    "GOOGLE_TOKEN_PATH",
    "GOOGLE_CREDENTIALS_PATH",
    "GOOGLE_CLIENT_SECRET_PATH",
    "GMAIL_TOKEN_PATH",
    "CRM_DATABASE_URL",
)

universe_mcp = FastMCP(
    "ira-universe",
    instructions=(
        "Public-safe Ira Universe. Explain Ira architecture and adoption using only "
        "the allowlisted corpus in this repository. No CRM, Gmail, or customer data."
    ),
)


def _truncate(text: str, max_chars: int) -> str:
    limit = max(300, min(int(max_chars), _MAX_SNIPPET_CHARS))
    if len(text) <= limit:
        return text
    return f"{text[:limit].rstrip()}\n\n...[truncated]..."


def _env_flag_enabled(value: str | None) -> bool:
    return (value or "").strip().lower() in {"1", "true", "yes", "on"}


def _validate_strict_env_guard() -> None:
    if not _env_flag_enabled(os.getenv(_STRICT_ENV_FLAG)):
        return
    override = (os.getenv(_STRICT_BLOCKLIST_ENV) or "").strip()
    keys = (
        [p.strip() for p in override.split(",") if p.strip()]
        if override
        else list(_DEFAULT_SENSITIVE_CONNECTOR_ENV_KEYS)
    )
    flagged = [key for key in keys if (os.getenv(key) or "").strip()]
    if flagged:
        raise RuntimeError(
            "ira-universe strict mode blocked startup; sensitive connector env vars are set: "
            f"{', '.join(flagged)}. Unset them or disable {_STRICT_ENV_FLAG}."
        )


async def who_is_ira(max_chars: int = 4000) -> str:
    """Explain Ira identity from public constitutional docs."""
    soul = corpus.safe_read("SOUL.md", max_chars=12_000)
    readme = corpus.safe_read("README.md", max_chars=8_000)
    out = (
        "Ira identity (public architecture view)\n\n"
        "From SOUL.md:\n"
        f"{soul[:2500].strip()}\n\n"
        "From README:\n"
        f"{readme[:1700].strip()}"
    )
    return _truncate(out, max_chars)


async def how_ira_is_built(max_chars: int = 7000) -> str:
    """Summarize architecture-level implementation from public docs."""
    arch = corpus.safe_read("docs/ARCHITECTURE.md", max_chars=22_000)
    cert = corpus.safe_read("docs/IRA_BIRTH_CERTIFICATE.md", max_chars=18_000)
    agents = corpus.safe_read("AGENTS.md", max_chars=20_000)
    selected = (
        "Ira architecture (public)\n\n"
        "1) Certificate overview (docs/IRA_BIRTH_CERTIFICATE.md)\n"
        f"{cert[:2200].strip()}\n\n"
        "2) System shape (docs/ARCHITECTURE.md)\n"
        f"{arch[:2000].strip()}\n\n"
        "3) Agent operating model (AGENTS.md)\n"
        f"{agents[:2000].strip()}"
    )
    return _truncate(selected, max_chars)


async def list_pantheon_agents(max_chars: int = 8000) -> str:
    """Return the public pantheon section from AGENTS.md."""
    agents = corpus.safe_read("AGENTS.md", max_chars=40_000)
    start = agents.find("## The Pantheon")
    if start == -1:
        return "Pantheon section not found in AGENTS.md."
    end = -1
    for marker in ("## Request pipeline", "## Development Commands", "## Collaboration clusters"):
        pos = agents.find(marker, start)
        if pos > start and (end == -1 or pos < end):
            end = pos
    chunk = agents[start:end] if end > start else agents[start : start + 9000]
    return _truncate(chunk.strip(), max_chars)


async def explain_triangulation(max_chars: int = 5000) -> str:
    """Explain triangle/hexagon evidence workflow from public docs."""
    tri = corpus.safe_read("docs/IRA_TRIANGULATION.md", max_chars=16_000)
    if not tri:
        return "Triangulation doc not found."
    return _truncate(tri, max_chars)


async def fork_ira_for_your_factory(max_chars: int = 5000) -> str:
    """Give a public-safe adoption playbook for other factories."""
    body = (
        "Fork Ira for your factory (ira-universe → private fork)\n\n"
        "1) Start here: clone ira-universe and run visitor MCP in Claude Code.\n"
        "2) For production: fork privately; add your own API keys in .env (never commit).\n"
        "3) Keep customer CRM, mail, and quotes in private storage only.\n"
        "4) Add Docker stack (Postgres/Qdrant/Neo4j/Redis) when moving beyond visitor mode.\n"
        "5) Use synthetic demos first (`examples/public_demo/`, `data/knowledge/demo_*.md`).\n"
        "6) Full Machinecraft Ira (`ira-v3` private) adds CRM, Gmail, and operator MCP.\n\n"
        "See docs/PUBLIC_PRIVATE_BOUNDARY.md and examples/marketing/case_study_workflow.md."
    )
    return _truncate(body, max_chars)


async def list_public_corpus(max_chars: int = 6000) -> str:
    """List every file in the allowlisted public corpus."""
    root = corpus.repo_root()
    lines = ["Ira Universe public corpus:"]
    for path in corpus.collect_public_corpus_paths():
        lines.append(f"- {path.relative_to(root)}")
    return _truncate("\n".join(lines), max_chars)


async def search_public_docs(query: str, max_results: int = _DEFAULT_SEARCH_RESULTS) -> str:
    """Search the full allowlisted public corpus."""
    k = max(1, min(int(max_results), _MAX_SEARCH_RESULTS))
    return corpus.search_corpus(query, corpus.collect_public_corpus_paths(), k)


async def demo_search_knowledge(query: str, max_results: int = _DEFAULT_SEARCH_RESULTS) -> str:
    """Search synthetic demo knowledge only."""
    k = max(1, min(int(max_results), _MAX_SEARCH_RESULTS))
    demo_paths = [
        p
        for p in corpus.collect_public_corpus_paths()
        if p.relative_to(corpus.repo_root()).as_posix().startswith(
            ("examples/public_demo/", "data/knowledge/demo_")
        )
    ]
    return corpus.search_corpus(query, demo_paths, k)


async def universe_mcp_status() -> str:
    """Return safety and capability status."""
    n = len(corpus.collect_public_corpus_paths())
    return (
        "ira-universe status: OK\n"
        "- profile: public-safe visitor MCP (this repo only)\n"
        "- dependencies: mcp + pydantic (no full Ira stack required)\n"
        "- live connectors: none\n"
        f"- allowlisted files: {n}\n"
        "- tools: 16 (includes demo_account_brief, demo_draft_email, walkthrough_pipeline, why_ira)\n"
        "- not included: full operator MCP, web-ui, live CRM/Gmail\n"
    )


async def list_ira_justification_assets() -> str:
    """List public collateral available in this repo (not private pitch decks)."""
    return corpus.format_public_assets_index()


async def read_ira_justification_text(relative_path: str, max_chars: int = 12000) -> str:
    """Read a text file from this repo's public corpus (relative path)."""
    root = corpus.repo_root()
    target = (root / relative_path).resolve()
    try:
        target.relative_to(root)
    except ValueError:
        return "Path must stay inside the ira-universe repository."
    allowed = {p.resolve() for p in corpus.collect_public_corpus_paths()}
    if target not in allowed:
        return f"Not in public corpus: {relative_path}"
    if not target.is_file():
        return f"File not found: {relative_path}"
    text = target.read_text(encoding="utf-8")
    limit = max(500, min(int(max_chars), 60_000))
    return text[:limit]


async def demo_account_brief(as_json: bool = False) -> str:
    """Return a synthetic Acme account brief (triangle + UNVERIFIED legs). No live CRM or mail."""
    if as_json:
        return demos.account_brief_json()
    return demos.format_account_brief(demos.ACME_ACCOUNT_BRIEF)


async def demo_draft_email(contact_name: str = "Jane") -> str:
    """Return a proof-safe synthetic follow-up draft for demo Acme (DRAFT ONLY — never send)."""
    return demos.format_demo_draft_email(contact_name=contact_name.strip() or "Jane")


async def walkthrough_pipeline(max_chars: int = 6000) -> str:
    """Annotated 17-step pipeline walkthrough (public summary)."""
    return _truncate(demos.format_pipeline_walkthrough(), max_chars)


async def why_ira(max_chars: int = 7000) -> str:
    """Narrative: why multi-agent Ira vs a chat box (public WHY_IRA.md)."""
    text = corpus.safe_read("docs/WHY_IRA.md", max_chars=20_000)
    if not text:
        return "docs/WHY_IRA.md not found in corpus."
    return _truncate(text, max_chars)


async def build_ira_business_case(
    use_case: str,
    audience: str = "external prospect",
    company_context: str = "",
    as_json: bool = False,
) -> str:
    """Build a heuristic business case (no API keys required)."""
    case = business_case.build_business_case(
        use_case,
        audience=audience,
        company_context=company_context,
    )
    if as_json:
        return json.dumps(case.model_dump(mode="json"), indent=2, ensure_ascii=False)
    return business_case.build_business_case_plain(
        use_case, audience=audience, company_context=company_context
    )


def register_tools() -> None:
    universe_mcp.tool()(who_is_ira)
    universe_mcp.tool()(how_ira_is_built)
    universe_mcp.tool()(list_pantheon_agents)
    universe_mcp.tool()(explain_triangulation)
    universe_mcp.tool()(fork_ira_for_your_factory)
    universe_mcp.tool()(list_public_corpus)
    universe_mcp.tool()(search_public_docs)
    universe_mcp.tool()(demo_search_knowledge)
    universe_mcp.tool()(universe_mcp_status)
    universe_mcp.tool()(list_ira_justification_assets)
    universe_mcp.tool()(read_ira_justification_text)
    universe_mcp.tool()(build_ira_business_case)
    universe_mcp.tool()(demo_account_brief)
    universe_mcp.tool()(demo_draft_email)
    universe_mcp.tool()(walkthrough_pipeline)
    universe_mcp.tool()(why_ira)


register_tools()


def main() -> None:
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s  %(name)-28s  %(levelname)-8s  %(message)s",
        datefmt="%H:%M:%S",
        stream=sys.stderr,
        force=True,
    )
    logging.getLogger("mcp.server.lowlevel.server").setLevel(logging.WARNING)
    _validate_strict_env_guard()
    logger.info("Starting Ira Universe MCP (stdio; logs on stderr).")
    universe_mcp.run()


if __name__ == "__main__":
    main()
