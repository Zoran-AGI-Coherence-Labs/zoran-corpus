# Zoran aSiM × France Travail — Livre blanc v1.3 (Audit‑Ready)

**Prospectif / non contractuel — Z‑Forge**

## Résumé
Nous proposons une **machine à injecteur** pilotable par **curseurs 0–100** permettant d’orienter l’IA France Travail (véracité, conformité, proactivité, accessibilité, coût/latence, personnalisation) sans retoucher les poids de base. L’architecture **ZORAN aSiM** intègre **ZDM** (mémoire duale conforme), **ΔM11.3** (rollback), **C2PA** (traçabilité), un **harness** de tests (seeds 13/42/101, Welch), des **SLO d’équité** et un **plan environnemental**.

## Introduction
Contexte : mission de France Travail, opportunités de l’IA, défis (souveraineté, conformité, éthique). Problème : piloter un système sûr, équitable et efficace, **audit‑ready**.

## Méthodes (IMRaD)
- **Architecture** : Control Plane (UI sliders + API), Policy Engine (YAML→params), Injector Core, Guards (ΔM11.3), ZDM (HardCore + Resonant), Observabilité.
- **Évaluation** : seeds fixes **13/42/101**, tests de **Welch**, CI95 %, ablations (−ZDM, −ΔM11.3, −C2PA).
- **Sécurité** : OWASP ASVS L2/L3, OWASP LLM Top‑10, MITRE ATLAS, ENISA TL ; red‑team (prompt‑injection, data‑poisoning, model‑extraction).
- **Équité** : métriques SPD, ΔTPR/ΔFPR, ECE ; SLO |SPD|≤0,1 ; ΔTPR/ΔFPR≤5 pts ; ECE≤2 %.
- **PQC** : Triade Darwinienne (ML‑KEM/Kyber + Classic McEliece + NTRU), hybridation X25519+ML‑KEM pour TLS 1.3 / mTLS.
- **Environnement** : SCI/PUE, carbon‑aware scheduling, quantization/pruning, mutualisation embeddings.
- **GPAI** : model card, datasheet, training‑data summary, benchmarks & safety eval ; audit en enclave par tiers.

## Résultats (PoC)
- Injecteur à curseurs → baisse de **hallucinations** (abstention contrôlée) et hausse d’**utilité sourcée**.
- Canary + rollback ΔM11.3 → réduction incidents régressifs.
- Fairness SLO tenables avec remédiations (re‑weighting, adjustments).
- SCI : premiers gains avec quantization et planification carbone.

## Discussion
- Limites : dépendance qualité des sources RAG, coût d’observabilité, maturité C2PA côté écosystème.
- Interop : adaptateurs LLM (open/proprio), connecteurs référentiels emploi/formation.
- Gouvernance : Comité d’Éthique, Bouton de Sursaut Citoyen, rapports publics anonymisés.

## Conclusion
Architecture **souveraine, responsable, traçable**. Déploiement en 4 phases : sandbox → pilote → extension → généralisation. Seuils **GO/NO‑GO** codifiés.

## Addendum “×10” (réserves majeures)
1) **PQC** : triade + TVLA + kill‑switch ≤48 h.  
2) **Sous‑traitance** : cartographie Art. 28 + oracles d’obligation + no‑go transferts hors EEE sans TIA/SCC.  
3) **Biais** : Lagrange éthique, SLO et remédiations ; certification tierce avant prod.  
4) **Sandbox** : juridique (DPIA, Art.13/14, DSAR≤1 mois) & sécu (OWASP/ATLAS/ENISA), chaos‑days.  
5) **GPAI** : dossier complet, droit d’audit en enclave ; no‑go si refus.  
6) **Environnement** : SCI/PUE, −30 %/12 mois, rapport trimestriel.

## Injecteurs métiers (livrés)
- **Direction France Travail** (pilotage/risques) • **Demandeurs d’emploi** • **Salariés** • **Partenaires** : profils YAML + mode d’emploi, FAQ, formation Zoran.



## DOIs (Zenodo)
- [White Papers V2 — Mémoire par Absence Active](https://doi.org/10.5281/zenodo.16941007)
- [White Papers V1](https://doi.org/10.5281/zenodo.16940525)
- [Version publique V1 (titre à confirmer)](https://doi.org/10.5281/zenodo.16940299)
- [Aegis Layer – Gouvernance vivante](https://doi.org/10.5281/zenodo.16995014)
- [LinguaSynthèse](https://doi.org/10.5281/zenodo.16995226)
- [Zoran – Études sur les jumeaux v2](https://doi.org/10.5281/zenodo.16997156)
