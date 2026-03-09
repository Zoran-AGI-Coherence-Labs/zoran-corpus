# PRE-REG — Non-Absorbable Transversal Experimental Program

Date: 2026-01-24
Pivot DOI: 10.5281/zenodo.18360840

## Objective
Define and test a single experimental pipeline (observables → metrics → dynamics → decision)
across heterogeneous consciousness domains using public data only.
No subjective ground truth is assumed.

## Exclusive Outputs
Each analysis unit outputs exactly one label:
PASS | FAIL | INDETERMINATE
INDETERMINATE must never be collapsed in reporting.

## Minimal Common Metrics (mandatory)
A. Structure / Integration
- Multi-scale complexity (e.g., entropy over band-power distributions)
- Propagation / integration proxy (e.g., mean pairwise coherence or evoked spatiotemporal spread)
- PCIst when perturbation data exist (external reference implementation only)

B. Dissipation / Noise
- Instability (window-to-window drift)
- Unexplained variance / artifact sensitivity indicators

C. Phenomenal Coherence (descriptive constraint)
- Cφ := D_KL(P || Q)
  - P: distribution derived from observables of the current state
  - Q: “dissolution” distribution derived from explicit surrogates (shuffles / phase randomization) or equilibrated baselines
Cφ must not be used as a performance score.

## Fixed Thresholds (global, pre-registered)
- Separation: AUC ≥ 0.70 (or equivalent, reported explicitly)
- Shuffle degradation: ≥ 30% relative drop (structure/propagation)
- Dose monotonicity (if applicable): |Spearman ρ| ≥ 0.30
- Discordance rule: if structure increases while propagation/integration decreases beyond tolerance → INDETERMINATE

## Mandatory Negative Controls
A. Shuffles / Surrogates
- Block shuffles
- Phase randomization
Expected: ≥30% degradation; else FAIL.

B. Ordinal Break (Anesthesia)
- Random permutation of dose/level labels
Expected: loss of monotonicity; else FAIL.

C. Inter-Domain Transfer Failure
- Calibrate on domain A, test on B
Expected: no spurious invariance; else FAIL.

D. DOC Access Constraint
- If controlled-access DOC data unavailable → INDETERMINATE (no extrapolation).

## Anti-Absorption Rule (global)
If any mandatory negative control does not break the pipeline as specified → GLOBAL FAIL.

## Reporting (required)
- Verdict per domain (PASS/FAIL/INDETERMINATE)
- GLOBAL verdict
- Explicit negative-control outcomes
- Fixed seeds, environment lock, and artifact hashes for all outputs
