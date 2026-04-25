#!/bin/bash
#
# Infra Pilot - Test Runner Script
#
# This script runs tests for all services.
# Supports: Python (pytest), JavaScript (npm test), Java (Maven test)

set -euo pipefail

echo "🧪 Infra Pilot Test Suite"
echo "=========================="

# Color codes
GREEN='\033[0;32m'
BLUE='\033[0;34m'
YELLOW='\033[1;33m'
RED='\033[0;31m'
NC='\033[0m' # No Color

# Configuration
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

# Helper functions
log_section() {
    echo ""
    echo -e "${BLUE}─────────────────────────────────────${NC}"
    echo -e "${BLUE}$1${NC}"
    echo -e "${BLUE}─────────────────────────────────────${NC}"
}

log_info() {
    echo -e "${BLUE}ℹ️  $1${NC}"
}

log_success() {
    echo -e "${GREEN}✓ $1${NC}"
}

log_warning() {
    echo -e "${YELLOW}⚠️  $1${NC}"
}

log_error() {
    echo -e "${RED}✗ $1${NC}"
}

run_pytest_suite() {
    local test_target="$1"
    local service_name="$2"

    set +e
    pytest "$test_target" -v --tb=short
    local rc=$?
    set -e

    if [ "$rc" -eq 0 ]; then
        log_success "Tests passed for $service_name"
        PASSED_TESTS=$((PASSED_TESTS + 1))
    elif [ "$rc" -eq 5 ]; then
        log_warning "No tests collected for $service_name"
        SKIPPED_TESTS=$((SKIPPED_TESTS + 1))
    else
        log_error "Tests failed for $service_name"
        FAILED_TESTS=$((FAILED_TESTS + 1))
    fi
}

# Parse arguments
for arg in "$@"; do
    case $arg in
        --coverage)
            SHOW_COVERAGE=true
            ;;
        --offline)
            OFFLINE=true
            ;;
        --json)
            JSON_OUTPUT=true
            ;;
        *)
            echo "Unknown option: $arg"
            echo "Usage: $0 [--coverage] [--offline] [--json]"
            exit 1
            ;;
    esac
done

if [ "$OFFLINE" = true ]; then
    log_info "Offline mode enabled: Java Maven tests will be skipped"
fi

# Run tests for each service
for service in "${TEST_SERVICES[@]}"; do
    if [ ! -d "$service" ]; then
        log_warning "Service not found: $service"
        SKIPPED_TESTS=$((SKIPPED_TESTS + 1))
        continue
    fi

    SERVICE_NAME=$(basename "$service")
    log_section "Testing $SERVICE_NAME"

    pushd "$service" > /dev/null

    # Determine test command based on service type
    if [[ "$SERVICE_NAME" == "orchestrator-agent" ]]; then
        if command -v python3 &> /dev/null; then
            if [ -f "venv/bin/activate" ]; then
                # shellcheck disable=SC1091
                source venv/bin/activate
            fi

            if command -v pytest &> /dev/null; then
                log_info "Running pytest..."
                if [ -d "tests" ]; then
                    run_pytest_suite "tests/" "$SERVICE_NAME"
                else
                    log_warning "No tests directory found for $SERVICE_NAME"
                    SKIPPED_TESTS=$((SKIPPED_TESTS + 1))
                fi
            else
                log_warning "pytest not installed, skipping tests"
                SKIPPED_TESTS=$((SKIPPED_TESTS + 1))
            fi

            if [ -f "venv/bin/activate" ]; then
                deactivate 2>/dev/null || true
            fi
        else
            log_warning "Python not available, skipping tests"
            SKIPPED_TESTS=$((SKIPPED_TESTS + 1))
        fi

    elif [[ "$SERVICE_NAME" == "discord-service" ]] || [[ "$SERVICE_NAME" == "management-panel" ]]; then
        if [ -f "package.json" ]; then
            if command -v npm &> /dev/null; then
                if node -e "const p=require('./package.json'); process.exit(p.scripts && p.scripts.test ? 0 : 1)"; then
                    log_info "Running npm test..."
                    set +e
                    if [ "$SHOW_COVERAGE" = true ]; then
                        npm run test -- --coverage
                    else
                        npm run test
                    fi
                    rc=$?
                    set -e

                    if [ "$rc" -eq 0 ]; then
                        log_success "Tests passed for $SERVICE_NAME"
                        PASSED_TESTS=$((PASSED_TESTS + 1))
                    else
                        log_error "Tests failed for $SERVICE_NAME"
                        FAILED_TESTS=$((FAILED_TESTS + 1))
                    fi
                else
                    log_warning "No test script defined in package.json"
                    SKIPPED_TESTS=$((SKIPPED_TESTS + 1))
                fi
            else
                log_warning "npm not available, skipping tests"
                SKIPPED_TESTS=$((SKIPPED_TESTS + 1))
            fi
        else
            log_warning "No package.json found"
            SKIPPED_TESTS=$((SKIPPED_TESTS + 1))
        fi

    elif [[ "$SERVICE_NAME" == "service-core" ]]; then
        if [ "$OFFLINE" = true ]; then
            log_warning "Offline mode: skipping Maven tests"
            SKIPPED_TESTS=$((SKIPPED_TESTS + 1))
        elif [ -f "pom.xml" ]; then
            if command -v mvn &> /dev/null; then
                log_info "Running Maven tests..."
                set +e
                if [ "$SHOW_COVERAGE" = true ]; then
                    mvn test jacoco:report -q
                else
                    mvn test -q
                fi
                rc=$?
                set -e

                if [ "$rc" -eq 0 ]; then
                    log_success "Tests passed for $SERVICE_NAME"
                    PASSED_TESTS=$((PASSED_TESTS + 1))
                else
                    log_error "Tests failed for $SERVICE_NAME"
                    FAILED_TESTS=$((FAILED_TESTS + 1))
                fi
            else
                log_warning "Maven not available, skipping tests"
                SKIPPED_TESTS=$((SKIPPED_TESTS + 1))
            fi
        else
            log_warning "No pom.xml found"
            SKIPPED_TESTS=$((SKIPPED_TESTS + 1))
        fi
    fi

    popd > /dev/null
done

# Summary
echo ""
log_section "Test Summary"
log_info "Passed: $PASSED_TESTS"
log_info "Skipped: $SKIPPED_TESTS"
log_info "Failed: $FAILED_TESTS"

if [ "$JSON_OUTPUT" = true ]; then
    printf '{"script":"test","passed":%s,"skipped":%s,"failed":%s,"offline":%s}\n' \
      "$PASSED_TESTS" "$SKIPPED_TESTS" "$FAILED_TESTS" "$OFFLINE"
fi

if [ "$FAILED_TESTS" -eq 0 ]; then
    log_success "No failing test suites detected"
    exit 0
else
    log_error "$FAILED_TESTS test suite(s) failed"
    exit 1
fi
