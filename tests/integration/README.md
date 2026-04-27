Integration Test Scaffolding
==========================

- Purpose
  - Provide a growth path for end-to-end / integration tests as services come online.
- Structure
  - tests/integration/
    - __init__.py
    - test_placeholder.py
    - README.md
- How to run
  - Run: pytest -q
  - Pytest will discover tests in tests/integration because we placed tests with the pattern test_*.py and added an integration marker.
- How to expand
  - Add new test modules under this directory, e.g. test_<scenario>.py with @pytest.mark.integration.
  - Implement real service clients / fixtures as services come online.
