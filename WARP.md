# WARP.md

This file provides guidance to WARP (warp.dev) when working with code in this repository.

Repository overview
- Monorepo managed with npm workspaces (root package.json workspaces: apps/*, packages/*). Node.js >= 18.17 required (see engines in package.json).
- Implemented today:
  - apps/api: minimal Node HTTP server (no external deps). Entrypoint: apps/api/src/index.js. Endpoints: GET / (basic info), GET /health (status).
  - data/: documentation for datasets structure and handling (see data/README.md).
- Planned (placeholders in README): apps/web (Next.js), packages/ui, packages/config, docs/.

Common commands
- Install (root):
  - npm install
- Develop API (from repo root):
  - npm run dev:api
  - Or targeted workspace: npm -w @apps/api run dev
  - Change port (PowerShell): $env:PORT=4001; npm run dev:api
- Start API (same as dev for now):
  - npm -w @apps/api run start
- Build (root):
  - npm run build
  - Note: currently a placeholder script in the root package.json
- Lint (root):
  - npm run lint
  - Auto-fix: npm run lint:fix
- Tests (root):
  - All tests: npm run test
  - Watch mode: npm run test:watch
  - Single test file: npm run test -- apps/api/test/api.spec.js

API details (apps/api)
- Entrypoint: apps/api/src/index.js
- Default port: 4000 (overridable with PORT)
- Available endpoints:
  - GET / → { name: 'AI Career GPS API', status: 'ok' }
  - GET /health → { ok: true }

Important notes from README
- Quick start: Node.js 18+ and Git installed. From root, run npm run dev:api to start the API.
- When ready to scaffold the Next.js web app (non-interactive example):
  - npx create-next-app@latest apps/web --ts --eslint --use-npm --no-tailwind --src-dir --app --import-alias "@/*" --yes

Streamlit app
- Local run (Windows PowerShell):
  - python -m venv .venv; .\.venv\Scripts\Activate.ps1; pip install -r requirements.txt; streamlit run streamlit_app.py
- Streamlit Cloud deploy:
  - App entrypoint: streamlit_app.py (at repo root)
  - Optional secret: API_URL (if calling an external API for /health)
  - Secrets template: .streamlit/secrets.template.toml (copy values into Streamlit Cloud > App > Settings > Secrets)

Workspace layout and conventions
- Root package.json defines npm workspaces for apps/* and packages/*.
- apps/api has its own package.json with scripts: dev and start, both invoking node src/index.js.
- No ESLint/Prettier/Jest/Vitest configs are present. Lint/test scripts at the root are placeholders and can be wired up when those tools are introduced.

CI/CD and tooling
- No CI workflows or third-party agent rules files detected (no CLAUDE.md, .cursor/rules, .cursorrules, or .github/copilot-instructions.md in this repository).
