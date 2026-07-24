from sqlalchemy import (
    Column,
    UUID,
    String,
    DateTime
)
from sqlalchemy.orm import relationship

from datetime import datetime
import uuid

from database import Base


class Category(Base):

    __tablename__ = "categories"

    id = Column(
        UUID(as_uuid=True),
        primary_key=True,
        default=uuid.uuid4
    )

    name = Column(
        String,
        nullable=False
    )

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
    line_items = relationship(
        "Expense_line_item",
        back_populates="category"
    )