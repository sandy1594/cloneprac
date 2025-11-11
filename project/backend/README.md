 # Healthcare Platform Backend

FastAPI-based backend service for the Practo-like healthcare platform. It exposes authentication, patient, doctor, and admin endpoints aligned with the product specification.

## Getting Started

### 1. Prerequisites

- Python 3.11+
- PostgreSQL 14+
- Redis (optional, used for caching and queues)
- [Poetry](https://python-poetry.org/docs/) for dependency management (`pipx install poetry`)

### 2. Environment Variables

Copy `.env.example` to `.env` and adjust values as needed.

```bash
cp .env.example .env
```

### 3. Install Dependencies

```bash
poetry install
```

### 4. Run Database Migrations (Placeholder)

Alembic scaffolding is not yet included. For now, create the database and tables manually or via SQLAlchemy metadata.

### 5. Start the Server

```bash
poetry run uvicorn app.main:app --reload
```

The API will be available at `http://localhost:8000/api`.

### 6. Interactive Documentation

- Swagger UI: `http://localhost:8000/api/docs`
- ReDoc: `http://localhost:8000/api/redoc` (enable by adjusting `app/main.py` if desired)

## Project Structure

```
backend/
  ├── app/
  │   ├── api/              # Route handlers grouped by module
  │   ├── core/             # Configuration & security helpers
  │   ├── db/               # SQLAlchemy engine and base metadata
  │   ├── models/           # ORM models reflecting the data schema
  │   ├── schemas/          # Pydantic models for request/response validation
  │   ├── services/         # Domain logic (e.g., availability)
  │   └── main.py           # FastAPI initialization
  ├── pyproject.toml        # Poetry configuration
  └── README.md             # This file
```

## Roadmap

- ✅ Base models and core endpoints
- ⬜ Alembic migrations and seed scripts
- ⬜ Redis-backed notification and queue processors
- ⬜ Integration tests covering auth and appointment flows
- ⬜ WebSocket updates for realtime queue management
