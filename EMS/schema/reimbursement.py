from pydantic import BaseModel
from uuid import UUID
from decimal import Decimal
from datetime import datetime

class ReimbursementCreate(BaseModel):
    claim_id: UUID
    paid_amount: Decimal
    payment_date: datetime
    payment_mode: str
    transaction_reference: str


class ReimbursementUpdate(BaseModel):
    claim_id: UUID
    paid_amount: Decimal | None = None
    payment_date: datetime | None = None
    payment_mode: str | None = None
    transaction_reference: str | None = None