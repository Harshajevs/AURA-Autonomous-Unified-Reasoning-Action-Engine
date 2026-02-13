from sqlalchemy.orm import Session
from sqlalchemy.sql import func

from app.models.execution import Execution
from app.services.task_service import (
    create_tasks_for_execution,
    update_task_status,
    TASK_RUNNING,
    TASK_COMPLETED
)

EXECUTION_CREATED = "CREATED"
EXECUTION_RUNNING = "RUNNING"
EXECUTION_COMPLETED = "COMPLETED"


def run_execution(db: Session, execution: Execution):
    """
    Core execution loop (sequential, synchronous).
    """

    # 🔒 0️⃣ Guard: do not re-run execution
    if execution.status != EXECUTION_CREATED:
        print(f"Execution {execution.id} already processed with status {execution.status}")
        return execution

    # 1️⃣ Mark execution as RUNNING
    execution.status = EXECUTION_RUNNING
    db.commit()

    print(f"Execution {execution.id} started")

    # 2️⃣ Extract task names from workflow definition
    workflow_def = execution.workflow.definition
    task_names = workflow_def.get("nodes", [])

    # 3️⃣ Create TaskInstances
    tasks = create_tasks_for_execution(
        db=db,
        execution_id=execution.id,
        task_names=task_names
    )

    # 4️⃣ Run tasks sequentially (stub logic)
    for task in tasks:
        print(f"Running task {task.task_name}")

        update_task_status(db, task, TASK_RUNNING)

        # Placeholder: actual work will come later
        update_task_status(
            db,
            task,
            TASK_COMPLETED,
            output={"result": f"{task.task_name} done"}
        )

        print(f"Completed task {task.task_name}")

    # 5️⃣ Mark execution as COMPLETED
    execution.status = EXECUTION_COMPLETED
    execution.ended_at = func.now()   
    db.commit()

    print(f"Execution {execution.id} completed")

    return execution