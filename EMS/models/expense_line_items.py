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

class Expense_line_item(Base):
    __tablename__="expense_line_items"
    id = Column(UUID(as_uuid=True),default=uuid.uuid4,primary_key=True)
    claim_id = Column(UUID,ForeignKey("expense_claims.id"))
    category_id = Column(UUID,ForeignKey("categories.id"))
    amount = Column(DECIMAL)
    description = Column(Text)
    receipt_url = Column(String(500))
    created_at = Column(DateTime)
    created_by = Column(UUID(as_uuid=True))
    updated_at = Column(DateTime)
    updated_by = Column(UUID(as_uuid=True))
    claim = relationship(
        "Expense_claim",
        back_populates="line_items"
    )
    category = relationship(
        "Category",
        back_populates="line_items"
    )
