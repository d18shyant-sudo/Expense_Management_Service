from sqlalchemy import (
    Column,
    String,
    UUID,
    ForeignKey,
    DateTime,
    Boolean
)

from sqlalchemy.orm import relationship

import uuid
from datetime import datetime

from database import Base


class Employee(Base):

    __tablename__ = "employees"

    id = Column(
        UUID(as_uuid=True),
        primary_key=True,
        default=uuid.uuid4
    )

    name = Column(String)

    email = Column(String)

    role_id = Column(
        UUID(as_uuid=True),
        ForeignKey("roles.id")
    )

    department_id = Column(
        UUID(as_uuid=True),
        ForeignKey("departments.id")
    )

    is_active = Column(Boolean)

    created_at = Column(
        DateTime,
        default=datetime.utcnow
    )

    created_by = Column(
        UUID(as_uuid=True)
    )

    updated_at = Column(DateTime)

    updated_by = Column(
        UUID(as_uuid=True)
    )

    role = relationship(
        "Role",
        back_populates="employees"
    )

    department = relationship(
        "Department",
        back_populates="employees",
        foreign_keys=[department_id]
    )
    expense_claims = relationship(
    "Expense_claim",
    back_populates="employee"
    )


    approved_status_histories = relationship(
    "Status_history",
    back_populates="approver"
    )
    budget_requests_created = relationship(
    "Budget_requests",
    foreign_keys="Budget_requests.requested_by",
    back_populates="requester"
    )
    budget_requests_approved = relationship(
    "Budget_requests",
    foreign_keys="Budget_requests.approved_by",
    back_populates="approver"
    )
