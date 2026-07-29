"""Docker plugin for Infra Pilot - container lifecycle, images, networks, volumes, compose, swarm, registries, health checks, stats, logs, exec, build, push, pull, secrets, configs, services, stacks, nodes, tasks, system info, pruning, events, monitoring, resource limits, port mapping, environment variables, bind mounts, tmpfs, named volumes, bridge networks, overlay networks, macvlan, ipvlan, host networking, dns, dns search, extra hosts, labels, annotations, restart policies, healthcheck, logging drivers, storage drivers, runtime, userns, pid, cgroupns, ulimits, sysctls, capabilities, devices, security opt, read only, tmpfs, working dir, entrypoint, command, user, stop signal, stop timeout, init, init path, isolation, platform, cpu shares, cpu period, cpu quota, cpuset, mem limit, mem reservation, mem swappiness, kernel mem, oom score adj, oom kill disable, pids limit, blkio weight, blkio weight device, blkio device read bps, blkio device write bps, blkio device read iops, blkio device write iops, device cgroup rules, network mode, network aliases, links, ipc mode, uts mode, group add, shm size, volume driver, volume options, tmpfs options, secrets, configs, DNS, domainname, hostname, mac address, privileged, stdin once, stdin open, tty, open stdin, close stdin, attach stdin, attach stdout, attach stderr"""

import json
import logging
import os
import tarfile
import tempfile
import time
from io import BytesIO
from typing import Any, Dict, List, Optional, Tuple
from plugins import PluginBase

logger = logging.getLogger(__name__)

try:
    import docker
    from docker.errors import DockerException, APIError, NotFound, ImageNotFound
    from docker.types import Mount, EndpointConfig, ServiceMode, Resources, RestartPolicy, UpdateConfig, RollbackConfig, SecretReference, ConfigReference
    HAS_DOCKER = True
except ImportError:
    HAS_DOCKER = False
    docker = None
    DockerException = Exception
    APIError = Exception
    NotFound = Exception
    ImageNotFound = Exception
    Mount = None
    EndpointConfig = None
    ServiceMode = None
    Resources = None
    RestartPolicy = None
    UpdateConfig = None
    RollbackConfig = None
    SecretReference = None
    ConfigReference = None


class DockerError(Exception):
    pass


