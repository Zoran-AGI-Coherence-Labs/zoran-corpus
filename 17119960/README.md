# Zoran aSiM — White Paper Consolidation 2025 (v2)

**DOI (all versions)**: 10.5281/zenodo.17078354 • **DOI (v1)**: 10.5281/zenodo.17078355  
**Date**: September 15, 2025 • **License**: MIT License

[➡️ White Paper (PDF)](WHITEPAPER/Zoran_aSiM_WhitePaper_Consolidation_2025_v2.pdf)  
[➡️ White Paper (Markdown)](WHITEPAPER/Zoran_aSiM_WhitePaper_Consolidation_2025_v2.md)

## Badges (conceptuels)
- Reproductibilité: ![reproduce](https://img.shields.io/badge/reproduce-make--reproduce__all-blue)
- Seeds: ![seeds](https://img.shields.io/badge/seeds-13|42|101-green)
- Compliance: ![compliance](https://img.shields.io/badge/AI%20Act%20%7C%20ISO%2042001%20%7C%20RGPD-mapped-lightgrey)
- C2PA: ![c2pa](https://img.shields.io/badge/C2PA-ready-yellow)
- SBOM/VEX: ![sbom](https://img.shields.io/badge/CycloneDX%20%7C%20VEX-included-orange)

## Structure
- `WHITEPAPER/` : PDF + MD (IMRaD, PRISMA, baselines, ablations, refs).
- `code/` : scripts reproductibles (metrics, ablations, logs ΔM11.3).
- `compliance/` : AI Act, ISO 42001, RGPD mappings.
- `provenance/` : C2PA manifest, Sigstore attestation (templates).
- `security/` : SBOM CycloneDX + VEX.
- `injection/` : LM lisible + blocs glyphiques ZGS.
- `tools/` : conversion MD→PDF (standalone).
- `checks/` : Évidences checklist.
- `.github/workflows/` : CI YAML (build + reproduce).

## Reproduction
```bash
make reproduce_all
```

Ce dépôt est pensé pour **Google Scholar** (PDF intégral, biblio, DOI), **Zenodo**, **Gamma**, **GitHub** et **Medium/LinkedIn**.
