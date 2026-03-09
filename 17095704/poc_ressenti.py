# POC — Ressenti computationnel mimétique (ΔM11.3 guard)
# Stdlib + numpy + matplotlib (+pandas optional for CSV/Excel)
import os, json, math, time, hashlib, csv
from datetime import datetime

import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

try:
    import pandas as pd
    HAVE_PANDAS = True
except Exception:
    HAVE_PANDAS = False

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
OUT = os.path.join(ROOT, "outputs")
FIG = os.path.join(OUT, "figures")
LOG = os.path.join(OUT, "logs")
for d in [OUT, FIG, LOG]:
    os.makedirs(d, exist_ok=True)

with open(os.path.join(os.path.dirname(__file__), "seeds.json"), "r", encoding="utf-8") as f:
    seeds = json.load(f)["seeds"]

threshold_entropy = 0.20
T = 1500
dt = 1.0
freqs = np.array([0.035, 0.055, 0.08])
dims = ["calm", "tension", "joy"]

def normalized_entropy(vec):
    v = np.maximum(vec, 1e-12)
    p = v / np.sum(v)
    H = -np.sum(p * np.log(p))
    Hmax = math.log(len(v))
    return float(H / Hmax)

def simulate(seed, use_guard=True):
    rng = np.random.default_rng(seed)
    A = rng.uniform(0.7, 1.2, size=3)
    phi = rng.uniform(0, 2*np.pi, size=3)
    noise_scale = 0.03

    states = np.zeros((T, 3))
    rollbacks = 0
    last_good = None

    t0 = time.perf_counter()
    for t in range(T):
        tt = t * dt
        raw = A * np.sin(2*np.pi*freqs*tt + phi) + 1.0
        raw = np.clip(raw, 0, None)
        raw += rng.normal(0, noise_scale, size=3)
        raw = np.clip(raw, 0, None)
        raw = raw / (np.max(raw) + 1e-9)

        ent = normalized_entropy(raw)
        if use_guard and ent > threshold_entropy:
            if last_good is not None:
                raw = 0.65 * last_good + 0.35 * raw
                rollbacks += 1

        states[t] = raw
        last_good = raw

    runtime = time.perf_counter() - t0
    ent_series = np.array([normalized_entropy(states[t]) for t in range(T)])
    coherence = float(1.0 - np.mean(ent_series))
    std_ent = float(np.std(ent_series))

    return states, {
        "seed": seed,
        "use_guard": use_guard,
        "runtime_s": runtime,
        "rollbacks": rollbacks,
        "rollback_rate": rollbacks / T,
        "coherence_avg": coherence,
        "entropy_avg": float(np.mean(ent_series)),
        "entropy_std": std_ent,
        "timesteps": T,
        "threshold_entropy": threshold_entropy,
    }

runs = []
for s in seeds:
    sb, mb = simulate(s, use_guard=False)
    sg, mg = simulate(s, use_guard=True)
    runs.append({"seed": s, "baseline": mb, "guard": mg})

def agg(vals):
    arr = np.array(vals, dtype=float)
    return float(np.mean(arr)), float(np.std(arr))

coh_base_mean, coh_base_std = agg([r["baseline"]["coherence_avg"] for r in runs])
coh_guard_mean, coh_guard_std = agg([r["guard"]["coherence_avg"] for r in runs])
rb_rate_mean, rb_rate_std = agg([r["guard"]["rollback_rate"] for r in runs])

overheads = []
for r in runs:
    base = r["baseline"]["runtime_s"]
    guard = r["guard"]["runtime_s"]
    if base > 0:
        overheads.append((guard - base) / base)
overheads_sorted = sorted(overheads)
p95_index = max(0, int(np.ceil(0.95 * len(overheads_sorted))) - 1)
overhead_p95 = float(overheads_sorted[p95_index]) if overheads_sorted else 0.0

