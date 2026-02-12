import uuid
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.dialects.postgresql import UUID, JSONB

from app.db.base import Base

class TaskInstance(Base):
    __tablename__ = "task_instances"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    execution_id = Column(UUID(as_uuid=True), ForeignKey("executions.id"), nullable=False)
    task_name = Column(String, nullable=False)
    status = Column(String, nullable=False)
    output = Column(JSONB, nullable=True)
