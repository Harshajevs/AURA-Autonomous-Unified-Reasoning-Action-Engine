from pydantic import BaseModel
from typing import Dict, Any
from uuid import UUID
from datetime import datetime

class ExecutionCreate(BaseModel):
    workflow_id: UUID
    input: Dict[str, Any]

class ExecutionResponse(BaseModel):
    id: UUID
    status: str
    started_at: datetime
