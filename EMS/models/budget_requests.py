from sqlalchemy import (
    Column,
    String,
    UUID,
    ForeignKey,
    DateTime,
    Boolean,
    Text,
    DECIMAL,
    Integer
)

from sqlalchemy.orm import relationship

import uuid
from datetime import datetime

from database import Base

class Budget_requests(Base):
    __tablename__="budget_requests"
    id = Column(UUID(as_uuid=True),primary_key=True,default=uuid.uuid4)
    claim_id = Column(UUID(as_uuid=True),ForeignKey("expense_claims.id"))
    department_id = Column(UUID(as_uuid=True),ForeignKey("departments.id"))
    requested_by = Column(UUID(as_uuid=True),ForeignKey("employees.id"))
    requested_amount = Column(DECIMAL)
    status = Column(String)
    approved_by = Column(UUID(as_uuid=True),ForeignKey("employees.id"))
    approved_at = Column(DateTime)
    remarks = Column(Text)
    created_at = Column(DateTime,default=datetime.utcnow)
    created_by = Column(UUID(as_uuid=True))
    updated_at = Column(DateTime)
    updated_by = Column(UUID(as_uuid=True))
    claim = relationship(
        "Expense_claim",
        back_populates="budget_requests"
    )

    department = relationship(
        "Department",
        back_populates="budget_requests"
    )

    requester = relationship(
    "Employee",
    foreign_keys=[requested_by],
    back_populates="budget_requests_created"
    )

    approver = relationship(
    "Employee",
    foreign_keys=[approved_by],
    back_populates="budget_requests_approved"
    )