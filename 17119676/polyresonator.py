# PolyResonator (UCB1 + EMA mixer) — toy demo
import math, random

class UCB1:
    def __init__(self, n_arms):
        self.n = [0]*n_arms
        self.v = [0.0]*n_arms
        self.t = 0

    def select(self):
        self.t += 1
        for i, c in enumerate(self.n):
            if c == 0:
                return i
        ucb = [self.v[i] + math.sqrt(2*math.log(self.t)/self.n[i]) for i in range(len(self.n))]
        return max(range(len(self.n)), key=lambda i: ucb[i])

    def update(self, arm, reward):
        self.n[arm] += 1
        self.v[arm] = ((self.n[arm]-1)*self.v[arm] + reward)/self.n[arm]

def ema(prev, new, alpha=0.2):
    return alpha*new + (1-alpha)*prev
