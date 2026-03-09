repro:
	uv run --locked main.py | tee outputs/run.txt
	cyclonedx-py --format json --output artifacts/sbom.cdx.json
	uv build
	sigstore sign dist/*.whl --bundle artifacts/whl.sigstore.json

verify:
	sigstore verify dist/*.whl --bundle artifacts/whl.sigstore.json
