# src/pages — Demo & Reference Library

The page components in this directory are **not wired into the app**.
`App.tsx` routes only to the pages listed there (dashboard, monitoring,
apps, backups, logs, reports, audit, activity, knowledge-base, settings,
customers). Everything else in this folder is a demo/reference build:

- **Purpose:** design references and feature blueprints built on the
  panel's design system (cards, tables, dialogs, forms).
- **Data:** they render with mock/inline data and do **not** call the
  backend API.
- **Cost:** they compile with every `tsc`/lint run, so keep them
  compiling, but do not extend them.

## Promoting a page into the app

1. Replace the mock data with calls to the real API (`src/lib/api`).
2. Add a route in `src/App.tsx` and a nav entry in the layout.
3. Add the page to `tests/playwright` or unit tests.

Do not edit demo pages in place — copy the parts you need into a new
page component under a feature-specific directory.
