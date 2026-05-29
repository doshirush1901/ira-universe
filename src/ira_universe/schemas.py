"""Structured business-case schema for Ira Universe."""

from __future__ import annotations

from pydantic import BaseModel, Field


class IraBusinessCase(BaseModel):
    use_case: str
    audience: str
    one_liner: str
    problem_statement: str
    ira_vs_generic: list[str] = Field(default_factory=list)
    roi_thesis: str
    implementation_path: list[str] = Field(default_factory=list)
    risks_and_mitigations: list[str] = Field(default_factory=list)
    recommended_collateral: list[str] = Field(default_factory=list)
    call_to_action: str
    unverified_gaps: list[str] = Field(default_factory=list)


def format_ira_business_case_plain(case: IraBusinessCase) -> str:
    lines = [
        f"IRA BUSINESS CASE — {case.use_case}",
        f"Audience: {case.audience}",
        "",
        case.one_liner,
        "",
        "PROBLEM",
        case.problem_statement,
        "",
        "IRA VS GENERIC AI",
    ]
    lines.extend(f"- {b}" for b in case.ira_vs_generic)
    lines.extend(["", "ROI THESIS", case.roi_thesis, "", "IMPLEMENTATION PATH"])
    lines.extend(f"{i}. {step}" for i, step in enumerate(case.implementation_path, 1))
    lines.extend(["", "RISKS & MITIGATIONS"])
    lines.extend(f"- {r}" for r in case.risks_and_mitigations)
    if case.recommended_collateral:
        lines.extend(["", "RECOMMENDED COLLATERAL"])
        lines.extend(f"- {c}" for c in case.recommended_collateral)
    lines.extend(["", "CALL TO ACTION", case.call_to_action])
    if case.unverified_gaps:
        lines.extend(["", "UNVERIFIED (verify before external use)"])
        lines.extend(f"- {g}" for g in case.unverified_gaps)
    return "\n".join(lines)
