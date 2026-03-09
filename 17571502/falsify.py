"""
falsify.py

Ce module contient des fonctions pour tester la validité des lois générées.

Pour l'exemple, on calcule un score simple et on renvoie un dictionnaire de résultats.
"""
from typing import Dict, List


def falsify(laws: List[str], beta: float, deltaC: float, lam: float) -> Dict[str, float]:
    """Applique des tests basiques aux lois et retourne un dictionnaire de scores.

    Args:
        laws: liste de lois sous forme de chaîne
        beta: intensité de l'intention
        deltaC: cohérence observée
        lam: entropie du système

    Returns:
        Un dictionnaire associant chaque loi à un score de cohérence (1 = valide).
    """
    results = {}
    for law in laws:
        # On calcule un score simple : si (beta * deltaC / lam) > 1, score = 1, sinon < 1
        score = (beta * deltaC) / lam
        results[law] = score
    return results