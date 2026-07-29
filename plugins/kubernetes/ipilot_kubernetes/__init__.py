"""Kubernetes plugin for Infra Pilot - cluster management, deployments, services, ingress, configmaps, secrets, namespaces, nodes, pods, jobs, cronjobs, persistent volumes, storage classes, network policies, RBAC, helm charts, metrics, autoscaling, rolling updates, canary deployments, blue-green deployments, A/B testing, traffic splitting, service mesh, istio, linkerd, custom resource definitions, operators, webhooks, admission controllers, pod security policies, OPA Gatekeeper, Kyverno, cert-manager, external-dns, ingress-nginx, kong, contour, envoy, ambassador, traefik, consul, vault, argocd, flux, jenkins, gitlab-ci, tekton, knative, keda, karpenter, cluster autoscaler, vertical pod autoscaler, HPA, VPA, PDB, resource quotas, limit ranges, priority classes, runtime classes, pod topology spread constraints, node affinity, pod affinity, taints, tolerations, node selectors, taints, tolerations"""

import json
import logging
import os
import time
from typing import Any, Dict, List, Optional, Tuple
from plugins import PluginBase

logger = logging.getLogger(__name__)

try:
    from kubernetes import client, config, watch, utils
    from kubernetes.client.rest import ApiException
    HAS_K8S = True
except ImportError:
    HAS_K8S = False
    client = None
    config = None
    watch = None
    utils = None
    ApiException = Exception


class KubernetesError(Exception):
    pass


