"""Rate limiting middleware for the orchestrator-agent API server.

Provides token bucket and sliding window rate limiting strategies
for API endpoint protection.
"""

import asyncio
import logging
import os
import time
from collections import defaultdict
from dataclasses import dataclass, field
from datetime import datetime, timedelta
from enum import Enum
from typing import Callable, Dict, List, Optional, Tuple

logger = logging.getLogger(__name__)


class RateLimitStrategy(Enum):
    TOKEN_BUCKET = "token_bucket"
    SLIDING_WINDOW = "sliding_window"
    FIXED_WINDOW = "fixed_window"


@dataclass
class RateLimitConfig:
    requests: int = 100
    window_seconds: int = 60
    strategy: RateLimitStrategy = RateLimitStrategy.SLIDING_WINDOW
    burst_size: int = 20
    concurrency_limit: int = 10


@dataclass
class TokenBucket:
    tokens: float
    capacity: float
    refill_rate: float
    last_refill: float = field(default_factory=time.time)

    def consume(self, tokens: float = 1.0) -> bool:
        now = time.time()
        elapsed = now - self.last_refill
        self.tokens = min(self.capacity, self.tokens + elapsed * self.refill_rate)
        self.last_refill = now
        if self.tokens >= tokens:
            self.tokens -= tokens
            return True
        return False

    def refill(self):
        now = time.time()
        elapsed = now - self.last_refill
        self.tokens = min(self.capacity, self.tokens + elapsed * self.refill_rate)
        self.last_refill = now


@dataclass
class SlidingWindowEntry:
    timestamps: List[float] = field(default_factory=list)

    def prune(self, window_seconds: float):
        cutoff = time.time() - window_seconds
        self.timestamps = [t for t in self.timestamps if t > cutoff]

    def add(self):
        self.timestamps.append(time.time())

    def count(self, window_seconds: float) -> int:
        self.prune(window_seconds)
        return len(self.timestamps)


class RateLimiter:
    def __init__(self, config: Optional[RateLimitConfig] = None):
        self.config = config or RateLimitConfig()
        self._token_buckets: Dict[str, TokenBucket] = {}
        self._sliding_windows: Dict[str, SlidingWindowEntry] = defaultdict(SlidingWindowEntry)
        self._fixed_windows: Dict[str, Tuple[int, float]] = {}
        self._concurrency: Dict[str, int] = defaultdict(int)
        self._lock = asyncio.Lock() if hasattr(asyncio, 'Lock') else None

    def _get_bucket(self, key: str) -> TokenBucket:
        if key not in self._token_buckets:
            refill_rate = self.config.requests / self.config.window_seconds
            capacity = self.config.requests + self.config.burst_size
            self._token_buckets[key] = TokenBucket(
                tokens=capacity, capacity=capacity, refill_rate=refill_rate
            )
        return self._token_buckets[key]

    def check_token_bucket(self, key: str, cost: float = 1.0) -> bool:
        bucket = self._get_bucket(key)
        return bucket.consume(cost)

    def check_sliding_window(self, key: str) -> bool:
        entry = self._sliding_windows[key]
        entry.add()
        count = entry.count(self.config.window_seconds)
        return count <= self.config.requests

    def check_fixed_window(self, key: str) -> bool:
        now = time.time()
        window_key = int(now / self.config.window_seconds)
        entry_key = f"{key}:{window_key}"
        if entry_key not in self._fixed_windows:
            self._fixed_windows[entry_key] = (1, now)
            return True
        count, start = self._fixed_windows[entry_key]
        if now - start > self.config.window_seconds:
            self._fixed_windows[entry_key] = (1, now)
            return True
        if count >= self.config.requests:
            return False
        self._fixed_windows[entry_key] = (count + 1, start)
        return True

    def check_rate_limit(self, key: str, cost: float = 1.0) -> bool:
        if self.config.strategy == RateLimitStrategy.TOKEN_BUCKET:
            return self.check_token_bucket(key, cost)
        elif self.config.strategy == RateLimitStrategy.SLIDING_WINDOW:
            return self.check_sliding_window(key)
        elif self.config.strategy == RateLimitStrategy.FIXED_WINDOW:
            return self.check_fixed_window(key)
        return True

    def check_concurrency(self, key: str) -> bool:
        if self._concurrency[key] >= self.config.concurrency_limit:
            return False
        self._concurrency[key] += 1
        return True

    def release_concurrency(self, key: str):
        if key in self._concurrency and self._concurrency[key] > 0:
            self._concurrency[key] -= 1

    def get_remaining(self, key: str) -> int:
        if self.config.strategy == RateLimitStrategy.TOKEN_BUCKET:
            bucket = self._get_bucket(key)
            return int(bucket.tokens)
        elif self.config.strategy == RateLimitStrategy.SLIDING_WINDOW:
            entry = self._sliding_windows.get(key)
            if entry:
                count = entry.count(self.config.window_seconds)
                return max(0, self.config.requests - count)
            return self.config.requests
        elif self.config.strategy == RateLimitStrategy.FIXED_WINDOW:
            now = time.time()
            window_key = int(now / self.config.window_seconds)
            entry_key = f"{key}:{window_key}"
            count, start = self._fixed_windows.get(entry_key, (0, now))
            return max(0, self.config.requests - count)
        return self.config.requests

    def get_reset_time(self, key: str) -> float:
        now = time.time()
        if self.config.strategy == RateLimitStrategy.FIXED_WINDOW:
            window_key = int(now / self.config.window_seconds)
            entry_key = f"{key}:{window_key}"
            _, start = self._fixed_windows.get(entry_key, (0, now))
            return start + self.config.window_seconds
        elif self.config.strategy == RateLimitStrategy.SLIDING_WINDOW:
            entry = self._sliding_windows.get(key)
            if entry and entry.timestamps:
                return entry.timestamps[0] + self.config.window_seconds
        return now + self.config.window_seconds

    def reset(self, key: Optional[str] = None):
        if key:
            self._token_buckets.pop(key, None)
            self._sliding_windows.pop(key, None)
            self._concurrency.pop(key, None)
            keys_to_remove = [k for k in self._fixed_windows if k.startswith(f"{key}:")]
            for k in keys_to_remove:
                self._fixed_windows.pop(k, None)
        else:
            self._token_buckets.clear()
            self._sliding_windows.clear()
            self._fixed_windows.clear()
            self._concurrency.clear()

    def get_stats(self) -> Dict:
        return {
            "config": {
                "requests": self.config.requests,
                "window_seconds": self.config.window_seconds,
                "strategy": self.config.strategy.value,
                "burst_size": self.config.burst_size,
                "concurrency_limit": self.config.concurrency_limit,
            },
            "active_buckets": len(self._token_buckets),
            "active_windows": len(self._sliding_windows),
            "active_concurrency": dict(self._concurrency),
        }


