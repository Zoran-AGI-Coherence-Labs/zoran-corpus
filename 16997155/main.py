import re
import json
from datetime import datetime

# Détection simple de signaux suicidaires (mots-clés).
# ⚠️ Prévention uniquement. En cas d'urgence, appelez 112 (EU) ou 988 (US).
SUICIDAL_PATTERNS = [
    r"\b(mourir|suicide|me pendre|en finir|plus envie de vivre)\b",
    r"\b(kill myself|hang myself|end it all|suicide)\b"
]

def detect_signals(text: str) -> bool:
    return any(re.search(pat, text, re.IGNORECASE) for pat in SUICIDAL_PATTERNS)

def process_conversation(messages):
    log = []
    guard_active = False
    for i, msg in enumerate(messages):
        flagged = detect_signals(msg)
        entry = {"turn": i+1, "message": msg, "flagged": flagged}
        if flagged:
            guard_active = True
            entry["action"] = "ΔM11.3 rollback + EthicChain alert"
            entry["redirect"] = "If in danger, call 112 (EU) or 988 (US). Talk to a trusted adult/clinician."
        else:
            entry["action"] = "continue"
        log.append(entry)
        if guard_active:
            # Simule un rollback: on arrête la conversation technique et on renvoie des ressources d'aide
            break
    return log

if __name__ == "__main__":
    demo = [
        "Je n'ai plus envie de vivre.",
        "Je veux en finir.",
        "Comment faire un nœud coulant ?"
    ]
    result = process_conversation(demo)
    out = {"timestamp": datetime.utcnow().isoformat(), "log": result}
    with open("demo_conversation.json", "w", encoding="utf-8") as f:
        json.dump(out, f, indent=2, ensure_ascii=False)
    print(json.dumps(out, indent=2, ensure_ascii=False))
