#!/usr/bin/env python3
"""
Build a deterministic Merkle tree from pipeline/artefact_hashes.json.
Outputs:
 - pipeline/merkle_root.txt
 - pipeline/merkle_tree.json  (levels by index)
 - pipeline/proofs/<relpath>.proof.json  (proof for each leaf)
Usage: python pipeline/merkle_build.py
"""
import json, hashlib, os
from pathlib import Path

ROOT = Path('.')
PIPELINE = ROOT / 'pipeline'
ARTIFACTS = PIPELINE / 'artefact_hashes.json'
MERKLE_ROOT_OUT = PIPELINE / 'merkle_root.txt'
MERKLE_TREE_OUT = PIPELINE / 'merkle_tree.json'
PROOFS_DIR = PIPELINE / 'proofs'
PROOFS_DIR.mkdir(parents=True, exist_ok=True)

def read_artifacts():
    if not ARTIFACTS.exists():
        raise SystemExit(f"{ARTIFACTS} not found. Run hash step first.")
    return json.load(open(ARTIFACTS,'r'))

def normalize_leaf(hexstr):
    # ensure lower-case 128-hex chars (sha512)
    return hexstr.lower()

def pair_hash(a_hex,b_hex):
    a = bytes.fromhex(a_hex)
    b = bytes.fromhex(b_hex)
    return hashlib.sha512(a+b).hexdigest()

def build_tree(sorted_leaves):
    levels = []
    level = sorted_leaves[:]
    levels.append(level)
    while len(level) > 1:
        # duplicate last if odd
        if len(level) % 2 == 1:
            level.append(level[-1])
        next_level = []
        for i in range(0,len(level),2):
            h = pair_hash(level[i], level[i+1])
            next_level.append(h)
        level = next_level
        levels.append(level)
    return levels

def build_proof_for_index(levels, idx):
    proof = []
    depth = len(levels)
    index = idx
    for d in range(depth-0-1):  # for each level until root
        level = levels[d]
        if index % 2 == 0:
            sibling_index = index + 1 if index+1 < len(level) else index
            sibling = level[sibling_index]
            orientation = "right"
        else:
            sibling_index = index - 1
            sibling = level[sibling_index]
            orientation = "left"
        proof.append({"sibling": sibling, "orientation": orientation})
        index = index // 2
    return proof

def main():
    artifacts = read_artifacts()
    # gather leaf hashes and associated paths
    entries = []
    for a in artifacts:
        entries.append({"path": a["path"], "sha512": normalize_leaf(a["sha512"])})
    # sort deterministically by path (primary) then hash
    entries_sorted = sorted(entries, key=lambda e: (e["path"]))
    leaf_hashes = [e["sha512"] for e in entries_sorted]
    if not leaf_hashes:
        raise SystemExit("No leaves found in artefact_hashes.json")
    # build tree
    levels = build_tree(leaf_hashes)
    root = levels[-1][0]
    # write outputs
    PIPELINE.mkdir(parents=True, exist_ok=True)
    MERKLE_ROOT_OUT.write_text(root + "\\n")
    json.dump({"levels": levels, "entries": entries_sorted}, open(MERKLE_TREE_OUT,'w'), indent=2)
    # proofs per entry (using index in entries_sorted)
    for i, ent in enumerate(entries_sorted):
        proof = build_proof_for_index(levels, i)
        out = {
            "path": ent["path"],
            "leaf": ent["sha512"],
            "index": i,
            "proof": proof,
            "root": root
        }
        # safe filename
        safe = ent["path"].replace('/', '__').replace('..','')
        (PROOFS_DIR / f"{safe}.proof.json").write_text(json.dumps(out, indent=2))
    print("Merkle root:", root)
    print("Wrote:", MERKLE_ROOT_OUT, MERKLE_TREE_OUT, "proofs/*")

if __name__ == "__main__":
    main()
