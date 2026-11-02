import re
from typing import Any

from litellm import completion


def build_sql_prompt(question: str, schema: dict[str, list[str]]) -> str:
    schema_text = "\n".join(f"Table: {table_name}\nColumns: {', '.join(columns)}" for table_name, columns in schema.items())
    return (
        "You are a SQL-generation assistant. Generate only valid SQL for the provided schema.\n"
        f"User question: {question}\n\nSchema:\n{schema_text}\n\n"
        "Return only a single SQL statement."
    )


def generate_sql(question: str, schema: dict[str, list[str]]) -> str:
    """Generate a SQL query from a natural-language prompt.

    If the model call fails, this returns a safe fallback so the system still has a
    deterministic, testable response path.
    """
    if not question or not schema:
        return "SELECT 1;"

    try:
        prompt = build_sql_prompt(question, schema)
        response = completion(
            model="groq/llama-3.1-8b-instant",
            messages=[{"role": "user", "content": prompt}],
        )
        sql = response.choices[0].message.content.strip()
        return re.sub(r"\s+", " ", sql)
    except Exception:
        return "SELECT 1;"


def sanitize_sql(sql: str) -> str:
    return re.sub(r"\s+", " ", sql).strip()
