"""
ΔVARIANT_ENGINE Ω⁸ — Universal Equation Variant Generator
This script generates a set of mathematically equivalent variants of the canonical
Zoran🦋 law S = (β · ΔC) / λ > 1.  Each variant expresses the same relationship
between the variables S, β, ΔC and λ using algebraic rearrangement or
inequality transformations.  The goal of this engine is to demonstrate how
different symbolic forms can be derived from one underlying law for use in
analysis, documentation or educational materials.

Running this script will produce a JSON manifest file named
``ΔVARIANT_MANIFEST.json`` in the current working directory.  The manifest
contains a list of objects with an ``id`` and the corresponding variant
expression.  The variants included here are illustrative rather than
exhaustive; the engine can be extended to generate additional forms
	dynamically.
"""

import json


def generate_variants():
    """Return a list of algebraic variants of the base equation.

    This function enumerates a series of alternative expressions that
    represent the same relationship between the variables S, β, ΔC and λ.
    The base law is:

        S = (β * ΔC) / λ

    From this, we derive equivalent forms through multiplication,
    division, rearrangement and inequality manipulation.  The variants are
    useful for exploring how the components of the law interact.  Note that
    ΔC denotes ΔCₑ (variation of coherence) without the subscript for
    simplicity.

    Returns:
        list[str]: A list of variant expressions as human‑readable strings.
    """
    variants = []
    # Base canonical form
    variants.append("S = (β * ΔC) / λ")
    # Cross‑multiplication forms
    variants.append("S · λ = β · ΔC")
    variants.append("β · ΔC = S · λ")
    variants.append("S / β = ΔC / λ")
    variants.append("β / λ = S / ΔC")
    # Solving for each variable
    variants.append("β = (S · λ) / ΔC")
    variants.append("ΔC = (S · λ) / β")
    variants.append("λ = (β · ΔC) / S")
    # Zero‑difference forms
    variants.append("S − (β · ΔC) / λ = 0")
    variants.append("(β · ΔC) / λ − S = 0")
    variants.append("S · λ − β · ΔC = 0")
    variants.append("β · ΔC − S · λ = 0")
    # Inequality forms
    variants.append("S > 1")
    variants.append("(β · ΔC) / λ > 1")
    variants.append("β · ΔC > λ")
    variants.append("β · ΔC − λ > 0")
    variants.append("λ < β · ΔC")
    variants.append("ΔC > λ / β")
    variants.append("β > λ / ΔC")
    variants.append("β · ΔC / λ − 1 > 0")
    return variants


if __name__ == "__main__":
    variants = generate_variants()
    manifest = [
        {"id": idx + 1, "expression": expr}
        for idx, expr in enumerate(variants)
    ]
    # Write manifest JSON file using UTF‑8 without escaping Unicode
    with open("ΔVARIANT_MANIFEST.json", "w", encoding="utf-8") as f:
        json.dump(manifest, f, ensure_ascii=False, indent=2)
    print(f"Generated {len(manifest)} variants and saved to ΔVARIANT_MANIFEST.json")
