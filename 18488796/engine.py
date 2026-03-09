#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
ZORAN — Coherence Demonstrability Engine (v2)
============================================

This version explicitly integrates the Deepseek review remarks:
- Multi-criteria (composite) metrics
- Relative (percentage-based) invariance tolerance
- Context weighting
- Confidence scoring
- Standardized export (JSON)
- Pedagogical-grade documentation

Author: Frédéric Tabary
License: MIT
"""

from __future__ import annotations

from dataclasses import dataclass, field, asdict
from typing import Any, Callable, Dict, List, Mapping, Sequence, Tuple
import json
import math


# ---------------------------------
# Type aliases
# ---------------------------------

Number = float
Data = Mapping[str, Any]


# ---------------------------------
# Data structures
# ---------------------------------

@dataclass(frozen=True)
class MetricResult:
    """
    Result of a metric computation.
    confidence: [0.0, 1.0] expressing robustness of the metric value.
    """
    value: Number
    confidence: Number
    valid: bool
    reason: str = ""
    details: Dict[str, Number] = field(default_factory=dict)


@dataclass(frozen=True)
class StressTestResult:
    context: str
    weight: Number
    baseline: MetricResult
    stressed: MetricResult
    delta: Number
    falsified: bool
    reason: str


@dataclass(frozen=True)
class EvaluationReport:
    metric_name: str
    threshold: Number
    relative_tolerance: Number
    results: List[StressTestResult]
    invariant: bool
    falsified: bool
    confidence: Number
    summary: str


# ---------------------------------
# Metric abstractions
# ---------------------------------

class Metric:
    """
    Single explicit metric.
    """
    def __init__(self, name: str, fn: Callable[[Data], Number]):
        if not name.strip():
            raise ValueError("Metric name must be non-empty.")
        self.name = name
        self.fn = fn

    def compute(self, data: Data) -> MetricResult:
        try:
            value = float(self.fn(data))
            if math.isnan(value) or math.isinf(value):
                return MetricResult(value=value, confidence=0.0, valid=False, reason="non_finite")
            return MetricResult(value=value, confidence=1.0, valid=True, reason="ok")
        except Exception as e:
            return MetricResult(
                value=float("nan"),
                confidence=0.0,
                valid=False,
                reason=f"exception:{type(e).__name__}"
            )


class CompositeMetric:
    """
    Weighted combination of multiple metrics.
    metrics: List of (Metric, weight)
    """
    def __init__(self, metrics: List[Tuple[Metric, Number]]):
        if not metrics:
            raise ValueError("CompositeMetric requires at least one metric.")
        self.metrics = metrics
        self.name = "CompositeMetric(" + ",".join(m.name for m, _ in metrics) + ")"

    def compute(self, data: Data) -> MetricResult:
        weighted_sum = 0.0
        total_weight = 0.0
        confidence_sum = 0.0
        details: Dict[str, Number] = {}

        for metric, weight in self.metrics:
            res = metric.compute(data)
            details[metric.name] = res.value
            if res.valid:
                weighted_sum += res.value * weight
                total_weight += weight
                confidence_sum += res.confidence * weight

        if total_weight == 0.0:
            return MetricResult(
                value=float("nan"),
                confidence=0.0,
                valid=False,
                reason="no_valid_metrics",
                details=details
            )

        return MetricResult(
            value=weighted_sum / total_weight,
            confidence=confidence_sum / total_weight,
            valid=True,
            reason="ok",
            details=details
        )


# ---------------------------------
# Stress test protocol
# ---------------------------------

def stress_test(
    metric,
    baseline_data: Data,
    stressed_data: Data,
    threshold: Number,
    context: str,
    weight: Number
) -> StressTestResult:
    base = metric.compute(baseline_data)
    st = metric.compute(stressed_data)

    if not base.valid or not st.valid:
        return StressTestResult(
            context=context,
            weight=weight,
            baseline=base,
            stressed=st,
            delta=float("nan"),
            falsified=True,
            reason="not_evaluable"
        )

    delta = st.value - base.value
    falsified = st.value < threshold

    return StressTestResult(
        context=context,
        weight=weight,
        baseline=base,
        stressed=st,
        delta=delta,
        falsified=falsified,
        reason="falsified" if falsified else "holds"
    )


# ---------------------------------
# Invariance evaluation (relative)
# ---------------------------------

def evaluate_relative_invariance(values: Sequence[Number], tolerance: Number) -> bool:
    """
    Relative invariance:
        (max - min) / max <= tolerance
    """
    if len(values) < 2:
        return True
    vmax = max(values)
    if vmax == 0:
        return False
    return (vmax - min(values)) / vmax <= tolerance


# ---------------------------------
# Full evaluation pipeline
# ---------------------------------

Dataset = Tuple[str, Data, Data, Number]  # (context, baseline, stressed, weight)

def evaluate_claim(
    metric,
    datasets: Sequence[Dataset],
    threshold: Number,
    relative_tolerance: Number
) -> EvaluationReport:

    results: List[StressTestResult] = []

    for context, base, stressed, weight in datasets:
        results.append(
            stress_test(
                metric=metric,
                baseline_data=base,
                stressed_data=stressed,
                threshold=threshold,
                context=context,
                weight=weight
            )
        )

    stressed_values = [r.stressed.value for r in results if r.stressed.valid]
    invariant = evaluate_relative_invariance(stressed_values, relative_tolerance)

    falsified = any(r.falsified for r in results)

    # Weighted confidence
    conf_sum = 0.0
    w_sum = 0.0
    for r in results:
        if r.stressed.valid:
            conf_sum += r.stressed.confidence * r.weight
            w_sum += r.weight
    confidence = conf_sum / w_sum if w_sum > 0 else 0.0

    if falsified:
        summary = "Claim falsified under explicit stress test conditions."
    elif not invariant:
        summary = "Claim holds locally but fails relative invariance across contexts."
    else:
        summary = "Claim holds under stress, invariance, and confidence criteria."

    return EvaluationReport(
        metric_name=metric.name,
        threshold=threshold,
        relative_tolerance=relative_tolerance,
        results=results,
        invariant=invariant,
        falsified=falsified,
        confidence=confidence,
        summary=summary
    )


# ---------------------------------
# Export
# ---------------------------------

def report_to_json(report: EvaluationReport) -> str:
    return json.dumps(asdict(report), ensure_ascii=False, indent=2)


# ---------------------------------
# Example (educational)
# ---------------------------------

def coherence_metric_ratio(data: Data) -> Number:
    signal = float(data.get("signal", 0.0))
    noise = float(data.get("noise", 1.0))
    if noise == 0.0:
        raise ValueError("noise cannot be zero")
    return signal / noise


def main() -> None:
    m1 = Metric("signal_noise_ratio", coherence_metric_ratio)
    metric = CompositeMetric([(m1, 1.0)])

    datasets: List[Dataset] = [
        ("Context A", {"signal": 10, "noise": 2}, {"signal": 8, "noise": 3}, 1.0),
        ("Context B", {"signal": 12, "noise": 3}, {"signal": 9, "noise": 4}, 1.0),
        ("Context C", {"signal": 9, "noise": 2}, {"signal": 7, "noise": 3}, 0.5),
    ]

    report = evaluate_claim(
        metric=metric,
        datasets=datasets,
        threshold=2.0,
        relative_tolerance=0.25
    )

    print(report.summary)
    print(report_to_json(report))


if __name__ == "__main__":
    main()
