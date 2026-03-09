
"""
Baseline matcher: compares CVs to Jobs using simple Jaccard across skills+keywords
and includes diversity penalty reduction + bias guard (ΔM11.3 placeholder).
No external deps. Python 3.10+ stdlib only.
Usage:
  python main.py --cvs cv_100.jsonl --jobs job_100.jsonl --out results.json
"""
import json, argparse, math, unicodedata, re
from collections import defaultdict

def normalize(t):
    t = t.lower()
    t = ''.join(c for c in unicodedata.normalize('NFD', t) if unicodedata.category(c) != 'Mn')
    t = re.sub(r'[^a-z0-9\+\#\.\- ]+',' ', t)
    return ' '.join(t.split())

def token_set(cv, job):
    cv_tokens = set()
    for s in cv.get("skills", []): cv_tokens.update(normalize(s).split())
    for e in cv.get("experiences", []):
        cv_tokens.update(normalize(e.get("title","")).split())
        for a in e.get("achievements", []): cv_tokens.update(normalize(a).split())
    # Add education field
    edu = cv.get("education",{}).get("field","")
    cv_tokens.update(normalize(edu).split())

    job_tokens = set()
    for s in job.get("requirements", []): job_tokens.update(normalize(s).split())
    for k in job.get("keywords", []): job_tokens.update(normalize(k).split())
    for m in job.get("missions", []): job_tokens.update(normalize(m).split())
    job_tokens.update(normalize(job.get("title","")).split())

    return cv_tokens, job_tokens

def jaccard(a,b):
    if not a or not b: return 0.0
    inter = len(a & b)
    uni = len(a | b)
    return inter / uni if uni else 0.0

def salary_compat(cv, job):
    # Overlap ratio between expected and offered ranges
    c_lo, c_hi = cv.get("expected_salary_EUR",[0,0])
    j_lo, j_hi = job.get("salary_EUR",[0,0])
    inter = max(0, min(c_hi, j_hi) - max(c_lo, j_lo))
    den = max(1, (c_hi - c_lo) + (j_hi - j_lo))
    return inter / den

def location_bonus(cv, job):
    return 0.05 if normalize(cv.get("city","")) == normalize(job.get("location","")) else 0.0

def deltaM_guard(score):
    # Placeholder ΔM11.3 guard: clamp + slight penalty if score too spiky (heuristic)
    return max(0.0, min(1.0, score * 0.995))

def match_score(cv, job):
    cvt, jt = token_set(cv, job)
    s = 0.70 * jaccard(cvt, jt) + 0.20 * salary_compat(cv, job) + 0.05 * location_bonus(cv, job)
    # diversity/light bias guard (favor variety of sectors/seniority)
    if cv.get("seniority") == "Junior" and job.get("experience_min_years",0) <= 2:
        s += 0.03
    if cv.get("seniority") in ("Senior","Lead","Manager") and job.get("experience_min_years",0) >= 4:
        s += 0.02
    return deltaM_guard(s)

def run(cvs_path, jobs_path, out_path, topk=5):
    cvs = [json.loads(l) for l in open(cvs_path, encoding="utf-8")]
    jobs = [json.loads(l) for l in open(jobs_path, encoding="utf-8")]
    results = []
    for cv in cvs:
        scored = []
        for job in jobs:
            scored.append((match_score(cv, job), job["id"]))
        scored.sort(reverse=True)
        results.append({"cv_id": cv["id"], "top_matches": [{"job_id": jid, "score": round(sc,4)} for sc, jid in scored[:topk]]})
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(results, f, ensure_ascii=False, indent=2)

if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--cvs", default="cv_100.jsonl")
    ap.add_argument("--jobs", default="job_100.jsonl")
    ap.add_argument("--out", default="results.json")
    args = ap.parse_args()
    run(args.cvs, args.jobs, args.out)
