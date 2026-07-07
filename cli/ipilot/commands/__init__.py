"""Command modules are registered here and discovered by the CLI."""
from ..core.command_registry import register

# Infrastructure (4)
from .infrastructure.server import app as server_app
from .infrastructure.backup import app as backup_app
from .infrastructure.deploy import app as deploy_app
from .infrastructure.logs import app as logs_app
register("server", "Server management commands")(server_app)
register("backup", "Backup management")(backup_app)
register("deploy", "Deployment commands")(deploy_app)
register("logs", "Log management")(logs_app)

# Edge & IoT (8)
from .edge_computing.edge import app as edge_app
from .edge_computing.functions import app as fn_app
from .edge_computing.ml import app as ml_app
from .edge_computing.iot import app as iot_app
from .edge_computing.cdn import app as cdn_app
from .edge_computing.mesh import app as mesh_app
from .edge_computing.lorawan import app as gw_app
from .edge_computing.pipeline import app as pipeline_app
register("edge", "Edge device management")(edge_app)
register("fn", "Edge function management")(fn_app)
register("ml", "Edge ML management")(ml_app)
register("iot", "IoT provisioning")(iot_app)
register("cdn", "Edge CDN management")(cdn_app)
register("mesh", "Mesh network management")(mesh_app)
register("gw", "LoRaWAN gateway management")(gw_app)
register("pipeline", "IoT data pipeline")(pipeline_app)

# Green Computing (10)
from .green.energy import app as energy_app
from .green.carbon import app as carbon_app
from .green.scheduler import app as green_app
from .green.reclaim import app as reclaim_app
from .green.shutdown import app as shutdown_app
from .green.hardware import app as hardware_app
from .green.pue import app as pue_app
from .green.provider import app as provider_app
from .green.offset import app as offset_app
from .green.efficiency import app as efficiency_app
register("energy", "Energy consumption")(energy_app)
register("carbon", "Carbon footprint")(carbon_app)
register("green", "Green scheduling")(green_app)
register("reclaim", "Idle resource reclamation")(reclaim_app)
register("shutdown", "Auto-shutdown policies")(shutdown_app)
register("hardware", "Hardware lifecycle")(hardware_app)
register("pue", "PUE/DCIM")(pue_app)
register("provider", "Provider rankings")(provider_app)
register("offset", "CO2 offset")(offset_app)
register("efficiency", "Efficiency scorecards")(efficiency_app)

# Networking (12)
from .networking.sdwan import app as sdwan_app
from .networking.vpn import app as vpn_app
from .networking.dns import app as dns_app
from .networking.bgp import app as bgp_app
from .networking.proxy import app as proxy_app
from .networking.segmentation import app as segment_app
from .networking.capture import app as capture_app
from .networking.dnsfilter import app as dnsfilter_app
from .networking.dhcp import app as dhcp_app
from .networking.netcost import app as netcost_app
from .networking.cell import app as cell_app
register("sdwan", "SD-WAN management")(sdwan_app)
register("vpn", "VPN management")(vpn_app)
register("dns", "DNS management")(dns_app)
register("bgp", "BGP management")(bgp_app)
register("proxy", "Reverse proxy management")(proxy_app)
register("segment", "Network segmentation")(segment_app)
register("capture", "Packet capture")(capture_app)
register("dnsfilter", "DNS filtering")(dnsfilter_app)
register("dhcp", "DHCP management")(dhcp_app)
register("netcost", "Network cost")(netcost_app)
register("cell", "5G/LTE management")(cell_app)

# Security & Identity (12)
from .security.identity import app as identity_app
from .security.oidc import app as oidc_app
from .security.webauthn import app as webauthn_app
from .security.sessions import app as sessions_app
from .security.pam import app as pam_app
from .security.breach import app as breach_app
from .security.policy import app as policy_app
from .security.compliance import app as compliance_app
from .security.audit import app as audit_app
from .security.classify import app as classify_app
from .security.vendor import app as vendor_app
from .security.soc import app as soc_app
# login and logout are registered as flat commands in main.py
register("oidc", "OIDC client management")(oidc_app)
register("webauthn", "WebAuthn credential management")(webauthn_app)
register("session", "Session management")(sessions_app)
register("pam", "Privileged access management")(pam_app)
register("breach", "Breach notification")(breach_app)
register("policy", "Policy as code")(policy_app)
register("compliance", "Compliance scanning")(compliance_app)
register("audit", "Audit analytics")(audit_app)
register("classify", "Data classification")(classify_app)
register("vendor", "Vendor risk management")(vendor_app)

