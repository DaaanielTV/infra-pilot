.PHONY: verify verify-offline verify-json healthcheck

healthcheck:
	bash ./scripts/healthcheck.sh

verify:
	bash ./scripts/verify.sh

verify-offline:
	bash ./scripts/verify.sh --offline

verify-json:
	bash ./scripts/verify.sh --json
