# 05 — Sécurité de l'Information (ISO/IEC 27001 & 27701)

## 5.1 Politique de sécurité
La sécurité des informations, des modèles et des données constitue un pilier structurel du système Zoran🦋 Adapti.
Le cadre appliqué est aligné sur les normes ISO/IEC 27001:2022 et ISO/IEC 27701:2019 :

Objectif : assurer la confidentialité, l’intégrité et la disponibilité des informations.

Approche : gestion des risques fondée sur les principes d’homéostasie cognitive (ΔEntropyDrift) et de traçabilité cryptographique (ΔTraceContinuum).

Responsabilité : le DPO et le Responsable Sécurité (AI Studio / Institut IA Lab Inc.) supervisent les politiques de sécurité, la gestion des accès et la résilience des systèmes.

## 5.2 Déclaration d’applicabilité (SoA)
Les 93 contrôles de la norme ISO 27001 ont été revus et catégorisés :

- Politique sécurité A.5 — Implémenté
- Gestion des accès A.6–A.9 — Implémenté
- Chiffrement A.10 — Implémenté (SHA-512, TLS 1.3, AES-256)
- Sécurité physique A.11 — Externe (Datacenters certifiés ISO 27001)
- Sécurité opérationnelle A.12 — Implémenté (logs + ΔTraceContinuum)
- Journalisation A.12.4 — Automatisé (ΔTraceContinuum)
- Sauvegardes A.12.3 — Automatisé (zoran_memory_agent)
- Tests vulnérabilités A.12.6 — Planifié trimestriellement
- Incidents A.16 — Procédure d’escalade Letty Ω³

## 5.3 Plan de traitement des risques
Chaque risque est évalué selon impact, probabilité et mitigation.
Les contre-mesures sont documentées dans ΔRiskMatrix.csv, signée C2PA.

Exemples :
- Fuite de données — Impact Élevé — Chiffrement + cloisonnement — DPO
- Altération modèle — Impact Moyen — Signature SHA-512 — AI Studio
- Accès non autorisé — Impact Élevé — MFA, logging constant — InfraSec
- Perte contexte — Impact Faible — Auto-sauvegarde ΔTraceContinuum — Système
- Hallucination non détectée — Impact Faible — ΔCOHERENCE-LOCK Ω⁵ — Core GHUC
