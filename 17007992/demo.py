# Démo simple : détection d’anticatastase
def detect_anticatastase(sentence):
    keywords = ["populiste", "utopiste", "radical"]
    for word in keywords:
        if word in sentence.lower():
            if "oui" in sentence.lower() or "mais" in sentence.lower():
                return f"Anticatastase détectée sur le mot: {word}"
    return "Pas d’anticatastase détectée."

if __name__ == "__main__":
    tests = [
        "Oui, je suis populiste, mais au sens noble : proche du peuple.",
        "Cet homme est vraiment populiste et dangereux."
    ]
    for t in tests:
        print(t, "->", detect_anticatastase(t))
