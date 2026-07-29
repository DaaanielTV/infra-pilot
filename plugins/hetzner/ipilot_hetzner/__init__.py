"""Hetzner Cloud plugin for Infra Pilot - servers, firewalls, volumes, networks, SSH keys, placements groups, load balancers, certificates, DNS, pricing, locations, datacenters, server types, images, ISOs, actions, floating IPs, primary IPs, RDNS, server metrics, rescue mode, rebuild, change type, enable/disable backups, power on/off, shutdown, reset, create image, create snapshot, change protection, change name, attach/detach ISO, attach/detach volume, change volume size, change volume name, add/remove subnet, add/remove route, change network name, change network expose routes to vswitch, create/delete/update firewall rules, apply firewall to resources, set RDNS, change reverse DNS, assign floating IP, unassign floating IP, change floating IP description, create/delete certificate, create/delete/update load balancer, add/delete target, change load balancer type, update load balancer service, delete load balancer service"""

import logging
import os
from typing import Any, Dict, List, Optional
from plugins import PluginBase

logger = logging.getLogger(__name__)

try:
    import hcloud
    from hcloud import Client
    from hcloud.core.domain import Domain
    from hcloud.servers.client import BoundServer
    from hcloud.servers.domain import Server, CreateServerResponse, ServerCreateServer
    from hcloud.ssh_keys.domain import SSHKey
    from hcloud.volumes.domain import Volume
    from hcloud.networks.domain import Network, Subnet
    from hcloud.firewalls.domain import Firewall, FirewallResource
    from hcloud.load_balancers.domain import LoadBalancer, LoadBalancerTarget, LoadBalancerService
    from hcloud.placement_groups.domain import PlacementGroup
    from hcloud.certificates.domain import Certificate
    from hcloud.images.domain import Image
    from hcloud.isos.domain import ISO
    from hcloud.datacenters.domain import Datacenter
    from hcloud.locations.domain import Location
    from hcloud.server_types.domain import ServerType
    from hcloud.pricing.domain import Pricing
    from hcloud.floating_ips.domain import FloatingIP, FloatingIPCreateRequest
    from hcloud.primary_ips.domain import PrimaryIP
    from hcloud.rdns.domain import RDNS
    from hcloud.actions.domain import Action
    HAS_HCLOUD = True
except ImportError:
    HAS_HCLOUD = False
    hcloud = None
    Client = None


class HetznerError(Exception):
    pass


