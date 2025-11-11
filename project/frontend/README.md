# Healthcare Platform Frontend

Next.js 14 + TypeScript frontend for the Practo-style healthcare experience. It includes role-specific workspaces for patients, doctors, and administrators, backed by reusable layout components and API integration stubs.

## Getting Started

### 1. Prerequisites

- Node.js 18+
- npm (bundled with Node) or yarn / pnpm

### 2. Install Dependencies

```bash
npm install
```

### 3. Environment Variables

Copy the example file and adjust values when the backend is available.

```bash
cp .env.example .env.local
```

`NEXT_PUBLIC_API_BASE_URL` should point to the FastAPI backend (defaults to `http://localhost:8000/api`).

### 4. Run Development Server

```bash
npm run dev
```

Visit `http://localhost:3000` to view the app.

## Structure

```
frontend/
  ├── app/                # App Router structure with role-based segments
  ├── components/         # Presentational components and layouts
  ├── lib/                # API helpers
  ├── styles/             # Global styles (utility classes)
  └── types/              # Shared TypeScript types
```

## Roadmap

- ✅ Role-based navigation scaffolding
- ✅ API client stubs for key endpoints
- ⬜ Auth flow (login/register) with persistent sessions
- ⬜ Forms for booking, verification, and availability management
- ⬜ Mobile-responsive layout refinements
