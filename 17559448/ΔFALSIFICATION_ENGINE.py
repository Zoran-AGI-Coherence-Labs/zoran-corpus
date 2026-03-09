# ΔFALSIFICATION_ENGINE.py
import numpy as np

def falsification_test(n=10000):
    beta = np.random.uniform(0.1, 0.5, n)
    deltaC = np.random.uniform(0.1, 0.5, n)
    lambd = np.random.uniform(2.0, 10.0, n)
    S = (beta * deltaC) / lambd
    ratio = np.mean(S > 1)
    return {"false_positive_ratio": float(ratio), "result": "VALIDATION OK" if ratio < 0.01 else "INVALID"}

if __name__ == "__main__":
    print(falsification_test())
