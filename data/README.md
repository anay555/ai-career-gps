# Data Directory

Purpose:
- Hold datasets, schemas, seed scripts, and data dictionaries that power guidance, college comparisons, skills trends, and entrepreneurship insights.

Suggested structure:
- schemas/ → JSON/YAML schemas for entities (streams, colleges, skills, jobs, startups)
- sources/ → Raw/public datasets with source notes and dates
- processed/ → Cleaned and joined datasets used by the app
- seeds/ → Seed scripts for databases (Supabase/Firebase)

Notes:
- Keep PII out of version control. Use environment-specific storage for sensitive data.
- Document the source and freshness of each dataset in sources/README.md.
