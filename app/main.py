# ClarifyingEngine

A production-oriented Text-to-SQL engine that turns natural-language questions into safer, schema-aware SQL using PostgreSQL introspection, vector retrieval, and ambiguity detection.

Live demo: https://clarifyingengine.onrender.com

[![Python](https://img.shields.io/badge/Python-3.11%2B-3776AB?logo=python&logoColor=white)](https://www.python.org/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.110%2B-009688?logo=fastapi&logoColor=white)](https://fastapi.tiangolo.com/)
[![PostgreSQL](https://img.shields.io/badge/PostgreSQL-Database-336791?logo=postgresql&logoColor=white)](https://www.postgresql.org/)
[![Qdrant](https://img.shields.io/badge/Qdrant-Vector-DB-4C1D95?logo=qdrant&logoColor=white)](https://qdrant.tech/)
[![Pytest](https://img.shields.io/badge/Tests-Pytest-0A9EDC?logo=pytest&logoColor=white)](https://pytest.org/)

## Why this project matters

Most businesses ask questions in natural language, but data lives in structured tables. ClarifyingEngine helps bridge that gap by:

- reading the live database schema
- retrieving the most relevant tables with vector similarity search
- detecting ambiguous or underspecified questions before generating SQL
- returning a cleaner, safer SQL workflow for analytics and AI copilots

This is a strong resume project for backend, AI application, and data platform roles because it combines product thinking, system design, and practical data engineering.

## Core capabilities

- schema-aware Text-to-SQL generation
- Qdrant-backed indexing for relevant table retrieval
- ambiguity detection and clarification prompts
- PostgreSQL runtime introspection
- secure environment-based configuration
- deployment-ready FastAPI service

## Tech stack

- Python 3.11+
- FastAPI
- Pydantic + BaseSettings
- PostgreSQL
- Qdrant
- LiteLLM
- SQLGlot
- Pytest

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
├── requirements.txt
├── render.yaml
├── Procfile
├── runtime.txt
├── Dockerfile
├── README.md
└── .github/
```

## Local setup

```bash
git clone https://github.com/Nakul-Narang/ClarifyingEngine.git
cd ClarifyingEngine
python -m venv .venv
source .venv/bin/activate   # Windows: .venv\Scripts\activate
pip install -r requirements.txt
cp .env.example .env
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

## Environment variables

Create a `.env` file using the template in `.env.example`:

```env
DATABASE_URL=postgresql://user:password@host:5432/dbname?sslmode=require
QDRANT_URL=https://your-cluster-id.qdrant.tech
QDRANT_API_KEY=your-qdrant-key
GROQ_API_KEY=your-groq-or-openai-key
```

## Deployment on Render

This project is configured for a simple Render deployment.

1. Push this repository to GitHub.
2. In Render, create a New Web Service.
3. Connect your GitHub repo.
4. Use the following settings:
   - Build Command: `pip install -r requirements.txt`
   - Start Command: `uvicorn app.main:app --host 0.0.0.0 --port $PORT`
5. Add the required environment variables in the Render dashboard.
6. Deploy.

A deployment config file is also included at `render.yaml` for a faster setup.

## API endpoints

- `GET /` -> service welcome message
- `GET /health` -> health check
- `GET /config` -> configured environment status

## Resume notes

This repository is structured to look strong on a resume because it includes:

- a professional README
- a clear architecture and feature summary
- production-style Python configuration
- environment variable separation
- API-ready service deployment setup
- use of modern backend and AI/data tooling

## Roadmap

- add SQL validation and execution safeguards
- expand the clarification flow for ambiguous user requests
- add sample schema fixtures and integration tests
- create a hosted demo with a Postgres + Qdrant sandbox
- add CI checks and linting

## License

This project is set up for personal portfolio use. Add an explicit LICENSE file if you plan to distribute it beyond your profile and resume.
