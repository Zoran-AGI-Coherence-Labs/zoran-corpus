
import json, matplotlib.pyplot as plt, pathlib
m = json.load(open("metrics.json"))
xs = list(range(1, len(m["runs"])+1))
for k in ["reward_avg","coherence_avg","stability_avg","latency_p95","rollbacks"]:
    plt.figure()
    ys = [r[k] for r in m["runs"]]
    plt.plot(xs, ys, marker="o")
    plt.title(k); plt.xlabel("run"); plt.ylabel(k)
    outfile = f"fig_{k}.png"
    plt.savefig(outfile, dpi=180, bbox_inches="tight"); plt.close()
print("[OK] charts written: fig_*.png at root")
