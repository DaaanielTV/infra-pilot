import logging
import aiohttp
import asyncio
from typing import Dict, Any, Optional, List
from datetime import datetime
import json
import os

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)


class UnifiedUserManager:
    """Unified User Management - Cross-platform authentication and profile sync"""

    def __init__(self, config: Dict[str, Any]):
        self.config = config
        self.dashboard_url = config.get('dashboard_url', 'http://localhost:3000')
        self.discord_api_url = config.get('discord_api_url', 'http://localhost:3001')
        self.service_core_url = config.get('service_core_url', 'http://localhost:8080')
        self.session: Optional[aiohttp.ClientSession] = None

    async def initialize(self):
        self.session = aiohttp.ClientSession()
        logger.info("UnifiedUserManager initialized")

    async def close(self):
        if self.session:
            await self.session.close()

    async def create_user(self, user_data: Dict[str, Any]) -> Dict[str, Any]:
        """Create user across all platforms"""
        user_id = user_data.get('email', '').replace('@', '_at_').replace('.', '_')
        
        platform_users = {}
        
        # Create in Dashboard (Convex)
        try:
            async with self.session.post(
                f"{self.dashboard_url}/api/users",
                json=user_data
            ) as resp:
                if resp.status == 200:
                    platform_users['dashboard'] = await resp.json()
        except Exception as e:
            logger.warning(f"Dashboard user creation failed: {e}")

        # Create in Discord Service
        try:
            async with self.session.post(
                f"{self.discord_api_url}/api/users",
                json={**user_data, 'external_id': user_id}
            ) as resp:
                if resp.status == 200:
                    platform_users['discord'] = await resp.json()
        except Exception as e:
            logger.warning(f"Discord user creation failed: {e}")

        # Create in Service Core
        try:
            async with self.session.post(
                f"{self.service_core_url}/api/users",
                json=user_data
            ) as resp:
                if resp.status == 200:
                    platform_users['service_core'] = await resp.json()
        except Exception as e:
            logger.warning(f"Service Core user creation failed: {e}")

        return {
            'unified_id': user_id,
            'email': user_data.get('email'),
            'platforms': platform_users,
            'created_at': datetime.now().isoformat()
        }

    async def sync_user(self, user_id: str, platform: str) -> Optional[Dict[str, Any]]:
        """Sync user data from specific platform"""
        try:
            endpoints = {
                'dashboard': f"{self.dashboard_url}/api/users/{user_id}",
                'discord': f"{self.discord_api_url}/api/users/{user_id}",
                'service_core': f"{self.service_core_url}/api/users/{user_id}"
            }
            
            async with self.session.get(endpoints.get(platform)) as resp:
                if resp.status == 200:
                    return await resp.json()
        except Exception as e:
            logger.error(f"Sync from {platform} failed: {e}")
        
        return None

    async def get_unified_profile(self, email: str) -> Dict[str, Any]:
        """Get unified profile from all platforms"""
        profile = {'email': email, 'platforms': {}}
        
        # Fetch from all platforms in parallel
        tasks = [
            self.sync_user(email, 'dashboard'),
            self.sync_user(email, 'discord'),
            self.sync_user(email, 'service_core')
        ]
        
        results = await asyncio.gather(*tasks, return_exceptions=True)
        platform_names = ['dashboard', 'discord', 'service_core']
        
        for name, result in zip(platform_names, results):
            if isinstance(result, dict):
                profile['platforms'][name] = result

        return profile

    async def update_user(self, email: str, updates: Dict[str, Any]) -> bool:
        """Update user across all platforms"""
        tasks = []
        
        try:
            async with self.session.put(
                f"{self.dashboard_url}/api/users/{email}",
                json=updates
            ) as resp:
                tasks.append(resp.status == 200)
        except:
            tasks.append(False)

        try:
            async with self.session.put(
                f"{self.discord_api_url}/api/users/{email}",
                json=updates
            ) as resp:
                tasks.append(resp.status == 200)
        except:
            tasks.append(False)

        try:
            async with self.session.put(
                f"{self.service_core_url}/api/users/{email}",
                json=updates
            ) as resp:
                tasks.append(resp.status == 200)
        except:
            tasks.append(False)

        return any(tasks)


class CrossPlatformNotifier:
    """Cross-Service Operations - Synchronized notifications"""

    def __init__(self, config: Dict[str, Any]):
        self.config = config
        self.discord_webhook = config.get('discord_webhook')
        self.dashboard_ws = config.get('dashboard_ws')
        self.session: Optional[aiohttp.ClientSession] = None

    async def initialize(self):
        self.session = aiohttp.ClientSession()
        logger.info("CrossPlatformNotifier initialized")

    async def close(self):
        if self.session:
            await self.session.close()

    async def broadcast(self, message: Dict[str, Any]) -> bool:
        """Send notification to all platforms"""
        results = []
        
        # Send to Discord webhook
        if self.discord_webhook:
            try:
                async with self.session.post(
                    self.discord_webhook,
                    json=message
                ) as resp:
                    results.append(resp.status in [200, 204])
            except Exception as e:
                logger.warning(f"Discord webhook failed: {e}")
                results.append(False)

        # Send to Dashboard WebSocket (via HTTP webhook for now)
        if self.dashboard_ws:
            try:
                async with self.session.post(
                    self.dashboard_ws,
                    json=message
                ) as resp:
                    results.append(resp.status == 200)
            except Exception as e:
                logger.warning(f"Dashboard notification failed: {e}")
                results.append(False)

        return any(results)

    async def notify_server_event(self, event_type: str, server_name: str, details: Dict[str, Any]) -> bool:
        """Notify about server events across platforms"""
        event_messages = {
            'server_created': f"🎉 New server '{server_name}' created!",
            'server_started': f"🟢 Server '{server_name}' started",
            'server_stopped': f"🔴 Server '{server_name}' stopped",
            'server_deleted': f"🗑️ Server '{server_name}' deleted",
            'server_error': f"❌ Error on server '{server_name}': {details.get('error', 'Unknown error')}"
        }
        
        message = {
            'embeds': [{
                'title': event_messages.get(event_type, f"Server event: {event_type}"),
                'description': json.dumps(details),
                'timestamp': datetime.now().isoformat(),
                'color': 0x007bff
            }]
        }
        
        return await self.broadcast(message)


