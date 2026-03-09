# policy_engine.py — mapping curseurs → paramètres (démo)
def map_params(sliders: dict) -> dict:
    s = lambda k, d=50: int(sliders.get(k, d))
    creativity = s('creativity',35)/100
    rag = s('rag_intensity',70)/100
    return {
        "temperature": round(0.1 + 0.9*(creativity**1.7), 3),
        "top_p": round(0.6 + 0.4*creativity, 3),
        "top_k": int(3 + round(17*rag)),
        "rag_alpha": round(0.25 + 0.65*rag, 3),
        "abstain_threshold": round(0.3 + 0.7*(s('no_hallu',85)/100), 3)
    }
