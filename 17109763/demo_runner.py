"""Run all PoCs and dump metrics (demo)."""
import json, os, importlib

YEARS = ['2035','2075','2125','2325','3025']
POCS = [
 'poc_low_token',
 'poc_protocol_invention',
 'poc_resilience_rollback',
 'poc_self_patch_quorum',
 'poc_xenoparity_modules',
 'poc_edge_offline_first'
]

def run_all():
    base = os.path.dirname(__file__)
    metrics_dir = os.path.join(os.path.dirname(base), 'metrics')
    os.makedirs(metrics_dir, exist_ok=True)
    reports = []
    for year in YEARS:
        for poc in POCS:
            mod_path = f'src.pocs.{year}.{poc}'
            try:
                mod = importlib.import_module(mod_path)
                m = mod.run_poc()
                reports.append(m)
                out = os.path.join(metrics_dir, f'metrics_{year}_{poc}.json')
                with open(out, 'w', encoding='utf-8') as f:
                    json.dump(m, f, ensure_ascii=False, indent=2)
            except Exception as e:
                reports.append({'year':year,'poc':poc,'error':str(e)})
    agg = os.path.join(metrics_dir, 'reproducibility_log.json')
    with open(agg, 'w', encoding='utf-8') as f:
        json.dump(reports, f, ensure_ascii=False, indent=2)
    print(f"Wrote {len(reports)} reports.")

if __name__ == '__main__':
    import argparse
    p = argparse.ArgumentParser()
    p.add_argument('--all', action='store_true')
    args = p.parse_args()
    if args.all:
        run_all()
    else:
        run_all()
