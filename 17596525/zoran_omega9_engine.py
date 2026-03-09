"""
Zoran Omega9 Engine
Moteur de calcul pour la Loi du Vivant Ω⁹
Version : 2.0 (Post-Red-Team)
Auteur : Frédéric Tabary, Institut🦋 IA Inc.
Licence : Creative-Ethic BY v1.0
Contact : Tabary01@gmail.com
"""

import numpy as np
import pandas as pd
from sklearn.feature_selection import mutual_info_regression
from typing import Dict, Tuple
import warnings
warnings.filterwarnings('ignore')


class ZoranOmega9Engine:
    """
    Moteur de calcul pour évaluer la vitalité d'un système
    selon la Loi du Vivant Ω⁹
    """
    
    def __init__(self, baseline_shuffles: int = 100, normalization_factor: float = 1.0):
        """
        Args:
            baseline_shuffles: Nombre de permutations pour baseline anti-bruit
            normalization_factor: Facteur issu de calibration empirique
        """
        self.baseline_shuffles = baseline_shuffles
        self.normalization_factor = normalization_factor
    
    
    def coherence_robust(self, df: pd.DataFrame) -> float:
        """Cohérence via information mutuelle"""
        n_vars = df.shape[1]
        if n_vars < 2:
            return 0.0
        
        mi_scores = []
        for i in range(n_vars):
            for j in range(i+1, n_vars):
                X = df.iloc[:, i].values.reshape(-1, 1)
                y = df.iloc[:, j].values
                
                if np.std(X) > 0 and np.std(y) > 0:
                    mi = mutual_info_regression(X, y, random_state=42)[0]
                    mi_scores.append(mi)
        
        return float(np.mean(mi_scores)) if mi_scores else 0.0
    
    
    def dispersion(self, df: pd.DataFrame) -> float:
        """Dispersion via variance moyenne"""
        return float(np.mean(np.var(df.values, axis=0)))
    
    
    def memory_coherence(self, df: pd.DataFrame, lag: int = 1) -> float:
        """Mémoire fonctionnelle I(passé;futur)"""
        if len(df) <= lag:
            return 0.0
        
        mi_scores = []
        for col in df.columns:
            past = df[col].iloc[:-lag].values.reshape(-1, 1)
            future = df[col].iloc[lag:].values
            
            if np.std(past) > 0 and np.std(future) > 0:
                mi = mutual_info_regression(past, future, random_state=42)[0]
                mi_scores.append(mi)
        
        return float(np.mean(mi_scores)) if mi_scores else 0.0
    
    
    def causal_coherence(self, df: pd.DataFrame, lag: int = 1) -> float:
        """Causalité active (corrélation croisée retardée)"""
        if len(df) <= lag:
            return 0.0
        
        n_vars = df.shape[1]
        causal_scores = []
        
        for i in range(n_vars):
            for j in range(n_vars):
                if i != j:
                    cause = df.iloc[:-lag, i].values
                    effect = df.iloc[lag:, j].values
                    
                    if np.std(cause) > 0 and np.std(effect) > 0:
                        corr = np.corrcoef(cause, effect)[0, 1]
                        causal_scores.append(abs(corr))
        
        return float(np.mean(causal_scores)) if causal_scores else 0.0
    
    
    def beta_proxy(self, df: pd.DataFrame) -> float:
        """
        Intention β via ratio spectral basses/hautes fréquences
        """
        fft_data = np.fft.fft(df.values, axis=0)
        power = np.abs(fft_data)**2
        
        cutoff = max(1, len(power) // 10)
        low_freq_power = np.sum(power[:cutoff])
        total_power = np.sum(power)
        
        return low_freq_power / (total_power + 1e-9)
    
    
    def compute_baseline(self, df: pd.DataFrame) -> float:
        """Calcul baseline via données shufflées"""
        baseline_scores = []
        
        for _ in range(self.baseline_shuffles):
            df_shuffled = df.copy()
            for col in df_shuffled.columns:
                df_shuffled[col] = np.random.permutation(df_shuffled[col].values)
            
            ΔC_shuffled = self.coherence_robust(df_shuffled)
            baseline_scores.append(ΔC_shuffled)
        
        return np.mean(baseline_scores)
    
    
    def S0_score(self, df: pd.DataFrame, use_baseline: bool = True) -> Dict[str, float]:
        """
        Calcul du score S₀ avec anti-bruit
        
        Returns:
            Dict avec S0, ΔCₑ, λ, baseline, ΔCₑ_effective
        """
        # Cohérence réelle
        ΔCₑ = self.coherence_robust(df)
        
        # Baseline (optionnel mais recommandé)
        if use_baseline:
            baseline = self.compute_baseline(df)
            ΔCₑ_effective = max(0, ΔCₑ - baseline)
        else:
            baseline = 0.0
            ΔCₑ_effective = ΔCₑ
        
        # Dispersion
        λ = self.dispersion(df)
        
        # Score S₀
        S0 = ΔCₑ_effective / (λ + 1e-9)
        S0_normalized = S0 / self.normalization_factor
        
        return {
            'S0': S0_normalized,
            'S0_raw': S0,
            'ΔCₑ': ΔCₑ,
            'ΔCₑ_effective': ΔCₑ_effective,
            'λ': λ,
            'baseline': baseline
        }
    
    
    def is_alive(self, df: pd.DataFrame, 
                 threshold: float = 1.0,
                 min_memory: float = 0.01,
                 min_causal: float = 0.01) -> Dict:
        """
        Évaluation complète selon critère tripartite Ω⁹
        
        Args:
            df: DataFrame temporel du système
            threshold: Seuil S₀ (défaut 1.0 après calibration)
            min_memory: Seuil minimal ΔC_mémoire
            min_causal: Seuil minimal ΔC_causale
        
        Returns:
            Dict avec verdict, scores, et diagnostics
        """
        # Calculs
        s0_result = self.S0_score(df, use_baseline=True)
        S0 = s0_result['S0']
        
        ΔC_mem = self.memory_coherence(df)
        ΔC_caus = self.causal_coherence(df)
        β = self.beta_proxy(df)
        
        # Critère tripartite
        condition_1 = S0 > threshold
        condition_2 = ΔC_mem > min_memory
        condition_3 = ΔC_caus > min_causal
        
        is_alive = condition_1 and condition_2 and condition_3
        
        # Score vivant intentionnel
        S_intention = β * S0
        
        # Diagnostic
        if not condition_1:
            reason = "Structure insuffisante (S₀ < seuil)"
        elif not condition_2:
            reason = "Pas de mémoire fonctionnelle"
        elif not condition_3:
            reason = "Pas de causalité autonome"
        else:
            reason = "Satisfait les 3 critères"
        
        # Régime de viabilité
        if S0 < 0.5:
            regime = "Effondrement"
        elif S0 < 1.0:
            regime = "Dérive"
        elif S0 < 3.0:
            regime = "Viabilité"
        elif S0 < 10.0:
            regime = "Régénération"
        else:
            regime = "Émergence"
        
        return {
            'is_alive': is_alive,
            'S0': S0,
            'S_intention': S_intention,
            'ΔC_mémoire': ΔC_mem,
            'ΔC_causale': ΔC_caus,
            'β_intention': β,
            'regime': regime,
            'conditions': {
                'structure': condition_1,
                'memory': condition_2,
                'causality': condition_3
            },
            'reason': reason,
            'details': s0_result
        }


# ============================================================================
# EXEMPLE D'UTILISATION
# ============================================================================

if __name__ == "__main__":
    print("\n" + "="*60)
    print("ZORAN Ω⁹ ENGINE - EXEMPLE D'UTILISATION")
    print("="*60 + "\n")
    
    # Génération données synthétiques (cellule simulée)
    n = 1000
    t = np.linspace(0, 50, n)
    
    glucose = 5 + 2*np.sin(t/5) + np.random.randn(n)*0.2
    atp = np.zeros(n)
    atp[0] = 10
    
    for i in range(1, n):
        atp[i] = 0.9*atp[i-1] + 0.1*glucose[i] + np.random.randn()*0.2
    
    cell_data = pd.DataFrame({
        'glucose': glucose,
        'atp': atp,
        'nadh': 0.5*atp + np.random.randn(n)*0.1,
        'proteins': np.cumsum(atp)/n + np.random.randn(n)*0.05
    })
    
    # Analyse
    engine = ZoranOmega9Engine(baseline_shuffles=50)
    result = engine.is_alive(cell_data)
    
    print(f"Système analysé : Cellule synthétique")
    print(f"Vivant : {result['is_alive']}")
    print(f"S₀ : {result['S0']:.3f}")
    print(f"Régime : {result['regime']}")
    print(f"ΔC_mémoire : {result['ΔC_mémoire']:.4f}")
    print(f"ΔC_causale : {result['ΔC_causale']:.4f}")
    print(f"Raison : {result['reason']}")
    print("\n" + "="*60)
