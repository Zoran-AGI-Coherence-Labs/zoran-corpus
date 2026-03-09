import numpy as np
NAME = "human_political_exec"

def map(df):
    beta = np.sign(df["decision_effect"].diff().fillna(0)).abs()
    delta_phi = df["decision_effect"].diff().fillna(0)
    T = df["legal_costs"] + df["administrative_costs"]
    sigma = df["normative_instability"]
    return beta, delta_phi, T, sigma
