# Testing Guide

- Node services: tests are discovered via the package.json's test script. If absent, tests are skipped by the runner.
- Python services: tests discovered by pytest under tests/ directories inside the service; if none, runner skips.
- Integration tests: a lightweight harness collects tests under tests/integration and runs them with pytest.
- To run locally:
  - Node: go to a service directory with a package.json that has a test script and run npm test
  - Python: ensure requirements.txt exists and tests are described in pytest format, then run the runner
  - CI: see .github/workflows/ci.yml for full pipeline
