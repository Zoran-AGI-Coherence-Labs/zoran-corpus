# ΔM11.3 guard (simplified)
import statistics as stats

def entropy(score_series):
    # normalized entropy proxy: std / (1 + mean)
    if not score_series:
        return 0.0
    m = sum(score_series)/len(score_series)
    s = stats.pstdev(score_series) if len(score_series) > 1 else 0.0
    return s / (1.0 + abs(m))

def should_rollback(score_series, threshold=0.15):
    return entropy(score_series) > threshold

def rollback_state(history):
    # keep previous stable snapshot (last low-entropy window)
    if not history:
        return {}
    return history[-1]
