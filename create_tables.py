from app.db.session import engine
from app.db.base import Base

from app.models.workflow import Workflow
from app.models.execution import Execution
from app.models.task_instance import TaskInstance

Base.metadata.create_all(bind=engine)
