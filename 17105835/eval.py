#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import json, os

INP = "metrics.json"
OUT = "metrics_ablation.json"

def main():
    if not os.path.exists(INP):
        print("Run main.py first.")
        return
    with open(INP, "r", encoding="utf-8") as f:
        m = json.load(f)
    runs = m.get("runs", [])
    ablation = {
        "baseline": m.get("aggregates", {}),
        "minus_Z5": "N/A (demo)",
        "minus_ZDM": "N/A (demo)",
        "minus_DeltaM11_3": "N/A (demo)",
        "minus_Glyphnet": "N/A (demo)"
    }
    with open(OUT, "w", encoding="utf-8") as f:
        json.dump(ablation, f, ensure_ascii=False, indent=2)
    print("Wrote", OUT)

if __name__ == "__main__":
    main()
