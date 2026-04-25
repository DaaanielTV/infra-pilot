# Workflow Optimization Audit (2026-04-25)

## Scope
This audit focuses on executable project workflows for:
- `scripts/setup.sh`
- `scripts/test.sh`
- `tools/run-all-tests.sh`
- `tools/lint-all.sh`

## Executed Work-Steps

1. **Baseline test workflow**
   - Ran `./scripts/test.sh`.
   - Observed immediate failure in `orchestrator-agent` because `pytest` returned exit code `5` when no tests were collected.

2. **Cross-service test workflow**
   - Ran `./tools/run-all-tests.sh` (permission denied due to missing executable bit).
   - Re-ran with `bash ./tools/run-all-tests.sh`.
   - Observed dependency install failures caused by restricted upstream package access (HTTP 403/proxy errors).

3. **Lint workflow**
   - Ran `bash ./tools/lint-all.sh`.
   - Verified script executes linting but currently fails on existing TypeScript/React lint errors in `management-panel`.

4. **Setup workflow**
   - Ran `bash ./scripts/setup.sh`.
   - Observed service setup continues on partial failures, but hides useful install error details and includes a stale path check variable.

## Implemented Optimizations

### 1) Test pipeline robustness
- `scripts/test.sh`
  - Added strict shell mode (`set -euo pipefail`).
  - Added explicit pass/skip/fail counters.
  - Treated `pytest` exit code `5` (no tests collected) as **skip**, not failure.
  - Added safe checks for missing test scripts and missing test directories.
  - Removed broad stderr suppression to keep actionable diagnostics visible.

### 2) Setup workflow reliability
- `scripts/setup.sh`
  - Added strict shell mode.
  - Removed invalid `SERVICES_PATH` gate and replaced it with direct tool checks.
  - Replaced fragile `cd` usage with `pushd/popd` for deterministic directory restoration.
  - Improved Node installation logic by using `npm ci` when lockfiles are present.
  - Preserved non-blocking behavior for optional service setup failures while retaining full error output.

### 3) Cross-service test orchestration
- `tools/run-all-tests.sh`
  - Added pass/skip/fail summary counters.
  - Added lockfile-aware Node dependency install strategy (`npm ci` vs `npm install`).
  - Added Python test-directory checks to avoid unnecessary environment bootstrap when no tests exist.
  - Handled `pytest` no-test condition as skipped.
  - Added per-test-venv isolation (`.venv`) and clearer final status output.

### 4) Lint orchestration flexibility
- `tools/lint-all.sh`
  - Added skip/fail summary.
  - Uses service lint scripts when available; otherwise falls back to `npx eslint`.
  - Supports both JavaScript and TypeScript React extension sets (`.js,.ts,.tsx`).
  - Keeps services with missing npm/tooling from blocking unrelated lint runs.

## High-Value Edge Cases To Keep Monitoring

1. **No-test services**
   - Many services may intentionally ship without tests during early stages. Mark as skipped, not failed.

2. **Offline / restricted network CI runners**
   - Package managers can fail with proxy/403 responses. Consider:
     - artifact caching
     - internal registries
     - retry + backoff with explicit timeout

3. **Script execution permissions**
   - Some helper scripts may not have executable mode set. Prefer documented invocation via `bash <script>` or normalize permissions in repo.

4. **Monorepo dependency drift**
   - Mixed ecosystems (Maven, pip, npm) can fail independently. Keep workflows tolerant and report per-service outcomes.

5. **Hidden diagnostics**
   - Suppressing stderr (`2>/dev/null`) can hide root cause. Keep user-friendly summaries, but preserve raw failure output.

## Implemented Follow-Up Optimizations (2026-04-25)

- Added a unified workflow entrypoint:
  - `scripts/verify.sh` with selectable stages (`health,setup,test,lint,integration`)
  - root `Makefile` targets: `verify`, `verify-offline`, `verify-json`
- Added offline-safe execution mode:
  - `scripts/setup.sh --offline`
  - `scripts/test.sh --offline`
  - `tools/lint-all.sh --offline`
  - `tools/run-all-tests.sh --offline`
- Added machine-readable summary mode:
  - `scripts/test.sh --json`
  - `tools/lint-all.sh --json`
  - `tools/run-all-tests.sh --json`
  - `scripts/verify.sh --json`
- Added workflow health probes:
  - `scripts/healthcheck.sh` validates key manifests/config files before heavier stages.
