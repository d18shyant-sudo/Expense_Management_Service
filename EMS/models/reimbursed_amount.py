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

class Reimbursed_amount(Base):
    __tablename__="reimbursed_amount"
    id = Column(UUID(as_uuid=True),primary_key=True,default=uuid.uuid4)
    claim_id = Column(UUID,ForeignKey("expense_claims.id"))
    paid_amount = Column(DECIMAL)
    payment_date = Column(DateTime)
    payment_mode = Column(String)
    transaction_reference = Column(String(500))
    created_at = Column(DateTime,default=datetime.utcnow)
    created_by = Column(UUID)
    updated_at = Column(DateTime)
    updated_by = Column(UUID)
    claim = relationship(
    "Expense_claim",
    back_populates="reimbursement"
    )