#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "$0")/.." && pwd)"
OFFLINE=false
JSON_OUTPUT=false

while [ $# -gt 0 ]; do
  case "$1" in
    --offline)
      OFFLINE=true
      shift
      ;;
    --json)
      JSON_OUTPUT=true
      shift
      ;;
    *)
      echo "Unknown option: $1" >&2
      echo "Usage: $0 [--offline] [--json]" >&2
      exit 1
      ;;
  esac
done

echo "Running lint across JavaScript/TypeScript sources..."
if [ "$OFFLINE" = true ]; then
  echo "Offline mode enabled: dependency installation steps will be skipped."
fi

FAILED=0
SKIPPED=0

for svc in "$ROOT_DIR"/services/*; do
  if [ -d "$svc" ] && [ -f "$svc/package.json" ]; then
    name=$(basename "$svc")
    echo "--> Lint: $name"

    if ! command -v npm >/dev/null 2>&1; then
      echo "---- Skipping $name (npm not installed)"
      SKIPPED=$((SKIPPED + 1))
      continue
    fi

    if [ "$OFFLINE" = false ]; then
      if [ -f "$svc/package-lock.json" ]; then
        (cd "$svc" && npm ci --silent >/dev/null 2>&1 || true)
      else
        (cd "$svc" && npm install --silent >/dev/null 2>&1 || true)
      fi
    elif [ ! -d "$svc/node_modules" ]; then
      echo "---- Skipping $name (offline and no node_modules)"
      SKIPPED=$((SKIPPED + 1))
      continue
    fi

    if (cd "$svc" && node -e "const p=require('./package.json'); process.exit(p.scripts && p.scripts.lint ? 0 : 1)"); then
      (cd "$svc" && npm run lint) || FAILED=$((FAILED + 1))
    else
      (cd "$svc" && npx eslint . --ext .js,.ts,.tsx) || FAILED=$((FAILED + 1))
    fi
  fi
done

if [ "$JSON_OUTPUT" = true ]; then
  printf '{"script":"lint-all","skipped":%s,"failed":%s,"offline":%s}\n' \
    "$SKIPPED" "$FAILED" "$OFFLINE"
else
  echo "Lint summary: skipped=$SKIPPED failed=$FAILED"
fi

if [ "$FAILED" -gt 0 ]; then
  exit 1
fi

echo "Linting completed."
