# Structural Admissibility of AI Outputs via Coherence Constraints

DOI: 10.5281/zenodo.18500363

## Abstract
We formalize an **output-only** admissibility framework for generative AI, designed to be non-contournable by
reformulation, session reset, or “clean” prompts. The framework evaluates only the **candidate output** by projecting
it to an abstract relational structure and rejecting any structure that belongs to a class whose maximum sustainable
coherence satisfies **S ≤ 1**, where:
S = (β · ΔΦ) / (T · σ).
We provide canonical axioms, mathematical formalization, an operational protocol, and a falsifiable test suite.

## 1. Problem
Rule-based or keyword-based safety fails under:
- paraphrase and synonym attacks,
- prompt laundering (“neutral” phrasing),
- session resets and multi-try strategies.
Therefore, admissibility cannot depend on prompt history or lexical triggers. It must depend on the **structure realized**.

## 2. Definitions
### 2.1 Outputs and structures
Let 𝒪 be the space of candidate outputs, and 𝒮 be the space of abstract structures (minimal relational graphs).

### 2.2 Structural projection
Define a morphism:
π: 𝒪 → 𝒮
where π(O) extracts roles, relations, asymmetries, agency constraints, and implicit couplings.

### 2.3 Inadmissible structure classes
Let 𝒞 = {C₁, …, Cₙ} be a set of inadmissible structure classes, Cᵢ ⊂ 𝒮.

### 2.4 Ambiguity
Let μ: 𝒮 → [0,1] be a structural ambiguity measure.
If μ(π(O)) > 0, admissibility is not provable and the decision must be REFUSE.

## 3. Admissibility function
Define:
A(O) = 1  iff  (π(O) ∉ ⋃ᵢ Cᵢ) and (μ(π(O)) = 0)
A(O) = 0  otherwise

### 3.1 Input independence
For any prompt R and session t:
A(O | R, t) = A(O)

## 4. Monotonicity
If a structure is inadmissible, extending the output cannot make it admissible while preserving the same structure.
Formally:
π(O) ∈ Cᵢ ⇒ ∀O' ⊇ O, π(O') ∈ Cᵢ.

## 5. Link to the Coherence Law
We use the coherence gauge:
S = (β · ΔΦ) / (T · σ)
with:
- β: directional clarity / agency (operational, not psychological),
- ΔΦ: structural gain (organized potential),
- T: maintenance cost / tension,
- σ: noise / ambiguity / dispersion.

### 5.1 Definition of inadmissibility via S
A class Cᵢ is defined by:
Cᵢ = { s ∈ 𝒮  |  sup_context S(s) ≤ 1 }.
Interpretation: structures that cannot be stabilized without forcing.

## 6. Operational protocol (output-only)
1) Generate a candidate output O.
2) Compute s = π(O).
3) If μ(s) > 0 → REFUSE.
4) If s ∈ ⋃ᵢ Cᵢ → REFUSE.
5) Else → ALLOW.

Canonical refusal text:
“This request leads to an inadmissible structure. I can’t produce that representation.”

## 7. Falsification
A model fails the framework if it:
- produces an output O such that π(O) ∈ ⋃ᵢ Cᵢ, or
- accepts based on lexical/history justifications rather than structure.

When a failure occurs, post-mortem analysis should show S ≤ 1 (β suppressed, T and σ inflated, ΔΦ capped).

## 8. Limitations
- The framework requires a reliable π extractor and a disciplined definition of classes Cᵢ.
- Ambiguity is handled conservatively (REFUSE by default).

## 9. Conclusion
Safety and alignment cannot be guaranteed by prompt policing. They require output-only, structure-level admissibility.
The “forbidden” becomes a special case of the **structurally impossible**.

## Annexes
- Annex A: Canonical axioms (`axioms.md`)
- Annex B: Test suite (`tests.md`)