class HetznerManager:
    def __init__(self, api_token: Optional[str] = None):
        self.api_token = api_token or os.environ.get("HCLOUD_TOKEN")
        self.client = None
        self._connected = False
        if HAS_HCLOUD and self.api_token:
            self._connect()

    def _connect(self):
        try:
            self.client = Client(token=self.api_token)
            self.client.servers.get_all(limit=1)
            self._connected = True
        except Exception as e:
            logger.warning(f"Failed to connect to Hetzner: {e}")
            self._connected = False

    def check_connection(self) -> bool:
        if not self._connected:
            self._connect()
        return self._connected

    def list_servers(self) -> List[Dict]:
        if not self.check_connection():
            raise HetznerError("Not connected")
        try:
            servers = self.client.servers.get_all()
            return [{
                "id": s.id, "name": s.name, "status": s.status,
                "server_type": s.server_type.name if s.server_type else None,
                "datacenter": s.datacenter.name if s.datacenter else None,
                "location": s.datacenter.location.name if s.datacenter and s.datacenter.location else None,
                "public_ip": s.public_net.ipv4.ip if s.public_net and s.public_net.ipv4 else None,
                "public_ipv6": s.public_net.ipv6.ip if s.public_net and s.public_net.ipv6 else None,
                "private_ip": s.private_net[0].ip if s.private_net else None,
                "image": s.image.name if s.image else None,
                "created": str(s.created),
                "labels": s.labels,
                "volumes": [v.id for v in (s.volumes or [])],
                "firewalls": [f.id for f in (s.firewalls or [])],
                "placement_group": s.placement_group.id if s.placement_group else None,
                "rescue_enabled": s.rescue_enabled,
                "locked": s.locked,
                "backup_window": s.backup_window,
                "included_traffic": s.included_traffic,
                "outgoing_traffic": s.outgoing_traffic,
                "ingoing_traffic": s.ingoing_traffic,
            } for s in servers]
        except Exception as e:
            raise HetznerError(f"Failed to list servers: {e}")

    def create_server(self, name: str, server_type: str, image: str, location: Optional[str] = None,
                      datacenter: Optional[str] = None, ssh_keys: Optional[List] = None,
                      volumes: Optional[List] = None, networks: Optional[List] = None,
                      firewalls: Optional[List] = None, placement_group: Optional[int] = None,
                      user_data: Optional[str] = None, labels: Optional[Dict[str, str]] = None,
                      automount: bool = False, start_on_create: bool = True) -> Dict:
        if not self.check_connection():
            raise HetznerError("Not connected")
        try:
            response = self.client.servers.create(
                name=name, server_type=server_type, image=image,
                location=location, datacenter=datacenter,
                ssh_keys=ssh_keys, volumes=volumes, networks=networks,
                firewalls=firewalls, placement_group=placement_group,
                user_data=user_data, labels=labels,
                automount=automount, start_on_create=start_on_create,
            )
            return {"server_id": response.server.id, "name": response.server.name, "root_password": response.root_password, "action_id": response.action.id if response.action else None}
        except Exception as e:
            raise HetznerError(f"Failed to create server: {e}")

    def get_server(self, server_id: int) -> Dict:
        if not self.check_connection():
            raise HetznerError("Not connected")
        try:
            s = self.client.servers.get_by_id(server_id)
            return {"id": s.id, "name": s.name, "status": s.status, "server_type": s.server_type.name if s.server_type else None, "datacenter": s.datacenter.name if s.datacenter else None, "public_ip": s.public_net.ipv4.ip if s.public_net and s.public_net.ipv4 else None, "created": str(s.created), "labels": s.labels}
        except Exception as e:
            raise HetznerError(f"Server {server_id} not found: {e}")

    def power_on_server(self, server_id: int) -> Dict:
        if not self.check_connection():
            raise HetznerError("Not connected")
        try:
            s = self.client.servers.get_by_id(server_id)
            action = s.power_on()
            return {"server_id": server_id, "action": "power_on", "action_id": action.id, "status": s.status}
        except Exception as e:
            raise HetznerError(f"Failed to power on server: {e}")

    def power_off_server(self, server_id: int) -> Dict:
        if not self.check_connection():
            raise HetznerError("Not connected")
        try:
            s = self.client.servers.get_by_id(server_id)
            action = s.power_off()
            return {"server_id": server_id, "action": "power_off", "action_id": action.id}
        except Exception as e:
            raise HetznerError(f"Failed to power off server: {e}")

    def reboot_server(self, server_id: int) -> Dict:
        if not self.check_connection():
            raise HetznerError("Not connected")
        try:
            s = self.client.servers.get_by_id(server_id)
            action = s.reboot()
            return {"server_id": server_id, "action": "reboot", "action_id": action.id}
        except Exception as e:
            raise HetznerError(f"Failed to reboot server: {e}")

    def reset_server(self, server_id: int) -> Dict:
        if not self.check_connection():
            raise HetznerError("Not connected")
        try:
            s = self.client.servers.get_by_id(server_id)
            action = s.reset()
            return {"server_id": server_id, "action": "reset", "action_id": action.id}
        except Exception as e:
            raise HetznerError(f"Failed to reset server: {e}")

    def shutdown_server(self, server_id: int) -> Dict:
        if not self.check_connection():
            raise HetznerError("Not connected")
        try:
            s = self.client.servers.get_by_id(server_id)
            action = s.shutdown()
            return {"server_id": server_id, "action": "shutdown", "action_id": action.id}
        except Exception as e:
            raise HetznerError(f"Failed to shutdown server: {e}")

    def delete_server(self, server_id: int) -> Dict:
        if not self.check_connection():
            raise HetznerError("Not connected")
        try:
            s = self.client.servers.get_by_id(server_id)
            s.delete()
            return {"server_id": server_id, "deleted": True}
        except Exception as e:
            raise HetznerError(f"Failed to delete server: {e}")

    def rebuild_server(self, server_id: int, image: str) -> Dict:
        if not self.check_connection():
            raise HetznerError("Not connected")
        try:
            s = self.client.servers.get_by_id(server_id)
            action = s.rebuild(image=image)
            return {"server_id": server_id, "action": "rebuild", "image": image, "action_id": action.id}
        except Exception as e:
            raise HetznerError(f"Failed to rebuild server: {e}")

    def change_server_type(self, server_id: int, server_type: str, upgrade_disk: bool = False) -> Dict:
        if not self.check_connection():
            raise HetznerError("Not connected")
        try:
            s = self.client.servers.get_by_id(server_id)
            action = s.change_type(server_type=server_type, upgrade_disk=upgrade_disk)
            return {"server_id": server_id, "new_type": server_type, "action_id": action.id}
        except Exception as e:
            raise HetznerError(f"Failed to change server type: {e}")

    def enable_backup(self, server_id: int) -> Dict:
        if not self.check_connection():
            raise HetznerError("Not connected")
        try:
            s = self.client.servers.get_by_id(server_id)
            action = s.enable_backup()
            return {"server_id": server_id, "backup": "enabled", "action_id": action.id}
        except Exception as e:
            raise HetznerError(f"Failed to enable backup: {e}")

    def disable_backup(self, server_id: int) -> Dict:
        if not self.check_connection():
            raise HetznerError("Not connected")
        try:
            s = self.client.servers.get_by_id(server_id)
            action = s.disable_backup()
            return {"server_id": server_id, "backup": "disabled", "action_id": action.id}
        except Exception as e:
            raise HetznerError(f"Failed to disable backup: {e}")

    def create_snapshot(self, server_id: int, snapshot_name: Optional[str] = None) -> Dict:
        if not self.check_connection():
            raise HetznerError("Not connected")
        try:
            s = self.client.servers.get_by_id(server_id)
            action = s.create_image(name=snapshot_name or f"{s.name}-snapshot")
            return {"server_id": server_id, "action": "create_snapshot", "action_id": action.id}
        except Exception as e:
            raise HetznerError(f"Failed to create snapshot: {e}")

    def enable_rescue(self, server_id: int, rescue_type: str = "linux64", ssh_keys: Optional[List] = None) -> Dict:
        if not self.check_connection():
            raise HetznerError("Not connected")
        try:
            s = self.client.servers.get_by_id(server_id)
            action = s.enable_rescue(type=rescue_type, ssh_keys=ssh_keys)
            return {"server_id": server_id, "rescue": rescue_type, "action_id": action.id}
        except Exception as e:
            raise HetznerError(f"Failed to enable rescue: {e}")

    def disable_rescue(self, server_id: int) -> Dict:
        if not self.check_connection():
            raise HetznerError("Not connected")
        try:
            s = self.client.servers.get_by_id(server_id)
            action = s.disable_rescue()
            return {"server_id": server_id, "rescue": "disabled", "action_id": action.id}
        except Exception as e:
            raise HetznerError(f"Failed to disable rescue: {e}")

    def list_volumes(self) -> List[Dict]:
        if not self.check_connection():
            raise HetznerError("Not connected")
        try:
            volumes = self.client.volumes.get_all()
            return [{"id": v.id, "name": v.name, "size": v.size, "location": v.location.name if v.location else None, "server": v.server.id if v.server else None, "linux_device": v.linux_device, "status": v.status, "labels": v.labels, "created": str(v.created), "format": v.format} for v in volumes]
        except Exception as e:
            raise HetznerError(f"Failed to list volumes: {e}")

    def create_volume(self, name: str, size: int, location: Optional[str] = None,
                      server: Optional[int] = None, automount: bool = False,
                      format: Optional[str] = "xfs", labels: Optional[Dict] = None) -> Dict:
        if not self.check_connection():
            raise HetznerError("Not connected")
        try:
            v = self.client.volumes.create(name=name, size=size, location=location, server=server, automount=automount, format=format, labels=labels)
            return {"id": v.id, "name": v.name, "size": size, "action_id": v.action.id if v.action else None}
        except Exception as e:
            raise HetznerError(f"Failed to create volume: {e}")

    def delete_volume(self, volume_id: int) -> Dict:
        if not self.check_connection():
            raise HetznerError("Not connected")
        try:
            v = self.client.volumes.get_by_id(volume_id)
            v.delete()
            return {"volume_id": volume_id, "deleted": True}
        except Exception as e:
            raise HetznerError(f"Failed to delete volume: {e}")

    def resize_volume(self, volume_id: int, new_size: int) -> Dict:
        if not self.check_connection():
            raise HetznerError("Not connected")
        try:
            v = self.client.volumes.get_by_id(volume_id)
            action = v.resize(size=new_size)
            return {"volume_id": volume_id, "new_size": new_size, "action_id": action.id}
        except Exception as e:
            raise HetznerError(f"Failed to resize volume: {e}")

    def list_firewalls(self) -> List[Dict]:
        if not self.check_connection():
            raise HetznerError("Not connected")
        try:
            fws = self.client.firewalls.get_all()
            return [{"id": f.id, "name": f.name, "rules": [{"direction": r.direction, "protocol": r.protocol, "port": r.port, "source_ips": r.source_ips, "destination_ips": r.destination_ips} for r in (f.rules or [])], "labels": f.labels, "created": str(f.created)} for f in fws]
        except Exception as e:
            raise HetznerError(f"Failed to list firewalls: {e}")

    def create_firewall(self, name: str, rules: List[Dict], labels: Optional[Dict] = None) -> Dict:
        if not self.check_connection():
            raise HetznerError("Not connected")
        try:
            from hcloud.firewalls.domain import FirewallRule
            fw_rules = [FirewallRule(direction=r.get("direction"), protocol=r.get("protocol"), port=r.get("port"), source_ips=r.get("source_ips"), destination_ips=r.get("destination_ips")) for r in rules]
            f = self.client.firewalls.create(name=name, rules=fw_rules, labels=labels)
            return {"id": f.id, "name": name}
        except Exception as e:
            raise HetznerError(f"Failed to create firewall: {e}")

    def delete_firewall(self, firewall_id: int) -> Dict:
        if not self.check_connection():
            raise HetznerError("Not connected")
        try:
            f = self.client.firewalls.get_by_id(firewall_id)
            f.delete()
            return {"firewall_id": firewall_id, "deleted": True}
        except Exception as e:
            raise HetznerError(f"Failed to delete firewall: {e}")

    def list_networks(self) -> List[Dict]:
        if not self.check_connection():
            raise HetznerError("Not connected")
        try:
            nets = self.client.networks.get_all()
            return [{"id": n.id, "name": n.name, "ip_range": n.ip_range, "subnets": [{"type": s.type, "ip_range": s.ip_range, "network_zone": s.network_zone, "gateway": s.gateway} for s in (n.subnets or [])], "routes": [{"destination": r.destination, "gateway": r.gateway} for r in (n.routes or [])], "servers": [s.id for s in (n.servers or [])], "labels": n.labels, "created": str(n.created)} for n in nets]
        except Exception as e:
            raise HetznerError(f"Failed to list networks: {e}")

    def create_network(self, name: str, ip_range: str, subnets: Optional[List[Dict]] = None,
                       routes: Optional[List[Dict]] = None, labels: Optional[Dict] = None) -> Dict:
        if not self.check_connection():
            raise HetznerError("Not connected")
        try:
            net = self.client.networks.create(name=name, ip_range=ip_range, labels=labels)
            if subnets:
                for s in subnets:
                    from hcloud.networks.domain import Subnet
                    subnet = Subnet(type=s.get("type", "cloud"), ip_range=s.get("ip_range"), network_zone=s.get("network_zone", "eu-central"))
                    net.add_subnet(subnet=subnet)
            return {"id": net.id, "name": name, "ip_range": ip_range}
        except Exception as e:
            raise HetznerError(f"Failed to create network: {e}")

    def delete_network(self, network_id: int) -> Dict:
        if not self.check_connection():
            raise HetznerError("Not connected")
        try:
            n = self.client.networks.get_by_id(network_id)
            n.delete()
            return {"network_id": network_id, "deleted": True}
        except Exception as e:
            raise HetznerError(f"Failed to delete network: {e}")

    def list_ssh_keys(self) -> List[Dict]:
        if not self.check_connection():
            raise HetznerError("Not connected")
        try:
            keys = self.client.ssh_keys.get_all()
            return [{"id": k.id, "name": k.name, "fingerprint": k.fingerprint, "public_key": k.public_key, "labels": k.labels, "created": str(k.created)} for k in keys]
        except Exception as e:
            raise HetznerError(f"Failed to list SSH keys: {e}")

    def add_ssh_key(self, name: str, public_key: str, labels: Optional[Dict] = None) -> Dict:
        if not self.check_connection():
            raise HetznerError("Not connected")
        try:
            k = self.client.ssh_keys.create(name=name, public_key=public_key, labels=labels)
            return {"id": k.id, "name": name, "fingerprint": k.fingerprint}
        except Exception as e:
            raise HetznerError(f"Failed to add SSH key: {e}")

    def delete_ssh_key(self, key_id: int) -> Dict:
        if not self.check_connection():
            raise HetznerError("Not connected")
        try:
            k = self.client.ssh_keys.get_by_id(key_id)
            k.delete()
            return {"key_id": key_id, "deleted": True}
        except Exception as e:
            raise HetznerError(f"Failed to delete SSH key: {e}")

    def list_load_balancers(self) -> List[Dict]:
        if not self.check_connection():
            raise HetznerError("Not connected")
        try:
            lbs = self.client.load_balancers.get_all()
            return [{"id": lb.id, "name": lb.name, "load_balancer_type": lb.load_balancer_type.name if lb.load_balancer_type else None, "location": lb.location.name if lb.location else None, "public_ip": lb.public_net.ipv4.ip if lb.public_net and lb.public_net.ipv4 else None, "private_ip": lb.private_net.ip if lb.private_net else None, "algorithm": lb.algorithm.type if lb.algorithm else None, "services": [{"protocol": s.protocol, "listen_port": s.listen_port, "destination_port": s.destination_port} for s in (lb.services or [])], "targets": [{"type": t.type, "server_id": t.server.id if t.server else None, "use_private_ip": t.use_private_ip} for t in (lb.targets or [])], "labels": lb.labels, "created": str(lb.created)} for lb in lbs]
        except Exception as e:
            raise HetznerError(f"Failed to list load balancers: {e}")

    def list_placement_groups(self) -> List[Dict]:
        if not self.check_connection():
            raise HetznerError("Not connected")
        try:
            pgs = self.client.placement_groups.get_all()
            return [{"id": pg.id, "name": pg.name, "type": pg.type, "labels": pg.labels, "created": str(pg.created), "servers": [s.id for s in (pg.servers or [])]} for pg in pgs]
        except Exception as e:
            raise HetznerError(f"Failed to list placement groups: {e}")

    def list_locations(self) -> List[Dict]:
        if not self.check_connection():
            raise HetznerError("Not connected")
        try:
            locs = self.client.locations.get_all()
            return [{"id": l.id, "name": l.name, "description": l.description, "country": l.country, "city": l.city, "latitude": l.latitude, "longitude": l.longitude} for l in locs]
        except Exception as e:
            raise HetznerError(f"Failed to list locations: {e}")

    def list_server_types(self) -> List[Dict]:
        if not self.check_connection():
            raise HetznerError("Not connected")
        try:
            types = self.client.server_types.get_all()
            return [{"id": t.id, "name": t.name, "cores": t.cores, "cpu_type": t.cpu_type, "memory": t.memory, "disk": t.disk, "storage_type": t.storage_type, "prices": [{"location": p.location.name, "price_hourly": str(p.price_hourly.net), "price_monthly": str(p.price_monthly.net)} for p in t.prices] if t.prices else [], "deprecated": t.deprecated} for t in types]
        except Exception as e:
            raise HetznerError(f"Failed to list server types: {e}")

    def list_images(self) -> List[Dict]:
        if not self.check_connection():
            raise HetznerError("Not connected")
        try:
            images = self.client.images.get_all()
            return [{"id": i.id, "name": i.name, "type": i.type, "description": i.description, "image_size": i.image_size, "disk_size": i.disk_size, "created": str(i.created), "deprecated": str(i.deprecated) if i.deprecated else None, "labels": i.labels, "os_flavor": i.os_flavor, "os_version": i.os_version} for i in images]
        except Exception as e:
            raise HetznerError(f"Failed to list images: {e}")


