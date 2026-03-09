from metrics.zoran import compute_S_series
from metrics.trend import analyze_trend

class ZoranEngine:
    VERSION = "0.3"

    def __init__(self, domain):
        self.domain = domain

    def run(self, data, objective):
        beta, delta_phi, T, sigma = self.domain.map(data)

        S = compute_S_series(beta, delta_phi, T, sigma)
        slope, trend = analyze_trend(S)

        if trend == "STABLE_OR_IMPROVING":
            verdict = "ADMISSIBLE"
        elif trend == "CRITICAL":
            verdict = "CRITIQUE"
        else:
            verdict = "NON_ADMISSIBLE"

        return {
            "domain": self.domain.NAME,
            "objective": objective,
            "beta": beta.tolist(),
            "delta_phi": delta_phi.tolist(),
            "T": T.tolist(),
            "sigma": sigma.tolist(),
            "S": S.tolist(),
            "trend": {
                "slope": slope,
                "class": trend
            },
            "verdict": verdict,
            "engine_version": self.VERSION
        }
