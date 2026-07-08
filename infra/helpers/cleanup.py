from typing import Dict
from infra.naming import resolver


def teardown_resources(token: str, config: Dict[str, str]) -> Dict[str, object]:
    provider = resolver.resolve_provider(token)
    region = resolver.resolve_provider(config.get("region", "REGION_MOCK_US_EAST"))
    sku = resolver.resolve_provider(config.get("sku", "SKU_MOCK_SMALL"))
    return {
        "deleted": True,
        "provider": provider,
        "region": region,
        "sku": sku,
        "config": config,
    }