from pydantic import BaseModel
from uuid import UUID
from decimal import Decimal
class StatusHistoryCreate(BaseModel):
    claim_id: UUID
    approved_amount: Decimal
    status: str
    remarks: str


class StatusUpdate(BaseModel):
    status: str
    remarks: str
    approved_amount: Decimal