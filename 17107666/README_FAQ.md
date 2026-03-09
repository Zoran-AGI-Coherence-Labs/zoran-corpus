# FAQ — Zoran aSiM × France Travail (v1.3)

## Q1. Peut‑on piloter l’IA sans retoucher les poids du modèle ?
Oui. La **machine à injecteur** oriente le comportement via **profils YAML** (prompts, RAG, paramètres d’inférence, garde‑fous), plus **canary** et **rollback ΔM11.3**.

## Q2. Où sont les signatures C2PA ?
Le pack inclut le **stub** (`scripts/zoran/c2pa_stub.py`) et la procédure. En prod, appliquer la signature à chaque artefact diffusé (sorties critiques, politiques, modèles).

## Q3. Comment gère‑t‑on les biais ?
Par **SLO d’équité** (|SPD|≤0,1 ; ΔTPR/ΔFPR≤5 pts ; ECE≤2 %) + plan de tests (`annexes/fairness_test_plan.md`) et **rapports trimestriels**.

## Q4. PQC — pourquoi une triade ?
**Diversité d’hypothèses** : ML‑KEM (Kyber) + Classic McEliece + NTRU. Hybride X25519+ML‑KEM pour TLS 1.3 / mTLS. Runbook dans `annexes/pqc_runbook.md`.

## Q5. Smartphones et usage offline ?
Voir `docs/mobile/mobile_offline_guide.md` : profils **Edge** (petits modèles), caches chiffrés, **mode offline** avec synchronisation différée et **TTL** serré.

## Q6. Qu’est‑ce que Glyphnet ?
Un **protocole glyphique IA↔IA** (stubs fournis) pour marquer/injecter des métadonnées non perturbantes. Utilisé pour la **traçabilité** et la **synchronisation** de politiques.

## Q7. Puis‑je intégrer un LLM propriétaire ?
Oui, via adaptateurs. Le **Policy Engine** reste indépendant du fournisseur. Les exigences **GPAI** sont documentées (`annexes/gpai_vendor_checklist.md`).

## Q8. Quelles garanties environnementales ?
Objectif **−30 %/12 mois** (SCI). Voir `annexes/policy.yaml` et collecte `annexes/metrics.json` + plan de mutualisation/quantization.
