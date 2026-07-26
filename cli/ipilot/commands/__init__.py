"""All command modules get registered here."""

from ..core.command_registry import register

from .infrastructure.server import app as server_app
from .infrastructure.backup import app as backup_app
from .infrastructure.deploy import app as deploy_app
from .infrastructure.logs import app as logs_app

register("server", "Server management")(server_app)
register("backup", "Backup management")(backup_app)
register("deploy", "Deployment")(deploy_app)
register("logs", "Logs")(logs_app)

from .edge_computing.edge_computing import app as edge_computing_app
from .edge_computing.edge_functions import app as edge_functions_app
from .edge_computing.ml import app as ml_app
from .edge_computing.iot import app as iot_app
from .edge_computing.content_delivery_network import app as content_delivery_network_app
from .edge_computing.mesh import app as mesh_app
from .edge_computing.lorawan import app as gw_app
from .edge_computing.pipeline import app as pipeline_app

register("edge", "Edge devices")(edge_computing_app)
register("fn", "Edge functions")(edge_functions_app)
register("ml", "Machine learning")(ml_app)
register("iot", "IoT tools")(iot_app)
register("cdn", "CDN")(content_delivery_network_app)
register("mesh", "Mesh networks")(mesh_app)
register("gw", "LoRaWAN gateways")(gw_app)
register("pipeline", "Data pipelines")(pipeline_app)

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

register("energy", "Energy use")(energy_app)
register("carbon", "Carbon footprint")(carbon_app)
register("green", "Green scheduling")(green_app)
register("reclaim", "Reclaim idle resources")(reclaim_app)
register("shutdown", "Auto shutdown")(shutdown_app)
register("hardware", "Hardware")(hardware_app)
register("pue", "PUE")(pue_app)
register("provider", "Provider rankings")(provider_app)
register("offset", "CO2 offsets")(offset_app)
register("efficiency", "Efficiency")(efficiency_app)

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

register("sdwan", "SD-WAN")(sdwan_app)
register("vpn", "VPN")(vpn_app)
register("dns", "DNS")(dns_app)
register("bgp", "BGP")(bgp_app)
register("proxy", "Reverse proxy")(proxy_app)
register("segment", "Network segments")(segment_app)
register("capture", "Packet capture")(capture_app)
register("dnsfilter", "DNS filtering")(dnsfilter_app)
register("dhcp", "DHCP")(dhcp_app)
register("netcost", "Network cost")(netcost_app)
register("cell", "Cellular")(cell_app)

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

register("oidc", "OIDC")(oidc_app)
register("webauthn", "WebAuthn")(webauthn_app)
register("session", "Sessions")(sessions_app)
register("pam", "Access management")(pam_app)
register("breach", "Breach notifications")(breach_app)
register("policy", "Policy as code")(policy_app)
register("compliance", "Compliance scans")(compliance_app)
register("audit", "Audit")(audit_app)
register("classify", "Data classification")(classify_app)
register("vendor", "Vendors")(vendor_app)
register("soc", "Security")(soc_app)

from .operations.workflow import app as workflow_app
from .operations.pipelines import app as infra_pipeline_app
from .operations.drift import app as drift_app
from .operations.quotas import app as quota_app
from .operations.remediation import app as remediate_app
from .operations.maintenance import app as maintenance_app
from .operations.runbooks import app as runbook_app
from .operations.chaos import app as chaos_app
from .operations.healing import app as heal_app

register("workflow", "Workflows")(workflow_app)
register("infra-pipeline", "Pipelines")(infra_pipeline_app)
register("drift", "Drift detection")(drift_app)
register("quota", "Quotas")(quota_app)
register("remediate", "Auto fix")(remediate_app)
register("maintenance", "Maintenance")(maintenance_app)
register("runbook", "Runbooks")(runbook_app)
register("chaos", "Chaos testing")(chaos_app)
register("heal", "Self heal")(heal_app)

