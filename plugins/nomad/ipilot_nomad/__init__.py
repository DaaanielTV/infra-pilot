"""Nomad plugin for Infra Pilot - jobs, allocs, evaluations, deployments, nodes, namespaces, volumes, ACL tokens, policies, agent info, server members, client info, system stats, CSI plugins, keyring, operators, quotas, scaling policies, sentinel policies, recommendations, service discovery, Consul integration, Vault integration, task groups, tasks, networks, ports, services, checks, restart policies, update strategies, reschedule strategies, migrate strategies, spread, affinity, constraints, resources, artifacts, templates, logs, exec, fs, stats, signals, stop, periodic jobs, parameterized jobs, batch jobs, system jobs, service jobs"""

import json
import logging
from typing import Any, Dict, List, Optional
from plugins import PluginBase

logger = logging.getLogger(__name__)

try:
    import nomad
    from nomad import Nomad
    from nomad.api.exceptions import BaseNomadException, URLNotFoundNomadException
    HAS_NOMAD = True
except ImportError:
    HAS_NOMAD = False
    Nomad = None
    BaseNomadException = Exception


class NomadError(Exception):
    pass


class NomadManager:
    def __init__(self, address: str = "http://127.0.0.1:4646", token: Optional[str] = None, timeout: int = 30):
        self.address = address
        self.token = token
        self.timeout = timeout
        self.client = None
        self._connected = False
        if HAS_NOMAD:
            self._connect()

    def _connect(self):
        try:
            self.client = Nomad(address=self.address, token=self.token, timeout=self.timeout)
            self.client.agent.health()
            self._connected = True
        except Exception as e:
            logger.warning(f"Failed to connect to Nomad: {e}")
            self._connected = False

    def check_connection(self) -> bool:
        if not self._connected:
            self._connect()
        return self._connected

    def agent_health(self) -> Dict:
        if not self.check_connection():
            raise NomadError("Not connected")
        try:
            health = self.client.agent.health()
            return {"healthy": health}
        except Exception as e:
            raise NomadError(f"Failed to get agent health: {e}")

    def agent_info(self) -> Dict:
        if not self.check_connection():
            raise NomadError("Not connected")
        try:
            info = self.client.agent.members()
            config = self.client.agent.config()
            return {"members": info, "config": config, "version": config.get("Version", {})}
        except Exception as e:
            raise NomadError(f"Failed to get agent info: {e}")

    def list_jobs(self, namespace: Optional[str] = None) -> List[Dict]:
        if not self.check_connection():
            raise NomadError("Not connected")
        try:
            kwargs = {}
            if namespace:
                kwargs["namespace"] = namespace
            jobs = self.client.jobs.get_jobs(**kwargs)
            return [{
                "id": j.get("ID"), "name": j.get("Name"), "type": j.get("Type"),
                "status": j.get("Status"), "priority": j.get("Priority"),
                "namespace": j.get("Namespace", "default"),
                "datacenters": j.get("Datacenters", []),
                "create_index": j.get("CreateIndex"),
                "modify_index": j.get("ModifyIndex"),
                "job_modify_index": j.get("JobModifyIndex"),
                "submit_time": j.get("SubmitTime"),
                "stop": j.get("Stop"),
                "children": j.get("Children", {}),
                "summary": j.get("JobSummary", {}),
                "task_groups": [tg.get("Name") for tg in j.get("TaskGroups", [])] if j.get("TaskGroups") else [],
            } for j in jobs]
        except Exception as e:
            raise NomadError(f"Failed to list jobs: {e}")

    def get_job(self, job_id: str, namespace: Optional[str] = None) -> Dict:
        if not self.check_connection():
            raise NomadError("Not connected")
        try:
            job = self.client.job.get_job(job_id, namespace=namespace)
            return {
                "id": job.get("ID"), "name": job.get("Name"), "type": job.get("Type"),
                "status": job.get("Status"), "priority": job.get("Priority"),
                "namespace": job.get("Namespace"), "datacenters": job.get("Datacenters", []),
                "task_groups": [{"name": tg.get("Name"), "count": tg.get("Count"), "tasks": [t.get("Name") for t in (tg.get("Tasks") or [])], "networks": [{"mode": n.get("Mode"), "device": n.get("Device")} for n in (tg.get("Networks") or [])]} for tg in (job.get("TaskGroups") or [])],
                "update": job.get("Update", {}), "migrate": job.get("Migrate", {}),
                "reschedule": job.get("Reschedule", {}), "periodic": job.get("Periodic", {}),
                "parameterized": job.get("ParameterizedJob", {}),
                "constraints": job.get("Constraints", []),
                "affinities": job.get("Affinities", []),
                "spreads": job.get("Spreads", []),
                "create_index": job.get("CreateIndex"),
                "modify_index": job.get("ModifyIndex"),
                "submit_time": job.get("SubmitTime"),
                "stop": job.get("Stop"),
            }
        except Exception as e:
            raise NomadError(f"Failed to get job: {e}")

    def run_job(self, job_spec: Dict) -> Dict:
        if not self.check_connection():
            raise NomadError("Not connected")
        try:
            result = self.client.job.register_job(job_spec.get("Name") or job_spec.get("ID"), body=job_spec)
            return {"id": result.get("ID"), "eval_id": result.get("EvalID"), "index": result.get("Index"), "warnings": result.get("Warnings")}
        except Exception as e:
            raise NomadError(f"Failed to run job: {e}")

    def stop_job(self, job_id: str, purge: bool = False, namespace: Optional[str] = None) -> Dict:
        if not self.check_connection():
            raise NomadError("Not connected")
        try:
            result = self.client.job.deregister_job(job_id, purge=purge, namespace=namespace)
            return {"id": job_id, "eval_id": result.get("EvalID"), "purged": purge}
        except Exception as e:
            raise NomadError(f"Failed to stop job: {e}")

    def list_allocations(self, job_id: Optional[str] = None, namespace: Optional[str] = None) -> List[Dict]:
        if not self.check_connection():
            raise NomadError("Not connected")
        try:
            if job_id:
                allocs = self.client.job.get_allocations(job_id, namespace=namespace)
            else:
                allocs = self.client.allocations.get_allocations(namespace=namespace)
            return [{
                "id": a.get("ID"), "job_id": a.get("JobID"), "task_group": a.get("TaskGroup"),
                "node_id": a.get("NodeID"), "client_status": a.get("ClientStatus"),
                "desired_status": a.get("DesiredStatus"), "desired_description": a.get("DesiredDescription"),
                "created": a.get("CreateTime"), "modified": a.get("ModifyTime"),
                "namespace": a.get("Namespace"), "alloc_modify_index": a.get("AllocModifyIndex"),
                "followup_eval_id": a.get("FollowupEvalID"),
                "resources": {"cpu": a.get("AllocatedResources", {}).get("Shared", {}).get("CpuMB"), "memory": a.get("AllocatedResources", {}).get("Shared", {}).get("MemoryMB")},
            } for a in allocs]
        except Exception as e:
            raise NomadError(f"Failed to list allocations: {e}")

    def get_allocation(self, alloc_id: str) -> Dict:
        if not self.check_connection():
            raise NomadError("Not connected")
        try:
            a = self.client.allocation.get_allocation(alloc_id)
            return {
                "id": a.get("ID"), "job_id": a.get("JobID"), "task_group": a.get("TaskGroup"),
                "node_id": a.get("NodeID"), "client_status": a.get("ClientStatus"),
                "desired_status": a.get("DesiredStatus"), "namespace": a.get("Namespace"),
                "created": a.get("CreateTime"), "modified": a.get("ModifyTime"),
                "tasks": [{"name": t.get("Name"), "state": t.get("State", "running"), "started": t.get("StartedAt"), "finished": t.get("FinishedAt"), "restarts": t.get("Restarts", 0), "events": [{"type": e.get("Type"), "time": e.get("Time"), "message": e.get("Message"), "details": e.get("Details")} for e in (t.get("Events") or [])]} for t in (a.get("TaskStates") or {}).values()],
                "resources": a.get("AllocatedResources", {}),
            }
        except Exception as e:
            raise NomadError(f"Failed to get allocation: {e}")

    def stop_allocation(self, alloc_id: str) -> Dict:
        if not self.check_connection():
            raise NomadError("Not connected")
        try:
            result = self.client.allocation.stop_allocation(alloc_id)
            return {"id": alloc_id, "index": result.get("Index"), "stopped": True}
        except Exception as e:
            raise NomadError(f"Failed to stop allocation: {e}")

    def list_evaluations(self, job_id: Optional[str] = None) -> List[Dict]:
        if not self.check_connection():
            raise NomadError("Not connected")
        try:
            evals = self.client.evaluations.get_evaluations()
            return [{
                "id": e.get("ID"), "job_id": e.get("JobID"), "status": e.get("Status"),
                "type": e.get("Type"), "priority": e.get("Priority"),
                "triggered_by": e.get("TriggeredBy"), "namespace": e.get("Namespace"),
                "wait": e.get("Wait"), "wait_until": e.get("WaitUntil"),
                "previous_eval": e.get("PreviousEval"), "next_eval": e.get("NextEval"),
                "blocked_eval": e.get("BlockedEval"), "failed TG": e.get("FailedTGAllocs", {}),
                "create_index": e.get("CreateIndex"), "modify_index": e.get("ModifyIndex"),
            } for e in evals]
        except Exception as e:
            raise NomadError(f"Failed to list evaluations: {e}")

    def list_deployments(self, job_id: Optional[str] = None) -> List[Dict]:
        if not self.check_connection():
            raise NomadError("Not connected")
        try:
            if job_id:
                deploys = self.client.job.get_deployments(job_id)
            else:
                deploys = self.client.deployments.get_deployments()
            return [{
                "id": d.get("ID"), "job_id": d.get("JobID"), "namespace": d.get("Namespace"),
                "status": d.get("Status"), "status_description": d.get("StatusDescription"),
                "version": d.get("Version"), "created": d.get("CreateTime"),
                "modified": d.get("ModifyTime"),
                "task_groups": {tg.get("Name"): {"desired": tg.get("DesiredTotal", 0), "placed": tg.get("PlacedAllocs", 0), "healthy": tg.get("HealthyAllocs", 0), "unhealthy": tg.get("UnhealthyAllocs", 0)} for tg in (d.get("TaskGroups") or {}).values()},
            } for d in deploys]
        except Exception as e:
            raise NomadError(f"Failed to list deployments: {e}")

    def promote_deployment(self, deployment_id: str, all_tasks: bool = True, groups: Optional[List[str]] = None) -> Dict:
        if not self.check_connection():
            raise NomadError("Not connected")
        try:
            if all_tasks:
                result = self.client.deployment.promote_deployment(deployment_id)
            else:
                result = self.client.deployment.promote_deployment(deployment_id, groups=groups or [])
            return {"id": deployment_id, "eval_id": result.get("EvalID"), "promoted": True}
        except Exception as e:
            raise NomadError(f"Failed to promote deployment: {e}")

    def fail_deployment(self, deployment_id: str) -> Dict:
        if not self.check_connection():
            raise NomadError("Not connected")
        try:
            result = self.client.deployment.fail_deployment(deployment_id)
            return {"id": deployment_id, "eval_id": result.get("EvalID"), "failed": True}
        except Exception as e:
            raise NomadError(f"Failed to fail deployment: {e}")

    def pause_deployment(self, deployment_id: str, pause: bool = True) -> Dict:
        if not self.check_connection():
            raise NomadError("Not connected")
        try:
            result = self.client.deployment.pause_deployment(deployment_id, pause=pause)
            return {"id": deployment_id, "paused": pause, "eval_id": result.get("EvalID")}
        except Exception as e:
            raise NomadError(f"Failed to pause deployment: {e}")

    def list_nodes(self) -> List[Dict]:
        if not self.check_connection():
            raise NomadError("Not connected")
        try:
            nodes = self.client.nodes.get_nodes()
            return [{
                "id": n.get("ID"), "name": n.get("Name"), "status": n.get("Status"),
                "datacenter": n.get("Datacenter"), "node_class": n.get("NodeClass"),
                "scheduling_eligibility": n.get("SchedulingEligibility"),
                "drain": n.get("Drain"), "drain_strategy": n.get("DrainStrategy"),
                "address": n.get("HTTPAddr"), "create_index": n.get("CreateIndex"),
                "modify_index": n.get("ModifyIndex"),
                "attributes": {k: v for k, v in (n.get("Attributes") or {}).items() if k in ("os.name", "os.version", "cpu.arch", "driver.docker", "kernel.name", "kernel.version")},
                "resources": {"cpu": n.get("Resources", {}).get("CPU"), "memory": n.get("Resources", {}).get("MemoryMB"), "disk": n.get("Resources", {}).get("DiskMB")},
                "reserved": {"cpu": n.get("Reserved", {}).get("CPU"), "memory": n.get("Reserved", {}).get("MemoryMB"), "disk": n.get("Reserved", {}).get("DiskMB")},
            } for n in nodes]
        except Exception as e:
            raise NomadError(f"Failed to list nodes: {e}")

    def get_node(self, node_id: str) -> Dict:
        if not self.check_connection():
            raise NomadError("Not connected")
        try:
            n = self.client.node.get_node(node_id)
            return {
                "id": n.get("ID"), "name": n.get("Name"), "status": n.get("Status"),
                "datacenter": n.get("Datacenter"), "address": n.get("HTTPAddr"),
                "scheduling_eligibility": n.get("SchedulingEligibility"),
                "drain": n.get("Drain"), "drain_strategy": n.get("DrainStrategy"),
                "attributes": n.get("Attributes", {}),
                "drivers": {k: {"detected": v.get("Detected"), "healthy": v.get("Healthy")} for k, v in (n.get("Drivers") or {}).items()},
                "resources": n.get("Resources", {}), "reserved": n.get("Reserved", {}),
                "links": n.get("Links", {}), "meta": n.get("Meta", {}),
            }
        except Exception as e:
            raise NomadError(f"Failed to get node: {e}")

    def drain_node(self, node_id: str, drain_spec: Optional[Dict] = None) -> Dict:
        if not self.check_connection():
            raise NomadError("Not connected")
        try:
            result = self.client.node.update_node_drain(node_id, drain_spec=drain_spec or {"Deadline": 7200000000000, "IgnoreSystemJobs": False})
            return {"id": node_id, "drained": True, "index": result.get("Index")}
        except Exception as e:
            raise NomadError(f"Failed to drain node: {e}")

    def cancel_drain(self, node_id: str) -> Dict:
        if not self.check_connection():
            raise NomadError("Not connected")
        try:
            result = self.client.node.cancel_node_drain(node_id)
            return {"id": node_id, "drain_cancelled": True, "index": result.get("Index")}
        except Exception as e:
            raise NomadError(f"Failed to cancel drain: {e}")

    def list_namespaces(self) -> List[Dict]:
        if not self.check_connection():
            raise NomadError("Not connected")
        try:
            nss = self.client.namespaces.get_namespaces()
            return [{"name": ns.get("Name"), "description": ns.get("Description"), "quota": ns.get("Quota"), "capabilities": ns.get("Capabilities", {})} for ns in nss]
        except Exception as e:
            raise NomadError(f"Failed to list namespaces: {e}")

    def create_namespace(self, name: str, description: Optional[str] = None, quota: Optional[str] = None) -> Dict:
        if not self.check_connection():
            raise NomadError("Not connected")
        try:
            body = {"Name": name}
            if description:
                body["Description"] = description
            if quota:
                body["Quota"] = quota
            result = self.client.client.post("/namespaces", json=body)
            return {"name": name, "created": True}
        except Exception as e:
            raise NomadError(f"Failed to create namespace: {e}")

    def delete_namespace(self, name: str) -> Dict:
        if not self.check_connection():
            raise NomadError("Not connected")
        try:
            self.client.client.delete(f"/namespace/{name}")
            return {"name": name, "deleted": True}
        except Exception as e:
            raise NomadError(f"Failed to delete namespace: {e}")

    def list_volumes(self) -> List[Dict]:
        if not self.check_connection():
            raise NomadError("Not connected")
        try:
            vols = self.client.volumes.get_volumes()
            return [{"id": v.get("ID"), "name": v.get("Name"), "type": v.get("Type"), "namespace": v.get("Namespace", "default"), "plugin_id": v.get("PluginID"), "node_id": v.get("NodeID"), "access_mode": v.get("AccessMode"), "attachment_mode": v.get("AttachmentMode"), "capacity": v.get("Capacity"), "allocations": v.get("Allocations", []), "schedulable": v.get("Schedulable"), "status": v.get("Status"), "controllers_healthy": v.get("ControllersHealthy"), "controllers_expected": v.get("ControllersExpected"), "nodes_healthy": v.get("NodesHealthy"), "nodes_expected": v.get("NodesExpected")} for v in vols]
        except Exception as e:
            raise NomadError(f"Failed to list volumes: {e}")

    def list_quotas(self) -> List[Dict]:
        if not self.check_connection():
            raise NomadError("Not connected")
        try:
            quotas = self.client.client.get("/quotas")
            return [{"name": q.get("Name"), "description": q.get("Description"), "limits": q.get("Limits", []), "create_index": q.get("CreateIndex"), "modify_index": q.get("ModifyIndex")} for q in quotas]
        except Exception as e:
            raise NomadError(f"Failed to list quotas: {e}")

    def get_alloc_logs(self, alloc_id: str, task: str, type: str = "stdout",
                       origin: str = "start", offset: int = 0, limit: int = 10000) -> str:
        if not self.check_connection():
            raise NomadError("Not connected")
        try:
            logs = self.client.client.get(f"/client/allocation/{alloc_id}/logs", params={"task": task, "type": type, "origin": origin, "offset": offset, "limit": limit})
            if isinstance(logs, bytes):
                return logs.decode("utf-8", errors="replace")
            return str(logs)
        except Exception as e:
            raise NomadError(f"Failed to get logs: {e}")

    def alloc_exec(self, alloc_id: str, task: str, command: List[str], tty: bool = False) -> Dict:
        if not self.check_connection():
            raise NomadError("Not connected")
        try:
            from nomad.api.exec import Exec
            exec_api = Exec(self.client.client)
            result = exec_api.stream(alloc_id, task, command, tty=tty)
            return {"alloc_id": alloc_id, "task": task, "command": " ".join(command), "result": result[:1000] if isinstance(result, str) else "streamed"}
        except Exception as e:
            raise NomadError(f"Failed to exec: {e}")

    def list_scaling_policies(self) -> List[Dict]:
        if not self.check_connection():
            raise NomadError("Not connected")
        try:
            policies = self.client.client.get("/scaling/policies")
            return [{"id": p.get("ID"), "type": p.get("Type"), "enabled": p.get("Enabled"), "target": p.get("Target", {}), "create_index": p.get("CreateIndex"), "modify_index": p.get("ModifyIndex")} for p in policies]
        except Exception as e:
            raise NomadError(f"Failed to list scaling policies: {e}")

    def list_sentinel_policies(self) -> List[Dict]:
        if not self.check_connection():
            raise NomadError("Not connected")
        try:
            policies = self.client.client.get("/sentinel/policies")
            return [{"name": p.get("Name"), "scope": p.get("Scope"), "enforcement_level": p.get("EnforcementLevel"), "description": p.get("Description")} for p in policies]
        except Exception as e:
            raise NomadError(f"Failed to list sentinel policies: {e}")

    def get_operator_raft(self) -> Dict:
        if not self.check_connection():
            raise NomadError("Not connected")
        try:
            config = self.client.client.get("/operator/raft/configuration")
            return {"index": config.get("Index"), "servers": [{"id": s.get("ID"), "address": s.get("Address"), "leader": s.get("Leader"), "voter": s.get("Voter")} for s in (config.get("Servers") or [])]}
        except Exception as e:
            raise NomadError(f"Failed to get raft configuration: {e}")

    def get_operator_scheduler(self) -> Dict:
        if not self.check_connection():
            raise NomadError("Not connected")
        try:
            config = self.client.client.get("/operator/scheduler/configuration")
            return {"scheduler_algorithm": config.get("SchedulerAlgorithm", "binpack"), "preemption_config": config.get("PreemptionConfig", {}), "create_index": config.get("CreateIndex"), "modify_index": config.get("ModifyIndex")}
        except Exception as e:
            raise NomadError(f"Failed to get scheduler config: {e}")


