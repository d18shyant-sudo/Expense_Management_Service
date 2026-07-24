from sqlalchemy import (
    Column,
    String,
    UUID,
    ForeignKey,
    DateTime,
    Text,
    DECIMAL,
    Integer
)

from sqlalchemy.orm import relationship

import uuid
from datetime import datetime

from database import Base

class Expense_claim(Base):
    __tablename__="expense_claims"
    id = Column(UUID(as_uuid=True),primary_key=True,default=uuid.uuid4)
    employees_id = Column(UUID,ForeignKey("employees.id"))
    purpose = Column(Text)
    requested_amount = Column(DECIMAL)
    status = Column(String)
    revision_count = Column(Integer)
    submitted_at = Column(DateTime)
    last_resubmitted_at = Column(DateTime)
    approved_at = Column(DateTime)
    reimbursed_at = Column(DateTime)
    created_at = Column(DateTime)
    created_by = Column(UUID(as_uuid=True))
    updated_at = Column(DateTime)
    updated_by = Column(UUID(as_uuid=True))
    employee = relationship(
    "Employee",
    back_populates="expense_claims"
    )
    line_items = relationship(
        "Expense_line_item",
        back_populates="claim"
    )
    status_histories = relationship(
    "Status_history",
    back_populates="claim"
    )
    reimbursement = relationship(
    "Reimbursed_amount",
    back_populates="claim",
    uselist=False
    )
    partial_reimbursement = relationship(
    "Partial_reimbursed_amount",
    back_populates="claim",
    uselist=False
    )
    budget_requests = relationship(
    "Budget_requests",
    back_populates="claim"
    )