# REPORT — Results (template)

Date: 2026-01-24
Pivot DOI: 10.5281/zenodo.18360840

## Domain Verdicts
| Domain | Dataset | Verdict | Notes |
|---|---|---|---|
| Sleep | Sleep-EDF |  | |
| Anesthesia EEG | Cambridge propofol EEG |  | |
| Anesthesia fMRI | OpenNeuro ds006623 |  | |
| Perturbation | PCIst / TMS-EEG |  | |
| DOC | EBRAINS TMS-EEG |  | |

## Negative Controls
| Test | Expected | Observed | PASS/FAIL |
|---|---|---|---|
| Shuffles/surrogates | ≥30% degradation |  |  |
| Ordinal break (dose) | monotonicity destroyed |  |  |
| Transfer failure | no spurious invariance |  |  |

## Global Verdict
GLOBAL: 
Rule: any failed negative control → GLOBAL FAIL.
INDETERMINATE must be preserved (never collapsed).
