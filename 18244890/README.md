# Coherence Guard

Deterministic coherence-based filter preventing hallucinations in generative systems.

DOI: https://doi.org/10.5281/zenodo.18244890  
Author: Frédéric Tabary  
Licenses: MIT License (Open Core) + Commercial License  

---

## 1. What This Project Is

Coherence Guard is a deterministic publication filter designed to prevent the release of incoherent outputs (“hallucinations”) in generative systems.

It operates by enforcing a hard coherence constraint before any generated response is published.

The system is:
- model-agnostic,
- non-probabilistic,
- non-adaptive,
- refusal-native.

---

## 2. What This Project Is Not

Coherence Guard is not:
- a language model,
- a fact-checker,
- a truth oracle,
- a semantic validator,
- an optimization or ranking system.

It does not improve answers.  
It restricts which answers are allowed to exist.

---

## 3. Core Rule (Minimal)

A candidate response is publishable if and only if:

\[
S = \frac{\beta \cdot \Delta\Phi}{T \cdot \sigma} \ge 1
\]

If this condition is not met, the system must refuse to answer.

Refusal is a valid and correct system behavior.

---

## 4. Typical Usage Pattern

```text
User Query
   ↓
Generative Model (any)
   ↓
Candidate Answer (internal)
   ↓
Coherence Guard
   ↓
┌───────────────┬──────────────────┐
│ S < 1         │ REFUSAL           │
│ 1 ≤ S < 1.5   │ BOUNDED ANSWER    │
│ S ≥ 1.5       │ PUBLISHED ANSWER  │
└───────────────┴──────────────────┘
```

The generative model never decides whether an answer is published.

---

## 5. Guarantees

This project guarantees exactly one thing:

> No incoherent answer can be published.

It does not guarantee correctness, completeness, or usefulness.

---

## 6. Installation

There is no required installation.

Coherence Guard is designed to be:
- copied as a kernel,
- embedded as a middleware,
- audited as a standalone component.

Reference implementation is provided in Python (Appendix B of the White Paper).

---

## 7. Integration Example (Minimal)

```python
result = answer_with_coherence(question, generator)

if result.decision == "REFUS":
    return result.output

return result.output
```

No retry, no override, no fallback generation is allowed upstream.

---

## 8. Configuration Rules (Non-Negotiable)

To preserve the guarantee:

- thresholds must not be learned,
- thresholds must not be optimized,
- refusal must be allowed,
- no post-hoc publication override is permitted.

Violating any of these rules invalidates the guarantee.

---

## 9. Licensing

### MIT License (Open Core)

The coherence law, thresholds, and reference kernel are released under the MIT License.

This allows:
- academic use,
- research replication,
- independent audits.

### Commercial License

Commercial deployment, proprietary integration, certification, or SaaS usage require a commercial license.

Contact details and terms are provided in the Zenodo record.

---

## 10. Citation

Tabary, F. (2026). Coherence Guard: A Deterministic Coherence-Based Filter for Preventing Hallucinations in Large Language Models. Zenodo. https://doi.org/10.5281/zenodo.18244890

---

## 11. Status

This project is:
- complete,
- closed under its formal claims,
- stable by design.

---

## 12. Final Note

If a system cannot answer coherently, it should not answer at all.

Coherence Guard enforces this rule.
