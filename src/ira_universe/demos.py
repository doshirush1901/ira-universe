"""Hardcoded synthetic demos for ira-universe MCP (no CRM/Gmail)."""

from __future__ import annotations

import json
from typing import Any

# PUBLIC DEMO DATA — fictional Acme Thermoforming only.
ACME_ACCOUNT_BRIEF: dict[str, Any] = {
    "company": "Acme Thermoforming LLC",
    "domain": "demo-acme.com",
    "contact": "jane.buyer@demo-acme.com",
    "synthetic": True,
    "triangle": {
        "intent": {
            "status": "verified",
            "sources": ["data/knowledge/demo_product_specs.md"],
            "summary": "Interest in closed-chamber PF1-class tray line; gauge consistency pain.",
        },
        "relationship": {
            "status": "UNVERIFIED",
            "sources": [],
            "summary": "Visitor mode has no live CRM or Gmail. Private stack would search mail + deals.",
        },
        "identity": {
            "status": "verified",
            "sources": ["examples/sample_customer_context.md"],
            "summary": "US Midwest thermoformer; synthetic firmographics only.",
        },
    },
    "hexagon_gaps": [
        "production_truth — requires Atlas (private deploy)",
        "graph_neighbors — requires Neo4j (private deploy)",
        "proof_registry — see examples/public_demo/outbound_proof_artifacts.json",
        "corrections — requires Mnemon ledger (private deploy)",
    ],
    "recommended_next": [
        "Read examples/public_demo/journey_acme.md",
        "Run demo_draft_email for a proof-safe follow-up sketch",
        "Fork privately before citing real customers or prices",
    ],
}

PIPELINE_WALKTHROUGH: list[dict[str, str]] = [
    {"step": "1 PERCEIVE", "note": "Who is asking, which channel, emotional tone."},
    {"step": "2 REMEMBER", "note": "Conversation history, goals, coreference."},
    {"step": "2.5 FAST PATH", "note": "Trivial greetings / thanks — skip heavy routing."},
    {"step": "2.7 SPHINX", "note": "Vague query → clarifying questions only."},
    {"step": "3–5 ROUTE", "note": "Fast keywords → learned procedures → Athena LLM route."},
    {"step": "5.1 EMAIL SCOPE", "note": "Live vs imported mail (private connectors)."},
    {"step": "5.5 ENRICH", "note": "Style, episodes, endocrine tone modifiers."},
    {"step": "6 EXECUTE", "note": "Up to 5 parallel specialists, each bounded by agent timeout."},
    {"step": "6.1a ALETHEIA", "note": "Trace claims to sources — provenance."},
    {"step": "6.1b AEGIS", "note": "DLP — PII and confidential terms."},
    {"step": "6.2 MNEMON", "note": "Operator corrections override stale KB."},
    {"step": "6.3 GAPPER", "note": "Fill missing specs/dates from evidence — never invent."},
    {"step": "6.4 FAITHFULNESS", "note": "4-tier grounding; caveat if weak."},
    {"step": "7–9 SHAPE", "note": "Assess, reflect, voice for recipient/channel."},
    {"step": "10 LEARN", "note": "Background memory/CRM updates after response."},
    {"step": "11 RETURN", "note": "Final answer to user."},
]


def format_account_brief(brief: dict[str, Any]) -> str:
    lines = [
        f"ACCOUNT BRIEF — {brief['company']} (SYNTHETIC DEMO)",
        f"Domain: {brief['domain']} · Contact: {brief['contact']}",
        "",
        "TRIANGLE",
    ]
    for leg, data in brief["triangle"].items():
        status = data["status"].upper()
        lines.append(f"- {leg.title()}: {status}")
        lines.append(f"  {data['summary']}")
        if data.get("sources"):
            lines.append(f"  Sources: {', '.join(data['sources'])}")
    lines.extend(["", "HEXAGON (gaps in visitor mode)"])
    lines.extend(f"- {g}" for g in brief["hexagon_gaps"])
    lines.extend(["", "NEXT"])
    lines.extend(f"- {n}" for n in brief["recommended_next"])
    return "\n".join(lines)


def format_pipeline_walkthrough() -> str:
    lines = ["IRA PIPELINE WALKTHROUGH (17-step summary)", ""]
    for row in PIPELINE_WALKTHROUGH:
        lines.append(f"{row['step']}: {row['note']}")
    lines.extend(
        [
            "",
            "Early exits: dedup, fast path, Sphinx clarify-only, truth hints.",
            "See docs/PIPELINE_AUDIT.md and docs/TIMEOUT_MODEL.md.",
        ]
    )
    return "\n".join(lines)


def format_demo_draft_email(
    *,
    contact_name: str = "Jane",
    company: str = "Acme Thermoforming LLC",
) -> str:
    return f"""DRAFT ONLY — SYNTHETIC DEMO (do not send)

To: jane.buyer@demo-acme.com
Subject: {company} — closed-chamber forming review (demo)

Hi {contact_name},

Following our discussion on tray-line consistency, I wanted to share a short technical note aligned with our public demo registry (artifact: demo-acme-pf1-reference).

Allowed narrative only: Acme evaluated a servo closed-chamber approach for tray production. I am not stating price, delivery date, or throughput figures in this demo draft.

If useful, we can schedule a 30-minute technical review to map your part geometry and changeover goals.

Best regards,
[Operator name]

---
Policy: In production Ira, Calliope drafts; operator approves; send only on explicit "send" in OPERATIONAL mode.
Proof: examples/public_demo/outbound_proof_artifacts.json
"""


def account_brief_json() -> str:
    return json.dumps(ACME_ACCOUNT_BRIEF, indent=2, ensure_ascii=False)
