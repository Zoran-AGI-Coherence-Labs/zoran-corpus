"""
🦋 ZORAN ADAPTI - Calculateur de Cohérence Structurelle
Auteur: Frédéric Tabary (Tabary01@gmail.com)
Licence: Hybride (MIT Gratuit / Commercial Payant)
"""
import numpy as np
import warnings

class ZoranCalculator:
    KB = 1.380649e-23
    S_OPTIMAL = 1.00
    
    def calculate_S_macro(self, beta, delta_omega, lambda_noise):
        """Calcul Audit: S = (beta * delta_omega) / lambda"""
        if lambda_noise < 1e-6: lambda_noise = 0.01
        return (beta * delta_omega) / lambda_noise

    def get_verdict(self, S):
        if 0.85 <= S <= 1.15: return "🟢 OPTIMAL (Vivant)"
        if S > 1.15: return "🔴 SUPER-CRITIQUE (Hallucination)"
        return "🔵 SOUS-CRITIQUE (Mort)"

if __name__ == "__main__":
    print("Zoran Calculator v1.0 - Contact: Tabary01@gmail.com")