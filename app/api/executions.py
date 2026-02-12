from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.schemas.execution import ExecutionCreate, ExecutionResponse
from app.services.execution_service import create_execution, get_execution
from app.db.session import SessionLocal

router = APIRouter(prefix="/executions", tags=["executions"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/", response_model=ExecutionResponse)
def create(data: ExecutionCreate, db: Session = Depends(get_db)):
    return create_execution(db, data.workflow_id, data.input)

@router.get("/{3fa85f64-5717-4562-b3fc-2c963f66afa6}", response_model=ExecutionResponse)
def get(execution_id, db: Session = Depends(get_db)):
    execution = get_execution(db, execution_id)
    if not execution:
        raise HTTPException(status_code=404, detail="Execution not found")
    return execution
