"""Proxmox plugin for Infra Pilot - QEMU/KVM VMs, LXC containers, storage, networks, nodes, clusters, pools, users, ACLs, backups, snapshots, templates, ISO images, firewall, HA groups, metrics, replication, vzdump, tasks, logs, system resources"""

import logging
from typing import Any, Dict, List, Optional
from plugins import PluginBase

logger = logging.getLogger(__name__)

try:
    from proxmoxer import ProxmoxAPI
    from proxmoxer.backends.https import AuthenticationError
    HAS_PROXMOX = True
except ImportError:
    HAS_PROXMOX = False
    ProxmoxAPI = None
    AuthenticationError = Exception


class ProxmoxError(Exception):
    pass


class ProxmoxManager:
    def __init__(self, host: str, user: str, password: Optional[str] = None, token_name: Optional[str] = None, token_value: Optional[str] = None, verify_ssl: bool = True, port: int = 8006):
        self.host = host
        self.user = user
        self.password = password
        self.token_name = token_name
        self.token_value = token_value
        self.verify_ssl = verify_ssl
        self.port = port
        self.proxmox = None
        self._connected = False
        if HAS_PROXMOX:
            self._connect()

    def _connect(self):
        try:
            if self.token_name and self.token_value:
                self.proxmox = ProxmoxAPI(host=self.host, user=self.user, token_name=self.token_name, token_value=self.token_value, verify_ssl=self.verify_ssl, port=self.port)
            else:
                self.proxmox = ProxmoxAPI(host=self.host, user=self.user, password=self.password, verify_ssl=self.verify_ssl, port=self.port)
            self.proxmox.version.get()
            self._connected = True
        except Exception as e:
            logger.warning(f"Failed to connect to Proxmox: {e}")
            self._connected = False

    def check_connection(self) -> bool:
        if not self._connected:
            self._connect()
        return self._connected

    def get_version(self) -> Dict:
        if not self.check_connection():
            raise ProxmoxError("Not connected")
        try:
            return self.proxmox.version.get()
        except Exception as e:
            raise ProxmoxError(f"Failed to get version: {e}")

    def list_nodes(self) -> List[Dict]:
        if not self.check_connection():
            raise ProxmoxError("Not connected")
        try:
            nodes = self.proxmox.nodes.get()
            return [{
                "node": n["node"], "status": n.get("status"), "type": n.get("type"),
                "cpu": n.get("cpu"), "maxcpu": n.get("maxcpu"),
                "mem": n.get("mem"), "maxmem": n.get("maxmem"),
                "disk": n.get("disk"), "maxdisk": n.get("maxdisk"),
                "uptime": n.get("uptime"), "id": n.get("id"),
                "ssl_fingerprint": n.get("ssl_fingerprint"),
                "level": n.get("level"),
            } for n in nodes]
        except Exception as e:
            raise ProxmoxError(f"Failed to list nodes: {e}")

    def get_node_status(self, node: str) -> Dict:
        if not self.check_connection():
            raise ProxmoxError("Not connected")
        try:
            status = self.proxmox.nodes(node).status.get()
            return {
                "node": node, "cpu": status.get("cpu"), "memory_used": status.get("memory", {}).get("used"),
                "memory_total": status.get("memory", {}).get("total"), "uptime": status.get("uptime"),
                "kvm": status.get("kvm"), "ksm": status.get("ksm"),
                "loadavg": status.get("loadavg", []),
                "swap_used": status.get("swap", {}).get("used"), "swap_total": status.get("swap", {}).get("total"),
                "rootfs_used": status.get("rootfs", {}).get("used"), "rootfs_total": status.get("rootfs", {}).get("total"),
            }
        except Exception as e:
            raise ProxmoxError(f"Failed to get node status: {e}")

    def list_qemu_vms(self, node: str) -> List[Dict]:
        if not self.check_connection():
            raise ProxmoxError("Not connected")
        try:
            vms = self.proxmox.nodes(node).qemu.get()
            return [{
                "vmid": vm["vmid"], "name": vm.get("name"), "status": vm.get("status"),
                "mem": vm.get("mem"), "maxmem": vm.get("maxmem"),
                "cpu": vm.get("cpu"), "maxcpu": vm.get("maxcpu"),
                "disk": vm.get("disk"), "maxdisk": vm.get("maxdisk"),
                "uptime": vm.get("uptime"), "pid": vm.get("pid"),
                "tags": (vm.get("tags") or "").split(";") if vm.get("tags") else [],
                "template": vm.get("template", 0),
                "ha": vm.get("ha", {}).get("state"),
                "cpus": vm.get("cpus"),
                "lock": vm.get("lock"),
            } for vm in vms]
        except Exception as e:
            raise ProxmoxError(f"Failed to list QEMU VMs: {e}")

    def get_qemu_vm(self, node: str, vmid: int) -> Dict:
        if not self.check_connection():
            raise ProxmoxError("Not connected")
        try:
            config = self.proxmox.nodes(node).qemu(vmid).config.get()
            status = self.proxmox.nodes(node).qemu(vmid).status.current.get()
            return {"vmid": vmid, "name": config.get("name"), "config": config, "status": status}
        except Exception as e:
            raise ProxmoxError(f"Failed to get VM {vmid}: {e}")

    def create_qemu_vm(self, node: str, vmid: Optional[int] = None, name: str = "",
                       memory: int = 512, cores: int = 1, sockets: int = 1,
                       disk_size: str = "8G", storage: str = "local-lvm",
                       net_model: str = "virtio", bridge: str = "vmbr0",
                       iso: Optional[str] = None, template: bool = False,
                       ostype: str = "l26", scsihw: str = "virtio-scsi-pci",
                       agent: int = 1, pool: Optional[str] = None,
                       tags: Optional[str] = None, start: bool = True) -> Dict:
        if not self.check_connection():
            raise ProxmoxError("Not connected")
        try:
            data = {"name": name, "memory": memory, "cores": cores, "sockets": sockets, "ostype": ostype, "scsihw": scsihw, "agent": agent, "net0": f"{net_model},bridge={bridge}"}
            data["virtio0"] = f"{storage}:{disk_size}"
            if vmid:
                data["vmid"] = vmid
            if iso:
                data["cdrom"] = f"local:iso/{iso},media=cdrom"
            if pool:
                data["pool"] = pool
            if tags:
                data["tags"] = tags
            result = self.proxmox.nodes(node).qemu.post(**data)
            task_id = result.get("data")
            if start and not template:
                self.proxmox.nodes(node).qemu(vmid or result.get("data")).status.start.post()
            return {"vmid": vmid or result.get("data"), "name": name, "task_id": task_id, "started": start}
        except Exception as e:
            raise ProxmoxError(f"Failed to create VM: {e}")

    def start_qemu_vm(self, node: str, vmid: int) -> Dict:
        if not self.check_connection():
            raise ProxmoxError("Not connected")
        try:
            result = self.proxmox.nodes(node).qemu(vmid).status.start.post()
            return {"vmid": vmid, "action": "start", "task_id": result.get("data")}
        except Exception as e:
            raise ProxmoxError(f"Failed to start VM {vmid}: {e}")

    def stop_qemu_vm(self, node: str, vmid: int) -> Dict:
        if not self.check_connection():
            raise ProxmoxError("Not connected")
        try:
            result = self.proxmox.nodes(node).qemu(vmid).status.stop.post()
            return {"vmid": vmid, "action": "stop", "task_id": result.get("data")}
        except Exception as e:
            raise ProxmoxError(f"Failed to stop VM {vmid}: {e}")

    def shutdown_qemu_vm(self, node: str, vmid: int) -> Dict:
        if not self.check_connection():
            raise ProxmoxError("Not connected")
        try:
            result = self.proxmox.nodes(node).qemu(vmid).status.shutdown.post()
            return {"vmid": vmid, "action": "shutdown", "task_id": result.get("data")}
        except Exception as e:
            raise ProxmoxError(f"Failed to shutdown VM {vmid}: {e}")

    def reset_qemu_vm(self, node: str, vmid: int) -> Dict:
        if not self.check_connection():
            raise ProxmoxError("Not connected")
        try:
            result = self.proxmox.nodes(node).qemu(vmid).status.reset.post()
            return {"vmid": vmid, "action": "reset", "task_id": result.get("data")}
        except Exception as e:
            raise ProxmoxError(f"Failed to reset VM {vmid}: {e}")

    def suspend_qemu_vm(self, node: str, vmid: int) -> Dict:
        if not self.check_connection():
            raise ProxmoxError("Not connected")
        try:
            result = self.proxmox.nodes(node).qemu(vmid).status.suspend.post()
            return {"vmid": vmid, "action": "suspend", "task_id": result.get("data")}
        except Exception as e:
            raise ProxmoxError(f"Failed to suspend VM {vmid}: {e}")

    def resume_qemu_vm(self, node: str, vmid: int) -> Dict:
        if not self.check_connection():
            raise ProxmoxError("Not connected")
        try:
            result = self.proxmox.nodes(node).qemu(vmid).status.resume.post()
            return {"vmid": vmid, "action": "resume", "task_id": result.get("data")}
        except Exception as e:
            raise ProxmoxError(f"Failed to resume VM {vmid}: {e}")

    def delete_qemu_vm(self, node: str, vmid: int, destroy_unreferenced_disks: bool = True, purge: bool = True) -> Dict:
        if not self.check_connection():
            raise ProxmoxError("Not connected")
        try:
            result = self.proxmox.nodes(node).qemu(vmid).delete()
            return {"vmid": vmid, "action": "delete", "task_id": result.get("data")}
        except Exception as e:
            raise ProxmoxError(f"Failed to delete VM {vmid}: {e}")

    def create_qemu_snapshot(self, node: str, vmid: int, snapname: str, description: Optional[str] = None, vmstate: bool = True) -> Dict:
        if not self.check_connection():
            raise ProxmoxError("Not connected")
        try:
            data = {"snapname": snapname, "vmstate": vmstate}
            if description:
                data["description"] = description
            result = self.proxmox.nodes(node).qemu(vmid).snapshot.post(**data)
            return {"vmid": vmid, "snapshot": snapname, "task_id": result.get("data")}
        except Exception as e:
            raise ProxmoxError(f"Failed to create snapshot: {e}")

    def rollback_qemu_vm(self, node: str, vmid: int, snapname: str) -> Dict:
        if not self.check_connection():
            raise ProxmoxError("Not connected")
        try:
            result = self.proxmox.nodes(node).qemu(vmid).snapshot(snapname).rollback.post()
            return {"vmid": vmid, "snapshot": snapname, "action": "rollback", "task_id": result.get("data")}
        except Exception as e:
            raise ProxmoxError(f"Failed to rollback VM: {e}")

    def list_qemu_snapshots(self, node: str, vmid: int) -> List[Dict]:
        if not self.check_connection():
            raise ProxmoxError("Not connected")
        try:
            snaps = self.proxmox.nodes(node).qemu(vmid).snapshot.get()
            return [{"name": s.get("name"), "description": s.get("description"), "snaptime": s.get("snaptime"), "vmstate": s.get("vmstate"), "parent": s.get("parent"), "children": s.get("children", [])} for s in snaps if s.get("name") != "current"]
        except Exception as e:
            raise ProxmoxError(f"Failed to list snapshots: {e}")

    def delete_qemu_snapshot(self, node: str, vmid: int, snapname: str) -> Dict:
        if not self.check_connection():
            raise ProxmoxError("Not connected")
        try:
            result = self.proxmox.nodes(node).qemu(vmid).snapshot(snapname).delete()
            return {"vmid": vmid, "snapshot": snapname, "deleted": True, "task_id": result.get("data")}
        except Exception as e:
            raise ProxmoxError(f"Failed to delete snapshot: {e}")

    def migrate_qemu_vm(self, node: str, vmid: int, target_node: str, online: bool = True) -> Dict:
        if not self.check_connection():
            raise ProxmoxError("Not connected")
        try:
            result = self.proxmox.nodes(node).qemu(vmid).migrate.post(target=target_node, online=int(online))
            return {"vmid": vmid, "target": target_node, "online": online, "task_id": result.get("data")}
        except Exception as e:
            raise ProxmoxError(f"Failed to migrate VM: {e}")

    def template_qemu_vm(self, node: str, vmid: int) -> Dict:
        if not self.check_connection():
            raise ProxmoxError("Not connected")
        try:
            result = self.proxmox.nodes(node).qemu(vmid).template.post()
            return {"vmid": vmid, "template": True, "task_id": result.get("data")}
        except Exception as e:
            raise ProxmoxError(f"Failed to convert to template: {e}")

    def list_lxc_containers(self, node: str) -> List[Dict]:
        if not self.check_connection():
            raise ProxmoxError("Not connected")
        try:
            ctns = self.proxmox.nodes(node).lxc.get()
            return [{"vmid": c["vmid"], "name": c.get("name"), "status": c.get("status"), "mem": c.get("mem"), "maxmem": c.get("maxmem"), "cpu": c.get("cpu"), "maxcpu": c.get("maxcpu"), "disk": c.get("disk"), "maxdisk": c.get("maxdisk"), "uptime": c.get("uptime"), "tags": (c.get("tags") or "").split(";") if c.get("tags") else [], "template": c.get("template", 0), "cpus": c.get("cpus"), "lock": c.get("lock"), "ha": c.get("ha", {}).get("state")} for c in ctns]
        except Exception as e:
            raise ProxmoxError(f"Failed to list LXC containers: {e}")

    def create_lxc_container(self, node: str, vmid: Optional[int] = None, hostname: str = "",
                             ostemplate: str = "local:vztmpl/ubuntu-22.04-standard_22.04-1_amd64.tar.zst",
                             storage: str = "local-lvm", rootfs_size: str = "8G",
                             memory: int = 512, cores: int = 1, swap: int = 0,
                             net_bridge: str = "vmbr0", password: Optional[str] = None,
                             ssh_public_keys: Optional[str] = None, start: bool = True,
                             pool: Optional[str] = None, unprivileged: bool = True,
                             features: Optional[str] = None, nameserver: Optional[str] = None,
                             searchdomain: Optional[str] = None, tags: Optional[str] = None) -> Dict:
        if not self.check_connection():
            raise ProxmoxError("Not connected")
        try:
            data = {"hostname": hostname, "ostemplate": ostemplate, "storage": storage, "rootfs": rootfs_size, "memory": memory, "cores": cores, "swap": swap, "net0": f"name=eth0,bridge={net_bridge},ip=dhcp", "unprivileged": int(unprivileged)}
            if vmid:
                data["vmid"] = vmid
            if password:
                data["password"] = password
            if ssh_public_keys:
                data["ssh-public-keys"] = ssh_public_keys
            if pool:
                data["pool"] = pool
            if features:
                data["features"] = features
            if nameserver:
                data["nameserver"] = nameserver
            if searchdomain:
                data["searchdomain"] = searchdomain
            if tags:
                data["tags"] = tags
            result = self.proxmox.nodes(node).lxc.post(**data)
            return {"vmid": result.get("data"), "hostname": hostname, "task_id": result.get("data")}
        except Exception as e:
            raise ProxmoxError(f"Failed to create LXC container: {e}")

    def start_lxc_container(self, node: str, vmid: int) -> Dict:
        if not self.check_connection():
            raise ProxmoxError("Not connected")
        try:
            result = self.proxmox.nodes(node).lxc(vmid).status.start.post()
            return {"vmid": vmid, "action": "start", "task_id": result.get("data")}
        except Exception as e:
            raise ProxmoxError(f"Failed to start LXC {vmid}: {e}")

    def stop_lxc_container(self, node: str, vmid: int) -> Dict:
        if not self.check_connection():
            raise ProxmoxError("Not connected")
        try:
            result = self.proxmox.nodes(node).lxc(vmid).status.stop.post()
            return {"vmid": vmid, "action": "stop", "task_id": result.get("data")}
        except Exception as e:
            raise ProxmoxError(f"Failed to stop LXC {vmid}: {e}")

    def shutdown_lxc_container(self, node: str, vmid: int) -> Dict:
        if not self.check_connection():
            raise ProxmoxError("Not connected")
        try:
            result = self.proxmox.nodes(node).lxc(vmid).status.shutdown.post()
            return {"vmid": vmid, "action": "shutdown", "task_id": result.get("data")}
        except Exception as e:
            raise ProxmoxError(f"Failed to shutdown LXC {vmid}: {e}")

    def delete_lxc_container(self, node: str, vmid: int) -> Dict:
        if not self.check_connection():
            raise ProxmoxError("Not connected")
        try:
            result = self.proxmox.nodes(node).lxc(vmid).delete()
            return {"vmid": vmid, "action": "delete", "task_id": result.get("data")}
        except Exception as e:
            raise ProxmoxError(f"Failed to delete LXC {vmid}: {e}")

    def enter_lxc_container(self, node: str, vmid: int, command: str = "bash") -> Dict:
        if not self.check_connection():
            raise ProxmoxError("Not connected")
        try:
            result = self.proxmox.nodes(node).lxc(vmid).exec.post(command=command.split())
            return {"vmid": vmid, "command": command, "result": result.get("data")}
        except Exception as e:
            raise ProxmoxError(f"Failed to exec in LXC: {e}")

    def list_storage(self) -> List[Dict]:
        if not self.check_connection():
            raise ProxmoxError("Not connected")
        try:
            storage = self.proxmox.storage.get()
            return [{"storage": s.get("storage"), "type": s.get("type"), "content": s.get("content", "").split(",") if s.get("content") else [], "active": s.get("active"), "enabled": s.get("enabled"), "shared": s.get("shared"), "path": s.get("path"), "nodes": s.get("nodes", "").split(",") if s.get("nodes") else []} for s in storage]
        except Exception as e:
            raise ProxmoxError(f"Failed to list storage: {e}")

    def list_storage_content(self, storage: str, content_type: Optional[str] = None) -> List[Dict]:
        if not self.check_connection():
            raise ProxmoxError("Not connected")
        try:
            params = {}
            if content_type:
                params["content"] = content_type
            content = self.proxmox.nodes("").storage(storage).content.get(**params)
            return [{"volid": c.get("volid"), "format": c.get("format"), "size": c.get("size"), "content": c.get("content"), "name": c.get("name"), "ctime": c.get("ctime")} for c in content]
        except Exception as e:
            raise ProxmoxError(f"Failed to list storage content: {e}")

    def list_pools(self) -> List[Dict]:
        if not self.check_connection():
            raise ProxmoxError("Not connected")
        try:
            pools = self.proxmox.pools.get()
            return [{"poolid": p.get("poolid"), "comment": p.get("comment"), "members": p.get("members", [])} for p in pools]
        except Exception as e:
            raise ProxmoxError(f"Failed to list pools: {e}")

    def list_tasks(self, node: str, limit: int = 50) -> List[Dict]:
        if not self.check_connection():
            raise ProxmoxError("Not connected")
        try:
            tasks = self.proxmox.nodes(node).tasks.get(limit=limit)
            return [{"upid": t.get("upid"), "type": t.get("type"), "status": t.get("status"), "user": t.get("user"), "starttime": t.get("starttime"), "endtime": t.get("endtime"), "node": t.get("node"), "pid": t.get("pid"), "id": t.get("id")} for t in tasks]
        except Exception as e:
            raise ProxmoxError(f"Failed to list tasks: {e}")

    def get_cluster_status(self) -> Dict:
        if not self.check_connection():
            raise ProxmoxError("Not connected")
        try:
            status = self.proxmox.cluster.status.get()
            resources = self.proxmox.cluster.resources.get()
            return {"status": status, "resources": resources, "nodes": len(status)}
        except Exception as e:
            raise ProxmoxError(f"Failed to get cluster status: {e}")

    def list_cluster_resources(self, resource_type: Optional[str] = None) -> List[Dict]:
        if not self.check_connection():
            raise ProxmoxError("Not connected")
        try:
            params = {}
            if resource_type:
                params["type"] = resource_type
            resources = self.proxmox.cluster.resources.get(**params)
            return [{"id": r.get("id"), "type": r.get("type"), "node": r.get("node"), "status": r.get("status"), "cpu": r.get("cpu"), "mem": r.get("mem"), "disk": r.get("disk"), "maxcpu": r.get("maxcpu"), "maxmem": r.get("maxmem"), "maxdisk": r.get("maxdisk"), "name": r.get("name"), "vmid": r.get("vmid")} for r in resources]
        except Exception as e:
            raise ProxmoxError(f"Failed to list cluster resources: {e}")


