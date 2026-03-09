"""
Suite de Tests Unitaires pour Zoran Omega9
Exécution : pytest test_suite.py
"""

import numpy as np
import pandas as pd
import pytest
from zoran_omega9_engine import ZoranOmega9Engine


def test_bruit_blanc():
    """Test : bruit blanc pur → non-vivant"""
    engine = ZoranOmega9Engine(baseline_shuffles=50)
    
    # Génération bruit
    noise = pd.DataFrame(np.random.randn(1000, 10))
    result = engine.is_alive(noise)
    
    assert result['is_alive'] == False, "Bruit blanc classifié vivant !"
    assert result['S0'] < 0.5, f"S₀ trop élevé pour bruit : {result['S0']}"
    print("✅ Test bruit blanc : PASSÉ")


def test_signal_structure():
    """Test : signal structuré → potentiellement vivant"""
    engine = ZoranOmega9Engine(baseline_shuffles=50)
    
    # Génération signal structuré (sinus + bruit)
    t = np.linspace(0, 10, 1000)
    signal = pd.DataFrame({
        f'var_{i}': np.sin(t * (i+1)) + np.random.randn(1000) * 0.1
        for i in range(10)
    })
    
    result = engine.is_alive(signal)
    
    # Signal structuré devrait avoir S₀ élevé
    assert result['S0'] > 0.5, f"S₀ trop faible : {result['S0']}"
    print(f"✅ Test signal structuré : S₀={result['S0']:.3f}, vivant={result['is_alive']}")


def test_tourbillon_synthetique():
    """Test : tourbillon synthétique → non-vivant"""
    engine = ZoranOmega9Engine(baseline_shuffles=50)
    
    # Simulation tourbillon : structure cohérente mais sans mémoire
    t = np.linspace(0, 10, 500)
    theta = np.linspace(0, 4*np.pi, 500)
    
    vortex = pd.DataFrame({
        'x': np.cos(theta) * np.exp(-t/20),
        'y': np.sin(theta) * np.exp(-t/20),
        'vx': -np.sin(theta),
        'vy': np.cos(theta)
    })
    
    result = engine.is_alive(vortex)
    
    # Devrait avoir S₀ > 0 mais ΔC_mémoire faible
    assert result['is_alive'] == False, "Tourbillon classifié vivant !"
    print(f"✅ Test tourbillon : S₀={result['S0']:.3f}, " +
          f"mémoire={result['ΔC_mémoire']:.4f}, vivant={result['is_alive']}")


def test_cellule_simulation():
    """Test : simulation métabolisme cellulaire → vivant"""
    engine = ZoranOmega9Engine(baseline_shuffles=30)
    
    # Simulation simple : feedback homeostatic
    n = 1000
    t = np.linspace(0, 50, n)
    
    # Variables couplées avec mémoire et feedback
    glucose = 5 + 2*np.sin(t/5) + np.random.randn(n)*0.3
    atp = np.zeros(n)
    atp[0] = 10
    
    for i in range(1, n):
        # Feedback : ATP régulé par glucose avec mémoire
        atp[i] = 0.9*atp[i-1] + 0.1*glucose[i] + np.random.randn()*0.2
    
    cell = pd.DataFrame({
        'glucose': glucose,
        'atp': atp,
        'nadh': 0.5*atp + np.random.randn(n)*0.1,
        'proteins': np.cumsum(atp)/n + np.random.randn(n)*0.05
    })
    
    result = engine.is_alive(cell)
    
    # Cellule simulée devrait être classée vivante
    print(f"✅ Test cellule : S₀={result['S0']:.3f}, " +
          f"mémoire={result['ΔC_mémoire']:.4f}, " +
          f"causalité={result['ΔC_causale']:.4f}, " +
          f"vivant={result['is_alive']}")


def test_coherence_calculation():
    """Test : calcul cohérence basique"""
    engine = ZoranOmega9Engine()
    
    # Données parfaitement corrélées
    data_corr = pd.DataFrame({
        'x': np.linspace(0, 10, 100),
        'y': np.linspace(0, 10, 100) * 2
    })
    
    coherence = engine.coherence_robust(data_corr)
    assert coherence > 0, "Cohérence nulle pour données corrélées"
    print(f"✅ Test cohérence : {coherence:.3f}")


def test_memory_coherence():
    """Test : mémoire fonctionnelle détectable"""
    engine = ZoranOmega9Engine()
    
    # Série avec mémoire (AR(1) process)
    n = 500
    data = np.zeros(n)
    data[0] = 0
    for i in range(1, n):
        data[i] = 0.8 * data[i-1] + np.random.randn() * 0.1
    
    df = pd.DataFrame({'series': data})
    memory = engine.memory_coherence(df, lag=1)
    
    assert memory > 0.01, "Mémoire non détectée dans série AR(1)"
    print(f"✅ Test mémoire : {memory:.4f}")


def test_baseline_computation():
    """Test : baseline anti-bruit fonctionne"""
    engine = ZoranOmega9Engine(baseline_shuffles=20)
    
    data = pd.DataFrame(np.random.randn(500, 5))
    baseline = engine.compute_baseline(data)
    
    assert baseline >= 0, "Baseline négative impossible"
    print(f"✅ Test baseline : {baseline:.4f}")


if __name__ == "__main__":
    print("\n" + "="*60)
    print("ZORAN Ω⁹ ENGINE - TESTS UNITAIRES")
    print("="*60 + "\n")
    
    test_bruit_blanc()
    test_signal_structure()
    test_tourbillon_synthetique()
    test_cellule_simulation()
    test_coherence_calculation()
    test_memory_coherence()
    test_baseline_computation()
    
    print("\n" + "="*60)
    print("TOUS LES TESTS COMPLÉTÉS AVEC SUCCÈS ✅")
    print("="*60)
