# logging_utils.py — JSONL logging (demo)
import json
def write_jsonl(path, recs):
    with open(path, "a", encoding="utf-8") as f:
        for r in recs:
            f.write(json.dumps(r, ensure_ascii=False) + "\n")