class UnifiedMetrics:
    """Integrated Monitoring - Unified metrics aggregation"""

    def __init__(self, config: Dict[str, Any]):
        self.config = config
        self.service_core_url = config.get('service_core_url', 'http://localhost:8080')
        self.orchestrator_url = config.get('orchestrator_url', 'http://localhost:8000')
        self.session: Optional[aiohttp.ClientSession] = None

    async def initialize(self):
        self.session = aiohttp.ClientSession()
        logger.info("UnifiedMetrics initialized")

    async def close(self):
        if self.session:
            await self.session.close()

    async def collect_metrics(self) -> Dict[str, Any]:
        """Collect metrics from all services"""
        metrics = {
            'timestamp': datetime.now().isoformat(),
            'services': {}
        }
        
        # Service Core metrics
        try:
            async with self.session.get(
                f"{self.service_core_url}/api/metrics"
            ) as resp:
                if resp.status == 200:
                    metrics['services']['service_core'] = await resp.json()
        except Exception as e:
            logger.warning(f"Service Core metrics collection failed: {e}")

        # Orchestrator metrics
        try:
            async with self.session.get(
                f"{self.orchestrator_url}/api/metrics"
            ) as resp:
                if resp.status == 200:
                    metrics['services']['orchestrator'] = await resp.json()
        except Exception as e:
            logger.warning(f"Orchestrator metrics collection failed: {e}")

        return metrics

    async def get_unified_dashboard(self) -> Dict[str, Any]:
        """Get unified metrics for dashboard display"""
        metrics = await self.collect_metrics()
        
        summary = {
            'total_servers': 0,
            'active_servers': 0,
            'total_cpu_percent': 0,
            'total_memory_percent': 0,
            'by_platform': {}
        }
        
        if 'services' in metrics:
            for platform, data in metrics['services'].items():
                if isinstance(data, dict):
                    server_count = data.get('server_count', 0)
                    summary['total_servers'] += server_count
                    summary['by_platform'][platform] = {
                        'servers': server_count,
                        'cpu': data.get('cpu_percent', 0),
                        'memory': data.get('memory_percent', 0)
                    }

        return {**metrics, 'summary': summary}


class SharedConfigManager:
    """Shared Configuration Management - Centralized config for all services"""

    def __init__(self, config_path: str = 'shared_config.json'):
        self.config_path = config_path
        self.config: Dict[str, Any] = {}
        self.load()

    def load(self):
        """Load shared configuration"""
        try:
            if os.path.exists(self.config_path):
                with open(self.config_path, 'r') as f:
                    self.config = json.load(f)
                logger.info(f"Loaded config from {self.config_path}")
        except Exception as e:
            logger.error(f"Failed to load config: {e}")
            self.config = {}

    def save(self):
        """Save shared configuration"""
        try:
            with open(self.config_path, 'w') as f:
                json.dump(self.config, f, indent=2)
            logger.info(f"Saved config to {self.config_path}")
        except Exception as e:
            logger.error(f"Failed to save config: {e}")

    def get(self, key: str, default: Any = None) -> Any:
        """Get config value"""
        return self.config.get(key, default)

    def set(self, key: str, value: Any):
        """Set config value"""
        self.config[key] = value
        self.save()

    def get_all(self) -> Dict[str, Any]:
        """Get all config"""
        return self.config.copy()

    def update(self, updates: Dict[str, Any]):
        """Update multiple config values"""
        self.config.update(updates)
        self.save()


class IntegrationService:
    """Main Integration Service - Coordinates all integration features"""

    def __init__(self, config_path: str = 'integration_config.json'):
        self.config = self._load_config(config_path)
        self.user_manager = UnifiedUserManager(self.config)
        self.notifier = CrossPlatformNotifier(self.config)
        self.metrics = UnifiedMetrics(self.config)
        self.config_manager = SharedConfigManager()

    def _load_config(self, config_path: str) -> Dict[str, Any]:
        try:
            if os.path.exists(config_path):
                with open(config_path, 'r') as f:
                    return json.load(f)
        except Exception as e:
            logger.warning(f"Could not load config: {e}")
        return {
            'dashboard_url': os.getenv('DASHBOARD_URL', 'http://localhost:5173'),
            'discord_api_url': os.getenv('DISCORD_API_URL', 'http://localhost:3001'),
            'service_core_url': os.getenv('SERVICE_CORE_URL', 'http://localhost:8080'),
            'orchestrator_url': os.getenv('ORCHESTRATOR_URL', 'http://localhost:8000'),
            'discord_webhook': os.getenv('DISCORD_WEBHOOK')
        }

    async def start(self):
        """Start all integration components"""
        await self.user_manager.initialize()
        await self.notifier.initialize()
        await self.metrics.initialize()
        logger.info("Integration Service started")

    async def stop(self):
        """Stop all integration components"""
        await self.user_manager.close()
        await self.notifier.close()
        await self.metrics.close()
        logger.info("Integration Service stopped")


if __name__ == '__main__':
    service = IntegrationService()
    asyncio.run(service.start())