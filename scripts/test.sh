#!/bin/bash
#
# Infra Pilot - Test Runner Script
#
# This script runs tests for all services.
# Supports: Python (pytest), JavaScript (npm test), Java (Maven test)

set -e

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
FAILED_TESTS=0

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

# Parse arguments
for arg in "$@"; do
    case $arg in
        --coverage)
            SHOW_COVERAGE=true
            ;;
        *)
            echo "Unknown option: $arg"
            echo "Usage: $0 [--coverage]"
            exit 1
            ;;
    esac
done

# Run tests for each service
for service in "${TEST_SERVICES[@]}"; do
    if [ ! -d "$service" ]; then
        log_warning "Service not found: $service"
        continue
    fi

    SERVICE_NAME=$(basename "$service")
    log_section "Testing $SERVICE_NAME"

    cd "$service"

    # Determine test command based on service type
    if [[ "$SERVICE_NAME" == "orchestrator-agent" ]]; then
        # Python/pytest
        if [ -f "requirements.txt" ] || [ -f "tests/" ]; then
            if command -v python3 &> /dev/null; then
                log_info "Running pytest..."
                if [ -f "venv/bin/activate" ]; then
                    # shellcheck disable=SC1091
                    source venv/bin/activate
                fi
                
                if command -v pytest &> /dev/null; then
                    pytest tests/ -v --tb=short 2>/dev/null || {
                        log_error "Tests failed for $SERVICE_NAME"
                        ((FAILED_TESTS++))
                    }
                else
                    log_warning "pytest not installed, skipping tests"
                fi
                
                if [ -f "venv/bin/activate" ]; then
                    deactivate 2>/dev/null || true
                fi
            else
                log_warning "Python not available, skipping tests"
            fi
        else
            log_warning "No tests found for $SERVICE_NAME"
        fi

    elif [[ "$SERVICE_NAME" == "discord-service" ]] || [[ "$SERVICE_NAME" == "management-panel" ]]; then
        # JavaScript/npm test
        if [ -f "package.json" ]; then
            if command -v npm &> /dev/null; then
                log_info "Running npm test..."
                if [ "$SHOW_COVERAGE" = true ]; then
                    npm run test -- --coverage 2>/dev/null || {
                        log_error "Tests failed for $SERVICE_NAME"
                        ((FAILED_TESTS++))
                    }
                else
                    npm run test 2>/dev/null || {
                        log_error "Tests failed for $SERVICE_NAME"
                        ((FAILED_TESTS++))
                    }
                fi
            else
                log_warning "npm not available, skipping tests"
            fi
        else
            log_warning "No package.json found"
        fi

    elif [[ "$SERVICE_NAME" == "service-core" ]]; then
        # Java/Maven test
        if [ -f "pom.xml" ]; then
            if command -v mvn &> /dev/null; then
                log_info "Running Maven tests..."
                if [ "$SHOW_COVERAGE" = true ]; then
                    mvn test jacoco:report -q 2>/dev/null || {
                        log_error "Tests failed for $SERVICE_NAME"
                        ((FAILED_TESTS++))
                    }
                else
                    mvn test -q 2>/dev/null || {
                        log_error "Tests failed for $SERVICE_NAME"
                        ((FAILED_TESTS++))
                    }
                fi
            else
                log_warning "Maven not available, skipping tests"
            fi
        else
            log_warning "No pom.xml found"
        fi
    fi

    cd - > /dev/null
done

# Summary
echo ""
log_section "Test Summary"

if [ $FAILED_TESTS -eq 0 ]; then
    log_success "All tests passed!"
    exit 0
else
    log_error "$FAILED_TESTS test suite(s) failed"
    exit 1
fi
