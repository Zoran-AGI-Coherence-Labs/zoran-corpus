# ΔTRACE_ENGINE.py
import hashlib, time, json
from pathlib import Path

def log_trace(event:str, data:dict, file="proof/tracecontinuum.log"):
    timestamp = time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())
    line = f"{timestamp} | {event} | {json.dumps(data, ensure_ascii=False)}"
    Path(file).parent.mkdir(exist_ok=True, parents=True)
    with open(file, "a", encoding="utf-8") as f:
        f.write(line + "\n")
    return hashlib.sha512(line.encode("utf-8")).hexdigest()[:32]
