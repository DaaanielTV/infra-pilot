"""Background manifest watcher — polls Git repos for changes.

When the ``infra.yaml`` file in a tracked repository changes, the
watcher triggers a reconciliation run.  This makes Git the single
source of truth for infrastructure state.
"""

import asyncio
import logging
import os
import shutil
import tempfile
from dataclasses import dataclass, field
from datetime import datetime, timezone
from pathlib import Path
from typing import Callable, Dict, List, Optional

from manifest.engine import ManifestEngine, ReconcileResult
from manifest.schema import InfraFile

logger = logging.getLogger(__name__)

RECONCILE_CALLBACK = Callable[[InfraFile, ReconcileResult], None]
MANIFEST_FILENAME = "infra.yaml"


@dataclass
class GitRepoWatch:
    """A Git repository being watched for manifest changes."""
    url: str
    branch: str = "main"
    manifest_path: str = MANIFEST_FILENAME
    poll_interval_seconds: int = 60
    local_dir: str = ""
    last_commit: str = ""
    last_reconcile: Optional[datetime] = None
    enabled: bool = True

    def __post_init__(self):
        if not self.local_dir:
            self.local_dir = tempfile.mkdtemp(prefix="infrapilot_gitops_")


class ManifestWatcher:
    """Periodically clones/pulls repos and triggers reconciliation."""

    def __init__(
        self,
        engine: Optional[ManifestEngine] = None,
        on_reconcile: Optional[RECONCILE_CALLBACK] = None,
    ):
        self.engine = engine or ManifestEngine()
        self.on_reconcile = on_reconcile
        self.watches: List[GitRepoWatch] = []
        self._task: Optional[asyncio.Task] = None
        self._running = False

    def add_watch(self, watch: GitRepoWatch) -> None:
        """Add a repository to watch."""
        self.watches.append(watch)
        logger.info("Watching Git repo: %s (branch: %s, poll: %ds)", watch.url, watch.branch, watch.poll_interval_seconds)

    def remove_watch(self, repo_url: str) -> bool:
        """Stop watching a repository."""
        before = len(self.watches)
        self.watches = [w for w in self.watches if w.url != repo_url]
        return len(self.watches) < before

    async def start(self) -> None:
        """Start the background polling loop."""
        if self._running:
            return
        self._running = True
        self._task = asyncio.create_task(self._poll_loop())
        logger.info("Manifest watcher started (%d repo(s))", len(self.watches))

    async def stop(self) -> None:
        """Stop the background polling loop."""
        self._running = False
        if self._task:
            self._task.cancel()
            self._task = None
        logger.info("Manifest watcher stopped")

    async def poll_once(self) -> List[ReconcileResult]:
        """Check all watched repos and reconcile any changes."""
        results: List[ReconcileResult] = []
        for watch in self.watches:
            if not watch.enabled:
                continue
            try:
                result = await self._check_repo(watch)
                if result:
                    results.append(result)
            except Exception as exc:
                logger.error("Error checking repo %s: %s", watch.url, exc)
        return results

    async def _poll_loop(self) -> None:
        while self._running:
            await self.poll_once()
            await asyncio.sleep(30)

    async def _check_repo(self, watch: GitRepoWatch) -> Optional[ReconcileResult]:
        """Clone/pull the repo and reconcile if the manifest changed."""
        repo_dir = Path(watch.local_dir)

        if not (repo_dir / ".git").exists():
            await self._clone_repo(watch)
        else:
            await self._pull_repo(watch)

        manifest_file = repo_dir / watch.manifest_path
        if not manifest_file.exists():
            logger.debug("No %s found in %s", watch.manifest_path, watch.url)
            return None

        try:
            desired = ManifestEngine.load_yaml(str(manifest_file))
        except Exception as exc:
            logger.error("Failed to parse manifest from %s: %s", watch.url, exc)
            return None

        result = await self.engine.reconcile(desired)

        if self.on_reconcile:
            try:
                self.on_reconcile(desired, result)
            except Exception as exc:
                logger.error("Reconciliation callback failed: %s", exc)

        watch.last_reconcile = datetime.now(timezone.utc)
        return result

    async def _clone_repo(self, watch: GitRepoWatch) -> None:
        """Fresh clone of a repository."""
        repo_dir = Path(watch.local_dir)
        if repo_dir.exists():
            shutil.rmtree(str(repo_dir))
        repo_dir.mkdir(parents=True, exist_ok=True)

        proc = await asyncio.create_subprocess_exec(
            "git", "clone", "--branch", watch.branch,
            "--depth", "1", watch.url, str(repo_dir),
            stdout=asyncio.subprocess.PIPE,
            stderr=asyncio.subprocess.PIPE,
        )
        _, stderr = await proc.communicate()
        if proc.returncode != 0:
            logger.warning("Git clone failed for %s: %s", watch.url, stderr.decode())
        else:
            logger.info("Cloned %s (branch: %s)", watch.url, watch.branch)

    async def _pull_repo(self, watch: GitRepoWatch) -> None:
        """Pull latest changes for an existing clone."""
        proc = await asyncio.create_subprocess_exec(
            "git", "-C", watch.local_dir, "pull", "--ff-only",
            stdout=asyncio.subprocess.PIPE,
            stderr=asyncio.subprocess.PIPE,
        )
        _, stderr = await proc.communicate()
        if proc.returncode != 0:
            logger.warning("Git pull failed for %s: %s", watch.url, stderr.decode())
