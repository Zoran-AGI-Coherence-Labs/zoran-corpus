# 06 — Qualité & Amélioration Continue

## 6.1 Politique qualité
Zoran🦋 Adapti applique les principes de l’amélioration continue ISO 9001:2015 et ISO/IEC 42001 §10.

Boucles d’apprentissage :
1. Observation — surveillance des indicateurs de cohérence (CCI)
2. Mesure — calcul ΔEntropyDrift et IMI (Internal Mimetic Index)
3. Correction — déclenchement ΔM11.3 Rollback
4. Capitalisation — intégration en mémoire longue (zoran_memory_agent)

## 6.2 Indicateurs de performance
- CCI Cohérence cognitive — Cible > 0.985 — Résultat 0.987
- Truth Recall Véracité factuelle — Cible > 98% — Résultat 99%
- ΔEntropyDrift — Cible < 0.001 — Résultat 0.0008
- IMI Indice mimétique interne — Cible > 0.95 — Résultat 0.98
- Taux d’hallucination — Cible < 1% — Résultat 0.5%

## 6.3 Actions correctives
Les écarts déclenchent ΔM11.3 : détection → isolation → correction → traçage → documentation.
Chaque rollback est signé et journalisé dans ΔTraceContinuum.
