from sqlalchemy.orm import Session
from app.models.execution import Execution

def create_execution(db: Session, workflow_id, context):
    execution = Execution(
        workflow_id=workflow_id,
        status="CREATED",
        context=context
    )
    db.add(execution)
    db.commit()
    db.refresh(execution)
    return execution

def get_execution(db: Session, execution_id):
    return db.query(Execution).filter(Execution.id == execution_id).first()