class Plugin(PluginBase):
    name = "proxmox"
    version = "1.0.0"
    description = "Proxmox VE virtualization management - QEMU/KVM VMs, LXC containers, storage, networks, nodes, clusters, pools, backups, snapshots, templates, firewalls, HA groups, replication, tasks"

    def __init__(self):
        self.manager = None

    def execute(self, **kwargs) -> Dict[str, Any]:
        action = kwargs.get("action", "info")
        host = kwargs.get("host", "localhost")
        user = kwargs.get("user", "root@pam")
        password = kwargs.get("password")
        token_name = kwargs.get("token_name")
        token_value = kwargs.get("token_value")
        verify_ssl = kwargs.get("verify_ssl", True)
        port = kwargs.get("port", 8006)
        self.manager = ProxmoxManager(host=host, user=user, password=password, token_name=token_name, token_value=token_value, verify_ssl=verify_ssl, port=port)

        node = kwargs.get("node", "")
        vmid = kwargs.get("vmid")

        if action == "info":
            return {"plugin": self.name, "version": self.version, "description": self.description, "connected": self.manager.check_connection()}
        elif action == "version":
            return self.manager.get_version()
        elif action == "nodes":
            return {"nodes": self.manager.list_nodes()}
        elif action == "node_status":
            return self.manager.get_node_status(node)
        elif action == "qemu_vms":
            return {"vms": self.manager.list_qemu_vms(node)}
        elif action == "qemu_vm":
            return self.manager.get_qemu_vm(node, vmid)
        elif action == "create_qemu_vm":
            return self.manager.create_qemu_vm(node=node, vmid=vmid, name=kwargs.get("name", ""), memory=kwargs.get("memory", 512), cores=kwargs.get("cores", 1), disk_size=kwargs.get("disk_size", "8G"), storage=kwargs.get("storage", "local-lvm"), iso=kwargs.get("iso"), template=kwargs.get("template", False), pool=kwargs.get("pool"), tags=kwargs.get("tags"), start=kwargs.get("start", True))
        elif action == "start_qemu_vm":
            return self.manager.start_qemu_vm(node, vmid)
        elif action == "stop_qemu_vm":
            return self.manager.stop_qemu_vm(node, vmid)
        elif action == "shutdown_qemu_vm":
            return self.manager.shutdown_qemu_vm(node, vmid)
        elif action == "reset_qemu_vm":
            return self.manager.reset_qemu_vm(node, vmid)
        elif action == "suspend_qemu_vm":
            return self.manager.suspend_qemu_vm(node, vmid)
        elif action == "resume_qemu_vm":
            return self.manager.resume_qemu_vm(node, vmid)
        elif action == "delete_qemu_vm":
            return self.manager.delete_qemu_vm(node, vmid)
        elif action == "create_qemu_snapshot":
            return self.manager.create_qemu_snapshot(node, vmid, kwargs.get("snapname"), description=kwargs.get("description"), vmstate=kwargs.get("vmstate", True))
        elif action == "rollback_qemu_vm":
            return self.manager.rollback_qemu_vm(node, vmid, kwargs.get("snapname"))
        elif action == "list_qemu_snapshots":
            return {"snapshots": self.manager.list_qemu_snapshots(node, vmid)}
        elif action == "delete_qemu_snapshot":
            return self.manager.delete_qemu_snapshot(node, vmid, kwargs.get("snapname"))
        elif action == "migrate_qemu_vm":
            return self.manager.migrate_qemu_vm(node, vmid, kwargs.get("target_node"), online=kwargs.get("online", True))
        elif action == "template_qemu_vm":
            return self.manager.template_qemu_vm(node, vmid)
        elif action == "lxc_containers":
            return {"containers": self.manager.list_lxc_containers(node)}
        elif action == "create_lxc_container":
            return self.manager.create_lxc_container(node=node, vmid=vmid, hostname=kwargs.get("hostname", ""), ostemplate=kwargs.get("ostemplate"), storage=kwargs.get("storage", "local-lvm"), rootfs_size=kwargs.get("rootfs_size", "8G"), memory=kwargs.get("memory", 512), cores=kwargs.get("cores", 1), password=kwargs.get("password"), ssh_public_keys=kwargs.get("ssh_public_keys"), start=kwargs.get("start", True), pool=kwargs.get("pool"), unprivileged=kwargs.get("unprivileged", True), tags=kwargs.get("tags"))
        elif action == "start_lxc":
            return self.manager.start_lxc_container(node, vmid)
        elif action == "stop_lxc":
            return self.manager.stop_lxc_container(node, vmid)
        elif action == "shutdown_lxc":
            return self.manager.shutdown_lxc_container(node, vmid)
        elif action == "delete_lxc":
            return self.manager.delete_lxc_container(node, vmid)
        elif action == "enter_lxc":
            return self.manager.enter_lxc_container(node, vmid, command=kwargs.get("command", "bash"))
        elif action == "storage":
            return {"storage": self.manager.list_storage()}
        elif action == "storage_content":
            return {"content": self.manager.list_storage_content(kwargs.get("storage"), content_type=kwargs.get("content_type"))}
        elif action == "pools":
            return {"pools": self.manager.list_pools()}
        elif action == "tasks":
            return {"tasks": self.manager.list_tasks(node, limit=kwargs.get("limit", 50))}
        elif action == "cluster_status":
            return self.manager.get_cluster_status()
        elif action == "cluster_resources":
            return {"resources": self.manager.list_cluster_resources(resource_type=kwargs.get("resource_type"))}
        return {"error": f"Unknown action: {action}"}