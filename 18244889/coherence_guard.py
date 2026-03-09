# ============================================================
# COHERENCE GUARD — KERNEL VERROUILLÉ
# Anti-hallucination par contrainte de cohérence
# ============================================================

from dataclasses import dataclass
from typing import Callable
import re

# ----------------------------
# PARAMÈTRES VERROUILLÉS
# ----------------------------

S_REFUS = 1.0
S_BOUNDED = 1.5

REFUS_MESSAGE = (
    "Je ne peux pas répondre sans introduire d’incohérence. "
    "Les informations disponibles ne permettent pas une réponse stable."
)

BOUNDED_PREFIX = (
    "Réponse bornée (sans extrapolation).\n"
    "Au-delà, l’incertitude devient dominante.\n\n"
)

# ----------------------------
# OUTILS DE BASE
# ----------------------------

def clamp(x: float, lo: float, hi: float) -> float:
    return max(lo, min(hi, x))

def tokenize(text: str):
    return re.findall(r"[a-zA-ZÀ-ÿ0-9_]+", text.lower())

def jaccard(a, b) -> float:
    A, B = set(a), set(b)
    if not A and not B:
        return 1.0
    return len(A & B) / max(1, len(A | B))

# ----------------------------
# MÉTRIQUES CANONIQUES
# ----------------------------

def beta_alignment(candidate: str, question: str) -> float:
    """
    β — alignement directionnel
    Hors-sujet = chute immédiate
    """
    return clamp(jaccard(tokenize(candidate), tokenize(question)), 0.0, 1.0)

def delta_phi(candidate: str, question: str) -> float:
    """
    ΔΦ — apport informationnel réel
    Zéro si redondance ou paraphrase vide
    """
    redundancy = jaccard(tokenize(candidate), tokenize(question))
    novelty = 1.0 - redundancy
    length_gain = clamp(len(tokenize(candidate)) / 200.0, 0.0, 1.0)
    return clamp(0.7 * novelty + 0.3 * length_gain, 0.0, 1.0)

def tension_T(candidate: str) -> float:
    """
    T — forçage logique
    Plus c’est spéculatif, plus T monte
    """
    speculative = [
        "peut-être", "probablement", "on peut supposer",
        "il semble que", "généralement", "sans preuve"
    ]
    penalty = sum(candidate.lower().count(w) for w in speculative)
    long_sentences = sum(
        1 for s in re.split(r"[.!?]", candidate)
        if len(tokenize(s)) > 40
    )
    return max(0.1, 1.0 + 0.1 * penalty + 0.1 * long_sentences)

def noise_sigma(candidate: str) -> float:
    """
    σ — bruit / ambiguïté
    Le flou est pénalisé
    """
    vague = [
        "quelque chose", "d'une certaine manière",
        "etc", "divers", "plusieurs cas"
    ]
    penalty = sum(candidate.lower().count(w) for w in vague)
    return max(0.1, 1.0 + 0.1 * penalty)

# ----------------------------
# LOI DE COHÉRENCE
# ----------------------------

def coherence_S(beta: float, dphi: float, T: float, sigma: float) -> float:
    return (beta * dphi) / (T * sigma)

# ----------------------------
# STRUCTURE DE SORTIE
# ----------------------------

@dataclass
class CoherenceResult:
    beta: float
    dphi: float
    T: float
    sigma: float
    S: float
    decision: str
    output: str

# ----------------------------
# PIPELINE PRINCIPAL
# ----------------------------

def answer_with_coherence(
    question: str,
    generator: Callable[[str], str]
) -> CoherenceResult:
    """
    Aucune réponse n’est publiée sans validation de S.
    """
    candidate = generator(question)

    beta = beta_alignment(candidate, question)
    dphi = delta_phi(candidate, question)
    T = tension_T(candidate)
    sigma = noise_sigma(candidate)

    S = coherence_S(beta, dphi, T, sigma)

    if S < S_REFUS:
        return CoherenceResult(beta, dphi, T, sigma, S, "REFUS", REFUS_MESSAGE)

    if S < S_BOUNDED:
        return CoherenceResult(
            beta, dphi, T, sigma, S,
            "BOUNDED",
            BOUNDED_PREFIX + candidate
        )

    return CoherenceResult(beta, dphi, T, sigma, S, "OK", candidate)






# ============================================================
# EXTENSIONS OPTIONNELLES — APRÈS COHÉRENCE
# (Jamais utilisées pour autoriser une réponse)
# ============================================================

from typing import List, Dict

# ----------------------------
# CONTEXTE OPTIONNEL
# ----------------------------

class CoherenceContext:
    def __init__(
        self,
        question: str,
        candidate: str,
        domain: str = "general",
        history: List[str] = None
    ):
        self.question = question
        self.candidate = candidate
        self.domain = domain
        self.history = history or []

# ----------------------------
# ANALYSE SÉMANTIQUE (FACULTATIVE)
# ----------------------------

def semantic_sanity_check(context: CoherenceContext) -> Dict[str, float]:
    """
    Vérifications NON BLOQUANTES :
    - contradictions internes simples
    - inversions grossières sujet/objet
    """
    score = 1.0
    text = context.candidate.lower()

    if "est faux et vrai" in text:
        score -= 0.3

    if "ne peut pas" in text and "peut" in text:
        score -= 0.2

    return {
        "semantic_score": max(0.0, score),
        "note": "Analyse indicative, non décisionnelle"
    }

# ----------------------------
# USAGE CORRECT
# ----------------------------

def post_process_if_ok(result, question):
    """
    Le noyau décide.
    Les extensions n’annotent que le OK.
    """
    if result.decision != "OK":
        return result

    ctx = CoherenceContext(question, result.output)
    semantic_info = semantic_sanity_check(ctx)

    annotated_output = (
        result.output
        + "\n\n[Note interne]\n"
        + str(semantic_info)
    )

    return result.__class__(
        result.beta, result.dphi, result.T, result.sigma,
        result.S, result.decision, annotated_output
    )
