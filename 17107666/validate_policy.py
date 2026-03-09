#!/usr/bin/env python3
import sys, json, re

def load_policy(path):
    text = open(path, 'r', encoding='utf-8').read()
    # Minimal YAML/JSON loader: accept JSON; for YAML, parse simple key: value pairs
    if text.strip().startswith('{'):
        return json.loads(text)
    data = {}
    current = data
    stack = [(-1, data)]
    for line in text.splitlines():
        if not line.strip() or line.strip().startswith('#'):
            continue
        indent = len(line) - len(line.lstrip(' '))
        key, _, val = line.strip().partition(':')
        val = val.strip()
        # simple scalars only (for audit linting); complex YAML should use JSON path instead
        parsed = val
        if val in ('true','false'): parsed = val=='true'
        elif re.fullmatch(r'-?\d+(\.\d+)?', val):
            parsed = float(val) if '.' in val else int(val)
        elif val.startswith('[') and val.endswith(']'):
            parsed = [v.strip().strip('"\'') for v in val[1:-1].split(',') if v.strip()]
        while stack and indent <= stack[-1][0]:
            stack.pop()
        parent = stack[-1][1]
        if isinstance(parent, dict):
            parent[key] = parsed
            holder = key
        else:
            holder = None
        stack.append((indent, parent if holder is None else parent))
    return data

def check_slo(pol):
    # Navigate permissively
    get = lambda *ks: (lambda d=pol: [d:=d.get(k, {}) for k in ks][-1])()
    warnings = []
    fairness = pol.get('fairness') or get('fairness')
    if fairness:
        slo = fairness.get('slo', {})
        if slo.get('SPD_abs_max', 0.1) > 0.1:
            warnings.append('SPD_abs_max too high (should be ≤ 0.1)')
        for k, v in [('DeltaTPR_max_pts',5),('DeltaFPR_max_pts',5)]:
            if slo.get(k, 5) > 5: warnings.append(f'{k} too high (should be ≤ 5)')
        if slo.get('ECE_max_pct', 2) > 2:
            warnings.append('ECE_max_pct too high (should be ≤ 2)')
    return warnings

def main():
    if len(sys.argv) < 2:
        print('Usage: validate_policy.py <policy.(yaml|json)>')
        sys.exit(1)
    pol = load_policy(sys.argv[1])
    warnings = check_slo(pol)
    print('Policy loaded. Checks:', 'OK' if not warnings else 'WARN')
    for w in warnings:
        print(' -', w)

if __name__ == '__main__':
    main()
