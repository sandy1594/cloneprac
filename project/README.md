# Healthcare Platform Monorepo

Practo-inspired healthcare appointment system featuring a FastAPI backend and Next.js frontend. This repository houses everything required to bootstrap patient, doctor, and admin experiences.

## Contents

- `backend/` – FastAPI service exposing auth, patient, doctor, and admin endpoints
- `frontend/` – Next.js 14 App Router UI with role-based workspaces
- `docs/` – Product specification and architectural notes

## Quickstart

### Backend

```bash
cd backend
poetry install
poetry run uvicorn app.main:app --reload
```

### Frontend

```bash
cd frontend
npm install
npm run dev
```

Ensure PostgreSQL is running and accessible via the connection string in `backend/.env.example`. Update `.env` files as needed before running the services.

## Architecture Overview

```text
frontend (Next.js)
    ↕ REST/JSON
backend (FastAPI)
    ↕
PostgreSQL (Core data store)
Redis (caching, async queues - planned)
S3-compatible storage (media uploads - planned)
```

## Next Steps

- Implement authentication flow end-to-end (JWT storage, refresh, OAuth)
- Add Alembic migrations and seed data for core tables
- Wire frontend forms to backend endpoints with React Query
- Introduce automated tests (pytest, Playwright) and CI workflows
- Extend admin analytics and doctor availability with real data sources
