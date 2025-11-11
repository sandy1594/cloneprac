# Healthcare Platform — Technical Specification

## 1. Vision

A Practo-style, multi-tenant healthcare platform that allows patients to discover doctors, book appointments, manage health journeys, while clinics and administrators orchestrate verification, scheduling, and analytics.

## 2. Stack Summary

| Layer      | Technology  | Notes |
|------------|-------------|-------|
| Frontend   | Next.js 14 (App Router) + TypeScript | Role-based workspaces for patients, doctors, admins |
| Backend    | FastAPI + SQLAlchemy                 | REST API, JWT auth, modular routing |
| Database   | PostgreSQL                           | Relational store for users, appointments, transactions |
| Caching    | Redis (planned)                      | Session caching, queues, notification buffers |
| Storage    | AWS S3 (planned)                     | Avatars, documents, medical assets |

## 3. Modules & Features

### Patient
- Doctor search (specialty, location, symptoms keyword)
- Doctor profile details (experience, clinic info, fees, rating)
- Appointment booking & history
- Personal profile management

### Doctor / Clinic
- Onboarding & verification (admin workflow)
- Schedule + availability management
- Patient queue oversight
- Basic EHR (future)
- Analytics dashboard (visit volumes, patient metrics)

### Admin
- User management
- Doctor verification pipeline
- Reporting & analytics (revenue, appointments, growth)
- Payment reconciliation
- CMS for marketing content (phase 2+)

## 4. Data Model (simplified)

| Entity          | Key Attributes |
|-----------------|----------------|
| `User`          | `id`, `name`, `email`, `phone`, `role`, `avatar_url`, `hashed_password`, `created_at` |
| `DoctorProfile` | `id`, `user_id`, `specialty_id`, `experience_years`, `clinic_name`, `fee`, `rating`, `verified` |
| `Specialty`     | `id`, `name`, `description` |
| `Appointment`   | `id`, `patient_id`, `doctor_id`, `scheduled_time`, `status`, `reason` |
| `Transaction`   | `id`, `appointment_id`, `amount`, `status`, `payment_method` |
| `Notification`  | `id`, `user_id`, `title`, `message`, `read`, `created_at` |

All models are implemented in `backend/app/models` using SQLAlchemy 2.0 style with full typing support.

## 5. API Surface (MVP)

| Method | Endpoint                              | Module  | Description |
|--------|---------------------------------------|---------|-------------|
| POST   | `/api/auth/register`                 | Auth    | Register patient/doctor users |
| POST   | `/api/auth/login`                    | Auth    | Issue JWT tokens |
| POST   | `/api/auth/verify`                   | Auth    | Validate token, return user |
| GET    | `/api/doctors`                       | Patient | Search doctors (filters via query params) |
| GET    | `/api/doctors/{id}`                  | Patient | Doctor detail |
| POST   | `/api/appointments`                  | Patient | Book appointment (patient only) |
| GET    | `/api/appointments`                  | Patient | List patient appointments |
| POST   | `/api/doctor/profile`                | Doctor  | Upsert doctor profile (self-service) |
| GET    | `/api/doctor/appointments`           | Doctor  | Doctor schedule overview |
| PUT    | `/api/doctor/availability`           | Doctor  | Update availability slots (in-memory stub) |
| GET    | `/api/admin/doctors/pending-verification` | Admin | Pending doctor approvals |
| PUT    | `/api/admin/doctors/{id}/verify`     | Admin   | Approve doctor |
| GET    | `/api/admin/analytics`               | Admin   | High-level metrics |

> **Note:** Availability persistence uses an in-memory dictionary placeholder (`app/services/availability.py`). Replace with DB storage or third-party scheduling integration in future phases.

## 6. Frontend Information Architecture

### App Router Segments
- `/patient` — patient dashboard, doctor list, appointments, profile
- `/doctor` — dashboard, appointment queue, availability, profile
- `/admin` — dashboard, doctor verification, users, reports

Each segment reuses `RoleLayout` for navigation. API calls are wrapped by `@/lib/api` leveraging Axios; failures fall back to mock data to keep UI functional during early integration.

### Component Highlights
- `RoleLayout` — standard sidebar + content layout
- `MetricCard` — data summary widget
- Global CSS utilities in `styles/globals.css` (custom utility classes instead of Tailwind)

## 7. Dev Experience & Configuration

- **Backend**: Poetry-managed (`backend/pyproject.toml`), `.env.example` provided. Run via `uvicorn app.main:app`.
- **Frontend**: npm project (`frontend/package.json`), `.env.example` for API base URL, Next.js dev server via `npm run dev`.
- **Docs**: This spec plus per-package README files outlining setup steps and roadmap.

## 8. Roadmap

1. **Phase 1 (MVP)**
   - Complete auth flows (email verification, OAuth)
   - Finish doctor onboarding & admin verification
   - Appointment booking + status updates
2. **Phase 2**
   - Notifications (email, push), redis-backed queues
   - Payments integration (Razorpay/Stripe) tied to `Transaction`
   - Enhanced doctor/patient dashboards
3. **Phase 3**
   - Teleconsultation module
   - AI symptom checker integrations
   - Advanced analytics + CMS publishing

## 9. Testing Strategy (Planned)

- Backend: pytest (unit + API), HTMX/integration tests with httpx, coverage via `coverage.py`
- Frontend: Playwright or Cypress for flows, React Testing Library for components
- CI: GitHub Actions pipeline to run linting, type checking, tests on each PR

## 10. Future Enhancements

- Replace availability stub with persisted schedules + ICS export
- Add reference tables (cities, hospitals, specialties) with seeding scripts
- Implement role-based access control middleware (admin vs doctor vs patient)
- Introduce audit logs for admin actions
- Build CMS module for health articles

---

This document mirrors the implemented scaffolding and acts as a contract for subsequent feature development. Update it alongside architecture decisions to keep AI assistants and contributors aligned.
