#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "$0")/.." && pwd)"
OFFLINE=false
JSON_OUTPUT=false
STAGES="health,setup,test,lint,integration"

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
    --stages)
      STAGES="$2"
      shift 2
      ;;
    *)
      echo "Unknown option: $1" >&2
      echo "Usage: $0 [--offline] [--json] [--stages health,setup,test,lint,integration]" >&2
      exit 1
      ;;
  esac
done

IFS=',' read -r -a stage_list <<< "$STAGES"

run_stage() {
  local name="$1"
  shift

  echo "==> Stage: $name"
  if "$@"; then
    echo "✓ Stage succeeded: $name"
    return 0
  fi

  echo "✗ Stage failed: $name"
  return 1
}

FAILED=0
STAGE_JSON=""

for stage in "${stage_list[@]}"; do
  case "$stage" in
    health)
      cmd=("bash" "$ROOT_DIR/scripts/healthcheck.sh")
      ;;
    setup)
      cmd=("bash" "$ROOT_DIR/scripts/setup.sh")
      [ "$OFFLINE" = true ] && cmd+=("--offline")
      ;;
    test)
      cmd=("bash" "$ROOT_DIR/scripts/test.sh")
      [ "$OFFLINE" = true ] && cmd+=("--offline")
      ;;
    lint)
      cmd=("bash" "$ROOT_DIR/tools/lint-all.sh")
      [ "$OFFLINE" = true ] && cmd+=("--offline")
      ;;
    integration)
      cmd=("bash" "$ROOT_DIR/tools/run-all-tests.sh")
      [ "$OFFLINE" = true ] && cmd+=("--offline")
      ;;
    "")
      continue
      ;;
    *)
      echo "Unknown stage '$stage'" >&2
      FAILED=$((FAILED + 1))
      continue
      ;;
  esac

  if run_stage "$stage" "${cmd[@]}"; then
    status="passed"
  else
    status="failed"
    FAILED=$((FAILED + 1))
  fi

  if [ "$JSON_OUTPUT" = true ]; then
    if [ -n "$STAGE_JSON" ]; then
      STAGE_JSON+=" ,"
    fi
    STAGE_JSON+="{\"stage\":\"$stage\",\"status\":\"$status\"}"
  fi
done

if [ "$JSON_OUTPUT" = true ]; then
  printf '{"script":"verify","offline":%s,"failed":%s,"stages":[%s]}\n' "$OFFLINE" "$FAILED" "$STAGE_JSON"
fi

[ "$FAILED" -eq 0 ]
