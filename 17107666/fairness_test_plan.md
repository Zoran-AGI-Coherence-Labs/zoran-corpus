# Plan de tests Équité (Fairness Test Plan)

## Métriques
- SPD (Statistical Parity Difference) — cible |SPD| ≤ 0,1
- ΔTPR / ΔFPR — cibles ≤ 5 points
- ECE (Expected Calibration Error) — cible ≤ 2 %

## Processus
Pré‑prod (jeux stratifés) → canary → prod (monitoring). Détection drift (PSI/KL). Remédiations (re‑weighting, ajustement des seuils, abstention). Certification tierce avant prod ; rapports trimestriels.
