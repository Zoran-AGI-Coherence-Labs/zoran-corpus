#!/usr/bin/env python3
import argparse, json, random, time

def simulate(metrics_path):
    schema = json.load(open(metrics_path, 'r', encoding='utf-8'))
    lat = 120 + random.randint(-10, 10)
    cost = 0.03 + random.random()*0.02
    fairness_gap = random.random()*0.08  # simulated SPD abs
    return {
        "latency_p95_ms": lat,
        "cost_per_ticket_eur": round(cost, 4),
        "fairness_spd_abs": round(fairness_gap, 3),
        "go": fairness_gap <= schema["fairness"]["targets"]["SPD_abs_max"]
    }

if __name__ == '__main__':
    ap = argparse.ArgumentParser()
    ap.add_argument('--policy', required=True)
    ap.add_argument('--metrics', required=True)
    args = ap.parse_args()
    res = simulate(args.metrics)
    print('CANARY RESULT:', json.dumps(res, indent=2))
    if not res["go"]:
        print('ΔM11.3: ROLLBACK TRIGGERED (simulated)')