from .aiops.root_cause_analysis import app as root_cause_analysis_app
from .aiops.digital_experience_monitoring import app as digital_experience_monitoring_app
from .aiops.alert import app as alert_app
from .aiops.scaling import app as scaling_app
from .aiops.health import app as health_forecast_app
from .aiops.assistant import app as assistant_app
from .aiops.change import app as change_app
from .aiops.capacity import app as capacity_app
from .aiops.chatbot import app as chatbot_app
from .aiops.v6.alert_correlation import app as alert_correlation_app
from .aiops.v6.root_cause_analysis_v6 import app as root_cause_analysis_v6_app
from .aiops.v6.capacity_planning import app as capacity_planning_app
from .aiops.v6.change_risk_analysis import app as change_risk_analysis_app
from .aiops.v6.conversational_ops import app as conversational_ops_app
from .aiops.v6.digital_experience import app as digital_experience_app
from .aiops.v6.health_forecasting import app as health_forecasting_app
from .aiops.v6.incident_remediation import app as incident_remediation_app
from .aiops.v6.operations_chatbot import app as operations_chatbot_app
from .aiops.v6.predictive_scaling import app as predictive_scaling_app

register("rca", "Root cause analysis")(root_cause_analysis_app)
register("dem", "Digital experience")(digital_experience_monitoring_app)
register("alert", "Alerts")(alert_app)
register("scaling", "Scaling")(scaling_app)
register("health-f", "Health forecast")(health_forecast_app)
register("assistant", "Assistant")(assistant_app)
register("change", "Change risk")(change_app)
register("capacity", "Capacity")(capacity_app)
register("chatbot", "Chatbot")(chatbot_app)
register("alert-corr", "Alert correlation")(alert_correlation_app)
register("rca-v6", "Root cause v6")(root_cause_analysis_v6_app)
register("capacity-v6", "Capacity v6")(capacity_planning_app)
register("change-risk", "Change risk v6")(change_risk_analysis_app)
register("convo", "Conversational")(conversational_ops_app)
register("dex", "Digital exp v6")(digital_experience_app)
register("health-v6", "Health v6")(health_forecasting_app)
register("incident", "Incidents")(incident_remediation_app)
register("ops", "Ops bot")(operations_chatbot_app)
register("scaling-v6", "Scaling v6")(predictive_scaling_app)

from .finops import app as finops_app

register("finops", "FinOps")(finops_app)

from .cx import app as cx_app

register("cx", "Customer experience")(cx_app)

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

register("trade", "Trading")(trade_app)
register("appmarket", "App marketplace")(appmarket_app)
register("ppu", "Pay per use")(ppu_app)
register("reseller", "Resellers")(reseller_app)
register("whitelabel", "White label")(whitelabel_app)
register("sla", "SLAs")(mkt_sla_app)
register("credit", "Credits")(credit_app)
register("crypto", "Crypto")(crypto_app)
register("plans", "Plans")(plans_app)
register("reco", "Recommendations")(reco_app)
register("tax", "Tax")(tax_app)
register("loyalty", "Loyalty")(loyalty_app)

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
register("scaffold", "Scaffolding")(scaffold_app)
register("service-catalog", "Service catalog")(catalog_app)
register("scorecards", "Scorecards")(scorecards_app)
register("template-registry", "Template registry")(templatereg_app)
register("techdebt", "Tech debt")(techdebt_app)
register("environments", "Environments")(environments_app)
register("api-catalog", "API catalog")(apicatalog_app)
register("docgen", "Doc generator")(docgen_app)
register("pulse", "Developer pulse")(pulse_app)

from .compliance_v2.continuous_compliance import app as continuous_compliance_app
from .compliance_v2.evidence_collection import app as evidence_collection_app
from .compliance_v2.compliance_as_code import app as compliance_as_code_app
from .compliance_v2.attestation_reports import app as attestation_reports_app
from .compliance_v2.vendor_compliance import app as vendor_compliance_app
from .compliance_v2.regulatory_intelligence import app as regulatory_intelligence_app
from .compliance_v2.audit_management import app as audit_management_app
from .compliance_v2.data_residency import app as data_residency_app
from .compliance_v2.compliance_training import app as compliance_training_app
from .compliance_v2.auditor_portal import app as auditor_portal_app

register("cc", "Compliance")(continuous_compliance_app)
register("evidence", "Evidence")(evidence_collection_app)
register("cac", "Compliance as code")(compliance_as_code_app)
register("attest", "Attestation")(attestation_reports_app)
register("vcom", "Vendor compliance")(vendor_compliance_app)
register("regintel", "Regulatory intel")(regulatory_intelligence_app)
register("audit-mgmt", "Audit management")(audit_management_app)
register("dres", "Data residency")(data_residency_app)
register("train", "Compliance training")(compliance_training_app)
register("auditor", "Auditor portal")(auditor_portal_app)

