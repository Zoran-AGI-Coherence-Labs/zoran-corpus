import numpy as np
NAME = "health"

def map(df):
    beta = np.sign(df["life_expectancy"].diff().fillna(0)).abs()
    delta_phi = df["life_expectancy"].diff().fillna(0)
    T = df["health_spending"]
    sigma = df[["chronic_disease_rate", "polypharmacy"]].std(axis=1)
    return beta, delta_phi, T, sigma
