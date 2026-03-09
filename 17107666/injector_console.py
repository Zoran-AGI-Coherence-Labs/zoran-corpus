#!/usr/bin/env python3
import argparse, json, sys, re

def load_profile(path):
    text = open(path, 'r', encoding='utf-8').read()
    if text.strip().startswith('{'): return json.loads(text)
    prof = {}
    current = prof
    for line in text.splitlines():
        if not line.strip() or line.strip().startswith('#'): continue
        if ':' in line:
            k, v = line.strip().split(':', 1)
            prof.setdefault('sliders', {}) if k.strip()=='sliders' else None
            if k.strip() in ('meta','sliders'):
                # section header, skip
                continue
            val = v.strip()
            if re.fullmatch(r'-?\d+', val): val = int(val)
            elif val.startswith('"') and val.endswith('"'): val = val[1:-1]
            prof.setdefault('sliders', {})[k.strip()] = val
    return prof

def map_params(sl):
    s = lambda k, d=50: int(sl.get(k, d))
    creativity = s('creativity',35)/100
    rag = s('rag_intensity',70)/100
    params = {
        "temperature": round(0.1 + 0.9*(creativity**1.7), 3),
        "top_p": round(0.6 + 0.4*creativity, 3),
        "top_k": int(3 + round(17*rag)),
        "rag_alpha": round(0.25 + 0.65*rag, 3),
        "abstain_threshold": round(0.3 + 0.7*(s('no_hallu',85)/100), 3),
        "ttl_days": int(round(365*((1 - s('privacy_ttl',80)/100)**2)))
    }
    return params

def main():
    ap = argparse.ArgumentParser(description='Console injecteur (curseurs → paramètres).')
    ap.add_argument('--profile', required=True)
    ap.add_argument('--dry-run', action='store_true')
    args = ap.parse_args()
    prof = load_profile(args.profile)
    sliders = prof.get('sliders', {})
    params = map_params(sliders)
    print('SLIDERS:', json.dumps(sliders, indent=2, ensure_ascii=False))
    print('PARAMS :', json.dumps(params, indent=2, ensure_ascii=False))
    if not args.dry_run:
        print('PROMPT (système) : Vous êtes l’assistant France Travail... (démo)')

if __name__ == '__main__':
    main()
