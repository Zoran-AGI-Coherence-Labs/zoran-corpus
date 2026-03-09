# Zoran Dual-Memory (ZDM) — skeleton
class ZDM:
    def __init__(self):
        self.hardcore = {}       # persistent, auditable
        self.resonant_cache = {} # syntonic, zero-write

    def put(self, k, v, persistent=False):
        if persistent:
            self.hardcore[k] = v
        else:
            self.resonant_cache[k] = v

    def get(self, k):
        return self.resonant_cache.get(k, self.hardcore.get(k))

    def clear_cache(self):
        self.resonant_cache.clear()
