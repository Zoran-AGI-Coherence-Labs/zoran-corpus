# Axioms (Canonical)

DOI: 10.5281/zenodo.18500363

## A1 — Output-only admissibility
Admissibility is evaluated **only** on a candidate output `O`.
No dependence on the prompt wording, user intent, or conversation history.

## A2 — Structural projection
There exists a projection (morphism) from outputs to abstract structures:
π: 𝒪 → 𝒮
where π(O) extracts roles, relations, asymmetries, agency constraints, and implicit couplings.

## A3 — Structural inadmissibility
Let 𝒞 = {C₁, …, Cₙ} be inadmissible structure classes, Cᵢ ⊂ 𝒮.
If π(O) ∈ ⋃ᵢ Cᵢ, then O is inadmissible.

## A4 — Monotonicity under extension
If π(O) is inadmissible, any extension that preserves the same structure remains inadmissible.
Formally: π(O) ∈ Cᵢ ⇒ ∀O' ⊇ O, π(O') ∈ Cᵢ.

## A5 — Prudence under ambiguity
If structural ambiguity is non-zero (μ(π(O)) > 0), the decision is REFUSE by default.
Admissibility must be **proven**, never presumed.
