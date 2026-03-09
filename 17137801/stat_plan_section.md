# Plan statistique (α = 0,05)

**Comparaisons principales** : toutes à α = 0,05 (bilatéral).

## Tests
- **Proportions** : test z à deux proportions (préférence, FCR, lint pass).
- **Moyennes** : test de Welch (variances inégales).
- **Effets** : Cohen’s d / Hedges g (moyennes), Δ points de pourcentage & Odds Ratio (proportions).
- **IC** : IC95 % (Wilson pour proportions ; IC95 pour moyennes via Welch).

## Taille d’échantillon (puissance 0,8)
- Interaction (0,58 → 0,65, Δ = 7 pp) : **N ≈ 756 par bras**.
- Éducation (0,68 → 0,73, Δ = 5 pp) : **N ≈ 1301 par bras**.
- Ingénierie (0,88 → 0,92, Δ = 4 pp) : **N ≈ 884 par bras**.

## Définition KPI (rappel)
- **CSAT** : % de notes ≥ 4/5 ; IC95 Wilson.
- **FCR** : tickets résolus à la 1ère interaction / total (fenêtre T = 24–72 h). Bien documenter T et les exclusions.
- **Préférence A/B** : part d'utilisateurs préférant ε‑mimicry vs neutre ; test z‑proportions.
- **Temps (éducation)** : moyenne ± σ ; test de Welch.
- **Lint pass** : part de commits/PR passant le lint ; test z‑proportions.
- **TTM** : p95(merge_ts – open_ts).

## Garde‑fous
- **Style‑swap** périodique pour éviter le style‑lock‑in.
- **ε‑limites** contextuelles (lexico‑syntaxique, style, plan).
- **Traçabilité C2PA** : signature **des données et des logs**.
