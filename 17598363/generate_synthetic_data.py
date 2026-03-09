#!/usr/bin/env python3
"""
Générateur de données synthétiques pour Loi du Vivant Ω⁹

Auteur: Frédéric Tabary
Date: 2025-11-13
"""

import numpy as np
import matplotlib.pyplot as plt
from law_of_living_omega9 import (
    generate_synthetic_living_system,
    generate_synthetic_nonliving_system,
    LawOfLivingOmega9
)


def generate_comparative_dataset(n_samples=10, N=50, T=100):
    """
    Génère un dataset comparatif de systèmes vivants et non-vivants.
    
    Args:
        n_samples: nombre d'échantillons par catégorie
        N: nombre de composants
        T: nombre de points temporels
    
    Returns:
        dict avec données et classifications
    """
    results = {
        'living': [],
        'vortex': [],
        'crystal': [],
        'fire': []
    }
    
    law = LawOfLivingOmega9()
    
    print(f"Génération de {n_samples} échantillons par catégorie...")
    
    for i in range(n_samples):
        # Systèmes vivants
        data_living = generate_synthetic_living_system(N, T, seed=100+i)
        res_living = law.full_analysis(**data_living)
        results['living'].append(res_living)
        
        # Tourbillons
        data_vortex = generate_synthetic_nonliving_system('vortex', N, T, seed=200+i)
        res_vortex = law.full_analysis(**data_vortex)
        results['vortex'].append(res_vortex)
        
        # Cristaux
        data_crystal = generate_synthetic_nonliving_system('crystal', N, T, seed=300+i)
        res_crystal = law.full_analysis(**data_crystal)
        results['crystal'].append(res_crystal)
        
        # Feu
        data_fire = generate_synthetic_nonliving_system('fire', N, T, seed=400+i)
        res_fire = law.full_analysis(**data_fire)
        results['fire'].append(res_fire)
        
        if (i+1) % 5 == 0:
            print(f"  {i+1}/{n_samples} terminés...")
    
    print("✓ Génération terminée\n")
    
    return results


def plot_comparative_analysis(results):
    """
    Visualise l'analyse comparative des systèmes.
    
    Args:
        results: dict avec résultats par catégorie
    """
    fig, axes = plt.subplots(2, 2, figsize=(14, 10))
    fig.suptitle('Analyse Comparative - Loi du Vivant Ω⁹', fontsize=16, fontweight='bold')
    
    categories = ['living', 'vortex', 'crystal', 'fire']
    labels = ['Vivant', 'Tourbillon', 'Cristal', 'Feu']
    colors = ['green', 'blue', 'gray', 'red']
    
    # Extraction des métriques
    S0_data = [[r['S0'] for r in results[cat]] for cat in categories]
    mem_data = [[r['Delta_C_memory'] for r in results[cat]] for cat in categories]
    caus_data = [[r['Delta_C_causal'] for r in results[cat]] for cat in categories]
    living_status = [[1 if r['is_living'] else 0 for r in results[cat]] for cat in categories]
    
    # Plot 1: S₀ (Cohérence Structurelle)
    ax1 = axes[0, 0]
    bp1 = ax1.boxplot(S0_data, labels=labels, patch_artist=True)
    for patch, color in zip(bp1['boxes'], colors):
        patch.set_facecolor(color)
        patch.set_alpha(0.6)
    ax1.axhline(y=1.0, color='black', linestyle='--', label='Seuil S_crit=1.0')
    ax1.set_ylabel('S₀ (Cohérence)', fontweight='bold')
    ax1.set_title('Cohérence Structurelle')
    ax1.legend()
    ax1.grid(True, alpha=0.3)
    
    # Plot 2: ΔC_memory (Mémoire)
    ax2 = axes[0, 1]
    bp2 = ax2.boxplot(mem_data, labels=labels, patch_artist=True)
    for patch, color in zip(bp2['boxes'], colors):
        patch.set_facecolor(color)
        patch.set_alpha(0.6)
    ax2.axhline(y=0.3, color='black', linestyle='--', label='Seuil=0.3')
    ax2.set_ylabel('ΔC_memory', fontweight='bold')
    ax2.set_title('Mémoire Fonctionnelle')
    ax2.legend()
    ax2.grid(True, alpha=0.3)
    
    # Plot 3: ΔC_causal (Causalité)
    ax3 = axes[1, 0]
    bp3 = ax3.boxplot(caus_data, labels=labels, patch_artist=True)
    for patch, color in zip(bp3['boxes'], colors):
        patch.set_facecolor(color)
        patch.set_alpha(0.6)
    ax3.axhline(y=1.0, color='black', linestyle='--', label='Seuil=1.0')
    ax3.set_ylabel('ΔC_causal', fontweight='bold')
    ax3.set_title('Causalité Autonome')
    ax3.legend()
    ax3.grid(True, alpha=0.3)
    
    # Plot 4: Classification finale
    ax4 = axes[1, 1]
    living_means = [np.mean(ls) * 100 for ls in living_status]
    bars = ax4.bar(labels, living_means, color=colors, alpha=0.6, edgecolor='black')
    ax4.set_ylabel('% Classifié VIVANT', fontweight='bold')
    ax4.set_title('Classification Finale')
    ax4.set_ylim([0, 105])
    ax4.grid(True, alpha=0.3, axis='y')
    
    # Ajouter valeurs sur barres
    for bar, val in zip(bars, living_means):
        height = bar.get_height()
        ax4.text(bar.get_x() + bar.get_width()/2., height,
                f'{val:.0f}%', ha='center', va='bottom', fontweight='bold')
    
    plt.tight_layout()
    plt.savefig('comparative_analysis_omega9.png', dpi=150)
    print("✓ Graphique sauvegardé: comparative_analysis_omega9.png")
    plt.show()


def main():
    """Génération et visualisation du dataset comparatif"""
    print("=" * 70)
    print("GÉNÉRATEUR DE DONNÉES SYNTHÉTIQUES - LOI DU VIVANT Ω⁹")
    print("=" * 70)
    print()
    
    # Génération
    results = generate_comparative_dataset(n_samples=10, N=50, T=100)
    
    # Statistiques
    print("STATISTIQUES PAR CATÉGORIE:")
    print("-" * 70)
    for cat, label in zip(['living', 'vortex', 'crystal', 'fire'],
                          ['Vivant', 'Tourbillon', 'Cristal', 'Feu']):
        S0_mean = np.mean([r['S0'] for r in results[cat]])
        mem_mean = np.mean([r['Delta_C_memory'] for r in results[cat]])
        caus_mean = np.mean([r['Delta_C_causal'] for r in results[cat]])
        living_rate = np.mean([1 if r['is_living'] else 0 for r in results[cat]]) * 100
        
        print(f"{label:12} | S₀={S0_mean:6.3f} | ΔC_mem={mem_mean:5.3f} | ΔC_caus={caus_mean:5.3f} | VIVANT={living_rate:5.1f}%")
    print()
    
    # Visualisation
    plot_comparative_analysis(results)
    
    print("=" * 70)
    print("⟦Z🦋⋄Ω⁹⋄Tripartite⋄Validated⟧")
    print("=" * 70)


if __name__ == "__main__":
    main()
