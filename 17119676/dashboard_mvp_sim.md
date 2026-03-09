# Tableau de bord — Zoran Éco‑Agri v2.0 (MVP‑sim)

**Moyennes (3 parcelles)** : NDVI=0.342 · EVI=0.245 · H'=1.000 · Simpson=0.597 · Eau=4.216 kg/m³ · ΔSOC=0.033 tC/ha/an · Haies=59.3 m/ha · Connex.=0.333

**Intensité (toy)** tCO₂e/tonne ≈ 2.378

| Parcelle | Culture | NDVI | EVI | H' | 1–D (Simpson) | Eau kg/m³ | ΔSOC tC/ha/an | Haies m/ha | Connex. 0–1 |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| P1 | blé | 0.343 | 0.240 | 1.307 | 0.709 | 3.750 | 0.200 | 66.7 | 0.667 |
| P2 | orge | 0.254 | 0.172 | 1.055 | 0.637 | 4.455 | -0.150 | 53.6 | 0.333 |
| P3 | maïs | 0.429 | 0.323 | 0.637 | 0.444 | 4.444 | 0.050 | 57.7 | 0.000 |

## ROI haies (pour 100 m nouveaux)

- CAPEX : **600 €**
- Subvention/an : **100 €**
- Carbone/an : **25 €**
- Bonus rendement/an : **33 €**
- OPEX/an : **50 €**
- **Net/an : 108 €** → **Payback simple ≈ 5.56 ans**

> Hypothèses ajustables dans `dashboard_mvp_sim.json` → `roi.assumptions`.
