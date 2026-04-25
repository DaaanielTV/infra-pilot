#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "$0")/.." && pwd)"
JSON_OUTPUT=false
STRICT=false

while [ $# -gt 0 ]; do
  case "$1" in
    --json)
      JSON_OUTPUT=true
      shift
      ;;
    --strict)
      STRICT=true
      shift
      ;;
    *)
      echo "Unknown option: $1" >&2
      echo "Usage: $0 [--json] [--strict]" >&2
      exit 1
      ;;
  esac
done

check_file() {
  local file="$1"
  local label="$2"
  if [ -f "$file" ]; then
    echo "✓ $label"
    return 0
  fi
  echo "✗ $label (missing: $file)"
  return 1
}

OK=0
WARN=0

echo "Running workflow health checks..."

check_file "$ROOT_DIR/.env.example" ".env example present" && OK=$((OK + 1)) || WARN=$((WARN + 1))
check_file "$ROOT_DIR/docker-compose.yml" "docker compose config present" && OK=$((OK + 1)) || WARN=$((WARN + 1))
check_file "$ROOT_DIR/services/service-core/pom.xml" "service-core Maven manifest present" && OK=$((OK + 1)) || WARN=$((WARN + 1))
check_file "$ROOT_DIR/services/orchestrator-agent/requirements.txt" "orchestrator-agent Python manifest present" && OK=$((OK + 1)) || WARN=$((WARN + 1))
check_file "$ROOT_DIR/services/management-panel/package.json" "management-panel Node manifest present" && OK=$((OK + 1)) || WARN=$((WARN + 1))

if [ -f "$ROOT_DIR/services/discord-service/package.json" ]; then
  echo "✓ discord-service package manifest present"
  OK=$((OK + 1))
else
  echo "⚠ discord-service has no package.json (workflow scripts skip npm operations for this service)"
  WARN=$((WARN + 1))
fi

if [ "$JSON_OUTPUT" = true ]; then
  printf '{"script":"healthcheck","ok":%s,"warn":%s}\n' "$OK" "$WARN"
fi

echo "Health summary: ok=$OK warn=$WARN"
if [ "$STRICT" = true ] && [ "$WARN" -gt 0 ]; then
  exit 1
fi
exit 0
