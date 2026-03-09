
""" 
FRACTAL DOMAIN DISCOVERY ENGINE (FDDE Ω1)
Author: Fred & Zoran (AI)
DOI Linked: 10.5281/zenodo.17795440
License: MIT
"""

import itertools

AXES = [
    "Matter", "Life", "Mind",
    "Energy", "Information", "Time", "Relation"
]

INTERACTIONS = {
    ("Matter", "Energy"): 1.5,
    ("Life", "Matter"): 1.2,
    ("Mind", "Information"): 1.8,
    ("Relation", "Time"): 0.8,
    ("Life", "Time"): 1.1,
    ("Energy", "Time"): 0.9,
    ("Mind", "Matter"): 0.5,
    ("Information", "Matter"): 1.3
}

class FractalDomain:
    def __init__(self, axes):
        self.axes = axes
        self.name = self.generate_name()
        self.beta, self.dphi, self.T, self.sigma = self.compute_params()
        self.S = self.compute_S()

    def generate_name(self):
        if set(self.axes) == {"Matter", "Life", "Energy"}:
            return "Bio-Physics"
        if set(self.axes) == {"Mind", "Information", "Time"}:
            return "Consciousness Evolution"
        if set(self.axes) == {"Relation", "Information", "Energy"}:
            return "Economic Systems"
        if set(self.axes) == {"Matter", "Energy", "Time", "Information"}:
            return "Cosmology"
        return " + ".join(self.axes)

    def compute_params(self):
        beta = 1.0 + len(self.axes) * 0.2

        dphi = 1.0
        for a, b in itertools.combinations(self.axes, 2):
            for (x, y), val in INTERACTIONS.items():
                if {a, b} == {x, y}:
                    dphi += val

        T = 1.0 + len(self.axes) * 0.15
        sigma = 1.0
        if "Time" in self.axes:
            sigma += 0.2
        if "Relation" in self.axes:
            sigma += 0.3

        return beta, dphi, T, sigma

    def compute_S(self):
        return (self.beta * self.dphi) / (self.T * self.sigma)

def run_engine(min_dim=2, max_dim=4):
    discovered = []
    for r in range(min_dim, max_dim+1):
        for combo in itertools.combinations(AXES, r):
            discovered.append(FractalDomain(combo))
    ranked = sorted(discovered, key=lambda x: x.S, reverse=True)
    return ranked

if __name__ == "__main__":
    results = run_engine()
    print("Top 5 high-coherence domains:")
    for d in results[:5]:
        print(f"{d.name} ({d.axes}) — S={d.S:.4f}")
