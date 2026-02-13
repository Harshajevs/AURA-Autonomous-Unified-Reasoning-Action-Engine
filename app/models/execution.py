import uuid
from sqlalchemy import Column, String, DateTime, ForeignKey
from sqlalchemy.dialects.postgresql import UUID, JSONB
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship

from app.db.base import Base


class Execution(Base):
    __tablename__ = "executions"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)

    workflow_id = Column(
        UUID(as_uuid=True),
        ForeignKey("workflows.id", ondelete="CASCADE"),
        nullable=False
    )

    status = Column(String, nullable=False)

    context = Column(JSONB, nullable=True)

    started_at = Column(DateTime(timezone=True), server_default=func.now())
    ended_at = Column(DateTime(timezone=True), nullable=True)

    # 🔗 Relationship to Workflow
    workflow = relationship("Workflow", back_populates="executions")

    # 🔗 Relationship to TaskInstances
    tasks = relationship(
        "TaskInstance",
        back_populates="execution",
        cascade="all, delete-orphan"
    )