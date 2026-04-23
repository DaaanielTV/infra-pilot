import asyncio
import aiohttp
import logging
from datetime import datetime, timedelta
from typing import Dict, Any, List, Optional
import json
import os

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class BackupManager:
    """Integrated Backup System - Single backup controls for all services"""

    def __init__(self, config: Dict[str, Any]):
        self.config = config
        self.service_core_url = config.get('service_core_url', 'http://localhost:8080')
        self.orchestrator_url = config.get('orchestrator_url', 'http://localhost:8000')
        self.storage_path = config.get('backup_path', './backups')
        self.session: Optional[aiohttp.ClientSession] = None
        os.makedirs(self.storage_path, exist_ok=True)

    async def initialize(self):
        self.session = aiohttp.ClientSession()
        logger.info("BackupManager initialized")

    async def close(self):
        if self.session:
            await self.session.close()

    async def create_backup(self, service: str, server_id: Optional[str] = None) -> Dict[str, Any]:
        """Create backup for a service"""
        backup_id = f"{service}_{datetime.now().strftime('%Y%m%d_%H%M%S')}"
        
        if service == 'service_core':
            return await self._backup_service_core(server_id, backup_id)
        elif service == 'orchestrator':
            return await self._backup_orchestrator(server_id, backup_id)
        elif service == 'all':
            return await self._backup_all(backup_id)
        
        return {'error': f'Unknown service: {service}'}

    async def _backup_service_core(self, server_id: Optional[str], backup_id: str) -> Dict[str, Any]:
        try:
            async with self.session.get(
                f"{self.service_core_url}/api/backups"
            ) as resp:
                if resp.status == 200:
                    data = await resp.json()
                    backup_file = os.path.join(self.storage_path, f"{backup_id}_service_core.json")
                    with open(backup_file, 'w') as f:
                        json.dump(data, f, indent=2)
                    return {'backup_id': backup_id, 'service': 'service_core', 'file': backup_file}
        except Exception as e:
            logger.error(f"Service Core backup failed: {e}")
        return {'backup_id': backup_id, 'service': 'service_core', 'status': 'failed'}

    async def _backup_orchestrator(self, server_id: Optional[str], backup_id: str) -> Dict[str, Any]:
        try:
            async with self.session.get(
                f"{self.orchestrator_url}/api/backups"
            ) as resp:
                if resp.status == 200:
                    data = await resp.json()
                    backup_file = os.path.join(self.storage_path, f"{backup_id}_orchestrator.json")
                    with open(backup_file, 'w') as f:
                        json.dump(data, f, indent=2)
                    return {'backup_id': backup_id, 'service': 'orchestrator', 'file': backup_file}
        except Exception as e:
            logger.error(f"Orchestrator backup failed: {e}")
        return {'backup_id': backup_id, 'service': 'orchestrator', 'status': 'failed'}

    async def _backup_all(self, backup_id: str) -> Dict[str, Any]:
        results = await asyncio.gather(
            self._backup_service_core(None, backup_id),
            self._backup_orchestrator(None, backup_id),
            return_exceptions=True
        )
        return {
            'backup_id': backup_id,
            'services': {r.get('service'): r for r in results if isinstance(r, dict)}
        }

    async def restore_backup(self, backup_id: str, service: str) -> bool:
        """Restore backup from file"""
        backup_file = os.path.join(self.storage_path, f"{backup_id}_{service}.json")
        if not os.path.exists(backup_file):
            return False
        
        try:
            with open(backup_file, 'r') as f:
                data = json.load(f)
            
            if service == 'service_core':
                endpoint = f"{self.service_core_url}/api/restore"
            else:
                endpoint = f"{self.orchestrator_url}/api/restore"
            
            async with self.session.post(endpoint, json=data) as resp:
                return resp.status == 200
        except Exception as e:
            logger.error(f"Restore failed: {e}")
            return False

    def list_backups(self) -> List[Dict[str, Any]]:
        backups = []
        for filename in os.listdir(self.storage_path):
            if filename.endswith('.json'):
                parts = filename.replace('.json', '').split('_')
                if len(parts) >= 2:
                    backups.append({
                        'filename': filename,
                        'backup_id': parts[0],
                        'service': parts[1] if len(parts) > 1 else 'unknown',
                        'created': datetime.fromtimestamp(os.path.getctime(
                            os.path.join(self.storage_path, filename)
                        )).isoformat()
                    })
        return sorted(backups, key=lambda b: b['created'], reverse=True)

    async def cleanup_old_backups(self, days: int = 30):
        """Remove backups older than specified days"""
        cutoff = datetime.now() - timedelta(days=days)
        removed = 0
        for backup in self.list_backups():
            created = datetime.fromisoformat(backup['created'])
            if created < cutoff:
                os.remove(os.path.join(self.storage_path, backup['filename']))
                removed += 1
        return removed