from .emerging.blockchain import app as blockchain_app
from .emerging.storage import app as storage_app
from .emerging.quantum import app as quantum_app
from .emerging.contracts import app as contracts_app
from .emerging.web3id import app as web3id_app
from .emerging.confidential import app as confidential_app
from .emerging.federated import app as federated_app
from .emerging.zkp import app as zkp_app
from .emerging.dcn import app as dcn_app

register("blockchain", "Blockchain")(blockchain_app)
register("storage", "Decentralized storage")(storage_app)
register("quantum", "Quantum safe")(quantum_app)
register("contracts", "Smart contracts")(contracts_app)
register("web3id", "Web3 identity")(web3id_app)
register("confidential", "Confidential computing")(confidential_app)
register("federated", "Federated learning")(federated_app)
register("zkp", "Zero knowledge proofs")(zkp_app)
register("dcn", "Decentralized compute")(dcn_app)

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
register("active-active", "Active active")(active_active_app)
register("backup-sla", "Backup SLA")(backup_sla_app)
register("chaos-exp", "Chaos experiments")(chaos_exp_app)
register("res-score", "Resilience score")(res_score_app)
register("dep-sim", "Dependency sim")(dep_sim_app)
register("rb-exec", "Runbook exec")(rb_exec_app)
register("data-integrity", "Data integrity")(data_integrity_app)
register("res-pipeline", "Resilience pipeline")(res_pipeline_app)
register("bc-dashboard", "Business continuity")(bc_dashboard_app)


__all__: list[str] = [
    "server_app", "backup_app", "deploy_app", "logs_app",
    "edge_computing_app", "edge_functions_app", "ml_app", "iot_app", "content_delivery_network_app", "mesh_app",
    "gw_app", "pipeline_app",
    "energy_app", "carbon_app", "green_app", "reclaim_app", "shutdown_app",
    "hardware_app", "pue_app", "provider_app", "offset_app", "efficiency_app",
    "sdwan_app", "vpn_app", "dns_app", "bgp_app", "proxy_app", "segment_app",
    "capture_app", "dnsfilter_app", "dhcp_app", "netcost_app", "cell_app",
    "identity_app", "oidc_app", "webauthn_app", "sessions_app", "pam_app",
    "breach_app", "policy_app", "compliance_app", "audit_app", "classify_app",
    "vendor_app", "soc_app",
    "workflow_app", "infra_pipeline_app", "drift_app", "quota_app",
    "remediate_app", "maintenance_app", "runbook_app", "chaos_app", "heal_app",
    "root_cause_analysis_app", "digital_experience_monitoring_app", "alert_app", "scaling_app", "health_forecast_app",
    "assistant_app", "change_app", "capacity_app", "chatbot_app",
    "alert_correlation_app", "root_cause_analysis_v6_app", "capacity_planning_app", "change_risk_analysis_app",
    "conversational_ops_app", "digital_experience_app", "health_forecasting_app", "incident_remediation_app", "operations_chatbot_app",
    "predictive_scaling_app",
    "finops_app", "cx_app",
    "trade_app", "appmarket_app", "ppu_app", "reseller_app", "whitelabel_app",
    "mkt_sla_app", "credit_app", "crypto_app", "plans_app", "reco_app",
    "tax_app", "loyalty_app",
    "devportal_app", "scaffold_app", "catalog_app", "scorecards_app",
    "templatereg_app", "techdebt_app", "environments_app", "apicatalog_app",
    "docgen_app", "pulse_app",
    "continuous_compliance_app", "evidence_collection_app", "compliance_as_code_app", "attestation_reports_app", "vendor_compliance_app",
    "regulatory_intelligence_app", "audit_management_app", "data_residency_app", "compliance_training_app", "auditor_portal_app",
    "blockchain_app", "storage_app", "quantum_app", "contracts_app",
    "web3id_app", "confidential_app", "federated_app", "zkp_app", "dcn_app",
    "dr_app", "active_active_app", "backup_sla_app", "chaos_exp_app",
    "res_score_app", "dep_sim_app", "rb_exec_app", "data_integrity_app",
    "res_pipeline_app", "bc_dashboard_app",
]