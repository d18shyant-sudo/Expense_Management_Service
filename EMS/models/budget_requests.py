from sqlalchemy import (
    Column,
    String,
    UUID,
    ForeignKey,
    DateTime,
    Text,
    DECIMAL
)

from sqlalchemy.orm import relationship
import uuid
from datetime import datetime

from database import Base


class Budget_requests(Base):

    __tablename__ = "budget_requests"


    id = Column(
        UUID(as_uuid=True),
        primary_key=True,
        default=uuid.uuid4
    )


    # Expense claim which needs additional budget
    claim_id = Column(
        UUID(as_uuid=True),
        ForeignKey("expense_claims.id"),
        nullable=True
    )


    # Department requesting additional budget
    department_id = Column(
        UUID(as_uuid=True),
        ForeignKey("departments.id"),
        nullable=False
    )


    # Manager who raised the budget request
    requested_by = Column(
        UUID(as_uuid=True),
        ForeignKey("employees.id"),
        nullable=False
    )


    # Additional amount required
    requested_amount = Column(
        DECIMAL,
        nullable=False
    )


    status = Column(
        String,
        nullable=False,
        default="PENDING"
    )


    approved_by = Column(
        UUID(as_uuid=True),
        ForeignKey("employees.id"),
        nullable=True
    )


    approved_at = Column(
        DateTime,
        nullable=True
    )


    remarks = Column(
        Text,
        nullable=True
    )


    created_at = Column(
        DateTime,
        default=datetime.utcnow
    )


    created_by = Column(
        UUID(as_uuid=True),
        nullable=True
    )


    updated_at = Column(
        DateTime,
        nullable=True
    )


    updated_by = Column(
        UUID(as_uuid=True),
        nullable=True
    )


    # ---------------------------
    # Relationships
    # ---------------------------
    # Expense claim relationship
    claim = relationship(
        "Expense_claim",
        back_populates="budget_requests"
    )
    # Department relationship
    department = relationship(
        "Department",
        back_populates="budget_requests"
    )
    # Manager who created request
    requester = relationship(
        "Employee",
        foreign_keys=[requested_by],
        back_populates="budget_requests_created"
    )
    # Finance Admin who approved/rejected
    approver = relationship(
        "Employee",
        foreign_keys=[approved_by],
        back_populates="budget_requests_approved"
    )