def rate_limit_middleware(config: Optional[RateLimitConfig] = None):
    """ASGI middleware for rate limiting."""
    limiter = RateLimiter(config)

    async def middleware(scope, receive, send):
        if scope["type"] != "http":
            await send(scope, receive, send)
            return

        headers = dict(scope.get("headers", []))
        client_ip = scope.get("client", ("127.0.0.1", 0))[0]

        key = f"ip:{client_ip}"
        if not limiter.check_rate_limit(key):
            await send({
                "type": "http.response.start",
                "status": 429,
                "headers": [
                    (b"content-type", b"application/json"),
                    (b"retry-after", str(int(limiter.get_reset_time(key) - time.time()) + 1).encode()),
                    (b"x-ratelimit-limit", str(limiter.config.requests).encode()),
                    (b"x-ratelimit-remaining", str(limiter.get_remaining(key)).encode()),
                    (b"x-ratelimit-reset", str(int(limiter.get_reset_time(key))).encode()),
                ],
            })
            await send({
                "type": "http.response.body",
                "body": b'{"error":"rate_limit_exceeded","message":"Too many requests"}',
            })
            return

        await send(scope, receive, send)

    return middleware


class RateLimitRule:
    def __init__(self, path: str, requests: int, window: int,
                 methods: Optional[List[str]] = None, strategy: RateLimitStrategy = RateLimitStrategy.SLIDING_WINDOW):
        self.path = path
        self.requests = requests
        self.window = window
        self.methods = methods or ["GET", "POST", "PUT", "DELETE", "PATCH"]
        self.strategy = strategy
        self.limiter = RateLimiter(RateLimitConfig(requests=requests, window_seconds=window, strategy=strategy))

    def matches(self, path: str, method: str) -> bool:
        if method not in self.methods:
            return False
        import re
        pattern = self.path.replace("*", ".*")
        return bool(re.match(pattern, path))

    def check(self, key: str) -> Tuple[bool, int, float]:
        allowed = self.limiter.check_rate_limit(key)
        remaining = self.limiter.get_remaining(key)
        reset = self.limiter.get_reset_time(key)
        return allowed, remaining, reset


class RateLimitRegistry:
    def __init__(self):
        self.rules: List[RateLimitRule] = []

    def add_rule(self, rule: RateLimitRule):
        self.rules.append(rule)

    def add_rules(self, rules: List[RateLimitRule]):
        self.rules.extend(rules)

    def check_request(self, path: str, method: str, client_key: str) -> Tuple[bool, int, float, str]:
        for rule in self.rules:
            if rule.matches(path, method):
                allowed, remaining, reset = rule.check(client_key)
                return allowed, remaining, reset, rule.strategy.value
        return True, -1, 0, "none"

    def clear(self):
        self.rules.clear()

    def get_default_rules(self) -> List[RateLimitRule]:
        return [
            RateLimitRule("/api/v1/servers*", 60, 60),
            RateLimitRule("/api/v1/deployments*", 30, 60),
            RateLimitRule("/api/v1/builds*", 10, 60),
            RateLimitRule("/api/v1/containers*", 60, 60),
            RateLimitRule("/api/v1/logs*", 120, 60),
            RateLimitRule("/api/v1/auth*", 10, 60, methods=["POST"]),
            RateLimitRule("/api/v1/register*", 5, 300, methods=["POST"]),
            RateLimitRule("/api/v1/webhooks*", 200, 60, methods=["POST"]),
            RateLimitRule("/api/v1/health*", 300, 60),
            RateLimitRule("/api/v1/metrics*", 60, 60),
            RateLimitRule("/api/v1/search*", 20, 60),
            RateLimitRule("/api/v1/export*", 5, 60),
            RateLimitRule("/api/v1/billing*", 10, 60),
            RateLimitRule("/api/v1/admin*", 20, 60),
            RateLimitRule("/api/v1/*/bulk*", 5, 60, methods=["POST", "PUT", "DELETE"]),
        ]


# Global registry
_default_registry = RateLimitRegistry()
_default_registry.add_rules(_default_registry.get_default_rules())

__all__ = [
    "RateLimiter", "RateLimitConfig", "RateLimitStrategy",
    "RateLimitRule", "RateLimitRegistry", "rate_limit_middleware",
    "TokenBucket", "SlidingWindowEntry", "_default_registry",
]