# prisma_flow.py — outputs a simple Mermaid diagram for PRISMA
print("""flowchart TD
  A[Identification] --> B[Screening]
  B --> C[Eligibility]
  C --> D[Inclusion]
""")