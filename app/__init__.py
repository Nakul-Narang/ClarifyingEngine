# ClarifyingEngine

A production-oriented Text-to-SQL engine that combines database schema intelligence, vector retrieval, and clarification workflows to turn natural-language questions into safer, more accurate SQL.

Live demo: https://your-demo-url.example

[![Python](https://img.shields.io/badge/Python-3.11%2B-3776AB?logo=python&logoColor=white)](https://www.python.org/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.110%2B-009688?logo=fastapi&logoColor=white)](https://fastapi.tiangolo.com/)
[![PostgreSQL](https://img.shields.io/badge/PostgreSQL-Database-336791?logo=postgresql&logoColor=white)](https://www.postgresql.org/)
[![Qdrant](https://img.shields.io/badge/Qdrant-Vector-DB-4C1D95?logo=qdrant&logoColor=white)](https://qdrant.tech/)
[![Pytest](https://img.shields.io/badge/Tests-Pytest-0A9EDC?logo=pytest&logoColor=white)](https://pytest.org/)

## Why this project matters

Modern business users often ask questions in natural language, but databases are structured and strict. ClarifyingEngine bridges that gap by:

- understanding the underlying schema
- retrieving the most relevant tables using vector search
- detecting ambiguous questions before generating SQL
- producing safer SQL workflows for internal analytics and query copilots

This makes it a strong portfolio project for roles in data engineering, backend engineering, AI applications, and data platform work.

## Core features

- Text-to-SQL generation workflow with schema-aware context
- Qdrant-backed schema indexing for relevant table retrieval
- Ambiguity detection to avoid unsafe or overly broad SQL generation
- PostgreSQL schema introspection for runtime context
- Environment-based configuration for secure local and cloud deployment
- Test-ready project structure built with Python and pytest

## Tech stack

- Python 3.11+
- FastAPI
- Pydantic + BaseSettings
- PostgreSQL
- Qdrant
- LiteLLM
- SQLGlot
- Pytest

## Architecture

The engine follows a layered pipeline:

1. User asks a question in plain English.
2. The system inspects the database schema and relevant tables.
3. It retrieves the most relevant schema context using vector embeddings.
4. It checks whether the question is ambiguous or incomplete.
5. It generates SQL using a model-backed workflow.
6. The SQL is returned in a structured, inspectable format for downstream use.

## Project structure

```text
ClarifyingEngine/
├── app/
│   ├── __init__.py
│   ├── clarification_handler.py
│   ├── config.py
│   ├── database.py
│   ├── main.py
│   ├── schema_retriever.py
│   └── text_to_sql_direct.py
├── tests/
│   └── __init__.py
├── .env.example
├── .gitignore
├── pyproject.toml
├── README.md
└── .github/
```

## Local setup

```bash
git clone https://github.com/Nakul-Narang/ClarifyingEngine.git
cd ClarifyingEngine
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -e .
cp .env.example .env
uvicorn app.main:app --reload
```

## Environment variables

Create a `.env` file based on the example:

```env
DATABASE_URL=postgresql://user:password@host:5432/dbname?sslmode=require
QDRANT_URL=https://your-cluster-id.qdrant.tech
QDRANT_API_KEY=your-qdrant-key
GROQ_API_KEY=your-groq-or-openai-key
```

## Resume-oriented project checklist

This repository is structured to look professional on a resume:

- clear README with problem statement and architecture
- explicit tech stack
- secure environment variable handling
- configuration-ready project layout
- Python package structure with installable dependencies
- test-ready setup
- deployment-ready app entrypoint

## Roadmap

- add robust SQL validation before execution
- improve the clarification workflow for ambiguous queries
- add integration tests with sample schema fixtures
- create a hosted demo with a Postgres + Qdrant sandbox
- add CI checks and linting

## License

This project is currently set up for personal portfolio use. Add a license file if you plan to share it publicly beyond your resume and GitHub profile.
