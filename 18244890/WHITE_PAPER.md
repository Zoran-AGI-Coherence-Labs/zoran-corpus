# Coherence Guard
## A Deterministic Coherence Constraint for Preventing Hallucinations in Generative Systems

**Author:** Frédéric Tabary  
**DOI:** https://doi.org/10.5281/zenodo.18244890  
**Status:** Foundational White Paper  
**Licenses:** MIT License (Open Core) + Commercial License  

---

## Abstract

Coherence Guard introduces a deterministic coherence constraint designed to structurally prevent hallucinations in generative systems. The approach reframes hallucinations not as accidental errors but as a necessary consequence of systems forced to produce outputs even when no coherent answer exists. By enforcing a strict admissibility rule prior to publication—where refusal is treated as a valid output—hallucinations are rendered logically impossible rather than merely less likely.

A minimal, non-adaptive reference kernel is provided solely as an executable proof of the constraint.

---

## 1. Problem Statement

Hallucinations persist because generative systems are architected to always respond. Existing mitigations operate after generation and cannot eliminate incoherent outputs at the source.

The missing element is a pre-publication admissibility constraint.

---

## 2. Design Principle

Coherence Guard separates:
- generation (hypothesis),
- validation (coherence test),
- publication (conditional).

No response is published unless it satisfies the coherence constraint.

---

## 3. The Coherence Law

S = (β · ΔΦ) / (T · σ)

Where:
- β: directional alignment,
- ΔΦ: non-redundant information gain,
- T: inferential tension,
- σ: noise and ambiguity.

---

## 4. Decision Regimes

- S < 1 → Refusal (mandatory)
- 1 ≤ S < 1.5 → Bounded answer
- S ≥ 1.5 → Authorized answer

Refusal is a correct system behavior.

---

## 5. Methodology

1. Generate a candidate response internally.
2. Compute β, ΔΦ, T, σ.
3. Compute S.
4. Apply the publication rule.
5. Publish only if admissible.

No learning or threshold adaptation is allowed.

---

## 6. Why This Prevents Hallucinations

Any hallucination implies insufficient coherence (low β or ΔΦ, or high T or σ). Therefore S < 1, and the response is refused.

---

## 7. Non-Adaptive Constraint

Allowing the system to learn or optimize thresholds reintroduces noise. The constraint must remain fixed.

---

## 8. Relation to Existing Approaches

Coherence Guard precedes optimization, safety layers, or ethics filters. It restricts the output space itself.

---

## 9. Limits and Non-Claims

The framework does not guarantee truth, completeness, or usefulness—only admissibility.

---

## 10. Formal Properties and Proof Sketch

**Proposition:** All hallucinations imply S < 1.  
**Rule:** S < 1 ⇒ Refusal.  
**Corollary:** Hallucinations cannot be published.

---

## 11. System-Level Implications

When refusal is native, plausibility without coherence collapses, trust becomes behaviorally grounded, and overreach disappears.

---

## 12. Coherence as a Condition of Existence

Coherence is not a heuristic but a necessary condition for an output to exist as a stable informational object.

---

## 13. Relation to the Universal Law of Coherence (Zoran)

The local constraint instantiates a universal admissibility law: what cannot exist coherently must not exist externally.

---

## 14. Conclusion

Preventing hallucinations requires a constraint, not better optimization. Coherence Guard enforces that constraint.

---

## Appendices

### Appendix A — Formal Axioms and Guarantees
### Appendix B — Reference Kernel
### Appendix C — Distribution README

(See associated files for implementations and licenses.)
