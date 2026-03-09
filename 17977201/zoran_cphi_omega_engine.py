# zoran_cphi_omega_engine.py
# Instrumental Python Engine — ZORANC🦋CφΩ
# Implements S (predictive gauge) and Cφ (phenomenal coherence)

import numpy as np

def normalize(v):
    s = np.sum(v)
    if s <= 0:
        raise ValueError("Distribution sum must be > 0")
    return v / s

def kl_divergence(P, Q):
    P = normalize(np.array(P, dtype=float))
    Q = normalize(np.array(Q, dtype=float))
    eps = 1e-12
    return float(np.sum((P+eps) * np.log((P+eps)/(Q+eps))))

def compute_S(beta, delta_phi, T, sigma):
    if T <= 0 or sigma <= 0:
        raise ValueError("T and sigma must be > 0")
    return (beta * delta_phi) / (T * sigma)

def apply_operant(P_before, P_after, Q, beta, delta_phi, T, sigma):
    S = compute_S(beta, delta_phi, T, sigma)
    C_before = kl_divergence(P_before, Q)
    C_after = kl_divergence(P_after, Q)
    Omega = C_after - C_before
    return {
        "S": S,
        "Cphi_before": C_before,
        "Cphi_after": C_after,
        "Omega": Omega
    }