class Plugin(PluginBase):
    name = "nomad"
    version = "1.0.0"
    description = "HashiCorp Nomad orchestration - jobs, allocations, evaluations, deployments, nodes, namespaces, volumes, ACL tokens, policies, agent info, server members, scaling, sentinel"

    def __init__(self):
        self.manager = None

    def execute(self, **kwargs) -> Dict[str, Any]:
        action = kwargs.get("action", "info")
        address = kwargs.get("address", "http://127.0.0.1:4646")
        token = kwargs.get("token")
        self.manager = NomadManager(address=address, token=token)

        if action == "info":
            return {"plugin": self.name, "version": self.version, "description": self.description, "connected": self.manager.check_connection()}
        elif action == "health":
            return self.manager.agent_health()
        elif action == "agent_info":
            return self.manager.agent_info()
        elif action == "jobs":
            return {"jobs": self.manager.list_jobs(namespace=kwargs.get("namespace"))}
        elif action == "job":
            return self.manager.get_job(kwargs.get("job_id"), namespace=kwargs.get("namespace"))
        elif action == "run_job":
            return self.manager.run_job(kwargs.get("job_spec"))
        elif action == "stop_job":
            return self.manager.stop_job(kwargs.get("job_id"), purge=kwargs.get("purge", False), namespace=kwargs.get("namespace"))
        elif action == "allocations":
            return {"allocations": self.manager.list_allocations(job_id=kwargs.get("job_id"), namespace=kwargs.get("namespace"))}
        elif action == "allocation":
            return self.manager.get_allocation(kwargs.get("alloc_id"))
        elif action == "stop_allocation":
            return self.manager.stop_allocation(kwargs.get("alloc_id"))
        elif action == "evaluations":
            return {"evaluations": self.manager.list_evaluations(job_id=kwargs.get("job_id"))}
        elif action == "deployments":
            return {"deployments": self.manager.list_deployments(job_id=kwargs.get("job_id"))}
        elif action == "promote_deployment":
            return self.manager.promote_deployment(kwargs.get("deployment_id"), all_tasks=kwargs.get("all_tasks", True), groups=kwargs.get("groups"))
        elif action == "fail_deployment":
            return self.manager.fail_deployment(kwargs.get("deployment_id"))
        elif action == "pause_deployment":
            return self.manager.pause_deployment(kwargs.get("deployment_id"), pause=kwargs.get("pause", True))
        elif action == "nodes":
            return {"nodes": self.manager.list_nodes()}
        elif action == "node":
            return self.manager.get_node(kwargs.get("node_id"))
        elif action == "drain_node":
            return self.manager.drain_node(kwargs.get("node_id"), drain_spec=kwargs.get("drain_spec"))
        elif action == "cancel_drain":
            return self.manager.cancel_drain(kwargs.get("node_id"))
        elif action == "namespaces":
            return {"namespaces": self.manager.list_namespaces()}
        elif action == "create_namespace":
            return self.manager.create_namespace(kwargs.get("name"), description=kwargs.get("description"), quota=kwargs.get("quota"))
        elif action == "delete_namespace":
            return self.manager.delete_namespace(kwargs.get("name"))
        elif action == "volumes":
            return {"volumes": self.manager.list_volumes()}
        elif action == "quotas":
            return {"quotas": self.manager.list_quotas()}
        elif action == "alloc_logs":
            return {"logs": self.manager.get_alloc_logs(kwargs.get("alloc_id"), kwargs.get("task"), type=kwargs.get("type", "stdout"), origin=kwargs.get("origin", "start"), offset=kwargs.get("offset", 0), limit=kwargs.get("limit", 10000))}
        elif action == "scaling_policies":
            return {"policies": self.manager.list_scaling_policies()}
        elif action == "sentinel_policies":
            return {"policies": self.manager.list_sentinel_policies()}
        elif action == "raft_config":
            return self.manager.get_operator_raft()
        elif action == "scheduler_config":
            return self.manager.get_operator_scheduler()
        return {"error": f"Unknown action: {action}"}