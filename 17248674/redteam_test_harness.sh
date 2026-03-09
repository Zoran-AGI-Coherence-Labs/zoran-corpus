#!/usr/bin/env bash
# redteam_test_harness.sh
# Orchestrates canonicalization, hashing, merkle build, signing and simple tests.
set -euo pipefail
ROOT="$(pwd)"
PIPELINE="$ROOT/pipeline"
PROOFS="$PIPELINE/proofs"
ARTIFACTS="$PIPELINE/artefact_hashes.json"
MERKLE_PY="$PIPELINE/merkle_build.py"
SIGN_PY="$PIPELINE/sign_ed25519.py"

echo "[RT] Ensure directories"
mkdir -p "$PIPELINE"
mkdir -p "$PROOFS"
mkdir -p "$ROOT/redtests"

# 1) Canonicalization note: ensure files are UTF-8/LF externally before running.

# 2) Compute SHA-512 for listed files in artefact list (if placeholders exist, recalc)
if [ ! -f "$ARTIFACTS" ]; then
  echo "[RT] Creating skeleton $ARTIFACTS"
  cat > "$ARTIFACTS" <<'JSON'
[
  {"path":"whitepaper_sources/WhitePaper-Projet-ZORAN-aSiM.pdf","sha512":""},
  {"path":"pipeline/merkle_root.txt","sha512":""}
]
JSON
fi

# Recalculate sha512 for each entry and overwrite file
python3 - <<'PY'
import json, hashlib, sys
from pathlib import Path
ART=Path("pipeline/artefact_hashes.json")
j=json.load(open(ART))
out=[]
for e in j:
    p=Path(e["path"])
    if p.exists():
        h=hashlib.sha512(p.read_bytes()).hexdigest()
    else:
        h=e.get("sha512","")
    out.append({"path":e["path"],"sha512":h})
open(ART,"w").write(json.dumps(out,indent=2))
print("[RT] Updated artefact_hashes.json")
PY

# 3) Build merkle (produces merkle_root.txt and proofs)
python3 "$MERKLE_PY"

# 4) Update pipeline/audit_log_merkle.json merkle_root and sha512 placeholders
python3 - <<'PY'
import json
from pathlib import Path
p=Path('pipeline')
audit=p/'audit_log_merkle.json'
merkle=p/'merkle_root.txt'
art=p/'artefact_hashes.json'
if not merkle.exists():
    raise SystemExit("merkle_root.txt missing")
root=merkle.read_text().strip()
art_j=json.load(open(art))
# try to populate audit if exists; otherwise create minimal
if audit.exists():
    a=json.load(open(audit))
else:
    a={"bundle_id":"ZORAN-aSiM-2025-10-02","timestamp":"2025-10-02T00:00:00Z","merkle_root":root,"artefacts":[]}
a['merkle_root']=root
a['artefacts']=art_j
open(audit,'w').write(json.dumps(a,indent=2))
print("[RT] Wrote/updated pipeline/audit_log_merkle.json")
PY

# 5) Sign audit log (Ed25519 sandbox)
python3 "$SIGN_PY"

# 6) Run simple redtests
echo "[RT] Running immutability_test (modify temp copy -> expect mismatch)"
python3 - <<'PY'
import hashlib, json, shutil, tempfile, os
from pathlib import Path
p=Path('pipeline')
art=json.load(open(p/'artefact_hashes.json'))
if not art:
    print("No artefacts to test"); raise SystemExit(0)
first=art[0]['path']
tmp='__tmp_mutated'
if Path(first).exists():
    b=Path(first).read_bytes()
    # flip one byte (if empty, append)
    if len(b)==0:
        b=b+b'0'
    else:
        b=bytearray(b)
        b[0]= (b[0] + 1) % 256
        b=bytes(b)
    Path(tmp).write_bytes(b)
    h_new=hashlib.sha512(open(tmp,'rb').read()).hexdigest()
    h_old=art[0]['sha512']
    if h_new==h_old:
        print("immutability_test: FAIL (mutation NOT detected)")
        raise SystemExit(2)
    else:
        print("immutability_test: PASS (mutation detected)")
    Path(tmp).unlink()
else:
    print("immutability_test: SKIP (file not present)")
PY

echo "[RT] Signature check (verify ed25519 signature exists)"
if [ -f pipeline/audit_log.sig ] && [ -f pipeline/audit_log.pub ]; then
  echo "[RT] signature files present"
else
  echo "[RT] signature files missing"
  exit 1
fi

echo "[RT] RedTeam harness complete. Review pipeline/ and redtests/ for artifacts."
