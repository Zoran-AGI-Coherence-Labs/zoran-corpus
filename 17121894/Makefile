.PHONY: test sbom c2pa reproduce_all

test:
	python3 -m pytest -q

sbom:
	cyclonedx-py --format json -o sbom.cyclonedx.json

c2pa:
	c2patool sign --manifest c2pa.manifest.json --input README.md

reproduce_all: test sbom c2pa
