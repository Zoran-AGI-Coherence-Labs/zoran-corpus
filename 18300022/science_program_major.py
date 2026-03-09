import numpy as np
NAME = "human_scientific_program"

def map(df):
    beta = np.sign(df["local_success"].diff().fillna(0)).abs()
    delta_phi = df["local_success"].diff().fillna(0)
    T = df["complexity_cost"]
    sigma = df["theoretical_noise"]
    return beta, delta_phi, T, sigma
