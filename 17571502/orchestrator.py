"""
orchestrator.py

Script principal orchestrant les étapes de mesure, découverte, falsification et signature des preuves.

Usage :
    python3 orchestrator.py --domain=<domaine> --data=<chemin-vers-donnees>

Cette version simplifiée ignore la lecture réelle des données et renvoie des valeurs par défaut.
"""
import argparse
import json
from pathlib import Path

from measure import measure
from discover import discover
from falsify import falsify
from proofchain import sign_proofs


def save_results(results_path: Path, metrics: dict, proofs: dict, signature: str) -> None:
    """Sauvegarde les résultats dans le répertoire de sortie.

    Args:
        results_path: répertoire où écrire les fichiers
        metrics: dictionnaire des métriques calculées
        proofs: dictionnaire des lois et scores
        signature: empreinte SHA-512i
    """
    results_path.mkdir(parents=True, exist_ok=True)
    # metrics.json
    with open(results_path / "metrics.json", "w") as f:
        json.dump(metrics, f, indent=2)
    # proof_report.md
    with open(results_path / "proof_report.md", "w") as f:
        f.write("# Rapport de preuve\n\n")
        for law, score in proofs.items():
            f.write(f"- Loi : {law} — Score : {score}\n")
        f.write(f"\nEmpreinte SHA-512i : {signature}\n")
    # dashboard.html (simple placeholder)
    with open(results_path / "dashboard.html", "w") as f:
        f.write("<html><body><h1>Dashboard ΔPOLYMORPH-ENGINE</h1><p>Consultez metrics.json pour plus de détails.</p></body></html>")


def main():
    parser = argparse.ArgumentParser(description="Exécute le moteur ΔPOLYMORPH-ENGINE Ω⁸")
    parser.add_argument("--domain", required=True, help="Domaine d'application (energy, bio, ai, neuro, eco)")
    parser.add_argument("--data", required=True, help="Chemin vers le fichier de données d'entrée")
    args = parser.parse_args()

    # Ici, on ignore le chargement de données et on fournit un objet factice
    data_obj = None  # Dans la version complète, charger le fichier args.data

    beta, deltaC, lam = measure(data_obj, args.domain)
    candidate_laws = discover(beta, deltaC, lam)
    results = falsify(candidate_laws, beta, deltaC, lam)
    signature = sign_proofs(results)

    # Construire les métriques à enregistrer
    metrics = {
        "beta": beta,
        "deltaC": deltaC,
        "lambda": lam,
        "laws": candidate_laws,
        "scores": results,
    }

    # Enregistrer les résultats
    save_results(Path("results"), metrics, results, signature)

    print("Moteur ΔPOLYMORPH-ENGINE Ω⁸ exécuté avec succès.")


if __name__ == "__main__":
    main()