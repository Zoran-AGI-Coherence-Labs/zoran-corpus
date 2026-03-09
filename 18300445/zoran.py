import numpy as np

def compute_S_series(beta, delta_phi, T, sigma):
    S = []
    for b, d, t, s in zip(beta, delta_phi, T, sigma):
        if t == 0 or s == 0:
            S.append(np.inf)
        else:
            S.append((b * d) / (t * s))
    return np.array(S)
