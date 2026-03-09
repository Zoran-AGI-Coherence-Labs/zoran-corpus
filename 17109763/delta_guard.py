"""ΔM11.3 guard — entropy-based rollback (demo)."""
def should_rollback(entropy: float, threshold: float=0.5) -> bool:
    return entropy > threshold
