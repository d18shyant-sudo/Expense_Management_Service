from sqlalchemy import (
    Column,
    String,
    ForeignKey,
    UUID,
    DateTime
)

from sqlalchemy.orm import relationship

import uuid
from datetime import datetime

from database import Base


class Department(Base):

    __tablename__ = "departments"

    id = Column(
        UUID(as_uuid=True),
        primary_key=True,
        default=uuid.uuid4
    )

    name = Column(
        String,
        nullable=False
    )

    manager_id = Column(
        UUID(as_uuid=True),
        ForeignKey("employees.id")
    )

    finance_admin_id = Column(
        UUID(as_uuid=True),
        ForeignKey("employees.id")
    )

    created_at = Column(
        DateTime,
        default=datetime.utcnow
    )

    created_by = Column(
        UUID(as_uuid=True)
    )

    updated_at = Column(
        DateTime
    )

    updated_by = Column(
        UUID(as_uuid=True)
    )

    # employees belonging to this department
    employees = relationship(
        "Employee",
        back_populates="department",
        foreign_keys="Employee.department_id"
    )

    # department manager
    manager = relationship(
        "Employee",
        foreign_keys=[manager_id]
    )

    # department finance admin
    finance_admin = relationship(
        "Employee",
        foreign_keys=[finance_admin_id]
    )
    budget_requests = relationship(
    "Budget_requests",
    back_populates="department"
    )