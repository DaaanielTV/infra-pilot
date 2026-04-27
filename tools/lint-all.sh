#!/usr/bin/env bash
set -euo pipefail

# Lint all Node.js services in the repo by delegating to each service's lint script
# or running ESLint directly if no script is defined.

ROOT_DIR=$(cd "$(dirname "$0")/.." && pwd)

echo "[lint-all] Linting all services in: $ROOT_DIR"

CONTENTS=$(ls -1 "$ROOT_DIR"/*/package.json 2>/dev/null || true)
if [ -z "$CONTENTS" ]; then
  echo "[lint-all] No Node services with package.json found at top level."; exit 0
fi

EXIT_CODE=0

for pkg in $CONTENTS; do
  service_dir=$(dirname "$pkg")
  echo "[lint-all] Linting service: $service_dir"
  pushd "$service_dir" >/dev/null
  if npm run | grep -q 'lint'; then
    echo "[lint-all] Running: npm run lint";
    npm ci --silent || true
    npm run lint || EXIT_CODE=$?
  else
    if command -v npx >/dev/null 2>&1; then
      echo "[lint-all] Running: npx eslint .";
      npx eslint . || EXIT_CODE=$?
    else
      echo "[lint-all] No lint script or ESLint available in $service_dir; skipping.";
    fi
  fi
  popd >/dev/null
done

exit $EXIT_CODE
