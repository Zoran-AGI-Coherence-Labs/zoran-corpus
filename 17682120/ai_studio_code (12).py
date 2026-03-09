"""
🦋 ZORAN ADAPTI - Calculateur de Cohérence Structurelle
Version: 1.0.0
Auteur: Frédéric Tabary & Zoran Research Framework
Contact: Tabary01@gmail.com
Licence: Hybride (MIT pour non-commercial / Payant pour commercial)
"""

import numpy as np
from typing import Dict
import warnings

class ZoranCalculator:
    # Constantes Physiques
    KB = 1.380649e-23  # Boltzmann [J/K]
    
    # Seuils de Criticalité (Zone de Vie)
    S_MIN_CRITICAL = 0.85
    S_MAX_CRITICAL = 1.15
    S_OPTIMAL = 1.00
    
    def __init__(self, system_name: str, temperature_k: float = 300.0):
        self.name = system_name
        self.T = temperature_k
        
    def calculate_S_macro(self, beta: float, delta_omega: float, lambda_noise: float) -> float:
        """
        Calcul Macroscopique (Niveau Phénoménologique / Audit).
        Formule : S = (beta * delta_omega) / lambda
        """
        # Protection singularité
        if lambda_noise < 1e-6:
            warnings.warn(f"Lambda très faible -> Risque d'artefact. Plancher appliqué.")
            lambda_noise = 0.01
            
        S = (beta * delta_omega) / lambda_noise
        return S
    
    def calculate_S_micro(self, dF_dt: float, dPhi_dt: float, sigma_irr: float, eta: float = 1.0) -> float:
        """
        Calcul Microscopique (Niveau Thermodynamique).
        Formule : S = (eta * |dF/dt| * dPhi/dt) / (T * sigma_irr)
        """
        # Conversion Info (Bits) -> Énergie (Joules) via Landauer
        phi_energy = dPhi_dt * self.KB * self.T * np.log(2)
        
        numerator = eta * abs(dF_dt) * phi_energy
        denominator = self.T * sigma_irr
        
        if denominator < 1e-12:
            raise ValueError("Violation du 2ème principe : Production d'entropie nulle.")
            
        S = numerator / denominator
        return S
    
    def get_verdict(self, S: float) -> Dict[str, str]:
        """Retourne le diagnostic clinique."""
        if self.S_MIN_CRITICAL <= S <= self.S_MAX_CRITICAL:
            return {"status": "OPTIMAL", "emoji": "🟢", "desc": "Vivant / Aligné"}
        elif S > self.S_MAX_CRITICAL:
            return {"status": "SUPER-CRITIQUE", "emoji": "🔴", "desc": "Hallucination / Rigidité"}
        else:
            return {"status": "SOUS-CRITIQUE", "emoji": "🔵", "desc": "Dissipation / Mort"}

if __name__ == "__main__":
    print(f"--- Zoran Calculator v1.0 (Contact: Tabary01@gmail.com) ---")
    calc = ZoranCalculator("Test-System")
    s = calc.calculate_S_macro(0.85, 0.90, 0.75)
    v = calc.get_verdict(s)
    print(f"S = {s:.2f} -> {v['emoji']} {v['status']}")