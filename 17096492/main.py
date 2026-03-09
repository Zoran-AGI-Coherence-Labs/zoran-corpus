#!/usr/bin/env python3
# main.py — Single-run simulator (stdlib only)
import os, json, random, math, hashlib
from typing import Dict, Any
from glyphnet import encode as glyph_encode
from delta_guard import need_rollback

SEED = int(os.getenv("SEED", "13"))
RUNS = int(os.getenv("RUNS", "30"))

def sha256(s: str)->str:
    return hashlib.sha256(s.encode()).hexdigest()

def ucb1_estimate(step:int, base:float=0.55)->float:
    random.seed(SEED + step)
    noise = (random.random()-0.5)*0.04
    return max(0.0, min(1.0, base + 0.1 * (1 - math.exp(-step/20)) + noise))

def simulate_step(step:int, base:float=0.55)->Dict[str, Any]:
    reward = ucb1_estimate(step, base=base)
    coherence = 0.55 + 0.25 * reward
    stability = 0.50 + 0.35 * (reward - 0.5)
    latency_p95 = 110 + int(40 * reward)
    cost_rel = 1.00 + 0.12 * reward
    entropy = 0.18 + 0.1*(1-reward)
    rollback = need_rollback(entropy)
    rec = dict(step=step, reward=round(reward,3), coherence=round(coherence,3),
               stability=round(stability,3), latency_p95=latency_p95,
               cost_total=round(cost_rel,3), entropy=round(entropy,3),
               rollback=rollback)
    rec["glyph"] = glyph_encode({"OBJ":"run","CTX":step,"EVID":"sim","TRACE":sha256(str(rec))[:12]})
    return rec

def main():
    records = [simulate_step(s) for s in range(RUNS)]
    with open("metrics.json","w", encoding="utf-8") as f: json.dump(records, f, indent=2, ensure_ascii=False)
    print("metrics.json written with", len(records), "records.")

if __name__ == "__main__":
    main()
