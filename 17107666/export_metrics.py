import json, argparse, random, statistics, time

parser = argparse.ArgumentParser()
parser.add_argument('--out', default='metrics_report.json')
parser.add_argument('--seeds', nargs='*', default=['13','42','101'])
args = parser.parse_args()

seeds = list(map(int, args.seeds))
random.seed(sum(seeds))

def mock_metric(mu, sigma=0.005):
    return max(0.0, round(random.gauss(mu, sigma), 4))

report = {
    "timestamp": int(time.time()),
    "seeds": seeds,
    "fairness": {
        "SPD": mock_metric(0.032),
        "delta_TPR": mock_metric(0.021),
        "delta_FPR": mock_metric(0.015),
        "ECE": mock_metric(0.017)
    },
    "latency": {"p50_ms": 320, "p95_ms": 860},
    "cost_per_1k_req_eur": 2.47,
    "co2e_per_req_g": 0.8,
    "notes": "Valeurs simulées pour structure de rapport; utilisez vos mesures réelles en TEF/sandbox."
}

with open(args.out, 'w', encoding='utf-8') as f:
    json.dump(report, f, indent=2, ensure_ascii=False)

print(f"Écrit: {args.out}")
