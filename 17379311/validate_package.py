import csv, math, statistics, json
path = "data/logs_18000.csv"

def H(p):
    return -sum(x * math.log(x + 1e-12, 2) for x in p)

with open(path, newline="", encoding="utf-8") as f:
    rows = list(csv.DictReader(f))

truth = [float(r["truth_val"]) for r in rows]
conf  = [float(r["confidence"]) for r in rows]
recall = sum(t >= 0.95 and c > 0.8 for t, c in zip(truth, conf)) / len(rows)

drifts = []
for i in range(1, len(rows)):
    a = [float(x) for x in rows[i]["prob_dist"].split("|")]
    b = [float(x) for x in rows[i-1]["prob_dist"].split("|")]
    drifts.append(abs(H(a) - H(b)))
mean_drift = statistics.mean(drifts)

# seuil ajusté à 0.005 pour éviter les faux positifs
flag = int(mean_drift > 0.005)

print(json.dumps({
    "truth_recall": round(recall, 6),
    "mean_drift": round(mean_drift, 9),
    "anomaly_flag": flag
}, indent=2))