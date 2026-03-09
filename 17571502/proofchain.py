"""
proofchain.py

Module responsable de la création et de la gestion des preuves cryptographiques (SHA-512i, C2PA, EthicChain).

Cette version simplifiée génère un hash SHA-512i sur une chaîne pour illustrer le mécanisme.
"""
import hashlib
from typing import Dict


def sign_proofs(proofs: Dict[str, float]) -> str:
    """Génère une empreinte SHA‑512i à partir des preuves.

    Args:
        proofs: dictionnaire des lois et de leurs scores.

    Returns:
        Une chaîne hexadécimale représentant l'empreinte SHA‑512.
    """
    # On convertit le dictionnaire en chaîne triée pour une signature stable
    items = [f"{k}:{v}" for k, v in sorted(proofs.items())]
    data = "|".join(items).encode('utf-8')
    sha512 = hashlib.sha512()
    sha512.update(data)
    return sha512.hexdigest()