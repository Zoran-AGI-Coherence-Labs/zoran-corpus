# glyphnet.py — Structured AI Protocol (GlyphNet Eurêka demo)
def encode(obj: dict)->str:
    fields = ["OBJ","CTX","EVID","TRACE"]
    return "⟦" + "⋄".join(f"{k}:{obj.get(k,'')}" for k in fields) + "⟧"