class UnifiedReporting:
    """Unified Reporting System - Cross-service usage/billing reports"""

    def __init__(self, config: Dict[str, Any]):
        self.config = config
        self.service_core_url = config.get('service_core_url', 'http://localhost:8080')
        self.orchestrator_url = config.get('orchestrator_url', 'http://localhost:8000')
        self.dashboard_url = config.get('dashboard_url', 'http://localhost:5173')
        self.session: Optional[aiohttp.ClientSession] = None

    async def initialize(self):
        self.session = aiohttp.ClientSession()
        logger.info("UnifiedReporting initialized")

    async def close(self):
        if self.session:
            await self.session.close()

    async def generate_usage_report(self, start_date: str, end_date: str) -> Dict[str, Any]:
        """Generate usage report across all services"""
        report = {
            'period': {'start': start_date, 'end': end_date},
            'generated_at': datetime.now().isoformat(),
            'services': {}
        }
        
        endpoints = {
            'service_core': f"{self.service_core_url}/api/usage",
            'orchestrator': f"{self.orchestrator_url}/api/usage",
            'dashboard': f"{self.dashboard_url}/api/usage"
        }
        
        for service, endpoint in endpoints.items():
            try:
                async with self.session.get(
                    endpoint, params={'start': start_date, 'end': end_date}
                ) as resp:
                    if resp.status == 200:
                        report['services'][service] = await resp.json()
            except Exception as e:
                logger.warning(f"Failed to get {service} usage: {e}")

        report['summary'] = self._calculate_summary(report['services'])
        return report

    def _calculate_summary(self, services: Dict[str, Any]) -> Dict[str, Any]:
        total_servers = 0
        total_cpu_hours = 0
        total_memory_hours = 0
        
        for service_data in services.values():
            if isinstance(service_data, dict):
                total_servers += service_data.get('server_count', 0)
                total_cpu_hours += service_data.get('cpu_hours', 0)
                total_memory_hours += service_data.get('memory_hours', 0)
        
        return {
            'total_servers': total_servers,
            'total_cpu_hours': total_cpu_hours,
            'total_memory_hours': total_memory_hours
        }

    async def generate_billing_report(self, user_id: str, start_date: str, end_date: str) -> Dict[str, Any]:
        """Generate billing report for a user"""
        report = {
            'user_id': user_id,
            'period': {'start': start_date, 'end': end_date},
            'generated_at': datetime.now().isoformat(),
            'line_items': []
        }
        
        endpoints = {
            'service_core': f"{self.service_core_url}/api/billing/{user_id}",
            'orchestrator': f"{self.orchestrator_url}/api/billing/{user_id}"
        }
        
        for service, endpoint in endpoints.items():
            try:
                async with self.session.get(
                    endpoint, params={'start': start_date, 'end': end_date}
                ) as resp:
                    if resp.status == 200:
                        data = await resp.json()
                        report['line_items'].extend(data.get('items', []))
            except Exception as e:
                logger.warning(f"Failed to get {service} billing: {e}")

        report['total'] = sum(item.get('amount', 0) for item in report['line_items'])
        return report


async def main():
    config = {}
    backup_manager = BackupManager(config)
    await backup_manager.initialize()
    
    os.makedirs('./backups', exist_ok=True)
    
    print("Creating full system backup...")
    result = await backup_manager.create_backup('all')
    print(f"Backup result: {result}")
    
    await backup_manager.close()


if __name__ == '__main__':
    asyncio.run(main())