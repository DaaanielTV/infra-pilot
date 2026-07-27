$base = "cli/ipilot/commands"

# Map of old -> new file names
$renames = @(
    # emerging/
    @{"old"="$base/emerging/confidential.py"; "new"="$base/emerging/confidential_computing.py"},
    @{"old"="$base/emerging/contracts.py"; "new"="$base/emerging/smart_contracts.py"},
    @{"old"="$base/emerging/dcn.py"; "new"="$base/emerging/decentralized_compute.py"},
    @{"old"="$base/emerging/federated.py"; "new"="$base/emerging/federated_learning.py"},
    @{"old"="$base/emerging/quantum.py"; "new"="$base/emerging/quantum_cryptography.py"},
    @{"old"="$base/emerging/storage.py"; "new"="$base/emerging/decentralized_storage.py"},
    @{"old"="$base/emerging/web3id.py"; "new"="$base/emerging/web3_identity.py"},
    @{"old"="$base/emerging/zkp.py"; "new"="$base/emerging/zero_knowledge_proofs.py"},

    # finops/
    @{"old"="$base/finops/arbitrage.py"; "new"="$base/finops/cloud_arbitrage.py"},
    @{"old"="$base/finops/carbon.py"; "new"="$base/finops/carbon_footprint.py"},
    @{"old"="$base/finops/commitment.py"; "new"="$base/finops/commitment_discounts.py"},
    @{"old"="$base/finops/reports.py"; "new"="$base/finops/cost_reports.py"},
    @{"old"="$base/finops/spot.py"; "new"="$base/finops/spot_instances.py"},
    @{"old"="$base/finops/uoe.py"; "new"="$base/finops/unit_of_energy.py"},
    @{"old"="$base/finops/waste.py"; "new"="$base/finops/waste_analysis.py"},

    # green/
    @{"old"="$base/green/efficiency.py"; "new"="$base/green/energy_efficiency.py"},
    @{"old"="$base/green/energy.py"; "new"="$base/green/energy_management.py"},
    @{"old"="$base/green/hardware.py"; "new"="$base/green/hardware_lifecycle.py"},
    @{"old"="$base/green/offset.py"; "new"="$base/green/carbon_offset.py"},
    @{"old"="$base/green/provider.py"; "new"="$base/green/provider_ranking.py"},
    @{"old"="$base/green/pue.py"; "new"="$base/green/power_usage_effectiveness.py"},
    @{"old"="$base/green/reclaim.py"; "new"="$base/green/resource_reclamation.py"},
    @{"old"="$base/green/scheduler.py"; "new"="$base/green/green_scheduler.py"},
    @{"old"="$base/green/shutdown.py"; "new"="$base/green/auto_shutdown.py"},

    # infrastructure/
    @{"old"="$base/infrastructure/deploy.py"; "new"="$base/infrastructure/deployment.py"},

    # marketplace/
    @{"old"="$base/marketplace/appmarket.py"; "new"="$base/marketplace/app_marketplace.py"},
    @{"old"="$base/marketplace/credit.py"; "new"="$base/marketplace/credits.py"},
    @{"old"="$base/marketplace/crypto.py"; "new"="$base/marketplace/cryptocurrency.py"},
    @{"old"="$base/marketplace/loyalty.py"; "new"="$base/marketplace/loyalty_program.py"},
    @{"old"="$base/marketplace/ppu.py"; "new"="$base/marketplace/price_per_unit.py"},
    @{"old"="$base/marketplace/reco.py"; "new"="$base/marketplace/recommendations.py"},
    @{"old"="$base/marketplace/reseller.py"; "new"="$base/marketplace/reseller_management.py"},
    @{"old"="$base/marketplace/tax.py"; "new"="$base/marketplace/tax_management.py"},
    @{"old"="$base/marketplace/trade.py"; "new"="$base/marketplace/trading.py"},
    @{"old"="$base/marketplace/whitelabel.py"; "new"="$base/marketplace/white_label.py"},

    # networking/
    @{"old"="$base/networking/bgp.py"; "new"="$base/networking/border_gateway_protocol.py"},
    @{"old"="$base/networking/capture.py"; "new"="$base/networking/packet_capture.py"},
    @{"old"="$base/networking/cell.py"; "new"="$base/networking/cellular_networking.py"},
    @{"old"="$base/networking/dhcp.py"; "new"="$base/networking/dynamic_host_configuration_protocol.py"},
    @{"old"="$base/networking/dns.py"; "new"="$base/networking/domain_name_system.py"},
    @{"old"="$base/networking/dnsfilter.py"; "new"="$base/networking/dns_filtering.py"},
    @{"old"="$base/networking/netcost.py"; "new"="$base/networking/network_costs.py"},
    @{"old"="$base/networking/proxy.py"; "new"="$base/networking/proxy_management.py"},
    @{"old"="$base/networking/sdwan.py"; "new"="$base/networking/software_defined_wan.py"},
    @{"old"="$base/networking/segmentation.py"; "new"="$base/networking/network_segmentation.py"},
    @{"old"="$base/networking/vpn.py"; "new"="$base/networking/virtual_private_network.py"},

    # operations/
    @{"old"="$base/operations/chaos.py"; "new"="$base/operations/chaos_engineering.py"},
    @{"old"="$base/operations/drift.py"; "new"="$base/operations/drift_detection.py"},
    @{"old"="$base/operations/healing.py"; "new"="$base/operations/self_healing.py"},
    @{"old"="$base/operations/pipelines.py"; "new"="$base/operations/deployment_pipelines.py"},
    @{"old"="$base/operations/quotas.py"; "new"="$base/operations/resource_quotas.py"},
    @{"old"="$base/operations/remediation.py"; "new"="$base/operations/auto_remediation.py"},
    @{"old"="$base/operations/runbooks.py"; "new"="$base/operations/runbook_automation.py"},
    @{"old"="$base/operations/workflow.py"; "new"="$base/operations/workflow_orchestration.py"},

    # platform/
    @{"old"="$base/platform/devportal.py"; "new"="$base/platform/developer_portal.py"},
    @{"old"="$base/platform/docgen.py"; "new"="$base/platform/document_generator.py"},
    @{"old"="$base/platform/environments.py"; "new"="$base/platform/environment_orchestrator.py"},
    @{"old"="$base/platform/pulse.py"; "new"="$base/platform/developer_pulse.py"},
    @{"old"="$base/platform/scaffold.py"; "new"="$base/platform/golden_path_scaffolder.py"},
    @{"old"="$base/platform/techdebt.py"; "new"="$base/platform/tech_debt_tracker.py"},

    # platform/resiliency/
    @{"old"="$base/platform/resiliency/backup_sla.py"; "new"="$base/platform/resiliency/backup_sla_manager.py"},
    @{"old"="$base/platform/resiliency/bc_dashboard.py"; "new"="$base/platform/resiliency/business_continuity_dashboard.py"},
    @{"old"="$base/platform/resiliency/chaos_exp.py"; "new"="$base/platform/resiliency/chaos_experiments.py"},
    @{"old"="$base/platform/resiliency/dep_sim.py"; "new"="$base/platform/resiliency/dependency_simulator.py"},
    @{"old"="$base/platform/resiliency/dr.py"; "new"="$base/platform/resiliency/disaster_recovery.py"},
    @{"old"="$base/platform/resiliency/rb_exec.py"; "new"="$base/platform/resiliency/runbook_executor.py"},
    @{"old"="$base/platform/resiliency/res_pipeline.py"; "new"="$base/platform/resiliency/resilience_pipeline.py"},
    @{"old"="$base/platform/resiliency/res_score.py"; "new"="$base/platform/resiliency/resiliency_score.py"},

    # security/
    @{"old"="$base/security/breach.py"; "new"="$base/security/breach_detection.py"},
    @{"old"="$base/security/classify.py"; "new"="$base/security/data_classification.py"},
    @{"old"="$base/security/identity.py"; "new"="$base/security/identity_management.py"},
    @{"old"="$base/security/oidc.py"; "new"="$base/security/open_id_connect.py"},
    @{"old"="$base/security/pam.py"; "new"="$base/security/privileged_access_management.py"},
    @{"old"="$base/security/policy.py"; "new"="$base/security/security_policy.py"},
    @{"old"="$base/security/sessions.py"; "new"="$base/security/session_management.py"},
    @{"old"="$base/security/soc.py"; "new"="$base/security/security_operations_center.py"},
    @{"old"="$base/security/vendor.py"; "new"="$base/security/vendor_security.py"},
    @{"old"="$base/security/webauthn.py"; "new"="$base/security/web_authn.py"}
)

# Do all git mv operations
foreach ($r in $renames) {
    $old = $r["old"]
    $new = $r["new"]
    if (Test-Path $old) {
        git mv $old $new
        Write-Host "Renamed: $old -> $new"
    } else {
        Write-Host "WARNING: $old not found"
    }
}

Write-Host "`nAll renames done. Now the __init__.py needs updating."