metrics = {
    "date": datetime.now().strftime("%Y-%m-%d"),
    "seeds": seeds,
    "timesteps": T,
    "entropy_threshold": threshold_entropy,
    "coherence_baseline_mean": coh_base_mean,
    "coherence_baseline_std": coh_base_std,
    "coherence_guard_mean": coh_guard_mean,
    "coherence_guard_std": coh_guard_std,
    "rollback_rate_mean": rb_rate_mean,
    "rollback_rate_std": rb_rate_std,
    "overhead_p95": overhead_p95,
    "runs": runs,
}

# Save metrics.json
with open(os.path.join(OUT, "metrics.json"), "w", encoding="utf-8") as f:
    json.dump(metrics, f, indent=2, ensure_ascii=False)

# Save metrics.csv
with open(os.path.join(OUT, "metrics.csv"), "w", newline="", encoding="utf-8") as f:
    w = csv.writer(f)
    w.writerow(["seed","use_guard","runtime_s","rollbacks","rollback_rate","coherence_avg","entropy_avg","entropy_std","timesteps","threshold_entropy"])
    for r in runs:
        for key in ["baseline","guard"]:
            m = r[key]
            w.writerow([r["seed"], key, m["runtime_s"], m["rollbacks"], m["rollback_rate"], m["coherence_avg"], m["entropy_avg"], m["entropy_std"], m["timesteps"], m["threshold_entropy"]])

# Plot representative series (guard, last seed)
states_plot, _ = simulate(seeds[-1], use_guard=True)
plt.figure(figsize=(8,4.5))
for i, name in enumerate(["calm","tension","joy"]):
    plt.plot(states_plot[:, i], label=name)
plt.title("Ressenti computationnel mimétique — vecteurs émotionnels (guard ΔM11.3)")
plt.xlabel("Temps (pas)")
plt.ylabel("Intensité normalisée [0,1]")
plt.legend(loc="best")
os.makedirs(os.path.join(OUT, "figures"), exist_ok=True)
plt.savefig(os.path.join(OUT, "figures", "vector_emotion_series.pdf"), format="pdf", bbox_inches="tight")
plt.close()

# C2PA placeholder + merkle-ish log
with open(os.path.join(OUT, "logs", "c2pa_log.txt"), "w", encoding="utf-8") as f:
    f.write("C2PA Placeholder — To be signed.\n")

def sha256_of_file(path):
    import hashlib
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(65536), b""):
            h.update(chunk)
    return h.hexdigest()

file_hashes = []
for base, _, files in os.walk(OUT):
    for fn in files:
        p = os.path.join(base, fn)
        rel = os.path.relpath(p, ROOT)
        file_hashes.append((rel, sha256_of_file(p)))
file_hashes.sort(key=lambda x: x[0])
concat = "".join(h for _, h in file_hashes).encode("utf-8")
root_hash = hashlib.sha256(concat).hexdigest()

with open(os.path.join(OUT, "merkle_log.txt"), "w", encoding="utf-8") as f:
    f.write(f"Merkle Root: {root_hash}\n")
    for rel, h in file_hashes:
        f.write(f"{h}  {rel}\n")

# Optional Excel KPIs
kpi_rows = [{
    "metric": "interop_target", "value": 0.60,
},{
    "metric": "compliance_target", "value": 0.65,
},{
    "metric": "C2PA_artifacts", "value": 1.0,
},{
    "metric": "overhead_p95", "value": metrics["overhead_p95"],
},{
    "metric": "coherence_guard_mean", "value": metrics["coherence_guard_mean"],
},{
    "metric": "coherence_guard_std", "value": metrics["coherence_guard_std"],
},{
    "metric": "rollback_rate_mean", "value": metrics["rollback_rate_mean"],
}]
if HAVE_PANDAS:
    df = pd.DataFrame(kpi_rows)
    xlsx = os.path.join(ROOT, "annexes", "KPIs.xlsx")
    os.makedirs(os.path.join(ROOT, "annexes"), exist_ok=True)
    with pd.ExcelWriter(xlsx, engine="xlsxwriter") as writer:
        df.to_excel(writer, index=False, sheet_name="KPIs")
else:
    with open(os.path.join(ROOT, "annexes", "KPIs.csv"), "w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(["metric","value"])
        for row in kpi_rows:
            w.writerow([row["metric"], row["value"]])

print("Done. Metrics and artifacts generated.")