import asyncio
import aiohttp
import logging
from datetime import datetime
from typing import Dict, Any, List, Optional
import json
import os

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class UnifiedResourceTracker:
    """Resource Coordination - Unified resource tracking across services"""

    def __init__(self, config: Dict[str, Any]):
        self.config = config
        self.service_core_url = config.get('service_core_url', 'http://localhost:8080')
        self.orchestrator_url = config.get('orchestrator_url', 'http://localhost:8000')
        self.dashboard_url = config.get('dashboard_url', 'http://localhost:5173')
        self.session: Optional[aiohttp.ClientSession] = None

    async def initialize(self):
        self.session = aiohttp.ClientSession()
        logger.info("UnifiedResourceTracker initialized")

    async def close(self):
        if self.session:
            await self.session.close()

    async def get_all_resources(self) -> Dict[str, Any]:
        """Get resources from all services"""
        resources = {
            'timestamp': datetime.now().isoformat(),
            'total': {
                'servers': 0,
                'cpu_cores': 0,
                'memory_mb': 0,
                'storage_gb': 0
            },
            'by_service': {}
        }
        
        services = {
            'service_core': self.service_core_url,
            'orchestrator': self.orchestrator_url,
            'dashboard': self.dashboard_url
        }
        
        for service_name, base_url in services.items():
            try:
                async with self.session.get(
                    f"{base_url}/api/resources"
                ) as resp:
                    if resp.status == 200:
                        data = await resp.json()
                        resources['by_service'][service_name] = data
                        resources['total']['servers'] += data.get('servers', 0)
                        resources['total']['cpu_cores'] += data.get('cpu_cores', 0)
                        resources['total']['memory_mb'] += data.get('memory_mb', 0)
                        resources['total']['storage_gb'] += data.get('storage_gb', 0)
            except Exception as e:
                logger.warning(f"Failed to get {service_name} resources: {e}")

        return resources

    async def allocate_resource(self, service: str, resource_type: str, amount: int) -> Dict[str, Any]:
        """Allocate resource from pool"""
        resources = await self.get_all_resources()
        
        available = resources['total'].get(resource_type, 0)
        
        if available >= amount:
            return {
                'allocated': True,
                'service': service,
                'resource': resource_type,
                'amount': amount
            }
        
        return {
            'allocated': False,
            'reason': f'Insufficient {resource_type}. Available: {available}, Requested: {amount}'
        }

    async def get_resource_usage(self, user_id: Optional[str] = None) -> Dict[str, Any]:
        """Get resource usage by user"""
        usage = {'users': {}}
        
        services = {
            'service_core': f"{self.service_core_url}/api/usage",
            'orchestrator': f"{self.orchestrator_url}/api/usage"
        }
        
        for service_name, endpoint in services.items():
            try:
                url = endpoint if not user_id else f"{endpoint}/{user_id}"
                async with self.session.get(url) as resp:
                    if resp.status == 200:
                        usage['users'][service_name] = await resp.json()
            except Exception as e:
                logger.warning(f"Failed to get {service_name} usage: {e}")

        return usage


async def main():
    config = {}
    tracker = UnifiedResourceTracker(config)
    await tracker.initialize()
    
    print("Fetching unified resources...")
    resources = await tracker.get_all_resources()
    print(json.dumps(resources, indent=2))
    
    await tracker.close()


if __name__ == '__main__':
    asyncio.run(main())