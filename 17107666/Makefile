.PHONY: validate simulate reproduce_all
validate:
	python3 scripts/validate_policy.py policy/policy.yaml
simulate:
	python3 scripts/simulate_canary.py --policy policy/policy.yaml --metrics annexes/metrics.json
reproduce_all: validate simulate
	@echo 'Reproduction pipeline terminée (démo).'
