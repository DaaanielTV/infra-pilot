import sys
import inspect
import asyncio
from pathlib import Path

_project_root = str(Path(__file__).resolve().parent.parent)
if _project_root not in sys.path:
    sys.path.insert(0, _project_root)

_cli_root = str(Path(__file__).resolve().parent.parent / "cli")
if _cli_root not in sys.path:
    sys.path.insert(0, _cli_root)

if "cli" in sys.modules:
    del sys.modules["cli"]


def pytest_pyfunc_call(pyfuncitem):
    """Run async test functions without requiring pytest-asyncio.

    Several generated test modules define ``async def`` tests.  Keeping this
    tiny hook in the shared conftest makes those tests executable in minimal
    environments where the optional pytest-asyncio plugin is not installed.
    """
    testfunction = pyfuncitem.obj
    if not inspect.iscoroutinefunction(testfunction):
        return None

    funcargs = {
        name: pyfuncitem.funcargs[name]
        for name in pyfuncitem._fixtureinfo.argnames
    }
    asyncio.run(testfunction(**funcargs))
    return True
