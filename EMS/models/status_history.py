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

class Status_history(Base):
    __tablename__="status_history"
    id = Column(UUID(as_uuid=True),primary_key=True,default=uuid.uuid4)
    claim_id = Column(UUID,ForeignKey("expense_claims.id"))
    approver_id = Column(UUID,ForeignKey("employees.id"))
    requested_amount = Column(DECIMAL)
    approved_amount = Column(DECIMAL)
    remaining_amount = Column(DECIMAL)
    status = Column(String)
    remarks = Column(Text)
    action_time = Column(DateTime)
    created_at = Column(DateTime,default=datetime.utcnow)
    created_by = Column(UUID)
    updated_at = Column(DateTime)
    updated_by = Column(UUID)
    claim = relationship(
        "Expense_claim",
        back_populates="status_histories"
    )

    approver = relationship(
        "Employee",
        back_populates="approved_status_histories"
    )