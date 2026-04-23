import logging
import requests
import os

INTEGRATION_SERVICE_URL = os.getenv('INTEGRATION_SERVICE_URL', 'http://localhost:9000')

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


async def notify_integration(event_type: str, data: dict) -> bool:
    """Notify integration service about events"""
    try:
        response = requests.post(
            f"{INTEGRATION_SERVICE_URL}/api/notifications/server-event",
            json={
                'event_type': event_type,
                'server_name': data.get('server_name', 'unknown'),
                'details': data
            },
            timeout=5
        )
        return response.status_code in [200, 201]
    except Exception as e:
        logger.warning(f"Integration notification failed: {e}")
        return False


async def notify_server_created(server_id: str, server_name: str):
    """Notify when server is created"""
    return await notify_integration('server_created', {
        'server_id': server_id,
        'server_name': server_name,
        'service': 'orchestrator'
    })


async def notify_server_started(server_id: str, server_name: str):
    """Notify when server is started"""
    return await notify_integration('server_started', {
        'server_id': server_id,
        'server_name': server_name,
        'service': 'orchestrator'
    })


async def notify_server_stopped(server_id: str, server_name: str):
    """Notify when server is stopped"""
    return await notify_integration('server_stopped', {
        'server_id': server_id,
        'server_name': server_name,
        'service': 'orchestrator'
    })


async def notify_server_deleted(server_id: str, server_name: str):
    """Notify when server is deleted"""
    return await notify_integration('server_deleted', {
        'server_id': server_id,
        'server_name': server_name,
        'service': 'orchestrator'
    })


async def sync_user_to_integration(user_id: str, email: str, username: str) -> dict:
    """Sync user to integration service"""
    try:
        response = requests.post(
            f"{INTEGRATION_SERVICE_URL}/api/users",
            json={
                'email': email,
                'username': username,
                'discord_id': user_id
            },
            timeout=5
        )
        if response.status_code in [200, 201]:
            return response.json()
    except Exception as e:
        logger.warning(f"User sync failed: {e}")
    return {}


async def get_unified_metrics() -> dict:
    """Get unified metrics from integration service"""
    try:
        response = requests.get(
            f"{INTEGRATION_SERVICE_URL}/api/metrics/dashboard",
            timeout=5
        )
        if response.status_code == 200:
            return response.json()
    except Exception as e:
        logger.warning(f"Metrics fetch failed: {e}")
    return {}


async def broadcast_notification(message: str, title: str = "Notification") -> bool:
    """Broadcast notification to all platforms"""
    try:
        response = requests.post(
            f"{INTEGRATION_SERVICE_URL}/api/notifications",
            json={
                'content': message,
                'title': title
            },
            timeout=5
        )
        return response.status_code in [200, 201]
    except Exception as e:
        logger.warning(f"Broadcast failed: {e}")
        return False


if __name__ == '__main__':
    import asyncio
    
    async def test():
        result = await notify_server_created('test-123', 'test-server')
        print(f"Notification result: {result}")
        
        metrics = await get_unified_metrics()
        print(f"Metrics: {metrics}")
    
    asyncio.run(test())