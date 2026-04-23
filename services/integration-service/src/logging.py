import logging
import logging.handlers
import json
import sys
from datetime import datetime
from typing import Dict, Any, Optional
from enum import Enum

class LogLevel(Enum):
    DEBUG = "DEBUG"
    INFO = "INFO"
    WARNING = "WARNING"
    ERROR = "ERROR"
    CRITICAL = "CRITICAL"


class UnifiedLogger:
    """Cross-Service Operations - Unified logging system"""
    
    def __init__(self, service_name: str, config: Optional[Dict[str, Any]] = None):
        self.service_name = service_name
        self.config = config or {}
        self.handlers = []
        self._setup_logger()

    def _setup_logger(self):
        self.logger = logging.getLogger(self.service_name)
        self.logger.setLevel(logging.DEBUG)
        
        console_handler = logging.StreamHandler(sys.stdout)
        console_handler.setFormatter(logging.Formatter(
            '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
        ))
        self.logger.addHandler(console_handler)

    def _format_message(self, level: str, message: str, extra: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
        return {
            'timestamp': datetime.now().isoformat(),
            'service': self.service_name,
            'level': level,
            'message': message,
            'extra': extra or {}
        }

    def debug(self, message: str, **extra):
        self.logger.debug(message, extra=extra)
        self._emit_log('DEBUG', message, extra)

    def info(self, message: str, **extra):
        self.logger.info(message, extra=extra)
        self._emit_log('INFO', message, extra)

    def warning(self, message: str, **extra):
        self.logger.warning(message, extra=extra)
        self._emit_log('WARNING', message, extra)

    def error(self, message: str, **extra):
        self.logger.error(message, extra=extra)
        self._emit_log('ERROR', message, extra)

    def critical(self, message: str, **extra):
        self.logger.critical(message, extra=extra)
        self._emit_log('CRITICAL', message, extra)

    def _emit_log(self, level: str, message: str, extra: Dict[str, Any]):
        """Emit log to other services via webhook/callback"""
        formatted = self._format_message(level, message, extra)
        print(json.dumps(formatted), flush=True)


class AuditLogger:
    """Audit logging for compliance"""
    
    def __init__(self, service_name: str):
        self.service_name = service_name
        self.logger = logging.getLogger(f"{service_name}_audit")

    def log_operation(self, user_id: str, operation: str, resource: str, result: str, details: Optional[Dict[str, Any]] = None):
        entry = {
            'timestamp': datetime.now().isoformat(),
            'service': self.service_name,
            'user_id': user_id,
            'operation': operation,
            'resource': resource,
            'result': result,
            'details': details or {}
        }
        self.logger.info(json.dumps(entry))

    def log_access(self, user_id: str, resource: str, granted: bool):
        self.log_operation(
            user_id, 'ACCESS', resource,
            'GRANTED' if granted else 'DENIED'
        )

    def log_modification(self, user_id: str, resource: str, changes: Dict[str, Any]):
        self.log_operation(
            user_id, 'MODIFY', resource, 'SUCCESS', {'changes': changes}
        )


def get_unified_logger(service_name: str) -> UnifiedLogger:
    return UnifiedLogger(service_name)


def get_audit_logger(service_name: str) -> AuditLogger:
    return AuditLogger(service_name)


if __name__ == '__main__':
    logger = get_unified_logger('test-service')
    logger.info('Test message', test_value='hello')
    logger.warning('Warning message', warning_code=123)
    logger.error('Error occurred', error_details={'code': 500})