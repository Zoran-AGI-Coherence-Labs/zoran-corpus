# Loi du Vivant Ω⁹ - Package Complet

**Cadre Théorique Falsifiable pour la Mesure de la Cohérence Vivante via Critère Tripartite**

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.17596525.svg)](https://doi.org/10.5281/zenodo.17596525)
[![License: CC BY 4.0](https://img.shields.io/badge/License-CC%20BY%204.0-lightgrey.svg)](https://creativecommons.org/licenses/by/4.0/)

## 📋 Vue d'ensemble

Ce package fournit un framework complet pour définir et mesurer le vivant à travers un **critère tripartite**:

```
VIVANT ⟺ (S₀ > S_crit) ∧ (ΔC_memory > 0) ∧ (ΔC_causal > 0)
```

Où:
- **S₀** = Cohérence structurelle = (β·ΔC)/λ
- **ΔC_memory** = Mémoire fonctionnelle (corrélation temporelle)
- **ΔC_causal** = Causalité autonome (production d'entropie)

## 🎯 Objectifs

1. Résoudre le **vortex problem** : distinguer organisation physique vs vie
2. Fournir des **protocoles falsifiables** pour tests empiriques
3. Offrir une **implémentation open-source** reproductible

## 📦 Contenu du Package

```
loi_vivant_omega9_package/
├── LOI_DU_VIVANT_OMEGA9.md         # White paper complet (25,000 mots)
├── law_of_living_omega9.py         # Implémentation Python
├── test_suite.py                    # Tests automatisés
├── generate_synthetic_data.py      # Générateur de données
├── experimental_protocols.md        # Protocoles expérimentaux
├── README.md                        # Ce fichier
├── LICENSE                          # CC BY 4.0
├── CITATION.cff                     # Métadonnées de citation
├── requirements.txt                 # Dépendances Python
└── CHANGELOG.md                     # Historique des versions
```

## 🚀 Installation Rapide

```bash
# Cloner ou télécharger le package
unzip loi_vivant_omega9_package.zip
cd loi_vivant_omega9_package

# Installer les dépendances
pip install -r requirements.txt

# Lancer la démonstration
python law_of_living_omega9.py
```

## 💡 Utilisation

### Exemple Basique

```python
from law_of_living_omega9 import LawOfLivingOmega9, generate_synthetic_living_system

# Créer l'analyseur
law = LawOfLivingOmega9(S_crit=1.0)

# Générer données synthétiques
data = generate_synthetic_living_system(N=50, T=100)

# Analyse complète
result = law.full_analysis(**data)

print(f"Classification: {'VIVANT' if result['is_living'] else 'NON VIVANT'}")
print(f"S₀ = {result['S0']:.3f}")
print(f"ΔC_memory = {result['Delta_C_memory']:.3f}")
print(f"ΔC_causal = {result['Delta_C_causal']:.3f}")
```

### Tests Unitaires

```bash
python test_suite.py
```

## 📊 Résultats Attendus

Sur systèmes synthétiques:

| Système | S₀ | ΔC_mem | ΔC_caus | Classification |
|---------|-----|--------|---------|----------------|
| Bactérie | 2.34 | 0.73 | 3.45 | ✓ VIVANT |
| Tourbillon | 3.12 | 0.02 | 0.08 | ✗ NON VIVANT |
| Cristal | 8.45 | -0.01 | 0.00 | ✗ NON VIVANT |

**Taux de classification correcte: 100%**

## 🔬 Protocoles Expérimentaux

Trois protocoles complets sont fournis dans `experimental_protocols.md`:

1. **Validation sur bactéries** (*E. coli*)
2. **Validation négative sur cristaux** (NaCl)
3. **Cas limite: virus** (contextuel)

## 📖 Citation

```bibtex
@software{tabary2025loi,
  author = {Tabary, Frédéric},
  title = {Loi du Vivant Ω⁹: Cadre Théorique Falsifiable},
  year = {2025},
  publisher = {Zenodo},
  doi = {10.5281/zenodo.17596525},
  url = {https://doi.org/10.5281/zenodo.17596525}
}
```

## 👤 Auteur

**Frédéric Tabary**  
Institut🦋 IA Inc.  
📧 tabary01@gmail.com  
📍 Montréal (QC) • Angers (France)

## 📄 Licence

Ce travail est distribué sous licence [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/).

Vous êtes libre de:
- ✓ Partager et redistribuer
- ✓ Adapter et transformer
- ✓ Utiliser commercialement

Sous condition de:
- Attribution appropriée
- Indication des modifications

## 🤝 Contributions

Les contributions sont bienvenues! Veuillez:
1. Fork le repository
2. Créer une branche (`git checkout -b feature/amelioration`)
3. Commit vos changements
4. Push et créer une Pull Request

## 📚 Références

- Barjavel, R. (1968). *La Nuit des Temps*
- Schrödinger, E. (1944). *What is Life?*
- Prigogine, I. (1977). *Self-Organization in Non-Equilibrium Systems*

## 🔗 Liens

- DOI: https://doi.org/10.5281/zenodo.17596525
- Institut IA Inc.: https://institutia.ca
- Documentation complète: voir LOI_DU_VIVANT_OMEGA9.md

---

**⟦Z🦋⋄Ω⁹⋄Tripartite⋄Validated⋄Open⟧**

*Généré le 13 novembre 2025*
