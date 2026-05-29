from __future__ import annotations

from pathlib import Path

import pytest

import ira_universe.corpus as corpus
import ira_universe.mcp_server as mcp_mod


def test_universe_tool_registry() -> None:
    names = sorted(mcp_mod.universe_mcp._tool_manager._tools.keys())
    assert "build_ira_business_case" in names
    assert "who_is_ira" in names
    assert "demo_account_brief" in names
    assert "walkthrough_pipeline" in names
    assert len(names) == 16


def test_demo_account_brief_json() -> None:
    import json

    from ira_universe import demos

    data = json.loads(demos.account_brief_json())
    assert data["synthetic"] is True
    assert data["triangle"]["relationship"]["status"] == "UNVERIFIED"


def test_corpus_excludes_sensitive_paths() -> None:
    rels = {p.relative_to(corpus.repo_root()).as_posix() for p in corpus.collect_public_corpus_paths()}
    assert "PSG_Case_Study" not in rels
    assert not any(r.startswith("src/ira/interfaces/mcp_server.py") for r in rels)
    assert "SOUL.md" in rels


def test_strict_guard_blocks_sensitive_env(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setenv("IRA_VISITOR_MCP_STRICT", "1")
    monkeypatch.setenv("GOOGLE_TOKEN_PATH", "/tmp/t.json")
    with pytest.raises(RuntimeError):
        mcp_mod._validate_strict_env_guard()


def test_public_paths_exist() -> None:
    paths = corpus.collect_public_corpus_paths()
    assert paths
    assert all(isinstance(p, Path) and p.is_file() for p in paths)
