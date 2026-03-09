
# Z-Forge 1000 — White Paper V3 (Flat ZIP)
**SES-10 Edge Sensor × Zoran aSiM — From isolated device to universal mimetic module**  
Date: 2025-09-11 — Standard **Z-Forge Frédéric Tabary**  
Contact: tabary01@gmail.com

## Official links
- Gamma — Zoran aSiM: https://zoran-2040-asim-swxr6lh.gamma.site/
- GitHub — Zoran aSiM README: https://github.com/Zoran-IA-Mimetique/Zoran-2040-aSiM-Towards-a-Public-Ethical-and-Resilient-Super-Intelligence/blob/main/README.md

## Content (flat layout)
- `main_paper_IMRaD.md` – full white paper text (IMRaD)
- PRISMA, Glossary, Costs, KPIs/ETAs, TCO/ROI model, Bench protocol
- Makefile, Docker compose, policy, scripts (PRISMA, ROI, plots)
- Diagrams (ASCII + Mermaid), BibTeX references, placeholders for provenance/SBOM

## Quick run
```bash
# Reproduce demo runs and aggregate metrics (stdlib-only)
make reproduce_all

# Generate PRISMA demo outputs
make prisma

# Produce simple charts (saved as PNGs at root)
python3 plot_metrics.py

# Compute ROI/TCO from CSV assumptions
python3 roi_calc.py

# Generate SBOM (requires cyclonedx-bom installed) & C2PA manifests (stub)
make sbom c2pa
```
