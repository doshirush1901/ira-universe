"""Heuristic business-case builder (no LLM required for visitor mode)."""

from __future__ import annotations

from ira_universe.schemas import IraBusinessCase, format_ira_business_case_plain


def build_business_case(
    use_case: str,
    *,
    audience: str = "external prospect",
    company_context: str = "",
) -> IraBusinessCase:
    uc = (use_case or "").strip() or "general operations"
    ctx = (company_context or "").strip()
    return IraBusinessCase(
        use_case=uc,
        audience=(audience or "external prospect").strip(),
        one_liner=(
            "Ira is a company-specific multi-agent operating system — not a chat box — "
            f"designed for workflows like: {uc}."
        ),
        problem_statement=(
            "Generic AI assistants answer questions but do not run your factory workflows "
            "(evidence triangulation, draft-only outbound, production-aware pipeline) "
            "with institutional memory and human approval gates."
            + (f" Context: {ctx[:400]}" if ctx else "")
        ),
        ira_vs_generic=[
            "Workflow: brief → evidence → draft → human approve — not one-off chats",
            "Memory: corrections and documented sources beat stale copy-paste",
            "Truth: gaps are labeled UNVERIFIED instead of inventing CRM/mail history",
            "Specialists: bounded agents (sales, production, finance) stay in lane",
        ],
        roi_thesis=(
            "Illustrative: one operator with Ira can cover research, account context, and "
            "draft outreach that would otherwise fragment across tools or headcount. "
            "Verify numbers against your own labor and SaaS stack."
        ),
        implementation_path=[
            "Clone ira-universe and run visitor MCP in Claude Code",
            f"Pilot `{uc}` with synthetic demo data first",
            "Fork privately; add your CRM/mail/KB connectors under .env (never commit secrets)",
            "Keep send human-approved; expand to full Ira stack only when ready",
        ],
        risks_and_mitigations=[
            "Hallucination — mitigated by corpus-only visitor mode + source citations",
            "Over-scoping — start with visitor tools before operational MCP",
            "Data leakage — keep customer data in private remotes, not public repos",
        ],
        recommended_collateral=[
            "README.md",
            "docs/ARCHITECTURE.md",
            "docs/VISITOR_MCP.md",
            "examples/public_demo/",
        ],
        call_to_action="Run visitor MCP, then schedule a 20-minute architecture walkthrough.",
        unverified_gaps=["ROI and FTE equivalents need your own verification"],
    )


def build_business_case_plain(
    use_case: str,
    *,
    audience: str = "external prospect",
    company_context: str = "",
) -> str:
    return format_ira_business_case_plain(
        build_business_case(use_case, audience=audience, company_context=company_context)
    )
