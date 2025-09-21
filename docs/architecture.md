# Architecture Overview

Goals:
- Guide students end-to-end: stream → college → skills → jobs/startups
- Use real data and market insights for transparency and trust
- Bridge education–industry gap with live analytics and recommendations

## High-Level Modules
- Web App (Next.js)
  - Student onboarding, assessments, dashboards
  - Visualizations (D3/Recharts) for demand–supply, salary vs. business comparisons
- API Layer (Node.js)
  - REST endpoints for guidance flows and analytics
  - Adapters for external data providers (LinkedIn/Glassdoor, etc.)
- Data Layer
  - Aggregated datasets: streams, colleges, skills, jobs, startups
  - Storage: Firebase/Supabase (auth, DB), object storage for static datasets
- AI Services
  - Skill recommender and personalized roadmaps (Gemini/OpenAI)
  - Prompt templates and safety/grounding logic

## Data Sources (examples)
- Public datasets: education stats, college outcomes, salary reports
- Market signals: job postings, skills trends
- Startup data: incubators, grants, case studies

## Key Flows
1) Stream Guidance
   - Inputs: aptitude + interests → suggest Science/Commerce/Arts
   - Output: careers, salaries, job/business options
2) College Engine
   - Compare colleges on outcomes, research, entrepreneurship ecosystem
3) AI Skill Recommender
   - Recommend future-proof skills and learning roadmap
4) Entrepreneurship Pathways
   - Degree-linked startup opportunities, case studies

## Non-Functional
- Privacy & security for student data
- Observability (logs/metrics), rate limiting on external APIs
- Cost-conscious architecture; cache derived analytics

## Monorepo Structure
- apps/web (Next.js)
- apps/api (Node server)
- packages/ui (shared UI)
- packages/config (shared configs)
- data (datasets & schemas)
- docs (design, ADRs)
