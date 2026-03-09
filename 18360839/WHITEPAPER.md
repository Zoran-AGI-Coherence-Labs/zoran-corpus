# A Non-Absorbable Transversal Experimental Program for Consciousness States Using Public Data

Date: 2026-01-24
Pivot DOI: 10.5281/zenodo.18360840

## Abstract
We define a fully pre-registered experimental program to test the transversal validity of a single analysis
pipeline across heterogeneous consciousness states using public datasets only. The program spans
(i) natural sleep, (ii) pharmacological anesthesia (EEG and fMRI), (iii) causal perturbation (TMS-EEG with PCIst),
and (iv) disorders of consciousness (DOC), with an optional high-resolution intracranial extension.
Mandatory negative controls, inter-domain transfer tests, and a formal INDETERMINATE outcome prevent
post-hoc absorption. A global FAIL is enforced if negative controls do not break the pipeline. No subjective
ground truth is assumed.

## Scope
- Public-data-first (open datasets plus declared controlled-access sources)
- Multi-domain + multi-modality
- Causal tests prioritized when available (perturbation)

## Program Overview
Single form:
observables → metrics → dynamics → decision

Outputs:
PASS | FAIL | INDETERMINATE (exclusive)
INDETERMINATE is preserved and reported.

## Metrics (minimal common set)
### Structure / Integration
- multi-scale complexity (e.g., entropy over band power distributions)
- propagation/integration proxy (e.g., coherence-based or evoked spatiotemporal spread)
- PCIst (external reference implementation) when perturbation data exist

### Dissipation / Noise
- instability (window-to-window drift)
- unexplained variance / artifact sensitivity

### Phenomenal Coherence Constraint
Cφ := D_KL(P || Q)
- P: distribution built from current observables
- Q: explicit dissolution distribution built from shuffles/surrogates (or equilibrated baseline where justified)
Cφ is descriptive: it constrains admissibility; it is not a predictive performance score.

## Decision Rules (pre-registered)
- Separation (AUC or equivalent): threshold ≥ 0.70 (or report the chosen equivalent)
- Shuffle degradation: ≥ 30% relative drop for structure/propagation
- Dose monotonicity (when dose/level exists): |Spearman ρ| ≥ 0.30
- Discordance (structure↑ while propagation↓ beyond tolerance): INDETERMINATE
- Controlled-access DOC data unavailable: INDETERMINATE

## Mandatory Falsification (negative controls)
1) Shuffles / surrogates must break structure/propagation (≥30% drop).
2) Ordinal break (dose permutation) must destroy monotonicity.
3) Inter-domain transfer must not yield spurious invariance without domain-appropriate observables.
Failure of any negative control triggers GLOBAL FAIL.

## Datasets
See MANIFEST.yaml for URLs, access modes, and licenses.

## Reproducibility Requirements
- fixed seeds
- environment lock (ENV.lock)
- artifact hashes for all outputs
- no post-hoc threshold tuning

## Limitations (declared)
- “Subjective experience” is not used as ground truth; conclusions are restricted to observable/causal signatures.
- Controlled-access DOC datasets may be unavailable; the program is designed to emit INDETERMINATE rather than extrapolate.

## Ethics (minimal)
This program uses public datasets. For controlled-access clinical data, all access conditions must be respected,
and no re-identification attempts are permitted.
