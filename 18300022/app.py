from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Dict, List
import pandas as pd

from engine import ZoranEngine
import domains.macro as macro
import domains.health as health
import domains.ai as ai

DOMAIN_REGISTRY = {
    "macro": macro,
    "health": health,
    "ai": ai
}

class RunRequest(BaseModel):
    domain: str
    objective: str
    data: Dict[str, List[float]]

app = FastAPI(title="ZORAN Coherence Admissibility Engine", version="1.0")

@app.post("/run")
def run_engine(req: RunRequest):
    if req.domain not in DOMAIN_REGISTRY:
        raise HTTPException(status_code=400, detail="Unknown domain")
    df = pd.DataFrame(req.data)
    engine = ZoranEngine(DOMAIN_REGISTRY[req.domain])
    return engine.run(df, req.objective)
