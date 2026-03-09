# ZORAN Law Engine v1.0
# Scientific mode only. No narration.
# Invariants I0–I3, Laws L1–L5

import math, time

EPS = 1e-12

def normalize(p):
    s = sum(p)
    if s <= 0: raise ValueError("mass>0")
    return [max(EPS, x/s) for x in p]

def dkl(P, Q):
    Pn, Qn = normalize(P), normalize(Q)
    return sum(p * math.log(p/q) for p,q in zip(Pn,Qn))

# Invariants
def invariant_gate(state):
    return (
        state.get("continuity", False) and
        state.get("dissipation", 0) > 0 and
        state.get("trace", None) is not None and
        not state.get("singularity", False)
    )

# Laws
def L1_measurable_persistence(P, Q):
    Cphi = dkl(P, Q)
    return {"pass": Cphi > 0, "Cphi": Cphi}

def L2_coherence_selection(P_before, P_after, Q):
    return {
        "pass": dkl(P_after, Q) >= dkl(P_before, Q),
        "Cphi_before": dkl(P_before, Q),
        "Cphi_after": dkl(P_after, Q)
    }

def L3_time_arrow(dissipation_cost, delta_I):
    return {"pass": not (delta_I > 0 and dissipation_cost <= 0)}

def L4_forced_regularization(singularity, Pik_available):
    return {"pass": (not singularity) or Pik_available}

def L5_existence_trace(trace):
    return {"pass": trace is not None and len(str(trace)) > 0}

# Domains
def run_A(payload):
    return {"L4": L4_forced_regularization(payload["singularity"], payload.get("Pik_available", False))}

def run_B(payload):
    return {"L3": L3_time_arrow(payload["dissipation_cost"], payload["delta_I"])}

def run_C(payload):
    return {
        "L1": L1_measurable_persistence(payload["P"], payload["Q"]),
        "L2": L2_coherence_selection(payload["P_before"], payload["P_after"], payload["Q"])
    }

def run_D(payload):
    return {
        "L2": L2_coherence_selection(payload["P_before"], payload["P_after"], payload["Q"]),
        "L5": L5_existence_trace(payload["trace"])
    }

def run_all(domains):
    out = {"timestamp": time.time(), "results": {}}
    if "A" in domains: out["results"]["A"] = run_A(domains["A"])
    if "B" in domains: out["results"]["B"] = run_B(domains["B"])
    if "C" in domains: out["results"]["C"] = run_C(domains["C"])
    if "D" in domains: out["results"]["D"] = run_D(domains["D"])
    return out