#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "$0")/.." && pwd)"
echo "Running tests across all services in $ROOT_DIR..."

for svc in "$ROOT_DIR"/services/*; do
  if [ -d "$svc" ]; then
    name=$(basename "$svc")
    echo "==> Service: $name"
    if [ -f "$svc/package.json" ]; then
      echo "--> Node: $name"
      if grep -q '"test":' "$svc/package.json"; then
        (cd "$svc" && npm ci --silent && npm test) || exit 1
      else
        echo "---- Skipping Node tests for $name (no test script found)"
      fi
    fi
    if [ -f "$svc/requirements.txt" ]; then
      echo "--> Python: $name"
      python3 -V >/dev/null 2>&1 || { echo "Python3 not found"; exit 1; }
      (cd "$svc" && python3 -m venv venv && source venv/bin/activate && pip install -r requirements.txt && pytest -q) || exit 1
      deactivate || true
    fi
  fi
done

if [ -d "$ROOT_DIR/tests/integration" ]; then
  echo "==> Integration tests: integration"
  integ_dir="$ROOT_DIR/tests/integration"
  if [ -f "$integ_dir/requirements.txt" ]; then
    python3 -m venv venv && source venv/bin/activate && pip install -r "$integ_dir/requirements.txt"
  fi
  pytest -q "$integ_dir" || exit 1
  deactivate || true
fi

echo "All service tests completed successfully."