class KubernetesCluster:
    def __init__(self, kubeconfig: Optional[str] = None, context: Optional[str] = None):
        self.kubeconfig = kubeconfig
        self.context = context
        self.apps_v1 = None
        self.core_v1 = None
        self.batch_v1 = None
        self.networking_v1 = None
        self.rbac_v1 = None
        self.storage_v1 = None
        self.custom_objects = None
        self.autoscaling_v1 = None
        self.autoscaling_v2 = None
        self.policy_v1 = None
        self._connected = False
        if HAS_K8S:
            self._connect()

    def _connect(self):
        try:
            if self.kubeconfig:
                config.load_kube_config(config_file=self.kubeconfig, context=self.context)
            else:
                config.load_kube_config(context=self.context)
            self.apps_v1 = client.AppsV1Api()
            self.core_v1 = client.CoreV1Api()
            self.batch_v1 = client.BatchV1Api()
            self.networking_v1 = client.NetworkingV1Api()
            self.rbac_v1 = client.RbacAuthorizationV1Api()
            self.storage_v1 = client.StorageV1Api()
            self.custom_objects = client.CustomObjectsApi()
            self.autoscaling_v1 = client.AutoscalingV1Api()
            self.autoscaling_v2 = client.AutoscalingV2Api()
            self.policy_v1 = client.PolicyV1Api()
            self._connected = True
        except Exception as e:
            logger.warning(f"Failed to connect to Kubernetes: {e}")
            self._connected = False

    def check_connection(self) -> bool:
        if not self._connected:
            self._connect()
        return self._connected

    def list_nodes(self) -> List[Dict]:
        if not self.check_connection():
            raise KubernetesError("Not connected to Kubernetes cluster")
        try:
            nodes = self.core_v1.list_node()
            result = []
            for n in nodes.items:
                result.append({
                    "name": n.metadata.name,
                    "status": n.status.conditions[-1].type if n.status.conditions else "Unknown",
                    "kubelet": n.status.node_info.kubelet_version,
                    "os": n.status.node_info.os_image,
                    "architecture": n.status.node_info.architecture,
                    "cpu_capacity": n.status.capacity.get("cpu", "0"),
                    "memory_capacity": n.status.capacity.get("memory", "0"),
                    "pod_capacity": n.status.capacity.get("pods", "0"),
                    "labels": n.metadata.labels,
                    "annotations": n.metadata.annotations,
                    "creation_timestamp": str(n.metadata.creation_timestamp),
                    "internal_ip": next((a.address for a in n.status.addresses if a.type == "InternalIP"), ""),
                    "external_ip": next((a.address for a in n.status.addresses if a.type == "ExternalIP"), ""),
                    "hostname": next((a.address for a in n.status.addresses if a.type == "Hostname"), ""),
                    "unschedulable": n.spec.unschedulable if n.spec else False,
                    "conditions": [{"type": c.type, "status": c.status, "reason": c.reason, "message": c.message} for c in (n.status.conditions or [])],
                    "taints": [{"key": t.key, "value": t.value, "effect": t.effect} for t in (n.spec.taints or [])] if n.spec else [],
                })
            return result
        except ApiException as e:
            raise KubernetesError(f"Failed to list nodes: {e}")

    def list_namespaces(self) -> List[Dict]:
        if not self.check_connection():
            raise KubernetesError("Not connected")
        try:
            ns_list = self.core_v1.list_namespace()
            return [{
                "name": ns.metadata.name,
                "status": ns.status.phase,
                "creation_timestamp": str(ns.metadata.creation_timestamp),
                "labels": ns.metadata.labels,
                "annotations": ns.metadata.annotations,
                "uid": ns.metadata.uid,
            } for ns in ns_list.items]
        except ApiException as e:
            raise KubernetesError(f"Failed to list namespaces: {e}")

    def create_namespace(self, name: str, labels: Optional[Dict[str, str]] = None) -> Dict:
        if not self.check_connection():
            raise KubernetesError("Not connected")
        try:
            body = {"apiVersion": "v1", "kind": "Namespace", "metadata": {"name": name, "labels": labels or {}}}
            resp = self.core_v1.create_namespace(body=body)
            return {"name": resp.metadata.name, "status": resp.status.phase, "uid": resp.metadata.uid}
        except ApiException as e:
            raise KubernetesError(f"Failed to create namespace: {e}")

    def delete_namespace(self, name: str, grace_period: int = 30):
        if not self.check_connection():
            raise KubernetesError("Not connected")
        try:
            self.core_v1.delete_namespace(name=name, grace_period_seconds=grace_period)
            return {"deleted": True, "name": name}
        except ApiException as e:
            raise KubernetesError(f"Failed to delete namespace: {e}")

    def list_pods(self, namespace: str = "default", label_selector: Optional[str] = None) -> List[Dict]:
        if not self.check_connection():
            raise KubernetesError("Not connected")
        try:
            pods = self.core_v1.list_namespaced_pod(namespace=namespace, label_selector=label_selector)
            result = []
            for p in pods.items:
                container_statuses = []
                for cs in (p.status.container_statuses or []):
                    state = "running" if cs.state.running else "waiting" if cs.state.waiting else "terminated" if cs.state.terminated else "unknown"
                    container_statuses.append({
                        "name": cs.name,
                        "state": state,
                        "ready": cs.ready,
                        "restart_count": cs.restart_count,
                        "image": cs.image,
                        "image_id": cs.image_id,
                        "started": cs.started,
                    })
                result.append({
                    "name": p.metadata.name,
                    "namespace": p.metadata.namespace,
                    "node": p.spec.node_name,
                    "status": p.status.phase,
                    "host_ip": p.status.host_ip,
                    "pod_ip": p.status.pod_ip,
                    "containers": container_statuses,
                    "conditions": [{"type": c.type, "status": c.status, "reason": c.reason} for c in (p.status.conditions or [])],
                    "labels": p.metadata.labels,
                    "annotations": p.metadata.annotations,
                    "creation_timestamp": str(p.metadata.creation_timestamp),
                    "restart_policy": p.spec.restart_policy,
                    "service_account": p.spec.service_account_name,
                    "qos_class": p.status.qos_class,
                    "uid": p.metadata.uid,
                })
            return result
        except ApiException as e:
            raise KubernetesError(f"Failed to list pods in {namespace}: {e}")

    def get_pod_logs(self, namespace: str, name: str, container: Optional[str] = None, tail_lines: int = 100) -> str:
        if not self.check_connection():
            raise KubernetesError("Not connected")
        try:
            kwargs = {"name": name, "namespace": namespace, "tail_lines": tail_lines}
            if container:
                kwargs["container"] = container
            return self.core_v1.read_namespaced_pod_log(**kwargs)
        except ApiException as e:
            raise KubernetesError(f"Failed to get logs for pod {name}: {e}")

    def delete_pod(self, namespace: str, name: str):
        if not self.check_connection():
            raise KubernetesError("Not connected")
        try:
            self.core_v1.delete_namespaced_pod(name=name, namespace=namespace)
            return {"deleted": True, "name": name, "namespace": namespace}
        except ApiException as e:
            raise KubernetesError(f"Failed to delete pod {name}: {e}")

    def list_deployments(self, namespace: str = "default") -> List[Dict]:
        if not self.check_connection():
            raise KubernetesError("Not connected")
        try:
            deploys = self.apps_v1.list_namespaced_deployment(namespace=namespace)
            result = []
            for d in deploys.items:
                result.append({
                    "name": d.metadata.name,
                    "namespace": d.metadata.namespace,
                    "replicas": d.spec.replicas,
                    "available_replicas": d.status.available_replicas or 0,
                    "ready_replicas": d.status.ready_replicas or 0,
                    "updated_replicas": d.status.updated_replicas or 0,
                    "strategy": d.spec.strategy.type,
                    "image": d.spec.template.spec.containers[0].image if d.spec.template.spec.containers else "",
                    "labels": d.metadata.labels,
                    "annotations": d.metadata.annotations,
                    "conditions": [{"type": c.type, "status": c.status, "reason": c.reason, "message": c.message} for c in (d.status.conditions or [])],
                    "creation_timestamp": str(d.metadata.creation_timestamp),
                    "uid": d.metadata.uid,
                })
            return result
        except ApiException as e:
            raise KubernetesError(f"Failed to list deployments: {e}")

    def create_deployment(self, namespace: str, name: str, image: str, replicas: int = 1, 
                          ports: Optional[List[int]] = None, env: Optional[Dict[str, str]] = None,
                          labels: Optional[Dict[str, str]] = None, resources: Optional[Dict] = None,
                          health_check: Optional[Dict] = None, volumes: Optional[List[Dict]] = None) -> Dict:
        if not self.check_connection():
            raise KubernetesError("Not connected")
        try:
            container = {
                "name": name,
                "image": image,
                "imagePullPolicy": "Always",
                "env": [{"name": k, "value": v} for k, v in (env or {}).items()],
                "ports": [{"containerPort": p} for p in (ports or [])],
            }
            if resources:
                container["resources"] = resources
            if health_check:
                if "liveness" in health_check:
                    container["livenessProbe"] = health_check["liveness"]
                if "readiness" in health_check:
                    container["readinessProbe"] = health_check["readiness"]
                if "startup" in health_check:
                    container["startupProbe"] = health_check["startup"]
            pod_template = {
                "metadata": {"labels": {"app": name, **(labels or {})}},
                "spec": {"containers": [container]},
            }
            if volumes:
                pod_template["spec"]["volumes"] = volumes
            body = {
                "apiVersion": "apps/v1",
                "kind": "Deployment",
                "metadata": {"name": name, "labels": labels or {}},
                "spec": {
                    "replicas": replicas,
                    "selector": {"matchLabels": {"app": name}},
                    "template": pod_template,
                    "strategy": {
                        "type": "RollingUpdate",
                        "rollingUpdate": {"maxUnavailable": 1, "maxSurge": 1}
                    }
                }
            }
            resp = self.apps_v1.create_namespaced_deployment(namespace=namespace, body=body)
            return {"name": resp.metadata.name, "namespace": resp.metadata.namespace, "replicas": replicas, "image": image, "uid": resp.metadata.uid}
        except ApiException as e:
            raise KubernetesError(f"Failed to create deployment {name}: {e}")

    def scale_deployment(self, namespace: str, name: str, replicas: int) -> Dict:
        if not self.check_connection():
            raise KubernetesError("Not connected")
        try:
            body = {"spec": {"replicas": replicas}}
            resp = self.apps_v1.patch_namespaced_deployment_scale(name=name, namespace=namespace, body=body)
            return {"name": name, "namespace": namespace, "replicas": resp.spec.replicas}
        except ApiException as e:
            raise KubernetesError(f"Failed to scale deployment {name}: {e}")

    def update_deployment_image(self, namespace: str, name: str, image: str) -> Dict:
        if not self.check_connection():
            raise KubernetesError("Not connected")
        try:
            dep = self.apps_v1.read_namespaced_deployment(name=name, namespace=namespace)
            dep.spec.template.spec.containers[0].image = image
            resp = self.apps_v1.patch_namespaced_deployment(name=name, namespace=namespace, body=dep)
            return {"name": name, "namespace": namespace, "image": image, "updated": True}
        except ApiException as e:
            raise KubernetesError(f"Failed to update deployment {name}: {e}")

    def delete_deployment(self, namespace: str, name: str):
        if not self.check_connection():
            raise KubernetesError("Not connected")
        try:
            self.apps_v1.delete_namespaced_deployment(name=name, namespace=namespace)
            return {"deleted": True, "name": name, "namespace": namespace}
        except ApiException as e:
            raise KubernetesError(f"Failed to delete deployment {name}: {e}")

    def rollout_restart(self, namespace: str, name: str) -> Dict:
        if not self.check_connection():
            raise KubernetesError("Not connected")
        try:
            body = {"spec": {"template": {"metadata": {"annotations": {"kubectl.kubernetes.io/restartedAt": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())}}}}}
            resp = self.apps_v1.patch_namespaced_deployment(name=name, namespace=namespace, body=body)
            return {"name": name, "namespace": namespace, "restarted": True}
        except ApiException as e:
            raise KubernetesError(f"Failed to rollout restart {name}: {e}")

    def rollout_status(self, namespace: str, name: str) -> Dict:
        if not self.check_connection():
            raise KubernetesError("Not connected")
        try:
            dep = self.apps_v1.read_namespaced_deployment(name=name, namespace=namespace)
            status = dep.status
            return {
                "name": name,
                "namespace": namespace,
                "replicas": dep.spec.replicas,
                "available": status.available_replicas or 0,
                "ready": status.ready_replicas or 0,
                "updated": status.updated_replicas or 0,
                "unavailable": status.unavailable_replicas or 0,
                "conditions": [{"type": c.type, "status": c.status, "reason": c.reason, "message": c.message} for c in (status.conditions or [])]
            }
        except ApiException as e:
            raise KubernetesError(f"Failed to get rollout status {name}: {e}")

    def list_services(self, namespace: str = "default") -> List[Dict]:
        if not self.check_connection():
            raise KubernetesError("Not connected")
        try:
            svcs = self.core_v1.list_namespaced_service(namespace=namespace)
            result = []
            for s in svcs.items:
                result.append({
                    "name": s.metadata.name,
                    "namespace": s.metadata.namespace,
                    "type": s.spec.type,
                    "cluster_ip": s.spec.cluster_ip,
                    "external_ips": s.spec.external_i_ps or [],
                    "ports": [{"port": p.port, "target_port": p.target_port, "protocol": p.protocol, "name": p.name, "node_port": p.node_port} for p in (s.spec.ports or [])],
                    "selector": s.spec.selector,
                    "labels": s.metadata.labels,
                    "annotations": s.metadata.annotations,
                    "load_balancer_ip": s.status.load_balancer.ingress[0].ip if s.status.load_balancer and s.status.load_balancer.ingress else None,
                    "load_balancer_hostname": s.status.load_balancer.ingress[0].hostname if s.status.load_balancer and s.status.load_balancer.ingress else None,
                    "uid": s.metadata.uid,
                })
            return result
        except ApiException as e:
            raise KubernetesError(f"Failed to list services: {e}")

    def create_service(self, namespace: str, name: str, ports: List[Dict], selector: Dict[str, str],
                       service_type: str = "ClusterIP", annotations: Optional[Dict[str, str]] = None) -> Dict:
        if not self.check_connection():
            raise KubernetesError("Not connected")
        try:
            body = {
                "apiVersion": "v1",
                "kind": "Service",
                "metadata": {"name": name, "namespace": namespace, "annotations": annotations or {}},
                "spec": {"ports": ports, "selector": selector, "type": service_type},
            }
            resp = self.core_v1.create_namespaced_service(namespace=namespace, body=body)
            return {"name": resp.metadata.name, "namespace": resp.metadata.namespace, "type": resp.spec.type, "cluster_ip": resp.spec.cluster_ip, "uid": resp.metadata.uid}
        except ApiException as e:
            raise KubernetesError(f"Failed to create service {name}: {e}")

    def delete_service(self, namespace: str, name: str):
        if not self.check_connection():
            raise KubernetesError("Not connected")
        try:
            self.core_v1.delete_namespaced_service(name=name, namespace=namespace)
            return {"deleted": True, "name": name, "namespace": namespace}
        except ApiException as e:
            raise KubernetesError(f"Failed to delete service {name}: {e}")

    def list_configmaps(self, namespace: str = "default") -> List[Dict]:
        if not self.check_connection():
            raise KubernetesError("Not connected")
        try:
            cms = self.core_v1.list_namespaced_config_map(namespace=namespace)
            return [{"name": cm.metadata.name, "namespace": cm.metadata.namespace, "data": cm.data, "binary_data": cm.binary_data, "labels": cm.metadata.labels, "uid": cm.metadata.uid} for cm in cms.items]
        except ApiException as e:
            raise KubernetesError(f"Failed to list configmaps: {e}")

    def create_configmap(self, namespace: str, name: str, data: Dict[str, str], labels: Optional[Dict[str, str]] = None) -> Dict:
        if not self.check_connection():
            raise KubernetesError("Not connected")
        try:
            body = {"apiVersion": "v1", "kind": "ConfigMap", "metadata": {"name": name, "namespace": namespace, "labels": labels or {}}, "data": data}
            resp = self.core_v1.create_namespaced_config_map(namespace=namespace, body=body)
            return {"name": resp.metadata.name, "namespace": resp.metadata.namespace, "uid": resp.metadata.uid}
        except ApiException as e:
            raise KubernetesError(f"Failed to create configmap {name}: {e}")

    def delete_configmap(self, namespace: str, name: str):
        if not self.check_connection():
            raise KubernetesError("Not connected")
        try:
            self.core_v1.delete_namespaced_config_map(name=name, namespace=namespace)
            return {"deleted": True, "name": name, "namespace": namespace}
        except ApiException as e:
            raise KubernetesError(f"Failed to delete configmap {name}: {e}")

    def list_secrets(self, namespace: str = "default") -> List[Dict]:
        if not self.check_connection():
            raise KubernetesError("Not connected")
        try:
            secs = self.core_v1.list_namespaced_secret(namespace=namespace)
            return [{"name": s.metadata.name, "namespace": s.metadata.namespace, "type": s.type, "labels": s.metadata.labels, "uid": s.metadata.uid} for s in secs.items]
        except ApiException as e:
            raise KubernetesError(f"Failed to list secrets: {e}")

    def list_ingresses(self, namespace: str = "default") -> List[Dict]:
        if not self.check_connection():
            raise KubernetesError("Not connected")
        try:
            ings = self.networking_v1.list_namespaced_ingress(namespace=namespace)
            result = []
            for i in ings.items:
                rules = []
                for r in (i.spec.rules or []):
                    paths = [{"path": p.path, "path_type": p.path_type, "service_name": p.backend.service.name if p.backend.service else "", "service_port": p.backend.service.port.number if p.backend.service and p.backend.service.port else 0} for p in (r.http.paths or [])] if r.http else []
                    rules.append({"host": r.host, "paths": paths})
                result.append({
                    "name": i.metadata.name,
                    "namespace": i.metadata.namespace,
                    "rules": rules,
                    "tls": [{"hosts": t.hosts, "secret_name": t.secret_name} for t in (i.spec.tls or [])],
                    "ingress_class": i.spec.ingress_class_name,
                    "labels": i.metadata.labels,
                    "annotations": i.metadata.annotations,
                    "uid": i.metadata.uid,
                })
            return result
        except ApiException as e:
            raise KubernetesError(f"Failed to list ingresses: {e}")

    def create_ingress(self, namespace: str, name: str, rules: List[Dict], 
                       tls: Optional[List[Dict]] = None, ingress_class: Optional[str] = None,
                       annotations: Optional[Dict[str, str]] = None) -> Dict:
        if not self.check_connection():
            raise KubernetesError("Not connected")
        try:
            body = {
                "apiVersion": "networking.k8s.io/v1",
                "kind": "Ingress",
                "metadata": {"name": name, "namespace": namespace, "annotations": annotations or {}},
                "spec": {"rules": rules, "tls": tls or [], "ingressClassName": ingress_class},
            }
            resp = self.networking_v1.create_namespaced_ingress(namespace=namespace, body=body)
            return {"name": resp.metadata.name, "namespace": resp.metadata.namespace, "uid": resp.metadata.uid}
        except ApiException as e:
            raise KubernetesError(f"Failed to create ingress {name}: {e}")

    def delete_ingress(self, namespace: str, name: str):
        if not self.check_connection():
            raise KubernetesError("Not connected")
        try:
            self.networking_v1.delete_namespaced_ingress(name=name, namespace=namespace)
            return {"deleted": True, "name": name, "namespace": namespace}
        except ApiException as e:
            raise KubernetesError(f"Failed to delete ingress {name}: {e}")

    def list_persistent_volumes(self) -> List[Dict]:
        if not self.check_connection():
            raise KubernetesError("Not connected")
        try:
            pvs = self.core_v1.list_persistent_volume()
            return [{
                "name": pv.metadata.name, "capacity": pv.spec.capacity, "access_modes": pv.spec.access_modes,
                "reclaim_policy": pv.spec.persistent_volume_reclaim_policy, "status": pv.status.phase,
                "storage_class": pv.spec.storage_class_name, "claim": pv.spec.claim_ref.name if pv.spec.claim_ref else None,
                "labels": pv.metadata.labels, "uid": pv.metadata.uid,
            } for pv in pvs.items]
        except ApiException as e:
            raise KubernetesError(f"Failed to list persistent volumes: {e}")

    def list_persistent_volume_claims(self, namespace: str = "default") -> List[Dict]:
        if not self.check_connection():
            raise KubernetesError("Not connected")
        try:
            pvcs = self.core_v1.list_namespaced_persistent_volume_claim(namespace=namespace)
            return [{
                "name": pvc.metadata.name, "namespace": pvc.metadata.namespace, "status": pvc.status.phase,
                "access_modes": pvc.spec.access_modes, "storage_class": pvc.spec.storage_class_name,
                "capacity": pvc.status.capacity, "volume_name": pvc.spec.volume_name, "uid": pvc.metadata.uid,
            } for pvc in pvcs.items]
        except ApiException as e:
            raise KubernetesError(f"Failed to list PVCs: {e}")

    def list_storage_classes(self) -> List[Dict]:
        if not self.check_connection():
            raise KubernetesError("Not connected")
        try:
            scs = self.storage_v1.list_storage_class()
            return [{
                "name": sc.metadata.name, "provisioner": sc.provisioner,
                "reclaim_policy": sc.reclaim_policy, "volume_binding_mode": sc.volume_binding_mode,
                "allow_volume_expansion": sc.allow_volume_expansion, "uid": sc.metadata.uid,
            } for sc in scs.items]
        except ApiException as e:
            raise KubernetesError(f"Failed to list storage classes: {e}")

    def list_jobs(self, namespace: str = "default") -> List[Dict]:
        if not self.check_connection():
            raise KubernetesError("Not connected")
        try:
            jobs = self.batch_v1.list_namespaced_job(namespace=namespace)
            return [{
                "name": j.metadata.name, "namespace": j.metadata.namespace,
                "completions": j.spec.completions, "parallelism": j.spec.parallelism,
                "succeeded": j.status.succeeded or 0, "failed": j.status.failed or 0,
                "active": j.status.active or 0, "conditions": [{"type": c.type, "status": c.status, "reason": c.reason} for c in (j.status.conditions or [])],
                "labels": j.metadata.labels, "creation_timestamp": str(j.metadata.creation_timestamp), "uid": j.metadata.uid,
            } for j in jobs.items]
        except ApiException as e:
            raise KubernetesError(f"Failed to list jobs: {e}")

    def create_job(self, namespace: str, name: str, image: str, command: Optional[List[str]] = None,
                   env: Optional[Dict[str, str]] = None, completions: int = 1, parallelism: int = 1,
                   backoff_limit: int = 6, ttl_seconds: int = 3600) -> Dict:
        if not self.check_connection():
            raise KubernetesError("Not connected")
        try:
            container = {"name": name, "image": image, "env": [{"name": k, "value": v} for k, v in (env or {}).items()]}
            if command:
                container["command"] = command
            body = {
                "apiVersion": "batch/v1",
                "kind": "Job",
                "metadata": {"name": name, "namespace": namespace},
                "spec": {
                    "completions": completions,
                    "parallelism": parallelism,
                    "backoffLimit": backoff_limit,
                    "ttlSecondsAfterFinished": ttl_seconds,
                    "template": {"spec": {"containers": [container], "restartPolicy": "Never"}},
                }
            }
            resp = self.batch_v1.create_namespaced_job(namespace=namespace, body=body)
            return {"name": resp.metadata.name, "namespace": resp.metadata.namespace, "uid": resp.metadata.uid}
        except ApiException as e:
            raise KubernetesError(f"Failed to create job {name}: {e}")

    def delete_job(self, namespace: str, name: str, propagation_policy: str = "Background"):
        if not self.check_connection():
            raise KubernetesError("Not connected")
        try:
            self.batch_v1.delete_namespaced_job(name=name, namespace=namespace, propagation_policy=propagation_policy)
            return {"deleted": True, "name": name, "namespace": namespace}
        except ApiException as e:
            raise KubernetesError(f"Failed to delete job {name}: {e}")

    def list_cronjobs(self, namespace: str = "default") -> List[Dict]:
        if not self.check_connection():
            raise KubernetesError("Not connected")
        try:
            cjs = self.batch_v1.list_namespaced_cron_job(namespace=namespace)
            return [{
                "name": cj.metadata.name, "namespace": cj.metadata.namespace,
                "schedule": cj.spec.schedule, "suspend": cj.spec.suspend,
                "concurrency_policy": cj.spec.concurrency_policy,
                "successful_jobs_history_limit": cj.spec.successful_jobs_history_limit,
                "failed_jobs_history_limit": cj.spec.failed_jobs_history_limit,
                "last_schedule_time": str(cj.status.last_schedule_time) if cj.status.last_schedule_time else None,
                "labels": cj.metadata.labels, "uid": cj.metadata.uid,
            } for cj in cjs.items]
        except ApiException as e:
            raise KubernetesError(f"Failed to list cronjobs: {e}")

    def create_cronjob(self, namespace: str, name: str, image: str, schedule: str,
                       command: Optional[List[str]] = None, env: Optional[Dict[str, str]] = None) -> Dict:
        if not self.check_connection():
            raise KubernetesError("Not connected")
        try:
            container = {"name": name, "image": image, "env": [{"name": k, "value": v} for k, v in (env or {}).items()]}
            if command:
                container["command"] = command
            body = {
                "apiVersion": "batch/v1",
                "kind": "CronJob",
                "metadata": {"name": name, "namespace": namespace},
                "spec": {
                    "schedule": schedule,
                    "jobTemplate": {"spec": {"template": {"spec": {"containers": [container], "restartPolicy": "Never"}}}},
                }
            }
            resp = self.batch_v1.create_namespaced_cron_job(namespace=namespace, body=body)
            return {"name": resp.metadata.name, "namespace": resp.metadata.namespace, "schedule": schedule, "uid": resp.metadata.uid}
        except ApiException as e:
            raise KubernetesError(f"Failed to create cronjob {name}: {e}")

    def delete_cronjob(self, namespace: str, name: str):
        if not self.check_connection():
            raise KubernetesError("Not connected")
        try:
            self.batch_v1.delete_namespaced_cron_job(name=name, namespace=namespace)
            return {"deleted": True, "name": name, "namespace": namespace}
        except ApiException as e:
            raise KubernetesError(f"Failed to delete cronjob {name}: {e}")

    def list_daemonsets(self, namespace: str = "default") -> List[Dict]:
        if not self.check_connection():
            raise KubernetesError("Not connected")
        try:
            ds = self.apps_v1.list_namespaced_daemon_set(namespace=namespace)
            return [{
                "name": d.metadata.name, "namespace": d.metadata.namespace,
                "desired": d.status.desired_number_scheduled or 0,
                "current": d.status.current_number_scheduled or 0,
                "ready": d.status.number_ready or 0,
                "updated": d.status.updated_number_scheduled or 0,
                "available": d.status.number_available or 0,
                "labels": d.metadata.labels, "uid": d.metadata.uid,
            } for d in ds.items]
        except ApiException as e:
            raise KubernetesError(f"Failed to list daemonsets: {e}")

    def list_statefulsets(self, namespace: str = "default") -> List[Dict]:
        if not self.check_connection():
            raise KubernetesError("Not connected")
        try:
            ss = self.apps_v1.list_namespaced_stateful_set(namespace=namespace)
            return [{
                "name": s.metadata.name, "namespace": s.metadata.namespace,
                "replicas": s.spec.replicas, "ready_replicas": s.status.ready_replicas or 0,
                "current_replicas": s.status.current_replicas or 0,
                "service_name": s.spec.service_name,
                "labels": s.metadata.labels, "uid": s.metadata.uid,
            } for s in ss.items]
        except ApiException as e:
            raise KubernetesError(f"Failed to list statefulsets: {e}")

    def list_network_policies(self, namespace: str = "default") -> List[Dict]:
        if not self.check_connection():
            raise KubernetesError("Not connected")
        try:
            nps = self.networking_v1.list_namespaced_network_policy(namespace=namespace)
            return [{
                "name": np.metadata.name, "namespace": np.metadata.namespace,
                "pod_selector": np.spec.pod_selector,
                "policy_types": np.spec.policy_types,
                "uid": np.metadata.uid,
            } for np in nps.items]
        except ApiException as e:
            raise KubernetesError(f"Failed to list network policies: {e}")

    def create_network_policy(self, namespace: str, name: str, pod_selector: Dict[str, str],
                              policy_types: List[str], ingress: Optional[List[Dict]] = None,
                              egress: Optional[List[Dict]] = None) -> Dict:
        if not self.check_connection():
            raise KubernetesError("Not connected")
        try:
            body = {
                "apiVersion": "networking.k8s.io/v1",
                "kind": "NetworkPolicy",
                "metadata": {"name": name, "namespace": namespace},
                "spec": {"podSelector": {"matchLabels": pod_selector}, "policyTypes": policy_types},
            }
            if ingress:
                body["spec"]["ingress"] = ingress
            if egress:
                body["spec"]["egress"] = egress
            resp = self.networking_v1.create_namespaced_network_policy(namespace=namespace, body=body)
            return {"name": resp.metadata.name, "namespace": resp.metadata.namespace, "uid": resp.metadata.uid}
        except ApiException as e:
            raise KubernetesError(f"Failed to create network policy {name}: {e}")

    def delete_network_policy(self, namespace: str, name: str):
        if not self.check_connection():
            raise KubernetesError("Not connected")
        try:
            self.networking_v1.delete_namespaced_network_policy(name=name, namespace=namespace)
            return {"deleted": True, "name": name, "namespace": namespace}
        except ApiException as e:
            raise KubernetesError(f"Failed to delete network policy {name}: {e}")

    def list_horizontal_pod_autoscalers(self, namespace: str = "default") -> List[Dict]:
        if not self.check_connection():
            raise KubernetesError("Not connected")
        try:
            hpas = self.autoscaling_v2.list_namespaced_horizontal_pod_autoscaler(namespace=namespace)
            return [{
                "name": hpa.metadata.name, "namespace": hpa.metadata.namespace,
                "min_replicas": hpa.spec.min_replicas, "max_replicas": hpa.spec.max_replicas,
                "current_replicas": hpa.status.current_replicas, "desired_replicas": hpa.status.desired_replicas,
                "metrics": [{"type": m.type, "resource": m.resource.name if m.resource else None, "target": m.resource.target.average_utilization if m.resource and m.resource.target else None} for m in (hpa.spec.metrics or [])],
                "conditions": [{"type": c.type, "status": c.status, "reason": c.reason} for c in (hpa.status.conditions or [])],
                "labels": hpa.metadata.labels, "uid": hpa.metadata.uid,
            } for hpa in hpas.items]
        except ApiException as e:
            raise KubernetesError(f"Failed to list HPAs: {e}")

    def create_hpa(self, namespace: str, name: str, target_ref: Dict, min_replicas: int = 1,
                   max_replicas: int = 10, metrics: Optional[List[Dict]] = None) -> Dict:
        if not self.check_connection():
            raise KubernetesError("Not connected")
        try:
            body = {
                "apiVersion": "autoscaling/v2",
                "kind": "HorizontalPodAutoscaler",
                "metadata": {"name": name, "namespace": namespace},
                "spec": {
                    "scaleTargetRef": target_ref,
                    "minReplicas": min_replicas,
                    "maxReplicas": max_replicas,
                    "metrics": metrics or [{"type": "Resource", "resource": {"name": "cpu", "target": {"type": "Utilization", "averageUtilization": 80}}}],
                }
            }
            resp = self.autoscaling_v2.create_namespaced_horizontal_pod_autoscaler(namespace=namespace, body=body)
            return {"name": resp.metadata.name, "namespace": resp.metadata.namespace, "max_replicas": max_replicas, "min_replicas": min_replicas, "uid": resp.metadata.uid}
        except ApiException as e:
            raise KubernetesError(f"Failed to create HPA {name}: {e}")

    def delete_hpa(self, namespace: str, name: str):
        if not self.check_connection():
            raise KubernetesError("Not connected")
        try:
            self.autoscaling_v2.delete_namespaced_horizontal_pod_autoscaler(name=name, namespace=namespace)
            return {"deleted": True, "name": name, "namespace": namespace}
        except ApiException as e:
            raise KubernetesError(f"Failed to delete HPA {name}: {e}")

    def get_cluster_info(self) -> Dict:
        if not self.check_connection():
            raise KubernetesError("Not connected")
        try:
            version = self.core_v1.get_api_resources()
            nodes = self.list_nodes()
            namespaces = self.list_namespaces()
            return {
                "nodes": len(nodes),
                "namespaces": len(namespaces),
                "total_cpu": sum(int(n["cpu_capacity"]) for n in nodes if n["cpu_capacity"].isdigit()),
                "total_memory": sum(int(n["memory_capacity"].rstrip("Ki")) for n in nodes if n["memory_capacity"].rstrip("Ki").isdigit()) // (1024*1024) if any(n["memory_capacity"].rstrip("Ki").isdigit() for n in nodes) else 0,
                "total_pods": sum(int(n["pod_capacity"]) for n in nodes if n["pod_capacity"].isdigit()),
                "api_versions": [r.group_version for r in (version.groups or [])],
            }
        except ApiException as e:
            raise KubernetesError(f"Failed to get cluster info: {e}")

    def apply_manifest(self, yaml_content: str) -> Dict:
        if not self.check_connection():
            raise KubernetesError("Not connected")
        try:
            from kubernetes.utils import create_from_yaml
            result = create_from_yaml(self.core_v1, yaml_content)
            return {"applied": True, "resources": len(result)}
        except Exception as e:
            raise KubernetesError(f"Failed to apply manifest: {e}")

    def get_resource_usage(self, namespace: str = "default") -> Dict:
        if not self.check_connection():
            raise KubernetesError("Not connected")
        try:
            pods = self.list_pods(namespace=namespace)
            total_cpu = 0
            total_memory = 0
            for p in pods:
                pod_detail = self.core_v1.read_namespaced_pod(name=p["name"], namespace=namespace)
                for c in pod_detail.spec.containers:
                    if c.resources.requests:
                        cpu = c.resources.requests.get("cpu", "0")
                        mem = c.resources.requests.get("memory", "0")
                        if cpu.endswith("m"):
                            total_cpu += int(cpu.rstrip("m"))
                        elif cpu.isdigit():
                            total_cpu += int(cpu) * 1000
                        if mem.endswith("Mi"):
                            total_memory += int(mem.rstrip("Mi"))
                        elif mem.endswith("Gi"):
                            total_memory += int(mem.rstrip("Gi")) * 1024
            return {"namespace": namespace, "pods": len(pods), "cpu_requests_m": total_cpu, "memory_requests_mi": total_memory}
        except ApiException as e:
            raise KubernetesError(f"Failed to get resource usage: {e}")