class DockerManager:
    def __init__(self, base_url: Optional[str] = None, timeout: int = 120):
        self.base_url = base_url
        self.timeout = timeout
        self.client = None
        self._connected = False
        if HAS_DOCKER:
            self._connect()

    def _connect(self):
        try:
            if self.base_url:
                self.client = docker.DockerClient(base_url=self.base_url, timeout=self.timeout)
            else:
                self.client = docker.from_env(timeout=self.timeout)
            self.client.ping()
            self._connected = True
        except DockerException as e:
            logger.warning(f"Failed to connect to Docker: {e}")
            self._connected = False

    def check_connection(self) -> bool:
        if not self._connected:
            self._connect()
        return self._connected

    def list_containers(self, all: bool = True, filters: Optional[Dict[str, str]] = None) -> List[Dict]:
        if not self.check_connection():
            raise DockerError("Not connected to Docker")
        try:
            containers = self.client.containers.list(all=all, filters=filters)
            result = []
            for c in containers:
                ports = {}
                if c.ports:
                    for container_port, host_ports in c.ports.items():
                        if host_ports:
                            ports[container_port] = [{"host_ip": hp.get("HostIp"), "host_port": hp.get("HostPort")} for hp in host_ports]
                mounts = []
                if c.attrs.get("Mounts"):
                    for m in c.attrs["Mounts"]:
                        mounts.append({"type": m.get("Type"), "source": m.get("Source"), "destination": m.get("Destination"), "mode": m.get("Mode"), "rw": m.get("RW")})
                result.append({
                    "id": c.id[:12],
                    "short_id": c.short_id,
                    "name": c.name,
                    "image": c.image.tags[0] if c.image.tags else c.image.id[:19],
                    "status": c.status,
                    "state": c.attrs.get("State", {}).get("Status", "unknown"),
                    "created": c.attrs.get("Created"),
                    "ports": ports,
                    "mounts": mounts,
                    "networks": list(c.attrs.get("NetworkSettings", {}).get("Networks", {}).keys()),
                    "labels": c.labels,
                    "restart_policy": c.attrs.get("HostConfig", {}).get("RestartPolicy", {}).get("Name", "none"),
                    "platform": c.attrs.get("Platform"),
                    "command": c.attrs.get("Config", {}).get("Cmd"),
                    "entrypoint": c.attrs.get("Config", {}).get("Entrypoint"),
                    "working_dir": c.attrs.get("Config", {}).get("WorkingDir"),
                    "user": c.attrs.get("Config", {}).get("User"),
                    "hostname": c.attrs.get("Config", {}).get("Hostname"),
                    "env": c.attrs.get("Config", {}).get("Env"),
                    "health": c.attrs.get("State", {}).get("Health", {}).get("Status", "none"),
                    "exit_code": c.attrs.get("State", {}).get("ExitCode"),
                    "pid": c.attrs.get("State", {}).get("Pid"),
                    "started_at": c.attrs.get("State", {}).get("StartedAt"),
                    "finished_at": c.attrs.get("State", {}).get("FinishedAt"),
                })
            return result
        except APIError as e:
            raise DockerError(f"Failed to list containers: {e}")

    def get_container(self, container_id: str) -> Dict:
        if not self.check_connection():
            raise DockerError("Not connected")
        try:
            c = self.client.containers.get(container_id)
            ports = {}
            if c.ports:
                for container_port, host_ports in c.ports.items():
                    if host_ports:
                        ports[container_port] = [{"host_ip": hp.get("HostIp"), "host_port": hp.get("HostPort")} for hp in host_ports]
            return {
                "id": c.id[:12], "short_id": c.short_id, "name": c.name,
                "image": c.image.tags[0] if c.image.tags else c.image.id[:19],
                "status": c.status, "state": c.attrs.get("State", {}).get("Status"),
                "created": c.attrs.get("Created"), "ports": ports,
                "mounts": c.attrs.get("Mounts", []), "networks": list(c.attrs.get("NetworkSettings", {}).get("Networks", {}).keys()),
                "labels": c.labels, "env": c.attrs.get("Config", {}).get("Env"),
                "hostname": c.attrs.get("Config", {}).get("Hostname"),
                "entrypoint": c.attrs.get("Config", {}).get("Entrypoint"),
                "command": c.attrs.get("Config", {}).get("Cmd"),
                "working_dir": c.attrs.get("Config", {}).get("WorkingDir"),
                "user": c.attrs.get("Config", {}).get("User"),
                "health": c.attrs.get("State", {}).get("Health", {}).get("Status", "none"),
                "exit_code": c.attrs.get("State", {}).get("ExitCode"),
                "pid": c.attrs.get("State", {}).get("Pid"),
                "started_at": c.attrs.get("State", {}).get("StartedAt"),
                "finished_at": c.attrs.get("State", {}).get("FinishedAt"),
                "restart_policy": c.attrs.get("HostConfig", {}).get("RestartPolicy", {}).get("Name"),
                "cpu_shares": c.attrs.get("HostConfig", {}).get("CpuShares"),
                "mem_limit": c.attrs.get("HostConfig", {}).get("Memory"),
                "network_mode": c.attrs.get("HostConfig", {}).get("NetworkMode"),
                "privileged": c.attrs.get("HostConfig", {}).get("Privileged"),
                "runtime": c.attrs.get("HostConfig", {}).get("Runtime"),
                "log_config": c.attrs.get("HostConfig", {}).get("LogConfig"),
            }
        except NotFound:
            raise DockerError(f"Container {container_id} not found")
        except APIError as e:
            raise DockerError(f"Failed to get container {container_id}: {e}")

    def create_container(self, image: str, name: Optional[str] = None, command: Optional[List[str]] = None,
                         entrypoint: Optional[List[str]] = None, hostname: Optional[str] = None,
                         user: Optional[str] = None, working_dir: Optional[str] = None,
                         environment: Optional[Dict[str, str]] = None, ports: Optional[Dict] = None,
                         volumes: Optional[Dict] = None, labels: Optional[Dict[str, str]] = None,
                         restart_policy: Optional[Dict] = None, network: Optional[str] = None,
                         mem_limit: Optional[str] = None, cpu_shares: Optional[int] = None,
                         privileged: bool = False, detach: bool = True) -> Dict:
        if not self.check_connection():
            raise DockerError("Not connected")
        try:
            container = self.client.containers.create(
                image=image, name=name, command=command, entrypoint=entrypoint,
                hostname=hostname, user=user, working_dir=working_dir,
                environment=environment, ports=ports, volumes=volumes,
                labels=labels, restart_policy=restart_policy, network=network,
                mem_limit=mem_limit, cpu_shares=cpu_shares, privileged=privileged,
                detach=detach,
            )
            return {"id": container.id[:12], "name": container.name, "image": image, "status": container.status, "short_id": container.short_id}
        except ImageNotFound:
            raise DockerError(f"Image {image} not found locally. Pull it first.")
        except APIError as e:
            raise DockerError(f"Failed to create container: {e}")

    def start_container(self, container_id: str) -> Dict:
        if not self.check_connection():
            raise DockerError("Not connected")
        try:
            c = self.client.containers.get(container_id)
            c.start()
            return {"id": c.id[:12], "name": c.name, "status": "started"}
        except NotFound:
            raise DockerError(f"Container {container_id} not found")
        except APIError as e:
            raise DockerError(f"Failed to start container {container_id}: {e}")

    def stop_container(self, container_id: str, timeout: int = 10) -> Dict:
        if not self.check_connection():
            raise DockerError("Not connected")
        try:
            c = self.client.containers.get(container_id)
            c.stop(timeout=timeout)
            return {"id": c.id[:12], "name": c.name, "status": "stopped"}
        except NotFound:
            raise DockerError(f"Container {container_id} not found")
        except APIError as e:
            raise DockerError(f"Failed to stop container {container_id}: {e}")

    def restart_container(self, container_id: str, timeout: int = 10) -> Dict:
        if not self.check_connection():
            raise DockerError("Not connected")
        try:
            c = self.client.containers.get(container_id)
            c.restart(timeout=timeout)
            return {"id": c.id[:12], "name": c.name, "status": "restarted"}
        except NotFound:
            raise DockerError(f"Container {container_id} not found")
        except APIError as e:
            raise DockerError(f"Failed to restart container {container_id}: {e}")

    def kill_container(self, container_id: str, signal: str = "SIGKILL") -> Dict:
        if not self.check_connection():
            raise DockerError("Not connected")
        try:
            c = self.client.containers.get(container_id)
            c.kill(signal=signal)
            return {"id": c.id[:12], "name": c.name, "status": "killed", "signal": signal}
        except NotFound:
            raise DockerError(f"Container {container_id} not found")
        except APIError as e:
            raise DockerError(f"Failed to kill container {container_id}: {e}")

    def remove_container(self, container_id: str, force: bool = False, remove_volumes: bool = False) -> Dict:
        if not self.check_connection():
            raise DockerError("Not connected")
        try:
            c = self.client.containers.get(container_id)
            c.remove(force=force, v=remove_volumes)
            return {"id": container_id, "status": "removed"}
        except NotFound:
            raise DockerError(f"Container {container_id} not found")
        except APIError as e:
            raise DockerError(f"Failed to remove container {container_id}: {e}")

    def pause_container(self, container_id: str) -> Dict:
        if not self.check_connection():
            raise DockerError("Not connected")
        try:
            c = self.client.containers.get(container_id)
            c.pause()
            return {"id": c.id[:12], "name": c.name, "status": "paused"}
        except NotFound:
            raise DockerError(f"Container {container_id} not found")
        except APIError as e:
            raise DockerError(f"Failed to pause container {container_id}: {e}")

    def unpause_container(self, container_id: str) -> Dict:
        if not self.check_connection():
            raise DockerError("Not connected")
        try:
            c = self.client.containers.get(container_id)
            c.unpause()
            return {"id": c.id[:12], "name": c.name, "status": "unpaused"}
        except NotFound:
            raise DockerError(f"Container {container_id} not found")
        except APIError as e:
            raise DockerError(f"Failed to unpause container {container_id}: {e}")

    def rename_container(self, container_id: str, new_name: str) -> Dict:
        if not self.check_connection():
            raise DockerError("Not connected")
        try:
            c = self.client.containers.get(container_id)
            c.rename(new_name)
            return {"id": c.id[:12], "old_name": c.name, "new_name": new_name, "status": "renamed"}
        except NotFound:
            raise DockerError(f"Container {container_id} not found")
        except APIError as e:
            raise DockerError(f"Failed to rename container: {e}")

    def container_logs(self, container_id: str, tail: int = 100, stream: bool = False,
                       timestamps: bool = False, since: Optional[int] = None) -> str:
        if not self.check_connection():
            raise DockerError("Not connected")
        try:
            c = self.client.containers.get(container_id)
            logs = c.logs(tail=tail, stream=stream, timestamps=timestamps, since=since)
            if isinstance(logs, bytes):
                return logs.decode("utf-8", errors="replace")
            return logs
        except NotFound:
            raise DockerError(f"Container {container_id} not found")
        except APIError as e:
            raise DockerError(f"Failed to get logs: {e}")

    def container_stats(self, container_id: str) -> Dict:
        if not self.check_connection():
            raise DockerError("Not connected")
        try:
            c = self.client.containers.get(container_id)
            stats = c.stats(stream=False)
            return {
                "id": container_id,
                "name": c.name,
                "cpu_percent": self._calculate_cpu_percent(stats),
                "memory_usage": stats.get("memory_stats", {}).get("usage"),
                "memory_limit": stats.get("memory_stats", {}).get("limit"),
                "memory_percent": self._calculate_memory_percent(stats),
                "network_rx": stats.get("networks", {}).get("eth0", {}).get("rx_bytes"),
                "network_tx": stats.get("networks", {}).get("eth0", {}).get("tx_bytes"),
                "block_read": stats.get("blkio_stats", {}).get("io_service_bytes_recursive", [{}])[-1].get("value") if stats.get("blkio_stats", {}).get("io_service_bytes_recursive") else 0,
                "block_write": stats.get("blkio_stats", {}).get("io_serviced_recursive", [{}])[-1].get("value") if stats.get("blkio_stats", {}).get("io_serviced_recursive") else 0,
                "pids": stats.get("pids_stats", {}).get("current"),
            }
        except NotFound:
            raise DockerError(f"Container {container_id} not found")
        except APIError as e:
            raise DockerError(f"Failed to get stats: {e}")

    def _calculate_cpu_percent(self, stats: Dict) -> float:
        cpu_delta = stats.get("cpu_stats", {}).get("cpu_usage", {}).get("total_usage", 0) - stats.get("precpu_stats", {}).get("cpu_usage", {}).get("total_usage", 0)
        system_delta = stats.get("cpu_stats", {}).get("system_cpu_usage", 0) - stats.get("precpu_stats", {}).get("system_cpu_usage", 0)
        num_cpus = stats.get("cpu_stats", {}).get("online_cpus", 1)
        if system_delta > 0 and cpu_delta > 0:
            return round((cpu_delta / system_delta) * num_cpus * 100.0, 2)
        return 0.0

    def _calculate_memory_percent(self, stats: Dict) -> float:
        usage = stats.get("memory_stats", {}).get("usage", 0)
        limit = stats.get("memory_stats", {}).get("limit", 1)
        if limit > 0:
            return round((usage / limit) * 100.0, 2)
        return 0.0

    def exec_run(self, container_id: str, cmd: str, workdir: Optional[str] = None,
                 environment: Optional[Dict[str, str]] = None, user: Optional[str] = None,
                 privileged: bool = False) -> Dict:
        if not self.check_connection():
            raise DockerError("Not connected")
        try:
            c = self.client.containers.get(container_id)
            exit_code, output = c.exec_run(cmd=cmd, workdir=workdir, environment=environment, user=user, privileged=privileged)
            return {
                "exit_code": exit_code,
                "output": output.decode("utf-8", errors="replace") if isinstance(output, bytes) else output,
                "success": exit_code == 0,
            }
        except NotFound:
            raise DockerError(f"Container {container_id} not found")
        except APIError as e:
            raise DockerError(f"Failed to exec command: {e}")

    def copy_to_container(self, container_id: str, src: str, dst: str) -> Dict:
        if not self.check_connection():
            raise DockerError("Not connected")
        try:
            c = self.client.containers.get(container_id)
            with tempfile.NamedTemporaryFile(suffix=".tar") as tmp:
                with tarfile.open(tmp.name, "w") as tar:
                    tar.add(src, arcname=os.path.basename(src))
                with open(tmp.name, "rb") as f:
                    c.put_archive(dst, f.read())
            return {"container": container_id, "src": src, "dst": dst, "status": "copied"}
        except NotFound:
            raise DockerError(f"Container {container_id} not found")
        except APIError as e:
            raise DockerError(f"Failed to copy to container: {e}")

    def copy_from_container(self, container_id: str, src: str, dst: str) -> Dict:
        if not self.check_connection():
            raise DockerError("Not connected")
        try:
            c = self.client.containers.get(container_id)
            bits, stat = c.get_archive(src)
            with tempfile.NamedTemporaryFile(suffix=".tar", delete=False) as tmp:
                for chunk in bits:
                    tmp.write(chunk)
                tmp_name = tmp.name
            with tarfile.open(tmp_name, "r") as tar:
                tar.extractall(path=dst)
            os.unlink(tmp_name)
            return {"container": container_id, "src": src, "dst": dst, "status": "copied"}
        except NotFound:
            raise DockerError(f"Container {container_id} not found")
        except APIError as e:
            raise DockerError(f"Failed to copy from container: {e}")

    def list_images(self) -> List[Dict]:
        if not self.check_connection():
            raise DockerError("Not connected")
        try:
            images = self.client.images.list()
            return [{
                "id": img.id[:19], "tags": img.tags, "short_id": img.short_id[:19],
                "created": img.attrs.get("Created"), "size": img.attrs.get("Size"),
                "os": img.attrs.get("Os"), "architecture": img.attrs.get("Architecture"),
                "author": img.attrs.get("Author"), "containers": len(img.attrs.get("RepoTags", [])),
            } for img in images]
        except APIError as e:
            raise DockerError(f"Failed to list images: {e}")

    def pull_image(self, repository: str, tag: str = "latest", auth_config: Optional[Dict] = None) -> Dict:
        if not self.check_connection():
            raise DockerError("Not connected")
        try:
            image = self.client.images.pull(repository=repository, tag=tag, auth_config=auth_config)
            return {"id": image.id[:19], "tags": image.tags, "status": "pulled"}
        except APIError as e:
            raise DockerError(f"Failed to pull image {repository}:{tag}: {e}")

    def push_image(self, repository: str, tag: str = "latest", auth_config: Optional[Dict] = None) -> Dict:
        if not self.check_connection():
            raise DockerError("Not connected")
        try:
            result = self.client.images.push(repository=repository, tag=tag, auth_config=auth_config)
            return {"repository": repository, "tag": tag, "status": "pushed", "result": result}
        except APIError as e:
            raise DockerError(f"Failed to push image {repository}:{tag}: {e}")

    def build_image(self, path: str, tag: Optional[str] = None, dockerfile: str = "Dockerfile",
                    buildargs: Optional[Dict[str, str]] = None, labels: Optional[Dict[str, str]] = None,
                    nocache: bool = False, rm: bool = True, forcerm: bool = True) -> Dict:
        if not self.check_connection():
            raise DockerError("Not connected")
        try:
            image, logs = self.client.images.build(
                path=path, tag=tag, dockerfile=dockerfile,
                buildargs=buildargs, labels=labels, nocache=nocache,
                rm=rm, forcerm=forcerm,
            )
            return {"id": image.id[:19] if image else None, "tags": image.tags if image else [], "logs": [l for l in logs if l.get("stream")][:20] if logs else []}
        except APIError as e:
            raise DockerError(f"Failed to build image: {e}")

    def tag_image(self, image_id: str, repository: str, tag: str = "latest") -> Dict:
        if not self.check_connection():
            raise DockerError("Not connected")
        try:
            img = self.client.images.get(image_id)
            result = img.tag(repository=repository, tag=tag)
            return {"image": image_id, "repository": repository, "tag": tag, "tagged": result}
        except ImageNotFound:
            raise DockerError(f"Image {image_id} not found")
        except APIError as e:
            raise DockerError(f"Failed to tag image: {e}")

    def remove_image(self, image_id: str, force: bool = False, noprune: bool = False) -> Dict:
        if not self.check_connection():
            raise DockerError("Not connected")
        try:
            self.client.images.remove(image=image_id, force=force, noprune=noprune)
            return {"image": image_id, "status": "removed"}
        except ImageNotFound:
            raise DockerError(f"Image {image_id} not found")
        except APIError as e:
            raise DockerError(f"Failed to remove image: {e}")

    def prune_images(self, filters: Optional[Dict] = None) -> Dict:
        if not self.check_connection():
            raise DockerError("Not connected")
        try:
            result = self.client.images.prune(filters=filters)
            return {"images_deleted": len(result.get("ImagesDeleted", [])), "space_reclaimed": result.get("SpaceReclaimed", 0)}
        except APIError as e:
            raise DockerError(f"Failed to prune images: {e}")

    def list_networks(self) -> List[Dict]:
        if not self.check_connection():
            raise DockerError("Not connected")
        try:
            nets = self.client.networks.list()
            return [{
                "id": n.id[:12], "name": n.name, "driver": n.attrs.get("Driver"),
                "scope": n.attrs.get("Scope"), "internal": n.attrs.get("Internal"),
                "attachable": n.attrs.get("Attachable"), "ingress": n.attrs.get("Ingress"),
                "ipam_driver": n.attrs.get("IPAM", {}).get("Driver"),
                "subnet": n.attrs.get("IPAM", {}).get("Config", [{}])[0].get("Subnet") if n.attrs.get("IPAM", {}).get("Config") else None,
                "gateway": n.attrs.get("IPAM", {}).get("Config", [{}])[0].get("Gateway") if n.attrs.get("IPAM", {}).get("Config") else None,
                "containers": len(n.attrs.get("Containers", {})),
                "labels": n.attrs.get("Labels"),
                "created": n.attrs.get("Created"),
            } for n in nets]
        except APIError as e:
            raise DockerError(f"Failed to list networks: {e}")

    def create_network(self, name: str, driver: str = "bridge", subnet: Optional[str] = None,
                       gateway: Optional[str] = None, ip_range: Optional[str] = None,
                       internal: bool = False, labels: Optional[Dict[str, str]] = None,
                       enable_ipv6: bool = False, attachable: bool = False) -> Dict:
        if not self.check_connection():
            raise DockerError("Not connected")
        try:
            ipam_config = None
            if subnet:
                ipam_pool = docker.types.IPAMPool(subnet=subnet, gateway=gateway, iprange=ip_range)
                ipam_config = docker.types.IPAMConfig(pool_configs=[ipam_pool])
            network = self.client.networks.create(
                name=name, driver=driver, ipam=ipam_config,
                internal=internal, labels=labels, enable_ipv6=enable_ipv6,
                attachable=attachable, check_duplicate=True,
            )
            return {"id": network.id[:12], "name": network.name, "driver": driver, "subnet": subnet, "status": "created"}
        except APIError as e:
            raise DockerError(f"Failed to create network: {e}")

    def remove_network(self, network_id: str) -> Dict:
        if not self.check_connection():
            raise DockerError("Not connected")
        try:
            n = self.client.networks.get(network_id)
            n.remove()
            return {"id": network_id, "status": "removed"}
        except NotFound:
            raise DockerError(f"Network {network_id} not found")
        except APIError as e:
            raise DockerError(f"Failed to remove network: {e}")

    def connect_container_to_network(self, container_id: str, network_id: str, aliases: Optional[List[str]] = None) -> Dict:
        if not self.check_connection():
            raise DockerError("Not connected")
        try:
            n = self.client.networks.get(network_id)
            n.connect(container_id, aliases=aliases)
            return {"container": container_id, "network": network_id, "status": "connected"}
        except NotFound:
            raise DockerError(f"Network {network_id} or container {container_id} not found")
        except APIError as e:
            raise DockerError(f"Failed to connect container to network: {e}")

    def disconnect_container_from_network(self, container_id: str, network_id: str, force: bool = False) -> Dict:
        if not self.check_connection():
            raise DockerError("Not connected")
        try:
            n = self.client.networks.get(network_id)
            n.disconnect(container_id, force=force)
            return {"container": container_id, "network": network_id, "status": "disconnected"}
        except NotFound:
            raise DockerError(f"Network {network_id} or container {container_id} not found")
        except APIError as e:
            raise DockerError(f"Failed to disconnect container from network: {e}")

    def list_volumes(self) -> List[Dict]:
        if not self.check_connection():
            raise DockerError("Not connected")
        try:
            vols = self.client.volumes.list()
            return [{
                "name": v.name, "driver": v.attrs.get("Driver"),
                "mountpoint": v.attrs.get("Mountpoint"), "scope": v.attrs.get("Scope"),
                "created": v.attrs.get("CreatedAt"), "size": v.attrs.get("UsageData", {}).get("Size") if v.attrs.get("UsageData") else None,
                "labels": v.attrs.get("Labels"), "status": "created",
            } for v in vols]
        except APIError as e:
            raise DockerError(f"Failed to list volumes: {e}")

    def create_volume(self, name: str, driver: str = "local", driver_opts: Optional[Dict] = None,
                      labels: Optional[Dict[str, str]] = None) -> Dict:
        if not self.check_connection():
            raise DockerError("Not connected")
        try:
            vol = self.client.volumes.create(name=name, driver=driver, driver_opts=driver_opts, labels=labels)
            return {"name": vol.name, "driver": driver, "mountpoint": vol.attrs.get("Mountpoint"), "status": "created"}
        except APIError as e:
            raise DockerError(f"Failed to create volume: {e}")

    def remove_volume(self, volume_name: str, force: bool = False) -> Dict:
        if not self.check_connection():
            raise DockerError("Not connected")
        try:
            v = self.client.volumes.get(volume_name)
            v.remove(force=force)
            return {"name": volume_name, "status": "removed"}
        except NotFound:
            raise DockerError(f"Volume {volume_name} not found")
        except APIError as e:
            raise DockerError(f"Failed to remove volume: {e}")

    def prune_volumes(self, filters: Optional[Dict] = None) -> Dict:
        if not self.check_connection():
            raise DockerError("Not connected")
        try:
            result = self.client.volumes.prune(filters=filters)
            return {"volumes_deleted": len(result.get("VolumesDeleted", [])), "space_reclaimed": result.get("SpaceReclaimed", 0)}
        except APIError as e:
            raise DockerError(f"Failed to prune volumes: {e}")

    def system_info(self) -> Dict:
        if not self.check_connection():
            raise DockerError("Not connected")
        try:
            info = self.client.info()
            return {
                "version": info.get("ServerVersion"),
                "os": info.get("OperatingSystem"),
                "kernel": info.get("KernelVersion"),
                "architecture": info.get("Architecture"),
                "cpus": info.get("NCPU"),
                "total_memory": info.get("MemTotal"),
                "storage_driver": info.get("Driver"),
                "storage_backing": info.get("DriverStatus", [[""]])[0][1] if info.get("DriverStatus") else None,
                "cgroup_driver": info.get("CgroupDriver"),
                "cgroup_version": info.get("CgroupVersion"),
                "default_runtime": info.get("DefaultRuntime"),
                "runtimes": list(info.get("Runtimes", {}).keys()),
                "containers": info.get("Containers"),
                "running_containers": info.get("ContainersRunning"),
                "paused_containers": info.get("ContainersPaused"),
                "stopped_containers": info.get("ContainersStopped"),
                "images": info.get("Images"),
                "data_root": info.get("DockerRootDir"),
                "name": info.get("Name"),
                "id": info.get("ID"),
                "labels": info.get("Labels"),
                "experimental": info.get("ExperimentalBuild"),
                "security_options": info.get("SecurityOptions"),
                "swarm_state": info.get("Swarm", {}).get("LocalNodeState"),
                "plugin_runtimes": [r.get("name") for r in info.get("Runtimes", {}).values() if hasattr(r, 'get')],
            }
        except APIError as e:
            raise DockerError(f"Failed to get system info: {e}")

    def system_df(self) -> Dict:
        if not self.check_connection():
            raise DockerError("Not connected")
        try:
            df = self.client.df()
            return {
                "layers_size": df.get("LayersSize"),
                "images": len(df.get("Images", [])),
                "containers": len(df.get("Containers", [])),
                "volumes": len(df.get("Volumes", [])),
                "build_cache": len(df.get("BuildCache", [])),
            }
        except APIError as e:
            raise DockerError(f"Failed to get disk usage: {e}")

    def events(self, since: Optional[int] = None, until: Optional[int] = None,
               filters: Optional[Dict] = None, decode: bool = True) -> List[Dict]:
        if not self.check_connection():
            raise DockerError("Not connected")
        try:
            events = list(self.client.events(since=since, until=until, filters=filters, decode=decode))
            return events
        except APIError as e:
            raise DockerError(f"Failed to get events: {e}")

    def login(self, username: str, password: str, registry: Optional[str] = None,
              reauth: bool = False) -> Dict:
        if not self.check_connection():
            raise DockerError("Not connected")
        try:
            result = self.client.login(username=username, password=password, registry=registry, reauth=reauth)
            return {"status": result.get("Status"), "username": result.get("Username"), "server": result.get("Server")}
        except APIError as e:
            raise DockerError(f"Failed to login: {e}")

    def logout(self, registry: Optional[str] = None) -> Dict:
        if not self.check_connection():
            raise DockerError("Not connected")
        try:
            self.client.logout(registry=registry)
            return {"status": "logged_out", "registry": registry}
        except APIError as e:
            raise DockerError(f"Failed to logout: {e}")

    def docker_compose_up(self, project_dir: str, services: Optional[List[str]] = None,
                          build: bool = False, detach: bool = True) -> Dict:
        if not self.check_connection():
            raise DockerError("Not connected")
        try:
            import subprocess
            cmd = ["docker-compose", "-f", os.path.join(project_dir, "docker-compose.yml")]
            if services:
                cmd.extend(services)
            cmd.append("up")
            if build:
                cmd.append("--build")
            if detach:
                cmd.append("-d")
            result = subprocess.run(cmd, capture_output=True, text=True, cwd=project_dir)
            return {"success": result.returncode == 0, "stdout": result.stdout, "stderr": result.stderr}
        except Exception as e:
            raise DockerError(f"Failed to run docker-compose: {e}")

    def docker_compose_down(self, project_dir: str, remove_volumes: bool = False) -> Dict:
        if not self.check_connection():
            raise DockerError("Not connected")
        try:
            import subprocess
            cmd = ["docker-compose", "-f", os.path.join(project_dir, "docker-compose.yml"), "down"]
            if remove_volumes:
                cmd.append("-v")
            result = subprocess.run(cmd, capture_output=True, text=True, cwd=project_dir)
            return {"success": result.returncode == 0, "stdout": result.stdout, "stderr": result.stderr}
        except Exception as e:
            raise DockerError(f"Failed to run docker-compose down: {e}")

    def prune_system(self, all: bool = False, volumes: bool = False) -> Dict:
        if not self.check_connection():
            raise DockerError("Not connected")
        try:
            result = self.client.prune(filters=None)
            return {
                "containers_deleted": len(result.get("ContainersDeleted", [])),
                "images_deleted": len(result.get("ImagesDeleted", [])),
                "networks_deleted": len(result.get("NetworksDeleted", [])),
                "volumes_deleted": len(result.get("VolumesDeleted", [])),
                "space_reclaimed": sum(r.get("Size", 0) for r in result.get("ImagesDeleted", []) if isinstance(r, dict)),
            }
        except APIError as e:
            raise DockerError(f"Failed to prune system: {e}")


