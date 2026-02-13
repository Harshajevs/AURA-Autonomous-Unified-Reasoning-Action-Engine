from sqlalchemy.orm import Session
from app.models.task_instance import TaskInstance

TASK_PENDING = "PENDING"
TASK_RUNNING = "RUNNING"
TASK_COMPLETED = "COMPLETED"

def create_tasks_for_execution(
    db: Session,
    execution_id,
    task_names: list[str]
):
    """
    Create one TaskInstance per task name.
    """
    tasks = []

    for name in task_names:
        task = TaskInstance(
            execution_id=execution_id,
            task_name=name,
            status=TASK_PENDING
        )
        db.add(task)
        tasks.append(task)

    db.commit()

    return tasks


def update_task_status(
    db: Session,
    task: TaskInstance,
    new_status: str,
    output: dict | None = None
):
    task.status = new_status

    if output is not None:
        task.output = output

    db.commit()
    db.refresh(task)

    return task