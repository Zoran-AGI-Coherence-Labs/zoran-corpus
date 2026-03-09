# Zoran aSiM × France Travail — Pack v1.3 (Audit‑Ready)

**Statut :** Prospectif / non contractuel • **Version :** 1.3 • **Horodatage :** 2025-09-12 14:25:36 UTC

Ce dépôt regroupe le **Livre blanc v1.3** (structure IMRaD) et le **pack exécutable** prêt pour revue DPO/RSSI/Juridique : 
- **Templates** (DPIA CNIL, DPA Art. 28), **runbook PQC**, **plan fairness**, **sandbox sécu+juridique**,
- **policy.yaml** unifié (AI Act/RGPD/Sécu/PQC/Environnement) + **no_go_gates.yaml**,
- **AI System Card**, **PRISMA log**, **metrics.json**, **conservation_policy.csv**, **Makefile**,
- **Scripts Python** (console injecteur, validateur, simulateur canary, glyphnet stubs).

## Démarrage rapide
```bash
# 1) Prévisualisation (local)
less whitepaper_v1_3.md

# 2) Validation de la politique (sans dépendances externes)
python3 scripts/validate_policy.py policy/policy.yaml

# 3) Simulation canary + rollback ΔM11.3 (secours)
python3 scripts/simulate_canary.py --policy policy/policy.yaml --metrics annexes/metrics.json

# 4) Console (CLI) de l'injecteur (curseurs → prompt/params)
python3 scripts/injector_console.py --profile policy/profiles/injector_demandeur.yaml --dry-run
```

## Repères de conformité (inclus)
- **AI Act & ISO/IEC 42001** (mappage dans `annexes/ai_system_card.md` + `annexes/policy.yaml`)
- **RGPD / DPIA** (`annexes/dpia_template.md`, base légale Art 6(1)(e) + consentement pour personnalisation)
- **C2PA** (empreintes à apposer lors de l’industrialisation ; stub dans `scripts/zoran/c2pa_stub.py`)
- **Fairness** (SPD, ΔTPR/ΔFPR, ECE ; seuils SLO dans `annexes/fairness_test_plan.md`)
- **PQC** (Triade Darwinienne ; runbook dans `annexes/pqc_runbook.md`)
- **Environnement** (SCI/PUE ; objectifs et collecte dans `annexes/policy.yaml` + `annexes/metrics.json`)

## Licence
- **Code** : MIT • **Docs** : CC BY‑NC 4.0 • **Marques & données** : restent la propriété de leurs titulaires.


## DOIs (Zenodo)
- [White Papers V2 — Mémoire par Absence Active](https://doi.org/10.5281/zenodo.16941007)
- [White Papers V1](https://doi.org/10.5281/zenodo.16940525)
- [Version publique V1 (titre à confirmer)](https://doi.org/10.5281/zenodo.16940299)
- [Aegis Layer – Gouvernance vivante](https://doi.org/10.5281/zenodo.16995014)
- [LinguaSynthèse](https://doi.org/10.5281/zenodo.16995226)
- [Zoran – Études sur les jumeaux v2](https://doi.org/10.5281/zenodo.16997156)
