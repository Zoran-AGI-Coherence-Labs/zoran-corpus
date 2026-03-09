PY?=python3
SEEDS=13 42 101
RUNS?=30

all: reproduce_all

setup:
	@echo "Using system Python. Ensure Python >=3.11 is available."

reproduce_all: setup
	$(PY) run_experiments.py --runs $(RUNS) --seeds $(SEEDS)
	$(PY) stats_welch.py metrics_full.json > metrics_summary.md
	@echo "Reproduction finished."

sbom:
	$(PY) gen_sbom.py > SBOM.cyclonedx.json

sign:
	@echo "Sigstore signing requires internet; placeholder here."

c2pa:
	@echo "Attach C2PA manifest requires c2patool; placeholder here."
