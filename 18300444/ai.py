import numpy as np
NAME = "ai"

def map(df):
    beta = np.sign(df["benchmark"].diff().fillna(0)).abs()
    delta_phi = df["benchmark"].diff().fillna(0)
    T = df["compute"] + df["energy"]
    sigma = df["alignment_issues"]
    return beta, delta_phi, T, sigma
