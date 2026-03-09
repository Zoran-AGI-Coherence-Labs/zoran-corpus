
# Protocole de benchmarks réels (SES-10 × Zoran)

Données : 4 sites (industrie, BTP, énergie, tertiaire), 2 semaines, 2kHz, fenêtres 2s (6 analyses/min).  
Métriques : interop_rate, compliance_coverage, artefacts_c2pa_rate, overhead_p95, fail_rate, audit_time.  
Procédure : `make reproduce_all`, `make ablate`, `python3 plot_metrics.py`.  
Sorties : metrics*.json, fig_*.png, C2PA/SBOM/VEX signés, report_bench.md.
