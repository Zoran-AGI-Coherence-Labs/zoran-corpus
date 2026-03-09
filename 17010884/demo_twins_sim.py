#!/usr/bin/env python3
import json, random

random.seed(42)

def simulate_regime(label, steps=1000):
    # toy simulation: stability (0-1), coherence (0-1), microbiome_drift (0-1), cost tokens
    stability = 0.7 + 0.1*(1 if label=='A' else -1) + random.uniform(-0.05,0.05)
    coherence = 0.68 + 0.08*(1 if label=='A' else 0) + random.uniform(-0.06,0.06)
    microbiome_drift = 0.35 + 0.25*(1 if label=='A' else 0.1) + random.uniform(-0.05,0.05)
    cost = 10_000 + (500 if label=='A' else 800) + random.randint(-200,200)
    return dict(label=label, stability=round(stability,3), coherence=round(coherence,3),
                microbiome_drift=round(microbiome_drift,3), cost_tokens=cost)

def self_patch_quorum(metricsA, metricsB):
    votes = []
    for k in ['stability','coherence']:
        votes.append(('A' if metricsA[k]>=metricsB[k] else 'B'))
    # minimize drift and cost
    votes.append('A' if metricsA['microbiome_drift']<=metricsB['microbiome_drift'] else 'B')
    votes.append('A' if metricsA['cost_tokens']<=metricsB['cost_tokens'] else 'B')
    winner = 'A' if votes.count('A')>=votes.count('B') else 'B'
    return dict(votes=votes, winner=winner)

A = simulate_regime('A')
B = simulate_regime('B')
quorum = self_patch_quorum(A,B)

result = dict(run='twins_cognitive_regimes', A=A, B=B, quorum=quorum)
with open('metrics.json','w') as f:
    json.dump(result, f, indent=2)
print(json.dumps(result, indent=2))