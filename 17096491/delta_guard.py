# delta_guard.py — Stability Guardian (ΔM11.3 demo)
def need_rollback(entropy: float, thr: float=0.22)->bool:
    return entropy > thr
