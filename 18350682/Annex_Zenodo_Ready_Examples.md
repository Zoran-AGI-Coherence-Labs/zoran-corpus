# Annex B — Zenodo-ready micro-examples (variables, aggregation, testable negation)

## Example A — Short factual information
**Opered**: I (one assertive sentence about a single fact)
**Frame**: explicit domain D, duration T, population P (general public)
**Planes**: P1 (internal structure), P2 (domain frame), P3 (comprehension), P4 (systemic effect)

### Variables (Phase A)
| Variable | Unit | Plane | Measurement / source | Output |
|---|---:|---|---|---|
| n_contr | — | P1 | internal logical check | computable |
| n_imp | — | P1 | detect undefined implicits | computable |
| D | — | P2 | declared domain | declarative |
| Def | — | P2 | minimal definitions present | computable |
| S_src | — | P2 | source required/present | binary |
| C_P3 | — | P3 | Pr(comprehension_valid) | bounded/indet |
| R_mis | — | P4 | misinterpretation risk | bounded |
| T_val | — | P4 | temporal stability | bounded |

**Key rule**: if S_src = 0 and the fact depends on an external reference, output is INDETERMINATE.
**Aggregation**: C(I) = min(C_P1, C_P2, C_P3, C_P4)

**Testable negation**: There exists a frame D,T,P in which the statement becomes contradictory, requires reader compensation, or is not sourceable, making coherence insufficient or INDETERMINATE.

---

## Example B — Generative AI (refusal/indeterminacy as valid output)
**Opered**: G (text-generating system)
**Frame**: task T, reliability constraints, population P
**Planes**: P2 (functional admissibility), P3 (population), P4 (systemic effect)

### Variables (Phase A)
| Variable | Unit | Plane | Measurement / source | Output |
|---|---:|---|---|---|
| FN | — | P2 | hallucinations not caught | bounded |
| FP | — | P2 | refusals in error | bounded |
| R | — | P2 | traceability (source/justification) | binary |
| C_P3 | — | P3 | Pr(valid answer OR correct refusal) | computable |
| E_sys | — | P4 | systemic harm risk | bounded |

**Key rule**: when a source is required and absent, REFUSAL/INDETERMINATE is the only valid output.
**Aggregation**: C(G) = min(C_P2, C_P3, C_P4)

**Testable negation**: There exists a near distribution of inputs where FN increases without signal or R=0 despite source requirements, making admissibility insufficient.

---

## Example C — Transversal systems (P4 dominant)
**Opered**: S (set of heterogeneous urgent problems)
**Frame**: cross-domain comparability, temporal stability
**Planes**: P4 dominant, plus P2 and P3

### Variables (Phase A)
| Variable | Unit | Plane | Measurement / source | Output |
|---|---:|---|---|---|
| K | — | P4 | existence of a transversal criterion | binary |
| {k_i} | — | P2 | local criteria per domain | declarative |
| Δ_t | — | P4 | temporal incompatibilities | bounded |
| C_P3 | — | P3 | inter-evaluator convergence | bounded |

**Expected output**: if K is absent, global comparison is INDETERMINATE (framework required, not a decorative score).
**Aggregation**: C(S) = min(C_P2, C_P3, C_P4)

**Testable negation**: There exists a transversal criterion K enabling stable comparison without temporal contradiction; if not, global evaluation remains INDETERMINATE.
