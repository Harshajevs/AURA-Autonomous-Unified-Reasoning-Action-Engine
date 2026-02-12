from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.schemas.workflow import WorkflowCreate, WorkflowResponse
from app.services.workflow_service import create_workflow, get_workflow
from app.db.session import SessionLocal

router = APIRouter(prefix="/workflows", tags=["workflows"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/", response_model=WorkflowResponse)
def create(data: WorkflowCreate, db: Session = Depends(get_db)):
    return create_workflow(db, data.name, data.definition)

@router.get("/{workflow_id}", response_model=WorkflowResponse)
def get(workflow_id, db: Session = Depends(get_db)):
    workflow = get_workflow(db, workflow_id)
    if not workflow:
        raise HTTPException(status_code=404, detail="Workflow not found")
    return workflow
