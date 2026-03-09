import numpy as np
NAME = "macro_economy"

def map(df):
    beta = np.sign(df["gdp"].diff().fillna(0)).abs()
    delta_phi = df["gdp"].diff().fillna(0)
    T = df["debt"] + df["public_spending"]
    sigma = df[["inflation", "debt"]].std(axis=1)
    return beta, delta_phi, T, sigma
