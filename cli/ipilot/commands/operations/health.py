"""Health check commands for the CLI."""

from typing import Any, Dict, Optional

from ...client import ApiClient
from ...config import load_config


def get_health_status() -> Dict[str, Any]:
    """Check the health status of the API.

    Returns:
        Dictionary containing health status information including
        component statuses, version, timestamp, and uptime.
    """
    try:
        config = load_config()
        client = ApiClient(
            config.get('api_url', 'http://localhost:8080'),
            config.get('token'),
        )
        return client.health_check()
    except Exception as e:
        return {
            'status': 'error',
            'message': f'Health check failed: {str(e)}',
            'component': 'api',
        }


def format_health_output(health_data: Dict[str, Any]) -> Dict[str, Optional[Any]]:
    """Format raw health data into a standardized output structure.

    Args:
        health_data: Raw health data from the API health check.

    Returns:
        A formatted dictionary with standardized health status fields.
    """
    if 'error' in health_data:
        return {
            'status': 'UNHEALTHY',
            'error': health_data['error'],
            'timestamp': health_data.get('timestamp'),
        }
    return {
        'status': health_data.get('status', 'UNKNOWN').upper(),
        'api': health_data.get('api', 'UNKNOWN'),
        'database': health_data.get('database', 'UNKNOWN'),
        'cache': health_data.get('cache', 'UNKNOWN'),
        'version': health_data.get('version'),
        'timestamp': health_data.get('timestamp'),
        'uptime': health_data.get('uptime'),
    }