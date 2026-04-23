#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "$0")/.." && pwd)"
echo "Running lint across JavaScript/TypeScript sources..."

for svc in "$ROOT_DIR"/services/*; do
  if [ -d "$svc" ]; then
    if [ -f "$svc/package.json" ]; then
      echo "--> Lint: $(basename "$svc")"
      (cd "$svc" && npm ci --silent >/dev/null 2>&1 || true)
      (cd "$svc" && npx eslint . --ext .js,.ts) || exit 1
    fi
  fi
done

echo "Linting completed."
