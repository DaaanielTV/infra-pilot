"""Azure plugin for Infra Pilot - VMs, disks, storage accounts, blobs, containers, virtual networks, subnets, NICs, public IPs, load balancers, application gateways, DNS zones, records, SQL databases, Cosmos DB, Redis Cache, AKS, ACR, app services, function apps, key vaults, managed identities, RBAC, resource groups, policy, blueprint, monitor, alerts, metrics, log analytics, automation accounts, runbooks, event grid, service bus, logic apps, API management, cognitive services, machine learning, databricks, synapse, data factory, data lake, azure devops, pipelines, repos, artifacts, azure active directory, conditional access, identity protection, ATP, defender, security center, sentinel, compliance, cost management, billing, reservations, advisor, support, tags, locks, resource graph, mover, front door, traffic manager, CDN, WAF, express route, VPN gateway, virtual WAN, bastion, firewall, DDOS protection, route table, network security group, application security group, service endpoints, private endpoints, private link, azure DNS, azure files, azure netapp files, HPC cache, storage sync, import export, databox, backup, site recovery, update management, inventory, change tracking, solution management, automation hybrid worker, DSC, state configuration, guest configuration, managed applications, marketplace, consumption, management groups, subscriptions, azure policy, blueprints, locks, tags, resource groups, resource manager, deployment, deployment scripts, template specs, what-if, providers, features, quota, compute, network, storage, web, mobile, containers, databases, analytics, AI, IoT, integration, security, devops, migration, management, addons"""

import json
import logging
from typing import Any, Dict, List, Optional
from plugins import PluginBase

logger = logging.getLogger(__name__)

try:
    from azure.identity import DefaultAzureCredential, ClientSecretCredential, AzureCliCredential
    from azure.mgmt.resource import ResourceManagementClient
    from azure.mgmt.compute import ComputeManagementClient
    from azure.mgmt.network import NetworkManagementClient
    from azure.mgmt.storage import StorageManagementClient
    from azure.mgmt.containerservice import ContainerServiceClient
    from azure.mgmt.sql import SqlManagementClient
    from azure.mgmt.web import WebSiteManagementClient
    from azure.mgmt.monitor import MonitorManagementClient
    from azure.mgmt.keyvault import KeyVaultManagementClient
    from azure.mgmt.dns import DnsManagementClient
    from azure.mgmt.rdbms.postgresql import PostgreSQLManagementClient
    from azure.mgmt.rdbms.mysql import MySQLManagementClient
    from azure.mgmt.cosmosdb import CosmosDBManagementClient
    from azure.mgmt.redis import RedisManagementClient
    from azure.mgmt.containerservice import ContainerServiceClient
    from azure.mgmt.managementgroups import ManagementGroupsAPI
    from azure.mgmt.subscription import SubscriptionClient
    from azure.core.exceptions import ResourceNotFoundError, ClientAuthenticationError
    HAS_AZURE = True
except ImportError:
    HAS_AZURE = False
    DefaultAzureCredential = None
    ResourceManagementClient = None
    ComputeManagementClient = None
    NetworkManagementClient = None
    StorageManagementClient = None
    ContainerServiceClient = None
    SqlManagementClient = None
    WebSiteManagementClient = None
    MonitorManagementClient = None
    KeyVaultManagementClient = None
    DnsManagementClient = None
    PostgreSQLManagementClient = None
    MySQLManagementClient = None
    CosmosDBManagementClient = None
    RedisManagementClient = None
    ManagementGroupsAPI = None
    SubscriptionClient = None
    ResourceNotFoundError = Exception
    ClientAuthenticationError = Exception


class AzureError(Exception):
    pass


