from sqlalchemy.orm import Session
from app.models.workflow import Workflow

def create_workflow(db: Session, name: str, definition: dict):
    workflow = Workflow(
        name=name,
        version=1,
        definition=definition
    )
    db.add(workflow)
    db.commit()
    db.refresh(workflow)
    return workflow

def get_workflow(db: Session, workflow_id):
    return db.query(Workflow).filter(Workflow.id == workflow_id).first()
