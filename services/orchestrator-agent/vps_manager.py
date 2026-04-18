import docker
import asyncio
from dataclasses import dataclass
from typing import Dict, Optional, List
import logging
from datetime import datetime
import json
import os

@dataclass
class VPSConfig:
    cpu_limit: float  # Number of CPU cores
    memory_limit: int  # Memory limit in MB
    storage_limit: int  # Storage limit in GB
    image: str  # Docker image to use
    ports: Dict[str, str]  # Port mappings
    env_vars: Dict[str, str]  # Environment variables

class VPSManager:
    def __init__(self):
        self.client = docker.from_env()
        self.logger = logging.getLogger('vps_manager')
        self.vps_instances = {}
        self.load_instances()

    def load_instances(self):
        """Load saved VPS instances from disk"""
        try:
            if os.path.exists('vps_instances.json'):
                with open('vps_instances.json', 'r') as f:
                    self.vps_instances = json.load(f)
        except Exception as e:
            self.logger.error(f"Error loading VPS instances: {e}")
            self.vps_instances = {}

    def save_instances(self):
        """Save VPS instances to disk"""
        try:
            with open('vps_instances.json', 'w') as f:
                json.dump(self.vps_instances, f)
        except Exception as e:
            self.logger.error(f"Error saving VPS instances: {e}")

    async def create_vps(self, user_id: str, config: VPSConfig) -> Optional[str]:
        """Create a new VPS instance"""
        try:
            container = self.client.containers.run(
                image=config.image,
                detach=True,
                cpu_period=100000,
                cpu_quota=int(config.cpu_limit * 100000),
                mem_limit=f"{config.memory_limit}m",
                ports=config.ports,
                environment=config.env_vars,
                restart_policy={"Name": "unless-stopped"}
            )

            instance_info = {
                "container_id": container.id,
                "user_id": user_id,
                "created_at": datetime.now().isoformat(),
                "config": {
                    "cpu_limit": config.cpu_limit,
                    "memory_limit": config.memory_limit,
                    "storage_limit": config.storage_limit,
                    "image": config.image,
                    "ports": config.ports,
                }
            }

            self.vps_instances[container.id] = instance_info
            self.save_instances()

            return container.id
        except Exception as e:
            self.logger.error(f"Error creating VPS: {e}")
            return None

    async def delete_vps(self, container_id: str) -> bool:
        """Delete a VPS instance"""
        try:
            container = self.client.containers.get(container_id)
            container.stop()
            container.remove()
            
            del self.vps_instances[container_id]
            self.save_instances()
            
            return True
        except Exception as e:
            self.logger.error(f"Error deleting VPS: {e}")
            return False

    async def start_vps(self, container_id: str) -> bool:
        """Start a VPS instance"""
        try:
            container = self.client.containers.get(container_id)
            container.start()
            return True
        except Exception as e:
            self.logger.error(f"Error starting VPS: {e}")
            return False

    async def stop_vps(self, container_id: str) -> bool:
        """Stop a VPS instance"""
        try:
            container = self.client.containers.get(container_id)
            container.stop()
            return True
        except Exception as e:
            self.logger.error(f"Error stopping VPS: {e}")
            return False

    async def restart_vps(self, container_id: str) -> bool:
        """Restart a VPS instance"""
        try:
            container = self.client.containers.get(container_id)
            container.restart()
            return True
        except Exception as e:
            self.logger.error(f"Error restarting VPS: {e}")
            return False

    async def get_vps_stats(self, container_id: str) -> Optional[Dict]:
        """Get statistics for a VPS instance"""
        try:
            container = self.client.containers.get(container_id)
            stats = container.stats(stream=False)
            
            # Calculate CPU usage percentage
            cpu_delta = stats["cpu_stats"]["cpu_usage"]["total_usage"] - \
                       stats["precpu_stats"]["cpu_usage"]["total_usage"]
            system_delta = stats["cpu_stats"]["system_cpu_usage"] - \
                          stats["precpu_stats"]["system_cpu_usage"]
            cpu_usage = (cpu_delta / system_delta) * 100.0

            # Calculate memory usage
            memory_usage = stats["memory_stats"]["usage"]
            memory_limit = stats["memory_stats"]["limit"]
            memory_percent = (memory_usage / memory_limit) * 100.0

            return {
                "status": container.status,
                "cpu_usage": round(cpu_usage, 2),
                "memory_usage": round(memory_percent, 2),
                "network": {
                    "rx_bytes": stats["networks"]["eth0"]["rx_bytes"],
                    "tx_bytes": stats["networks"]["eth0"]["tx_bytes"]
                }
            }
        except Exception as e:
            self.logger.error(f"Error getting VPS stats: {e}")
            return None

    async def list_user_instances(self, user_id: str) -> List[Dict]:
        """List all VPS instances for a user"""
        return [
            {
                "container_id": container_id,
                "info": instance_info,
                "stats": await self.get_vps_stats(container_id)
            }
            for container_id, instance_info in self.vps_instances.items()
            if instance_info["user_id"] == user_id
        ]

    async def update_vps_config(self, container_id: str, config: VPSConfig) -> bool:
        """Update VPS configuration"""
        try:
            container = self.client.containers.get(container_id)
            
            # Stop the container to update resources
            container.stop()
            
            # Update container with new configuration
            container.update(
                cpu_period=100000,
                cpu_quota=int(config.cpu_limit * 100000),
                mem_limit=f"{config.memory_limit}m"
            )
            
            # Update stored configuration
            if container_id in self.vps_instances:
                self.vps_instances[container_id]["config"].update({
                    "cpu_limit": config.cpu_limit,
                    "memory_limit": config.memory_limit,
                    "storage_limit": config.storage_limit
                })
                self.save_instances()
            
            # Restart the container
            container.start()
            
            return True
        except Exception as e:
            self.logger.error(f"Error updating VPS configuration: {e}")
            return False

    async def create_backup(self, container_id: str) -> Optional[str]:
        """Create a backup of a VPS instance"""
        try:
            container = self.client.containers.get(container_id)
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            backup_name = f"{container.name}_backup_{timestamp}"
            
            # Create image from container
            image = container.commit(repository=backup_name)
            
            # Save backup info
            if container_id in self.vps_instances:
                if "backups" not in self.vps_instances[container_id]:
                    self.vps_instances[container_id]["backups"] = []
                
                self.vps_instances[container_id]["backups"].append({
                    "image_id": image.id,
                    "created_at": timestamp,
                    "name": backup_name
                })
                self.save_instances()
            
            return image.id
        except Exception as e:
            self.logger.error(f"Error creating backup: {e}")
            return None

    async def restore_backup(self, container_id: str, backup_image_id: str) -> bool:
        """Restore a VPS instance from backup"""
        try:
            # Stop and remove the current container
            await self.stop_vps(container_id)
            
            # Get the original container config
            instance_info = self.vps_instances[container_id]
            config = instance_info["config"]
            
            # Create new container from backup
            container = self.client.containers.run(
                image=backup_image_id,
                detach=True,
                cpu_period=100000,
                cpu_quota=int(config["cpu_limit"] * 100000),
                mem_limit=f"{config['memory_limit']}m",
                ports=config["ports"],
                restart_policy={"Name": "unless-stopped"}
            )
            
            # Update container ID in instances
            instance_info["container_id"] = container.id
            self.vps_instances[container.id] = instance_info
            del self.vps_instances[container_id]
            self.save_instances()
            
            return True
        except Exception as e:
            self.logger.error(f"Error restoring backup: {e}")
            return False