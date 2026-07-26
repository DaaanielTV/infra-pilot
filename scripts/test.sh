#!/usr/bin/env bash
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
ROOT_DIR="$(cd "$SCRIPT_DIR/.." && pwd)"

GREEN='\033[0;32m'
BLUE='\033[0;34m'
YELLOW='\033[1;33m'
RED='\033[0;31m'
NC='\033[0m'

info()     { echo -e "${BLUE}${1}${NC}"; }
success()  { echo -e "${GREEN}${1}${NC}"; }
warn()     { echo -e "${YELLOW}${1}${NC}"; }
error()    { echo -e "${RED}${1}${NC}" >&2; }
section()  { echo ""; echo -e "${BLUE}─────────────────────────────────────${NC}"; echo -e "${BLUE}${1}${NC}"; echo -e "${BLUE}─────────────────────────────────────${NC}"; }

usage() {
  cat <<EOF
Run tests for all Infra Pilot services.

Usage: $(basename "$0") [OPTIONS]

Options:
  --coverage  Include coverage reports
  --offline   Skip Maven tests (offline mode)
  --json      Output results as JSON
  --help      Show this help message
EOF
  exit 0
}

TEST_SERVICES=(
  "services/orchestrator-agent"
  "services/discord-service"
  "services/management-panel"
  "services/service-core"
)

SHOW_COVERAGE=false
OFFLINE=false
JSON_OUTPUT=false
FAILED_TESTS=0
SKIPPED_TESTS=0
PASSED_TESTS=0

while [[ $# -gt 0 ]]; do
  case "$1" in
    --coverage) SHOW_COVERAGE=true; shift ;;
    --offline) OFFLINE=true; shift ;;
    --json) JSON_OUTPUT=true; shift ;;
    --help) usage ;;
    *) echo "Unknown option: $1" >&2; usage ;;
  esac
done

cd "$ROOT_DIR"

run_pytest_suite() {
  local test_target="$1"
  local service_name="$2"

  set +e
  pytest "$test_target" -v --tb=short
  local rc=$?
  set -e

  if [ "$rc" -eq 0 ]; then
    success "Tests passed for $service_name"
    PASSED_TESTS=$((PASSED_TESTS + 1))
  elif [ "$rc" -eq 5 ]; then
    warn "No tests collected for $service_name"
    SKIPPED_TESTS=$((SKIPPED_TESTS + 1))
  else
    error "Tests failed for $service_name"
    FAILED_TESTS=$((FAILED_TESTS + 1))
  fi
}

if [ "$OFFLINE" = true ]; then
  info "Offline mode enabled: Java Maven tests will be skipped"
fi

for service in "${TEST_SERVICES[@]}"; do
  if [ ! -d "$service" ]; then
    warn "Service not found: $service"
    SKIPPED_TESTS=$((SKIPPED_TESTS + 1))
    continue
  fi

  SERVICE_NAME=$(basename "$service")
  section "Testing $SERVICE_NAME"

  pushd "$service" > /dev/null

  if [[ "$SERVICE_NAME" == "orchestrator-agent" ]]; then
    if command -v python3 &> /dev/null; then
      if [ -f "venv/bin/activate" ]; then
        # shellcheck disable=SC1091
        source venv/bin/activate
      fi

      if command -v pytest &> /dev/null; then
        if [ -d "tests" ]; then
          run_pytest_suite "tests/" "$SERVICE_NAME"
        else
          warn "No tests directory found for $SERVICE_NAME"
          SKIPPED_TESTS=$((SKIPPED_TESTS + 1))
        fi
      else
        warn "pytest not installed, skipping tests"
        SKIPPED_TESTS=$((SKIPPED_TESTS + 1))
      fi

      if [ -f "venv/bin/activate" ]; then
        deactivate 2>/dev/null || true
      fi
    else
      warn "Python not available, skipping tests"
      SKIPPED_TESTS=$((SKIPPED_TESTS + 1))
    fi

  elif [[ "$SERVICE_NAME" == "discord-service" ]] || [[ "$SERVICE_NAME" == "management-panel" ]]; then
    if [ -f "package.json" ]; then
      if command -v npm &> /dev/null; then
        if node -e "const p=require('./package.json'); process.exit(p.scripts && p.scripts.test ? 0 : 1)" 2>/dev/null; then
          info "Running npm test..."
          set +e
          if [ "$SHOW_COVERAGE" = true ]; then
            npm run test -- --coverage
          else
            npm run test
          fi
          rc=$?
          set -e

          if [ "$rc" -eq 0 ]; then
            success "Tests passed for $SERVICE_NAME"
            PASSED_TESTS=$((PASSED_TESTS + 1))
          else
            error "Tests failed for $SERVICE_NAME"
            FAILED_TESTS=$((FAILED_TESTS + 1))
          fi
        else
          warn "No test script defined in package.json"
          SKIPPED_TESTS=$((SKIPPED_TESTS + 1))
        fi
      else
        warn "npm not available, skipping tests"
        SKIPPED_TESTS=$((SKIPPED_TESTS + 1))
      fi
    else
      warn "No package.json found"
      SKIPPED_TESTS=$((SKIPPED_TESTS + 1))
    fi

  elif [[ "$SERVICE_NAME" == "service-core" ]]; then
    if [ "$OFFLINE" = true ]; then
      warn "Offline mode: skipping Maven tests"
      SKIPPED_TESTS=$((SKIPPED_TESTS + 1))
    elif [ -f "pom.xml" ]; then
      if command -v mvn &> /dev/null; then
        info "Running Maven tests..."
        set +e
        if [ "$SHOW_COVERAGE" = true ]; then
          mvn test jacoco:report -q
        else
          mvn test -q
        fi
        rc=$?
        set -e

        if [ "$rc" -eq 0 ]; then
          success "Tests passed for $SERVICE_NAME"
          PASSED_TESTS=$((PASSED_TESTS + 1))
        else
          error "Tests failed for $SERVICE_NAME"
          FAILED_TESTS=$((FAILED_TESTS + 1))
        fi
      else
        warn "Maven not available, skipping tests"
        SKIPPED_TESTS=$((SKIPPED_TESTS + 1))
      fi
    else
      warn "No pom.xml found"
      SKIPPED_TESTS=$((SKIPPED_TESTS + 1))
    fi
  fi

  popd > /dev/null
done

section "Test Summary"
info "Passed: $PASSED_TESTS"
info "Skipped: $SKIPPED_TESTS"
info "Failed: $FAILED_TESTS"

if [ "$JSON_OUTPUT" = true ]; then
  printf '{"script":"test","passed":%s,"skipped":%s,"failed":%s,"offline":%s}\n' \
    "$PASSED_TESTS" "$SKIPPED_TESTS" "$FAILED_TESTS" "$OFFLINE"
fi

if [ "$FAILED_TESTS" -eq 0 ]; then
  success "No failing test suites detected"
  exit 0
else
  error "$FAILED_TESTS test suite(s) failed"
  exit 1
fi