register("soc", "Security operations center")(soc_app)

# Orchestration / Operations
from .operations.workflow import app as workflow_app
from .operations.pipelines import app as infra_pipeline_app
from .operations.drift import app as drift_app
from .operations.quotas import app as quota_app
from .operations.remediation import app as remediate_app
from .operations.maintenance import app as maintenance_app
from .operations.runbooks import app as runbook_app
from .operations.chaos import app as chaos_app
from .operations.healing import app as heal_app
register("workflow", "Workflow automation")(workflow_app)
register("infra-pipeline", "CI/CD pipelines")(infra_pipeline_app)
register("drift", "Drift detection")(drift_app)
register("quota", "Resource quota management")(quota_app)
register("remediate", "Auto-remediation")(remediate_app)
register("maintenance", "Maintenance scheduling")(maintenance_app)
register("runbook", "Runbook templates")(runbook_app)
register("chaos", "Chaos engineering")(chaos_app)
register("heal", "Self-healing")(heal_app)

# AIOps (10 + 11 v6)
from .aiops.rca import app as rca_app
from .aiops.dem import app as dem_app
from .aiops.alert import app as alert_app
from .aiops.scaling import app as scaling_app
from .aiops.health import app as health_forecast_app
from .aiops.assistant import app as assistant_app
from .aiops.change import app as change_app
from .aiops.capacity import app as capacity_app
from .aiops.chatbot import app as chatbot_app
from .aiops.v6.alert_corr import app as alert_corr_app
from .aiops.v6.rca_v6 import app as rca_v6_app
from .aiops.v6.capacity_v6 import app as capacity_v6_app
from .aiops.v6.change_risk import app as change_risk_app
from .aiops.v6.convo import app as convo_app
from .aiops.v6.dex import app as dex_app
from .aiops.v6.health_f import app as health_f_app
from .aiops.v6.incident import app as incident_app
from .aiops.v6.ops import app as ops_app
from .aiops.v6.scaling_v6 import app as scaling_v6_app
register("rca", "Root cause analysis")(rca_app)
register("dem", "Digital experience monitoring")(dem_app)
register("alert", "Alert correlation")(alert_app)
register("scaling", "Predictive scaling")(scaling_app)
register("health-f", "Health forecasting")(health_forecast_app)
register("assistant", "Ops assistant")(assistant_app)
register("change", "Change risk analysis")(change_app)
register("capacity", "Capacity planning")(capacity_app)
register("chatbot", "Ops chatbot")(chatbot_app)
register("alert-corr", "Alert correlation v6")(alert_corr_app)
register("rca-v6", "Root cause analysis v6")(rca_v6_app)
register("capacity-v6", "Capacity planning v6")(capacity_v6_app)
register("change-risk", "Change risk v6")(change_risk_app)
register("convo", "Conversational ops v6")(convo_app)
register("dex", "Digital experience v6")(dex_app)
register("health-v6", "Health forecasting v6")(health_f_app)
register("incident", "Incident remediation v6")(incident_app)
register("ops", "Ops chatbot v6")(ops_app)
register("scaling-v6", "Predictive scaling v6")(scaling_v6_app)

# FinOps (parent app with nested sub-apps)
from .finops import app as finops_app
register("finops", "FinOps management")(finops_app)

# CX (parent app with nested sub-apps)
from .cx import app as cx_app
register("cx", "Customer experience")(cx_app)

# Marketplace (13)
from .marketplace.trade import app as trade_app
from .marketplace.appmarket import app as appmarket_app
from .marketplace.ppu import app as ppu_app
from .marketplace.reseller import app as reseller_app
from .marketplace.whitelabel import app as whitelabel_app
from .marketplace.sla import app as mkt_sla_app
from .marketplace.credit import app as credit_app
from .marketplace.crypto import app as crypto_app
from .marketplace.plans import app as plans_app
from .marketplace.reco import app as reco_app
from .marketplace.tax import app as tax_app
from .marketplace.loyalty import app as loyalty_app
register("trade", "Resource trading")(trade_app)
register("appmarket", "App marketplace")(appmarket_app)
register("ppu", "Pay-per-use")(ppu_app)
register("reseller", "Reseller management")(reseller_app)
register("whitelabel", "White-label settings")(whitelabel_app)
register("sla", "SLA management")(mkt_sla_app)
register("credit", "SLA credits")(credit_app)
register("crypto", "Crypto payments")(crypto_app)
register("plans", "Subscription plans")(plans_app)
register("reco", "Recommendations")(reco_app)
register("tax", "Tax automation")(tax_app)
register("loyalty", "Loyalty program")(loyalty_app)

