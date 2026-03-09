import numpy as np

def analyze_trend(series):
    slope = np.polyfit(range(len(series)), series, 1)[0]
    if slope > 0:
        return slope, "STABLE_OR_IMPROVING"
    elif abs(slope) < 1e-6:
        return slope, "CRITICAL"
    else:
        return slope, "DEGRADING"