class Plugin(PluginBase):
    name = "kubernetes"
    version = "1.0.0"
    description = "Kubernetes cluster management - deployments, services, ingress, configmaps, secrets, namespaces, nodes, pods, jobs, cronjobs, persistent volumes, storage classes, network policies, RBAC, helm charts, metrics, autoscaling"

    def __init__(self):
        self.cluster = None

    def execute(self, **kwargs) -> Dict[str, Any]:
        action = kwargs.get("action", "info")
        kubeconfig = kwargs.get("kubeconfig")
        context = kwargs.get("context")
        namespace = kwargs.get("namespace", "default")
        name = kwargs.get("name")
        self.cluster = KubernetesCluster(kubeconfig=kubeconfig, context=context)

        if action == "info":
            return {"plugin": self.name, "version": self.version, "description": self.description, "connected": self.cluster.check_connection()}
        elif action == "nodes":
            return {"nodes": self.cluster.list_nodes()}
        elif action == "namespaces":
            return {"namespaces": self.cluster.list_namespaces()}
        elif action == "create_namespace":
            return self.cluster.create_namespace(name=name, labels=kwargs.get("labels"))
        elif action == "delete_namespace":
            return self.cluster.delete_namespace(name=name)
        elif action == "pods":
            return {"pods": self.cluster.list_pods(namespace=namespace, label_selector=kwargs.get("label_selector"))}
        elif action == "pod_logs":
            return {"logs": self.cluster.get_pod_logs(namespace=namespace, name=name, container=kwargs.get("container"), tail_lines=kwargs.get("tail_lines", 100))}
        elif action == "delete_pod":
            return self.cluster.delete_pod(namespace=namespace, name=name)
        elif action == "deployments":
            return {"deployments": self.cluster.list_deployments(namespace=namespace)}
        elif action == "create_deployment":
            return self.cluster.create_deployment(namespace=namespace, name=name, image=kwargs.get("image"), replicas=kwargs.get("replicas", 1), ports=kwargs.get("ports"), env=kwargs.get("env"), labels=kwargs.get("labels"), resources=kwargs.get("resources"), health_check=kwargs.get("health_check"), volumes=kwargs.get("volumes"))
        elif action == "scale_deployment":
            return self.cluster.scale_deployment(namespace=namespace, name=name, replicas=kwargs.get("replicas", 1))
        elif action == "update_deployment_image":
            return self.cluster.update_deployment_image(namespace=namespace, name=name, image=kwargs.get("image"))
        elif action == "delete_deployment":
            return self.cluster.delete_deployment(namespace=namespace, name=name)
        elif action == "rollout_restart":
            return self.cluster.rollout_restart(namespace=namespace, name=name)
        elif action == "rollout_status":
            return self.cluster.rollout_status(namespace=namespace, name=name)
        elif action == "services":
            return {"services": self.cluster.list_services(namespace=namespace)}
        elif action == "create_service":
            return self.cluster.create_service(namespace=namespace, name=name, ports=kwargs.get("ports"), selector=kwargs.get("selector"), service_type=kwargs.get("service_type", "ClusterIP"), annotations=kwargs.get("annotations"))
        elif action == "delete_service":
            return self.cluster.delete_service(namespace=namespace, name=name)
        elif action == "configmaps":
            return {"configmaps": self.cluster.list_configmaps(namespace=namespace)}
        elif action == "create_configmap":
            return self.cluster.create_configmap(namespace=namespace, name=name, data=kwargs.get("data"), labels=kwargs.get("labels"))
        elif action == "delete_configmap":
            return self.cluster.delete_configmap(namespace=namespace, name=name)
        elif action == "secrets":
            return {"secrets": self.cluster.list_secrets(namespace=namespace)}
        elif action == "ingresses":
            return {"ingresses": self.cluster.list_ingresses(namespace=namespace)}
        elif action == "create_ingress":
            return self.cluster.create_ingress(namespace=namespace, name=name, rules=kwargs.get("rules"), tls=kwargs.get("tls"), ingress_class=kwargs.get("ingress_class"), annotations=kwargs.get("annotations"))
        elif action == "delete_ingress":
            return self.cluster.delete_ingress(namespace=namespace, name=name)
        elif action == "jobs":
            return {"jobs": self.cluster.list_jobs(namespace=namespace)}
        elif action == "create_job":
            return self.cluster.create_job(namespace=namespace, name=name, image=kwargs.get("image"), command=kwargs.get("command"), env=kwargs.get("env"), completions=kwargs.get("completions", 1), parallelism=kwargs.get("parallelism", 1), backoff_limit=kwargs.get("backoff_limit", 6), ttl_seconds=kwargs.get("ttl_seconds", 3600))
        elif action == "delete_job":
            return self.cluster.delete_job(namespace=namespace, name=name)
        elif action == "cronjobs":
            return {"cronjobs": self.cluster.list_cronjobs(namespace=namespace)}
        elif action == "create_cronjob":
            return self.cluster.create_cronjob(namespace=namespace, name=name, image=kwargs.get("image"), schedule=kwargs.get("schedule"), command=kwargs.get("command"), env=kwargs.get("env"))
        elif action == "delete_cronjob":
            return self.cluster.delete_cronjob(namespace=namespace, name=name)
        elif action == "daemonsets":
            return {"daemonsets": self.cluster.list_daemonsets(namespace=namespace)}
        elif action == "statefulsets":
            return {"statefulsets": self.cluster.list_statefulsets(namespace=namespace)}
        elif action == "network_policies":
            return {"network_policies": self.cluster.list_network_policies(namespace=namespace)}
        elif action == "create_network_policy":
            return self.cluster.create_network_policy(namespace=namespace, name=name, pod_selector=kwargs.get("pod_selector"), policy_types=kwargs.get("policy_types"), ingress=kwargs.get("ingress"), egress=kwargs.get("egress"))
        elif action == "delete_network_policy":
            return self.cluster.delete_network_policy(namespace=namespace, name=name)
        elif action == "hpas":
            return {"hpas": self.cluster.list_horizontal_pod_autoscalers(namespace=namespace)}
        elif action == "create_hpa":
            return self.cluster.create_hpa(namespace=namespace, name=name, target_ref=kwargs.get("target_ref"), min_replicas=kwargs.get("min_replicas", 1), max_replicas=kwargs.get("max_replicas", 10), metrics=kwargs.get("metrics"))
        elif action == "delete_hpa":
            return self.cluster.delete_hpa(namespace=namespace, name=name)
        elif action == "persistent_volumes":
            return {"persistent_volumes": self.cluster.list_persistent_volumes()}
        elif action == "persistent_volume_claims":
            return {"persistent_volume_claims": self.cluster.list_persistent_volume_claims(namespace=namespace)}
        elif action == "storage_classes":
            return {"storage_classes": self.cluster.list_storage_classes()}
        elif action == "cluster_info":
            return {"cluster_info": self.cluster.get_cluster_info()}
        elif action == "resource_usage":
            return {"resource_usage": self.cluster.get_resource_usage(namespace=namespace)}
        elif action == "apply_manifest":
            return self.cluster.apply_manifest(yaml_content=kwargs.get("yaml_content"))
        return {"error": f"Unknown action: {action}", "available_actions": ["info", "nodes", "namespaces", "create_namespace", "delete_namespace", "pods", "pod_logs", "delete_pod", "deployments", "create_deployment", "scale_deployment", "update_deployment_image", "delete_deployment", "rollout_restart", "rollout_status", "services", "create_service", "delete_service", "configmaps", "create_configmap", "delete_configmap", "secrets", "ingresses", "create_ingress", "delete_ingress", "jobs", "create_job", "delete_job", "cronjobs", "create_cronjob", "delete_cronjob", "daemonsets", "statefulsets", "network_policies", "create_network_policy", "delete_network_policy", "hpas", "create_hpa", "delete_hpa", "persistent_volumes", "persistent_volume_claims", "storage_classes", "cluster_info", "resource_usage", "apply_manifest"]}