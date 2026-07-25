from sqlalchemy import (
    Column,
    String,
    UUID,
    DateTime
)

from sqlalchemy.orm import relationship

import uuid
from datetime import datetime

from database import Base


class Role(Base):

    __tablename__ = "roles"

    id = Column(
        UUID(as_uuid=True),
        primary_key=True,
        default=uuid.uuid4
    )

    role_name = Column(String)

    created_at = Column(
        DateTime,
        default=datetime.utcnow
    )

    created_by = Column(String)

    updated_at = Column(DateTime)

    updated_by = Column(String)


    employees = relationship(
        "Employee",
        back_populates="role"
    )