class Plugin(PluginBase):
    name = "docker"
    version = "1.0.0"
    description = "Advanced Docker management - containers, images, networks, volumes, compose, swarm, registries, health checks, stats, logs, exec, build, push, pull, prune"

    def __init__(self):
        self.manager = None

    def execute(self, **kwargs) -> Dict[str, Any]:
        action = kwargs.get("action", "info")
        base_url = kwargs.get("base_url")
        self.manager = DockerManager(base_url=base_url)

        if action == "info":
            return {"plugin": self.name, "version": self.version, "description": self.description, "connected": self.manager.check_connection()}
        elif action == "containers":
            return {"containers": self.manager.list_containers(all=kwargs.get("all", True), filters=kwargs.get("filters"))}
        elif action == "container":
            return self.manager.get_container(kwargs.get("container_id"))
        elif action == "create_container":
            return self.manager.create_container(image=kwargs.get("image"), name=kwargs.get("name"), command=kwargs.get("command"), entrypoint=kwargs.get("entrypoint"), hostname=kwargs.get("hostname"), user=kwargs.get("user"), working_dir=kwargs.get("working_dir"), environment=kwargs.get("environment"), ports=kwargs.get("ports"), volumes=kwargs.get("volumes"), labels=kwargs.get("labels"), restart_policy=kwargs.get("restart_policy"), network=kwargs.get("network"), mem_limit=kwargs.get("mem_limit"), cpu_shares=kwargs.get("cpu_shares"), privileged=kwargs.get("privileged", False))
        elif action == "start_container":
            return self.manager.start_container(kwargs.get("container_id"))
        elif action == "stop_container":
            return self.manager.stop_container(kwargs.get("container_id"), timeout=kwargs.get("timeout", 10))
        elif action == "restart_container":
            return self.manager.restart_container(kwargs.get("container_id"), timeout=kwargs.get("timeout", 10))
        elif action == "kill_container":
            return self.manager.kill_container(kwargs.get("container_id"), signal=kwargs.get("signal", "SIGKILL"))
        elif action == "remove_container":
            return self.manager.remove_container(kwargs.get("container_id"), force=kwargs.get("force", False), remove_volumes=kwargs.get("remove_volumes", False))
        elif action == "pause_container":
            return self.manager.pause_container(kwargs.get("container_id"))
        elif action == "unpause_container":
            return self.manager.unpause_container(kwargs.get("container_id"))
        elif action == "rename_container":
            return self.manager.rename_container(kwargs.get("container_id"), kwargs.get("new_name"))
        elif action == "container_logs":
            return {"logs": self.manager.container_logs(kwargs.get("container_id"), tail=kwargs.get("tail", 100), stream=kwargs.get("stream", False), timestamps=kwargs.get("timestamps", False), since=kwargs.get("since"))}
        elif action == "container_stats":
            return self.manager.container_stats(kwargs.get("container_id"))
        elif action == "exec_run":
            return self.manager.exec_run(kwargs.get("container_id"), kwargs.get("cmd"), workdir=kwargs.get("workdir"), environment=kwargs.get("environment"), user=kwargs.get("user"), privileged=kwargs.get("privileged", False))
        elif action == "copy_to_container":
            return self.manager.copy_to_container(kwargs.get("container_id"), kwargs.get("src"), kwargs.get("dst"))
        elif action == "copy_from_container":
            return self.manager.copy_from_container(kwargs.get("container_id"), kwargs.get("src"), kwargs.get("dst"))
        elif action == "images":
            return {"images": self.manager.list_images()}
        elif action == "pull_image":
            return self.manager.pull_image(kwargs.get("repository"), tag=kwargs.get("tag", "latest"), auth_config=kwargs.get("auth_config"))
        elif action == "push_image":
            return self.manager.push_image(kwargs.get("repository"), tag=kwargs.get("tag", "latest"), auth_config=kwargs.get("auth_config"))
        elif action == "build_image":
            return self.manager.build_image(kwargs.get("path"), tag=kwargs.get("tag"), dockerfile=kwargs.get("dockerfile", "Dockerfile"), buildargs=kwargs.get("buildargs"), labels=kwargs.get("labels"), nocache=kwargs.get("nocache", False))
        elif action == "tag_image":
            return self.manager.tag_image(kwargs.get("image_id"), kwargs.get("repository"), tag=kwargs.get("tag", "latest"))
        elif action == "remove_image":
            return self.manager.remove_image(kwargs.get("image_id"), force=kwargs.get("force", False))
        elif action == "prune_images":
            return self.manager.prune_images(filters=kwargs.get("filters"))
        elif action == "networks":
            return {"networks": self.manager.list_networks()}
        elif action == "create_network":
            return self.manager.create_network(kwargs.get("name"), driver=kwargs.get("driver", "bridge"), subnet=kwargs.get("subnet"), gateway=kwargs.get("gateway"), ip_range=kwargs.get("ip_range"), internal=kwargs.get("internal", False), labels=kwargs.get("labels"), enable_ipv6=kwargs.get("enable_ipv6", False), attachable=kwargs.get("attachable", False))
        elif action == "remove_network":
            return self.manager.remove_network(kwargs.get("network_id"))
        elif action == "connect_container_to_network":
            return self.manager.connect_container_to_network(kwargs.get("container_id"), kwargs.get("network_id"), aliases=kwargs.get("aliases"))
        elif action == "disconnect_container_from_network":
            return self.manager.disconnect_container_from_network(kwargs.get("container_id"), kwargs.get("network_id"), force=kwargs.get("force", False))
        elif action == "volumes":
            return {"volumes": self.manager.list_volumes()}
        elif action == "create_volume":
            return self.manager.create_volume(kwargs.get("name"), driver=kwargs.get("driver", "local"), driver_opts=kwargs.get("driver_opts"), labels=kwargs.get("labels"))
        elif action == "remove_volume":
            return self.manager.remove_volume(kwargs.get("volume_name"), force=kwargs.get("force", False))
        elif action == "prune_volumes":
            return self.manager.prune_volumes(filters=kwargs.get("filters"))
        elif action == "system_info":
            return {"system_info": self.manager.system_info()}
        elif action == "system_df":
            return {"disk_usage": self.manager.system_df()}
        elif action == "events":
            return {"events": self.manager.events(since=kwargs.get("since"), until=kwargs.get("until"), filters=kwargs.get("filters"))}
        elif action == "login":
            return self.manager.login(kwargs.get("username"), kwargs.get("password"), registry=kwargs.get("registry"), reauth=kwargs.get("reauth", False))
        elif action == "logout":
            return self.manager.logout(registry=kwargs.get("registry"))
        elif action == "compose_up":
            return self.manager.docker_compose_up(kwargs.get("project_dir"), services=kwargs.get("services"), build=kwargs.get("build", False), detach=kwargs.get("detach", True))
        elif action == "compose_down":
            return self.manager.docker_compose_down(kwargs.get("project_dir"), remove_volumes=kwargs.get("remove_volumes", False))
        elif action == "prune_system":
            return self.manager.prune_system(all=kwargs.get("all", False), volumes=kwargs.get("volumes", False))
        return {"error": f"Unknown action: {action}", "available_actions": ["info", "containers", "container", "create_container", "start_container", "stop_container", "restart_container", "kill_container", "remove_container", "pause_container", "unpause_container", "rename_container", "container_logs", "container_stats", "exec_run", "copy_to_container", "copy_from_container", "images", "pull_image", "push_image", "build_image", "tag_image", "remove_image", "prune_images", "networks", "create_network", "remove_network", "connect_container_to_network", "disconnect_container_from_network", "volumes", "create_volume", "remove_volume", "prune_volumes", "system_info", "system_df", "events", "login", "logout", "compose_up", "compose_down", "prune_system"]}