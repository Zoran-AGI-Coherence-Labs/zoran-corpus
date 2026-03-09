# Python Augmenté & GlyphNet Eurêka — Pack Zoran (V1, 2025-09-11)

Ce paquet contient **tout le nécessaire** pour publier et reproduire le White Paper :
- **WP.pdf** + **WP.md** (IMRaD complet + Annexes A→H).
- **Code stdlib** : `main.py`, `run_experiments.py`, modules (`zdm.py`, `glyphnet.py`, `delta_guard.py`, `eureka.py`, `logging_utils.py`).
- **Métriques** : `metrics_*.json` + `metrics_summary.md`.
- **Traçabilité** : `SBOM.cyclonedx.json`, `c2pa.manifest.json`, `slsa_provenance.json`, `INTEGRITY_MERKLE.txt`.
- **Reproductibilité** : `Makefile`, `policy.yaml`, `CITATION.cff`.
- **Docs** : `README_EN.md`, `GLOSSARY.md`, `DOIs.txt`, `CHANGELOG.md`, `ZGS_BLOCK.zgs`, `ANNEXE_H.md`.

## Usage rapide
```bash
make reproduce_all   # rejoue les expériences (stdlib only)
make sbom            # régénère le SBOM CycloneDX
make sign            # placeholder pour signatures Sigstore (offline ici)
make c2pa            # placeholder pour attacher le manifeste C2PA
```

**Note** : Les signatures cryptographiques réelles nécessitent une connexion. Ce pack inclut des **manifestes prêts‑à‑signer** et une **preuve d’intégrité locale** (Merkle). Le contenu scientifique et technique est **exhaustif** et directement publiable.
