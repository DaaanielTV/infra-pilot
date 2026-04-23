import asyncio
import logging
from aiohttp import web
import json
from typing import Dict, Any
import os

from integration import (
    IntegrationService,
    UnifiedUserManager,
    CrossPlatformNotifier,
    UnifiedMetrics,
    SharedConfigManager
)

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)


class IntegrationAPIServer:
    """REST API for Integration Service"""

    def __init__(self, config_path: str = 'integration_config.json'):
        self.service = IntegrationService(config_path)
        self.app = web.Application()
        self._setup_routes()
        self.config_manager = SharedConfigManager()

    def _setup_routes(self):
        self.app.router.add_get('/', self.handle_index)
        self.app.router.add_get('/health', self.handle_health)
        
        # User Management
        self.app.router.add_post('/api/users', self.handle_create_user)
        self.app.router.add_get('/api/users/{email}', self.handle_get_user)
        self.app.router.add_put('/api/users/{email}', self.handle_update_user)
        
        # Notifications
        self.app.router.add_post('/api/notifications', self.handle_notification)
        self.app.router.add_post('/api/notifications/server-event', self.handle_server_event)
        
        # Metrics
        self.app.router.add_get('/api/metrics', self.handle_metrics)
        self.app.router.add_get('/api/metrics/dashboard', self.handle_metrics_dashboard)
        
        # Configuration
        self.app.router.add_get('/api/config', self.handle_get_config)
        self.app.router.add_put('/api/config', self.handle_update_config)

    async def handle_index(self, request: web.Request) -> web.Response:
        return web.json_response({
            'service': 'Integration Service',
            'version': '1.0.0',
            'endpoints': [
                '/api/users',
                '/api/notifications',
                '/api/metrics',
                '/api/config'
            ]
        })

    async def handle_health(self, request: web.Request) -> web.Response:
        return web.json_response({'status': 'healthy'})

    async def handle_create_user(self, request: web.Request) -> web.Response:
        try:
            user_data = await request.json()
            result = await self.service.user_manager.create_user(user_data)
            return web.json_response(result, status=201)
        except Exception as e:
            logger.error(f"Create user failed: {e}")
            return web.json_response({'error': str(e)}, status=500)

    async def handle_get_user(self, request: web.Request) -> web.Response:
        email = request.match_info['email']
        profile = await self.service.user_manager.get_unified_profile(email)
        return web.json_response(profile)

    async def handle_update_user(self, request: web.Request) -> web.Response:
        try:
            email = request.match_info['email']
            updates = await request.json()
            success = await self.service.user_manager.update_user(email, updates)
            return web.json_response({'success': success})
        except Exception as e:
            logger.error(f"Update user failed: {e}")
            return web.json_response({'error': str(e)}, status=500)

    async def handle_notification(self, request: web.Request) -> web.Response:
        try:
            message = await request.json()
            success = await self.service.notifier.broadcast(message)
            return web.json_response({'success': success})
        except Exception as e:
            logger.error(f"Notification failed: {e}")
            return web.json_response({'error': str(e)}, status=500)

    async def handle_server_event(self, request: web.Request) -> web.Response:
        try:
            data = await request.json()
            event_type = data.get('event_type')
            server_name = data.get('server_name')
            details = data.get('details', {})
            success = await self.service.notifier.notify_server_event(
                event_type, server_name, details
            )
            return web.json_response({'success': success})
        except Exception as e:
            logger.error(f"Server event notification failed: {e}")
            return web.json_response({'error': str(e)}, status=500)

    async def handle_metrics(self, request: web.Request) -> web.Response:
        metrics = await self.service.metrics.collect_metrics()
        return web.json_response(metrics)

    async def handle_metrics_dashboard(self, request: web.Request) -> web.Response:
        dashboard = await self.service.metrics.get_unified_dashboard()
        return web.json_response(dashboard)

    async def handle_get_config(self, request: web.Request) -> web.Response:
        return web.json_response(self.config_manager.get_all())

    async def handle_update_config(self, request: web.Request) -> web.Response:
        try:
            updates = await request.json()
            self.config_manager.update(updates)
            return web.json_response({'success': True})
        except Exception as e:
            logger.error(f"Config update failed: {e}")
            return web.json_response({'error': str(e)}, status=500)

    async def start(self, host: str = '0.0.0.0', port: int = 9000):
        await self.service.start()
        runner = web.AppRunner(self.app)
        await runner.setup()
        site = web.TCPSite(runner, host, port)
        await site.start()
        logger.info(f"Integration API running on http://{host}:{port}")

    async def stop(self):
        await self.service.stop()


async def main():
    server = IntegrationAPIServer()
    await server.start()
    
    try:
        await asyncio.Event().wait()
    except KeyboardInterrupt:
        pass
    finally:
        await server.stop()


if __name__ == '__main__':
    asyncio.run(main())