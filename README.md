# AI Career GPS: From Stream to Startup

Tagline: “Data-Driven Career GPS: From Stream to Startup”

## Problem
Students struggle with stream, college, and career choices due to vague guidance, outdated data, and lack of entrepreneurship insights.

## Solution
An AI-powered career pathway platform guiding students from stream selection → college choice → skills → jobs/startups, using real data & market insights.

## Key Features
- Stream Guidance (Class 10): Aptitude + interest → Science/Commerce/Arts with salary, jobs, business options.
- Education vs Industry Gap: Live analytics on graduate supply vs job demand.
- College Engine: Compare real packages, research, entrepreneurship ecosystem.
- AI Skill Recommender: Future-proof skills + personalized roadmaps.
- Degree + Entrepreneurship Path: Degrees linked to startup opportunities + case studies.

## Impact
Data-driven career choices, reduced industry mismatch, transparent roadmap trusted by parents, and promotion of entrepreneurship.

## Unique Edge
Salary vs business comparisons, real-time demand-supply gap, beyond-rankings college data, AI skill mapping, startup pathways.

## Tech Stack
- Frontend: React/Next.js, D3.js/Recharts
- Backend: Node.js (Express or serverless), Firebase/Supabase
- AI: Gemini/OpenAI
- Integrations: LinkedIn/Glassdoor APIs

## Monorepo Layout (initial)
- apps/web → Next.js app (to be scaffolded)
- apps/api → Node server (starter included)
- packages/ui → Shared UI components (placeholder)
- packages/config → Shared configs (placeholder)
- data → Datasets, schemas, seeders (placeholder)
- docs → Architecture, ADRs

## Quick Start
1) Ensure Node.js 18+ and Git are installed
2) From repo root:
   - API dev: `npm run dev:api`
   - Web app: scaffold with Next.js when ready (see below)

## Scaffolding the Web App (later)
When ready to create the Next.js app (non-interactive example):
```
npx create-next-app@latest apps/web --ts --eslint --use-npm --no-tailwind --src-dir --app --import-alias "@/*" --yes
```

## Roadmap (high level)
- v0: Data model, API endpoints for guidance, initial analytics stubs
- v1: Next.js UI with stream guidance flow and dashboards
- v2: Integrations (job market data), AI skill recommender
- v3: College engine, entrepreneurship pathways, advanced visualizations

## License
MIT (see LICENSE)
