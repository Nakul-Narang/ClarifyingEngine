from dataclasses import dataclass, field
from typing import Any


@dataclass
class ClarificationResult:
    is_ambiguous: bool = False
    questions: list[str] = field(default_factory=list)
    suggestions: list[str] = field(default_factory=list)


def detect_ambiguity(user_query: str, schema: dict[str, list[str]] | None = None) -> ClarificationResult:
    """Detect common ambiguity patterns in natural-language SQL queries.

    This is intentionally lightweight and deterministic so it can be used as a
    first-pass guardrail before invoking a larger model-driven text-to-SQL flow.
    """
    normalized = user_query.strip().lower()

    if not normalized:
        return ClarificationResult(
            is_ambiguous=True,
            questions=["What data would you like to query?"],
            suggestions=["Provide a clear question with the relevant table or metric."],
        )

    ambiguous_terms = ["recent", "total", "latest", "customer", "user", "sales", "revenue", "status"]
    matching_terms = [term for term in ambiguous_terms if term in normalized]

    if matching_terms:
        return ClarificationResult(
            is_ambiguous=True,
            questions=[f"Which '{term}' do you want to reference?" for term in matching_terms[:3]],
            suggestions=["Add the specific table, date range, or business entity you want to analyze."],
        )

    if schema is not None and not schema:
        return ClarificationResult(
            is_ambiguous=True,
            questions=["No database schema is available yet."],
            suggestions=["Connect to the database and index the schema before running the SQL workflow."],
        )

    return ClarificationResult(is_ambiguous=False)


def build_clarification_prompt(user_query: str, schema: dict[str, list[str]] | None = None) -> list[dict[str, str]]:
    schema_summary = "No schema loaded"
    if schema:
        schema_summary = "\n".join(
            f"Table: {table_name}\nColumns: {', '.join(columns)}" for table_name, columns in schema.items()
        )

    return [
        {
            "role": "system",
            "content": "You are a careful SQL assistant. Ask clarifying questions only when the request is ambiguous or underspecified.",
        },
        {
            "role": "user",
            "content": f"User question: {user_query}\n\nSchema context:\n{schema_summary}",
        },
    ]


__all__ = ["ClarificationResult", "detect_ambiguity", "build_clarification_prompt"]


# This module intentionally keeps a lightweight, dependency-free interface so the
# project remains easy to present on a resume and easy to test locally.