# Platform Engineering (11)
from .platform.devportal import app as devportal_app
from .platform.scaffold import app as scaffold_app
from .platform.service_catalog import app as catalog_app
from .platform.scorecards import app as scorecards_app
from .platform.template_registry import app as templatereg_app
from .platform.techdebt import app as techdebt_app
from .platform.environments import app as environments_app
from .platform.api_catalog import app as apicatalog_app
from .platform.docgen import app as docgen_app
from .platform.pulse import app as pulse_app
register("devportal", "Developer portal")(devportal_app)
register("scaffold", "Golden path scaffolding")(scaffold_app)
register("service-catalog", "Service catalog")(catalog_app)
register("scorecards", "DORA scorecards")(scorecards_app)
register("template-registry", "Template registry")(templatereg_app)
register("techdebt", "Tech debt management")(techdebt_app)
register("environments", "Ephemeral environments")(environments_app)
register("api-catalog", "API catalog")(apicatalog_app)
register("docgen", "Doc generator")(docgen_app)
register("pulse", "Developer pulse")(pulse_app)

# Compliance v2 (10)
from .compliance_v2.cc import app as cc_app
from .compliance_v2.evidence import app as evidence_app
from .compliance_v2.cac import app as cac_app
from .compliance_v2.attest import app as attest_app
from .compliance_v2.vcom import app as vcom_app
from .compliance_v2.regintel import app as regintel_app
from .compliance_v2.audit_mgmt import app as audit_mgmt_app
from .compliance_v2.dres import app as dres_app
from .compliance_v2.train import app as train_app
from .compliance_v2.auditor import app as auditor_app
register("cc", "Continuous compliance")(cc_app)
register("evidence", "Evidence collection")(evidence_app)
register("cac", "Compliance as code")(cac_app)
register("attest", "Attestation reports")(attest_app)
register("vcom", "Vendor compliance")(vcom_app)
register("regintel", "Regulatory intelligence")(regintel_app)
register("audit-mgmt", "Audit management")(audit_mgmt_app)
register("dres", "Data residency")(dres_app)
register("train", "Compliance training")(train_app)
register("auditor", "Auditor portal")(auditor_app)

# Emerging Tech (9)
from .emerging.blockchain import app as blockchain_app
from .emerging.storage import app as storage_app
from .emerging.quantum import app as quantum_app
from .emerging.contracts import app as contracts_app
from .emerging.web3id import app as web3id_app
from .emerging.confidential import app as confidential_app
from .emerging.federated import app as federated_app
from .emerging.zkp import app as zkp_app
from .emerging.dcn import app as dcn_app
register("blockchain", "Blockchain networks")(blockchain_app)
register("storage", "Decentralized storage")(storage_app)
register("quantum", "Quantum-safe")(quantum_app)
register("contracts", "Smart contracts")(contracts_app)
register("web3id", "Web3 identity")(web3id_app)
register("confidential", "Confidential computing")(confidential_app)
register("federated", "Federated learning")(federated_app)
register("zkp", "Zero-knowledge proofs")(zkp_app)
register("dcn", "Decentralized compute")(dcn_app)

# Resiliency (10) - in platform/resiliency/
from .platform.resiliency.dr import app as dr_app
from .platform.resiliency.active_active import app as active_active_app
from .platform.resiliency.backup_sla import app as backup_sla_app
from .platform.resiliency.chaos_exp import app as chaos_exp_app
from .platform.resiliency.res_score import app as res_score_app
from .platform.resiliency.dep_sim import app as dep_sim_app
from .platform.resiliency.rb_exec import app as rb_exec_app
from .platform.resiliency.data_integrity import app as data_integrity_app
from .platform.resiliency.res_pipeline import app as res_pipeline_app
from .platform.resiliency.bc_dashboard import app as bc_dashboard_app
register("dr", "Disaster recovery")(dr_app)
register("active-active", "Active-active regions")(active_active_app)
register("backup-sla", "Backup SLA management")(backup_sla_app)
register("chaos-exp", "Chaos experiments")(chaos_exp_app)
register("res-score", "Resilience score")(res_score_app)
register("dep-sim", "Dependency simulation")(dep_sim_app)
register("rb-exec", "Runbook execution")(rb_exec_app)
register("data-integrity", "Data integrity")(data_integrity_app)
register("res-pipeline", "Resilience pipelines")(res_pipeline_app)
register("bc-dashboard", "Business continuity dashboard")(bc_dashboard_app)
