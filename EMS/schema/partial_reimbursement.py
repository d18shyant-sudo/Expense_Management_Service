from pydantic import BaseModel
from uuid import UUID
from decimal import Decimal

class PartialReimbursementCreate(BaseModel):
    claim_id: UUID
    approved_amount: Decimal
    status: str
    reason: str


class PartialReimbursementUpdate(BaseModel):
    claim_id: UUID
    approved_amount: Decimal | None = None
    status: str | None = None
    reason: str | None = None