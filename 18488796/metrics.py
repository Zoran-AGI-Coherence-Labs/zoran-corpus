from typing import Mapping, Any

Number = float
Data = Mapping[str, Any]

def signal_noise_ratio(data: Data) -> Number:
    signal = float(data.get("signal", 0.0))
    noise = float(data.get("noise", 1.0))
    if noise == 0.0:
        raise ValueError("noise cannot be zero")
    return signal / noise

def clarity_metric(data: Data) -> Number:
    correct = float(data.get("correct_answers", 0))
    total = float(data.get("total_questions", 1))
    if total == 0:
        raise ValueError("total_questions cannot be zero")
    return correct / total