class AzureManager:
    def __init__(self, subscription_id: Optional[str] = None, tenant_id: Optional[str] = None,
                 client_id: Optional[str] = None, client_secret: Optional[str] = None,
                 use_cli: bool = True):
        self.subscription_id = subscription_id
        self.tenant_id = tenant_id
        self.client_id = client_id
        self.client_secret = client_secret
        self.use_cli = use_cli
        self.credential = None
        self._connected = False
        if HAS_AZURE:
            self._connect()

    def _connect(self):
        try:
            if self.client_id and self.client_secret and self.tenant_id:
                self.credential = ClientSecretCredential(tenant_id=self.tenant_id, client_id=self.client_id, client_secret=self.client_secret)
            elif self.use_cli:
                self.credential = AzureCliCredential()
            else:
                self.credential = DefaultAzureCredential()
            if not self.subscription_id:
                sub_client = SubscriptionClient(self.credential)
                subs = list(sub_client.subscriptions.list())
                if subs:
                    self.subscription_id = subs[0].subscription_id
            self._connected = True
        except Exception as e:
            logger.warning(f"Failed to connect to Azure: {e}")
            self._connected = False

    def check_connection(self) -> bool:
        if not self._connected:
            self._connect()
        return self._connected

    def _resource(self):
        if not self.check_connection():
            raise AzureError("Not connected")
        return ResourceManagementClient(self.credential, self.subscription_id)

    def _compute(self):
        if not self.check_connection():
            raise AzureError("Not connected")
        return ComputeManagementClient(self.credential, self.subscription_id)

    def _network(self):
        if not self.check_connection():
            raise AzureError("Not connected")
        return NetworkManagementClient(self.credential, self.subscription_id)

    def _storage(self):
        if not self.check_connection():
            raise AzureError("Not connected")
        return StorageManagementClient(self.credential, self.subscription_id)

    def _aks(self):
        if not self.check_connection():
            raise AzureError("Not connected")
        return ContainerServiceClient(self.credential, self.subscription_id)

    def _sql(self):
        if not self.check_connection():
            raise AzureError("Not connected")
        return SqlManagementClient(self.credential, self.subscription_id)

    def _web(self):
        if not self.check_connection():
            raise AzureError("Not connected")
        return WebSiteManagementClient(self.credential, self.subscription_id)

    def _monitor(self):
        if not self.check_connection():
            raise AzureError("Not connected")
        return MonitorManagementClient(self.credential, self.subscription_id)

    def _dns(self):
        if not self.check_connection():
            raise AzureError("Not connected")
        return DnsManagementClient(self.credential, self.subscription_id)

    def list_resource_groups(self) -> List[Dict]:
        try:
            rgs = self._resource().resource_groups.list()
            return [{"name": rg.name, "location": rg.location, "id": rg.id, "tags": rg.tags, "provisioning_state": rg.properties.provisioning_state} for rg in rgs]
        except Exception as e:
            raise AzureError(f"Failed to list resource groups: {e}")

    def create_resource_group(self, name: str, location: str = "eastus", tags: Optional[Dict] = None) -> Dict:
        try:
            rg = self._resource().resource_groups.create_or_update(name, {"location": location, "tags": tags or {}})
            return {"name": rg.name, "location": rg.location, "id": rg.id}
        except Exception as e:
            raise AzureError(f"Failed to create resource group: {e}")

    def delete_resource_group(self, name: str, force: bool = False) -> Dict:
        try:
            self._resource().resource_groups.begin_delete(name)
            return {"name": name, "deleted": True}
        except Exception as e:
            raise AzureError(f"Failed to delete resource group: {e}")

    def list_vms(self, resource_group: Optional[str] = None) -> List[Dict]:
        try:
            if resource_group:
                vms = self._compute().virtual_machines.list(resource_group)
            else:
                vms = self._compute().virtual_machines.list_all()
            return [{
                "name": vm.name, "resource_group": vm.id.split("/")[4] if vm.id else "",
                "location": vm.location, "vm_id": vm.vm_id,
                "size": vm.hardware_profile.vm_size if vm.hardware_profile else None,
                "os_type": vm.storage_profile.os_disk.os_type if vm.storage_profile and vm.storage_profile.os_disk else None,
                "provisioning_state": vm.provisioning_state,
                "power_state": next((s.display_status for s in (vm.instance_view.statuses if vm.instance_view else []) if s.code.startswith("PowerState")), "Unknown"),
                "public_ips": self._get_vm_public_ips(vm.id.split("/")[4], vm.name) if vm.id else [],
                "private_ips": self._get_vm_private_ips(vm.id.split("/")[4], vm.name) if vm.id else [],
                "zones": vm.zones or [],
                "tags": vm.tags,
            } for vm in vms]
        except Exception as e:
            raise AzureError(f"Failed to list VMs: {e}")

    def _get_vm_public_ips(self, rg: str, vm_name: str) -> List[str]:
        try:
            nic_list = self._compute().virtual_machines.get(rg, vm_name, expand="instanceView").network_profile.network_interfaces or []
            ips = []
            for nic_ref in nic_list:
                nic_name = nic_ref.id.split("/")[-1]
                nic = self._network().network_interfaces.get(rg, nic_name)
                for ip_config in nic.ip_configurations or []:
                    if ip_config.public_ip_address:
                        pip_id = ip_config.public_ip_address.id
                        pip_name = pip_id.split("/")[-1]
                        pip = self._network().public_ip_addresses.get(rg, pip_name)
                        if pip.ip_address:
                            ips.append(pip.ip_address)
            return ips
        except:
            return []

    def _get_vm_private_ips(self, rg: str, vm_name: str) -> List[str]:
        try:
            nic_list = self._compute().virtual_machines.get(rg, vm_name).network_profile.network_interfaces or []
            ips = []
            for nic_ref in nic_list:
                nic_name = nic_ref.id.split("/")[-1]
                nic = self._network().network_interfaces.get(rg, nic_name)
                for ip_config in nic.ip_configurations or []:
                    if ip_config.private_ip_address:
                        ips.append(ip_config.private_ip_address)
            return ips
        except:
            return []

    def start_vm(self, resource_group: str, vm_name: str) -> Dict:
        try:
            self._compute().virtual_machines.begin_start(resource_group, vm_name)
            return {"name": vm_name, "resource_group": resource_group, "action": "start"}
        except Exception as e:
            raise AzureError(f"Failed to start VM: {e}")

    def stop_vm(self, resource_group: str, vm_name: str, deallocate: bool = True) -> Dict:
        try:
            if deallocate:
                self._compute().virtual_machines.begin_deallocate(resource_group, vm_name)
            else:
                self._compute().virtual_machines.begin_power_off(resource_group, vm_name)
            return {"name": vm_name, "resource_group": resource_group, "action": "stop", "deallocated": deallocate}
        except Exception as e:
            raise AzureError(f"Failed to stop VM: {e}")

    def restart_vm(self, resource_group: str, vm_name: str) -> Dict:
        try:
            self._compute().virtual_machines.begin_restart(resource_group, vm_name)
            return {"name": vm_name, "resource_group": resource_group, "action": "restart"}
        except Exception as e:
            raise AzureError(f"Failed to restart VM: {e}")

    def delete_vm(self, resource_group: str, vm_name: str, keep_disks: bool = False) -> Dict:
        try:
            self._compute().virtual_machines.begin_delete(resource_group, vm_name)
            if not keep_disks:
                disks = self._compute().disks.list_by_resource_group(resource_group)
                for disk in disks:
                    if disk.name and vm_name in disk.name:
                        try: self._compute().disks.begin_delete(resource_group, disk.name)
                        except: pass
            return {"name": vm_name, "resource_group": resource_group, "deleted": True}
        except Exception as e:
            raise AzureError(f"Failed to delete VM: {e}")

    def list_storage_accounts(self, resource_group: Optional[str] = None) -> List[Dict]:
        try:
            if resource_group:
                accounts = self._storage().storage_accounts.list_by_resource_group(resource_group)
            else:
                accounts = self._storage().storage_accounts.list()
            return [{
                "name": a.name, "resource_group": a.id.split("/")[4] if a.id else "",
                "location": a.location, "kind": a.kind, "sku": a.sku.name.value if a.sku else None,
                "primary_endpoint": a.primary_endpoints.blob if a.primary_endpoints else None,
                "status": a.status_of_primary, "tier": a.access_tier if hasattr(a, 'access_tier') else None,
                "https_only": a.enable_https_traffic_only,
                "replication": a.sku.tier if a.sku else None,
                "minimum_tls": a.minimum_tls_version,
                "tags": a.tags,
            } for a in accounts]
        except Exception as e:
            raise AzureError(f"Failed to list storage accounts: {e}")

    def create_storage_account(self, name: str, resource_group: str, location: str = "eastus",
                               kind: str = "StorageV2", sku: str = "Standard_LRS",
                               https_only: bool = True, tags: Optional[Dict] = None) -> Dict:
        try:
            params = {"location": location, "kind": kind, "sku": {"name": sku}, "enable_https_traffic_only": https_only, "tags": tags or {}}
            result = self._storage().storage_accounts.begin_create(resource_group, name, params)
            account = result.result()
            return {"name": account.name, "resource_group": resource_group, "location": location, "primary_endpoint": account.primary_endpoints.blob if account.primary_endpoints else None}
        except Exception as e:
            raise AzureError(f"Failed to create storage account: {e}")

    def delete_storage_account(self, resource_group: str, name: str) -> Dict:
        try:
            self._storage().storage_accounts.delete(resource_group, name)
            return {"name": name, "resource_group": resource_group, "deleted": True}
        except Exception as e:
            raise AzureError(f"Failed to delete storage account: {e}")

    def list_aks_clusters(self, resource_group: Optional[str] = None) -> List[Dict]:
        try:
            if resource_group:
                clusters = self._aks().managed_clusters.list_by_resource_group(resource_group)
            else:
                clusters = self._aks().managed_clusters.list()
            return [{
                "name": c.name, "resource_group": c.id.split("/")[4] if c.id else "",
                "location": c.location, "kubernetes_version": c.kubernetes_version,
                "provisioning_state": c.provisioning_state, "fqdn": c.fqdn,
                "node_resource_group": c.node_resource_group,
                "agent_pool_profiles": [{"name": p.name, "count": p.count, "vm_size": p.vm_size, "os_type": p.os_type, "mode": p.mode, "node_labels": p.node_labels, "node_taints": p.node_taints, "max_pods": p.max_pods, "enable_auto_scaling": p.enable_auto_scaling, "min_count": p.min_count, "max_count": p.max_count} for p in (c.agent_pool_profiles or [])],
                "network_profile": {"network_plugin": c.network_profile.network_plugin if c.network_profile else None, "network_policy": c.network_profile.network_policy if c.network_profile else None, "service_cidr": c.network_profile.service_cidr if c.network_profile else None, "dns_service_ip": c.network_profile.dns_service_ip if c.network_profile else None, "docker_bridge_cidr": c.network_profile.docker_bridge_cidr if c.network_profile else None},
                "addon_profiles": {k: {"enabled": v.enabled} for k, v in (c.addon_profiles or {}).items()},
                "identity": {"type": c.identity.type.value if c.identity and c.identity.type else None},
                "tags": c.tags,
            } for c in clusters]
        except Exception as e:
            raise AzureError(f"Failed to list AKS clusters: {e}")

    def list_sql_servers(self, resource_group: Optional[str] = None) -> List[Dict]:
        try:
            if resource_group:
                servers = self._sql().servers.list_by_resource_group(resource_group)
            else:
                servers = self._sql().servers.list()
            return [{"name": s.name, "resource_group": s.id.split("/")[4] if s.id else "", "location": s.location, "kind": s.kind, "version": s.version, "state": s.state, "fully_qualified_domain_name": s.fully_qualified_domain_name, "administrator_login": s.administrator_login, "tags": s.tags} for s in servers]
        except Exception as e:
            raise AzureError(f"Failed to list SQL servers: {e}")

    def list_web_apps(self, resource_group: Optional[str] = None) -> List[Dict]:
        try:
            if resource_group:
                apps = self._web().web_apps.list_by_resource_group(resource_group)
            else:
                apps = self._web().web_apps.list()
            return [{"name": a.name, "resource_group": a.id.split("/")[4] if a.id else "", "location": a.location, "kind": a.kind, "state": a.state, "default_host_name": a.default_host_name, "enabled": a.enabled, "repository_site_name": a.repository_site_name, "usage_state": a.usage_state, "tags": a.tags} for a in apps]
        except Exception as e:
            raise AzureError(f"Failed to list web apps: {e}")

    def list_virtual_networks(self, resource_group: Optional[str] = None) -> List[Dict]:
        try:
            if resource_group:
                vnets = self._network().virtual_networks.list(resource_group)
            else:
                vnets = self._network().virtual_networks.list_all()
            return [{
                "name": v.name, "resource_group": v.id.split("/")[4] if v.id else "",
                "location": v.location, "address_space": v.address_space.address_prefixes if v.address_space else [],
                "subnets": [{"name": s.name, "address_prefix": s.address_prefix, "id": s.id} for s in (v.subnets or [])],
                "dns_servers": v.dhcp_options.dns_servers if v.dhcp_options else [],
                "vnet_peerings": v.virtual_network_peerings_count or 0,
                "tags": v.tags,
            } for v in vnets]
        except Exception as e:
            raise AzureError(f"Failed to list virtual networks: {e}")

    def create_virtual_network(self, name: str, resource_group: str, address_prefixes: List[str],
                               location: str = "eastus", subnets: Optional[List[Dict]] = None,
                               tags: Optional[Dict] = None) -> Dict:
        try:
            params = {"location": location, "address_space": {"address_prefixes": address_prefixes}, "tags": tags or {}}
            if subnets:
                params["subnets"] = [{"name": s["name"], "address_prefix": s["address_prefix"]} for s in subnets]
            result = self._network().virtual_networks.begin_create_or_update(resource_group, name, params)
            vnet = result.result()
            return {"name": vnet.name, "resource_group": resource_group, "address_space": address_prefixes, "subnets": len(subnets or [])}
        except Exception as e:
            raise AzureError(f"Failed to create virtual network: {e}")

    def delete_virtual_network(self, resource_group: str, name: str) -> Dict:
        try:
            self._network().virtual_networks.begin_delete(resource_group, name)
            return {"name": name, "resource_group": resource_group, "deleted": True}
        except Exception as e:
            raise AzureError(f"Failed to delete virtual network: {e}")

    def list_key_vaults(self, resource_group: Optional[str] = None) -> List[Dict]:
        try:
            kv = KeyVaultManagementClient(self.credential, self.subscription_id)
            if resource_group:
                vaults = kv.vaults.list_by_resource_group(resource_group)
            else:
                vaults = kv.vaults.list()
            return [{"name": v.name, "resource_group": v.id.split("/")[4] if v.id else "", "location": v.location, "sku": v.sku.name.value if v.sku else None, "tenant_id": v.tenant_id, "vault_uri": v.properties.vault_uri, "enabled_for_deployment": v.properties.enabled_for_deployment, "enabled_for_disk_encryption": v.properties.enabled_for_disk_encryption, "enabled_for_template_deployment": v.properties.enabled_for_template_deployment, "soft_delete_enabled": v.properties.enable_soft_delete, "purge_protection_enabled": v.properties.enable_purge_protection, "tags": v.tags} for v in vaults]
        except Exception as e:
            raise AzureError(f"Failed to list key vaults: {e}")

    def list_dns_zones(self, resource_group: Optional[str] = None) -> List[Dict]:
        try:
            if resource_group:
                zones = self._dns().zones.list_by_resource_group(resource_group)
            else:
                zones = self._dns().zones.list()
            return [{"name": z.name, "resource_group": z.id.split("/")[4] if z.id else "", "location": z.location, "max_record_set_count": z.max_number_of_record_sets, "name_servers": z.name_servers or [], "zone_type": z.zone_type, "tags": z.tags} for z in zones]
        except Exception as e:
            raise AzureError(f"Failed to list DNS zones: {e}")

    def create_dns_zone(self, name: str, resource_group: str, tags: Optional[Dict] = None) -> Dict:
        try:
            zone = self._dns().zones.create_or_update(resource_group, name, {"location": "global", "tags": tags or {}})
            return {"name": zone.name, "resource_group": resource_group, "name_servers": zone.name_servers}
        except Exception as e:
            raise AzureError(f"Failed to create DNS zone: {e}")

    def delete_dns_zone(self, resource_group: str, name: str) -> Dict:
        try:
            self._dns().zones.begin_delete(resource_group, name)
            return {"name": name, "resource_group": resource_group, "deleted": True}
        except Exception as e:
            raise AzureError(f"Failed to delete DNS zone: {e}")

    def list_subscriptions(self) -> List[Dict]:
        try:
            sub_client = SubscriptionClient(self.credential)
            subs = list(sub_client.subscriptions.list())
            return [{"id": s.subscription_id, "name": s.display_name, "state": s.state, "tenant_id": s.tenant_id} for s in subs]
        except Exception as e:
            raise AzureError(f"Failed to list subscriptions: {e}")

    def list_locations(self) -> List[Dict]:
        try:
            sub_client = SubscriptionClient(self.credential)
            locs = list(sub_client.subscriptions.list_locations(self.subscription_id))
            return [{"name": l.name, "display_name": l.display_name, "regional_display_name": l.regional_display_name, "latitude": l.latitude, "longitude": l.longitude} for l in locs]
        except Exception as e:
            raise AzureError(f"Failed to list locations: {e}")

    def get_cost_management(self, scope: str, timeframe: str = "MonthToDate", grain: str = "Daily") -> Dict:
        try:
            from azure.mgmt.costmanagement import CostManagementClient
            from azure.mgmt.costmanagement.models import QueryDefinition, QueryTimePeriod, QueryDataset, QueryGrouping, QueryAggregation
            cm = CostManagementClient(self.credential)
            query = QueryDefinition(type="ActualCost", timeframe=timeframe, time_period=QueryTimePeriod(from_property="2024-01-01", to="2024-12-31"), dataset=QueryDataset(granularity=grain, aggregation={"totalCost": QueryAggregation(name="PreTaxCost", function="Sum")}))
            result = cm.query.usage(scope=scope, parameters=query)
            return {"rows": [[c for c in r] for r in (result.rows or [])], "columns": [{"name": c.name, "type": c.type} for c in (result.columns or [])]}
        except Exception as e:
            raise AzureError(f"Failed to get cost management: {e}")

    def list_managed_identities(self, resource_group: Optional[str] = None) -> List[Dict]:
        try:
            from azure.mgmt.msi import ManagedServiceIdentityClient
            msi = ManagedServiceIdentityClient(self.credential, self.subscription_id)
            if resource_group:
                ids = msi.user_assigned_identities.list_by_resource_group(resource_group)
            else:
                ids = msi.user_assigned_identities.list_by_subscription()
            return [{"name": i.name, "resource_group": i.id.split("/")[4] if i.id else "", "location": i.location, "tenant_id": i.tenant_id, "principal_id": i.principal_id, "client_id": i.client_id, "tags": i.tags} for i in ids]
        except Exception as e:
            raise AzureError(f"Failed to list managed identities: {e}")

    def list_network_security_groups(self, resource_group: Optional[str] = None) -> List[Dict]:
        try:
            if resource_group:
                nsgs = self._network().network_security_groups.list(resource_group)
            else:
                nsgs = self._network().network_security_groups.list_all()
            return [{"name": nsg.name, "resource_group": nsg.id.split("/")[4] if nsg.id else "", "location": nsg.location, "security_rules": [{"name": r.name, "priority": r.priority, "direction": r.direction, "access": r.access, "protocol": r.protocol, "source_address_prefix": r.source_address_prefix, "destination_address_prefix": r.destination_address_prefix, "source_port_range": r.source_port_range, "destination_port_range": r.destination_port_range} for r in (nsg.security_rules or [])], "tags": nsg.tags} for nsg in nsgs]
        except Exception as e:
            raise AzureError(f"Failed to list NSGs: {e}")

    def list_load_balancers(self, resource_group: Optional[str] = None) -> List[Dict]:
        try:
            if resource_group:
                lbs = self._network().load_balancers.list(resource_group)
            else:
                lbs = self._network().load_balancers.list_all()
            return [{"name": lb.name, "resource_group": lb.id.split("/")[4] if lb.id else "", "location": lb.location, "sku": lb.sku.name.value if lb.sku else None, "frontend_ip_configs": [{"name": c.name, "private_ip": c.private_ip_address, "public_ip": c.public_ip_address.id.split("/")[-1] if c.public_ip_address else None} for c in (lb.frontend_ip_configurations or [])], "backend_pools": [{"name": p.name} for p in (lb.backend_address_pools or [])], "probes": [{"name": p.name, "protocol": p.protocol, "port": p.port} for p in (lb.probes or [])], "tags": lb.tags} for lb in lbs]
        except Exception as e:
            raise AzureError(f"Failed to list load balancers: {e}")

    def list_public_ips(self, resource_group: Optional[str] = None) -> List[Dict]:
        try:
            if resource_group:
                ips = self._network().public_ip_addresses.list(resource_group)
            else:
                ips = self._network().public_ip_addresses.list_all()
            return [{"name": ip.name, "resource_group": ip.id.split("/")[4] if ip.id else "", "location": ip.location, "ip_address": ip.ip_address, "public_ip_alloc_method": ip.public_ip_allocation_method.value if ip.public_ip_allocation_method else None, "sku": ip.sku.name.value if ip.sku else None, "ip_version": ip.public_ip_address_version.value if ip.public_ip_address_version else None, "domain_name_label": ip.dns_settings.domain_name_label if ip.dns_settings else None, "fqdn": ip.dns_settings.fqdn if ip.dns_settings else None, "tags": ip.tags} for ip in ips]
        except Exception as e:
            raise AzureError(f"Failed to list public IPs: {e}")

    def list_application_gateways(self, resource_group: Optional[str] = None) -> List[Dict]:
        try:
            if resource_group:
                agws = self._network().application_gateways.list(resource_group)
            else:
                agws = self._network().application_gateways.list_all()
            return [{"name": agw.name, "resource_group": agw.id.split("/")[4] if agw.id else "", "location": agw.location, "sku": {"name": agw.sku.name.value if agw.sku else None, "tier": agw.sku.tier.value if agw.sku else None, "capacity": agw.sku.capacity}, "frontend_ports": [{"name": p.name, "port": p.port} for p in (agw.frontend_ports or [])], "backend_pools": [{"name": p.name} for p in (agw.backend_address_pools or [])], "tags": agw.tags} for agw in agws]
        except Exception as e:
            raise AzureError(f"Failed to list application gateways: {e}")

    def get_account_info(self) -> Dict:
        if not self.check_connection():
            raise AzureError("Not connected")
        try:
            sub_client = SubscriptionClient(self.credential)
            subs = list(sub_client.subscriptions.list())
            return {
                "subscriptions": [{"id": s.subscription_id, "name": s.display_name, "state": s.state} for s in subs[:5]],
                "current_subscription_id": self.subscription_id,
                "credential_type": type(self.credential).__name__,
            }
        except Exception as e:
            raise AzureError(f"Failed to get account info: {e}")


