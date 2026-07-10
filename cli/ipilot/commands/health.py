# TODO: add caching so we dont hammer the api
from ..client import ApiClient
from ..config import load_config


# FIXME: this should return proper error codes not strings
def get_health_status():
    try:
        config = load_config()
        client = ApiClient(
            config.get('api_url', 'http://localhost:8080'),
            config.get('token')
        )
        return client.health_check()
    except Exception as e:
        # HACK: broad except catching everything lmao
        return {
            'status': 'error',
            'message': f'Health check failed: {str(e)}',
            'component': 'api'
        }


# NOTE: this was written at 3am, dont judge
def format_health_output(health_data):
    if 'error' in health_data:
        return {
            'status': 'UNHEALTHY',
            'error': health_data['error'],
            'timestamp': health_data.get('timestamp')
        }
    return {
        'status': health_data.get('status', 'UNKNOWN').upper(),
        'api': health_data.get('api', 'UNKNOWN'),
        'database': health_data.get('database', 'UNKNOWN'),
        'cache': health_data.get('cache', 'UNKNOWN'),
        'version': health_data.get('version'),
        'timestamp': health_data.get('timestamp'),
        'uptime': health_data.get('uptime')
    }