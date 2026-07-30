.PHONY: setup dev dev-services dev-services-down test test-coverage lint format clean help healthcheck

# ── Development ──────────────────────────────────────────────────────

setup:           ## Set up the development environment
	@bash scripts/setup.sh

dev:             ## Start core services and run management panel
	@docker compose up -d postgres redis && \
		npm run dev --prefix services/management-panel

dev-services:    ## Start all Docker services
	@docker compose up -d

dev-services-down: ## Stop all Docker services
	@docker compose down

# ── Testing ──────────────────────────────────────────────────────────

test:            ## Run all tests
	@pytest tests/ -v

test-coverage:   ## Run tests with coverage report
	@pytest tests/ --cov=cli/ipilot --cov=services

# ── Linting & Formatting ─────────────────────────────────────────────

lint:            ## Run linting checks
	@npm run lint --prefix services/management-panel

format:          ## Format code with Prettier
	@prettier --write "services/**/*.{ts,tsx,js,jsx}"

# ── Maintenance ──────────────────────────────────────────────────────

clean:           ## Remove Docker volumes and node_modules
	@docker compose down -v && rm -rf node_modules

healthcheck:     ## Run project health checks
	bash ./scripts/healthcheck.sh

# ── Help ─────────────────────────────────────────────────────────────

help:            ## Show this help message
	@echo "Available commands:"
	@echo "  setup              Set up the development environment"
	@echo "  dev                Start core services and run management panel"
	@echo "  dev-services       Start all Docker services"
	@echo "  dev-services-down  Stop all Docker services"
	@echo "  test               Run all tests"
	@echo "  test-coverage      Run tests with coverage report"
	@echo "  lint               Run linting checks"
	@echo "  format             Format code with Prettier"
	@echo "  clean              Remove Docker volumes and node_modules"
	@echo "  healthcheck        Run project health checks"
	@echo "  help               Show this help message"
