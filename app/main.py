from fastapi import FastAPI
from app.api import workflows, executions

app = FastAPI(title="AURA Core API")

app.include_router(workflows.router)
app.include_router(executions.router)

@app.get("/health")
def health():
    return {"status": "ok"}
