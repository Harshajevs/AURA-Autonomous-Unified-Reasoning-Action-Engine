from app.db.session import SessionLocal
from app.models.workflow import Workflow

db = SessionLocal()

workflow = Workflow(
    name="Refund Workflow",
    version=1,
    definition={
        "nodes": ["check_amount", "fraud_check"],
        "edges": []
    }
)

db.add(workflow)
db.commit()

print("Inserted workflow:", workflow.id)

wf = db.query(Workflow).first()
print(wf.name, wf.definition)
