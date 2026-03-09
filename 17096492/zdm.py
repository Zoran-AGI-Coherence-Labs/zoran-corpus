# zdm.py — Dual Memory (demo stdlib)
import os, time, json, hashlib

class ZDM:
    def __init__(self, hardcore_path="zdm_hardcore.jsonl"):
        self.hardcore_path = hardcore_path
        self.cache = {}

    def _hash(self, s: str)->str:
        return hashlib.sha256(s.encode()).hexdigest()

    def log_hardcore(self, record: dict):
        with open(self.hardcore_path, "a", encoding="utf-8") as f:
            f.write(json.dumps(record, ensure_ascii=False) + "\n")

    def write(self, key: str, value: dict):
        self.cache[key] = value
        rec = {"t": time.time(), "k": key, "sha": self._hash(json.dumps(value, sort_keys=True))}
        self.log_hardcore(rec)

    def read(self, key: str):
        return self.cache.get(key)
