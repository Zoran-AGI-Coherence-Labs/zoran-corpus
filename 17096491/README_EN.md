# Augmented Python & GlyphNet Eurêka — Zoran Pack (V1, 2025-09-11)

This bundle includes **everything** you need to publish and reproduce the White Paper:
- **WP.pdf** + **WP.md** (full IMRaD + Annexes A→H).
- **Stdlib code**: `main.py`, `run_experiments.py`, modules (`zdm.py`, `glyphnet.py`, `delta_guard.py`, `eureka.py`, `logging_utils.py`).
- **Metrics**: `metrics_*.json` + `metrics_summary.md`.
- **Traceability**: `SBOM.cyclonedx.json`, `c2pa.manifest.json`, `slsa_provenance.json`, `INTEGRITY_MERKLE.txt`.
- **Reproducibility**: `Makefile`, `policy.yaml`, `CITATION.cff`.
- **Docs**: `README_FR.md`, `GLOSSARY.md`, `DOIs.txt`, `CHANGELOG.md`, `ZGS_BLOCK.zgs`, `ANNEXE_H.md`.

## Quick start
```bash
make reproduce_all   # reruns experiments (stdlib only)
make sbom            # regenerate SBOM CycloneDX
make sign            # signature placeholder (offline here)
make c2pa            # C2PA manifest attach placeholder
```
