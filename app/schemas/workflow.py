from pydantic import BaseModel
from typing import Dict, Any
from uuid import UUID
from datetime import datetime

class WorkflowCreate(BaseModel):
    name: str
    definition: Dict[str, Any]

class WorkflowResponse(BaseModel):
    id: UUID
    name: str
    version: int
    created_at: datetime

# What input is allowed

# What output looks like