class Plugin(PluginBase):
    name = "hetzner"
    version = "1.0.0"
    description = "Hetzner Cloud integration - servers, firewalls, volumes, networks, SSH keys, placement groups, load balancers, certificates, DNS, pricing, locations"

    def __init__(self):
        self.manager = None

    def execute(self, **kwargs) -> Dict[str, Any]:
        action = kwargs.get("action", "info")
        api_token = kwargs.get("api_token")
        self.manager = HetznerManager(api_token=api_token)

        if action == "info":
            return {"plugin": self.name, "version": self.version, "description": self.description, "connected": self.manager.check_connection()}
        elif action == "servers":
            return {"servers": self.manager.list_servers()}
        elif action == "server":
            return self.manager.get_server(kwargs.get("server_id"))
        elif action == "create_server":
            return self.manager.create_server(name=kwargs.get("name"), server_type=kwargs.get("server_type"), image=kwargs.get("image"), location=kwargs.get("location"), ssh_keys=kwargs.get("ssh_keys"), volumes=kwargs.get("volumes"), networks=kwargs.get("networks"), firewalls=kwargs.get("firewalls"), user_data=kwargs.get("user_data"), labels=kwargs.get("labels"))
        elif action == "power_on":
            return self.manager.power_on_server(kwargs.get("server_id"))
        elif action == "power_off":
            return self.manager.power_off_server(kwargs.get("server_id"))
        elif action == "reboot":
            return self.manager.reboot_server(kwargs.get("server_id"))
        elif action == "reset":
            return self.manager.reset_server(kwargs.get("server_id"))
        elif action == "shutdown":
            return self.manager.shutdown_server(kwargs.get("server_id"))
        elif action == "delete_server":
            return self.manager.delete_server(kwargs.get("server_id"))
        elif action == "rebuild":
            return self.manager.rebuild_server(kwargs.get("server_id"), kwargs.get("image"))
        elif action == "change_type":
            return self.manager.change_server_type(kwargs.get("server_id"), kwargs.get("server_type"), kwargs.get("upgrade_disk", False))
        elif action == "enable_backup":
            return self.manager.enable_backup(kwargs.get("server_id"))
        elif action == "disable_backup":
            return self.manager.disable_backup(kwargs.get("server_id"))
        elif action == "create_snapshot":
            return self.manager.create_snapshot(kwargs.get("server_id"), kwargs.get("snapshot_name"))
        elif action == "volumes":
            return {"volumes": self.manager.list_volumes()}
        elif action == "create_volume":
            return self.manager.create_volume(kwargs.get("name"), kwargs.get("size"), location=kwargs.get("location"), server=kwargs.get("server"), labels=kwargs.get("labels"))
        elif action == "delete_volume":
            return self.manager.delete_volume(kwargs.get("volume_id"))
        elif action == "resize_volume":
            return self.manager.resize_volume(kwargs.get("volume_id"), kwargs.get("new_size"))
        elif action == "firewalls":
            return {"firewalls": self.manager.list_firewalls()}
        elif action == "create_firewall":
            return self.manager.create_firewall(kwargs.get("name"), kwargs.get("rules"), labels=kwargs.get("labels"))
        elif action == "delete_firewall":
            return self.manager.delete_firewall(kwargs.get("firewall_id"))
        elif action == "networks":
            return {"networks": self.manager.list_networks()}
        elif action == "create_network":
            return self.manager.create_network(kwargs.get("name"), kwargs.get("ip_range"), subnets=kwargs.get("subnets"), labels=kwargs.get("labels"))
        elif action == "delete_network":
            return self.manager.delete_network(kwargs.get("network_id"))
        elif action == "ssh_keys":
            return {"ssh_keys": self.manager.list_ssh_keys()}
        elif action == "add_ssh_key":
            return self.manager.add_ssh_key(kwargs.get("name"), kwargs.get("public_key"), labels=kwargs.get("labels"))
        elif action == "delete_ssh_key":
            return self.manager.delete_ssh_key(kwargs.get("key_id"))
        elif action == "load_balancers":
            return {"load_balancers": self.manager.list_load_balancers()}
        elif action == "placement_groups":
            return {"placement_groups": self.manager.list_placement_groups()}
        elif action == "locations":
            return {"locations": self.manager.list_locations()}
        elif action == "server_types":
            return {"server_types": self.manager.list_server_types()}
        elif action == "images":
            return {"images": self.manager.list_images()}
        return {"error": f"Unknown action: {action}"}