#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Zoran aSiM — Z5 compression + resonant cache (stdlib demo)
"""
import argparse, base64, hashlib, json, os, random, time, zlib
from datetime import datetime

SEEDS_DEFAULT = [13, 42, 101]

def z5_pack(b: bytes) -> str:
    return "Z5::" + base64.b64encode(zlib.compress(b)).decode()

def z5_unpack(s: str) -> bytes:
    assert s.startswith("Z5::")
    return zlib.decompress(base64.b64decode(s[4:]))

def resonant_key(text: str) -> str:
    return hashlib.sha256(text.encode()).hexdigest()[:16]

CACHE = {}

def resonant_get(prompt: str):
    k = resonant_key(prompt)
    v = CACHE.get(k)
    if not v: return None
    value, expires = v
    if time.time() > expires:
        del CACHE[k]
        return None
    return value

def resonant_set(prompt: str, value: str, ttl=3600):
    k = resonant_key(prompt)
    CACHE[k] = (value, time.time() + ttl)

def delta_guard(stability: float, threshold: float = 0.85) -> str:
    return "KEEP" if stability >= threshold else "ROLLBACK_ΔM11.3"

def read_text(path: str) -> str:
    with open(path, "r", encoding="utf-8") as f:
        return f.read()

def write_json(path: str, data):
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

def run(seeds, config_path):
    threshold, ttl = 0.85, 3600
    if os.path.exists(config_path):
        try:
            import yaml
            with open(config_path, "r", encoding="utf-8") as f:
                cfg = yaml.safe_load(f)
            threshold = cfg.get("delta_M11_3", {}).get("stability_threshold", threshold)
            ttl = cfg.get("zdm", {}).get("ttl_seconds_default", ttl)
        except Exception:
            pass

    os.makedirs("logs", exist_ok=True)
    sample_path = os.path.join("data", "sample_text.txt")
    with open(sample_path, "r", encoding="utf-8") as f:
        text = f.read()
    original = text.encode("utf-8")

    runs = []
    for s in seeds:
        random.seed(s)
        z5 = z5_pack(original)
        restored = z5_unpack(z5)
        ok = restored == original
        stability = 1.0 if ok else 0.0
        action = delta_guard(stability, threshold)

        t0 = time.time()
        _ = z5_pack(original)
        _ = z5_unpack(z5)
        latency_ms = (time.time() - t0) * 1000.0

        prompt = "zoran:demo:ondelette→fractal"
        if not resonant_get(prompt):
            resonant_set(prompt, z5, ttl=ttl)

        runs.append({
            "seed": s,
            "ok_roundtrip": ok,
            "stability": stability,
            "action": action,
            "original_bytes": len(original),
            "z5_bytes": len(z5.encode("utf-8")),
            "compression_ratio": len(z5.encode("utf-8")) / max(1, len(original)),
            "latency_ms": latency_ms
        })

    def avg(key):
        vals = [r[key] for r in runs]
        return sum(vals)/len(vals) if vals else 0.0

    metrics = {
        "timestamp": datetime.utcnow().isoformat() + "Z",
        "policy_used": {"threshold": threshold, "ttl": ttl},
        "runs": runs,
        "aggregates": {
            "stability_avg": avg("stability"),
            "latency_ms_avg": avg("latency_ms"),
            "compression_ratio_avg": avg("compression_ratio")
        }
    }
    write_json("metrics.json", metrics)
    print("Wrote metrics.json")

if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--seeds", nargs="*", type=int, default=SEEDS_DEFAULT)
    ap.add_argument("--config", type=str, default="policy.yaml")
    args = ap.parse_args()
    run(args.seeds, args.config)