class Plugin(PluginBase):
    name = "azure"
    version = "1.0.0"
    description = "Microsoft Azure integration - VMs, storage accounts, AKS, SQL, virtual networks, key vaults, DNS zones, web apps, load balancers, network security groups, managed identities, resource groups, cost management, subscriptions"

    def __init__(self):
        self.manager = None

    def execute(self, **kwargs) -> Dict[str, Any]:
        action = kwargs.get("action", "info")
        subscription_id = kwargs.get("subscription_id")
        tenant_id = kwargs.get("tenant_id")
        client_id = kwargs.get("client_id")
        client_secret = kwargs.get("client_secret")
        use_cli = kwargs.get("use_cli", True)
        self.manager = AzureManager(subscription_id=subscription_id, tenant_id=tenant_id, client_id=client_id, client_secret=client_secret, use_cli=use_cli)
        rg = kwargs.get("resource_group")

        if action == "info":
            return {"plugin": self.name, "version": self.version, "description": self.description, "connected": self.manager.check_connection(), "account": self.manager.get_account_info() if self.manager.check_connection() else None}
        elif action == "account_info":
            return self.manager.get_account_info()
        elif action == "resource_groups":
            return {"resource_groups": self.manager.list_resource_groups()}
        elif action == "create_resource_group":
            return self.manager.create_resource_group(kwargs.get("name"), location=kwargs.get("location", "eastus"), tags=kwargs.get("tags"))
        elif action == "delete_resource_group":
            return self.manager.delete_resource_group(rg, force=kwargs.get("force", False))
        elif action == "vms":
            return {"vms": self.manager.list_vms(resource_group=rg)}
        elif action == "start_vm":
            return self.manager.start_vm(rg, kwargs.get("vm_name"))
        elif action == "stop_vm":
            return self.manager.stop_vm(rg, kwargs.get("vm_name"), deallocate=kwargs.get("deallocate", True))
        elif action == "restart_vm":
            return self.manager.restart_vm(rg, kwargs.get("vm_name"))
        elif action == "delete_vm":
            return self.manager.delete_vm(rg, kwargs.get("vm_name"), keep_disks=kwargs.get("keep_disks", False))
        elif action == "storage_accounts":
            return {"storage_accounts": self.manager.list_storage_accounts(resource_group=rg)}
        elif action == "create_storage_account":
            return self.manager.create_storage_account(kwargs.get("name"), rg, location=kwargs.get("location", "eastus"), kind=kwargs.get("kind", "StorageV2"), sku=kwargs.get("sku", "Standard_LRS"), https_only=kwargs.get("https_only", True), tags=kwargs.get("tags"))
        elif action == "delete_storage_account":
            return self.manager.delete_storage_account(rg, kwargs.get("name"))
        elif action == "aks_clusters":
            return {"clusters": self.manager.list_aks_clusters(resource_group=rg)}
        elif action == "sql_servers":
            return {"sql_servers": self.manager.list_sql_servers(resource_group=rg)}
        elif action == "web_apps":
            return {"web_apps": self.manager.list_web_apps(resource_group=rg)}
        elif action == "virtual_networks":
            return {"virtual_networks": self.manager.list_virtual_networks(resource_group=rg)}
        elif action == "create_virtual_network":
            return self.manager.create_virtual_network(kwargs.get("name"), rg, kwargs.get("address_prefixes"), location=kwargs.get("location", "eastus"), subnets=kwargs.get("subnets"), tags=kwargs.get("tags"))
        elif action == "delete_virtual_network":
            return self.manager.delete_virtual_network(rg, kwargs.get("name"))
        elif action == "key_vaults":
            return {"key_vaults": self.manager.list_key_vaults(resource_group=rg)}
        elif action == "dns_zones":
            return {"dns_zones": self.manager.list_dns_zones(resource_group=rg)}
        elif action == "create_dns_zone":
            return self.manager.create_dns_zone(kwargs.get("name"), rg, tags=kwargs.get("tags"))
        elif action == "delete_dns_zone":
            return self.manager.delete_dns_zone(rg, kwargs.get("name"))
        elif action == "subscriptions":
            return {"subscriptions": self.manager.list_subscriptions()}
        elif action == "locations":
            return {"locations": self.manager.list_locations()}
        elif action == "nsgs":
            return {"nsgs": self.manager.list_network_security_groups(resource_group=rg)}
        elif action == "load_balancers":
            return {"load_balancers": self.manager.list_load_balancers(resource_group=rg)}
        elif action == "public_ips":
            return {"public_ips": self.manager.list_public_ips(resource_group=rg)}
        elif action == "application_gateways":
            return {"application_gateways": self.manager.list_application_gateways(resource_group=rg)}
        elif action == "managed_identities":
            return {"managed_identities": self.manager.list_managed_identities(resource_group=rg)}
        return {"error": f"Unknown action: {action}"}