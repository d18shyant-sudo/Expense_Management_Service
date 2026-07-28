from pydantic import BaseModel
from uuid import UUID
from decimal import Decimal

class BudgetRequestCreate(BaseModel):
    claim_id: UUID
    requested_amount: Decimal
    remarks: str


class BudgetRequestUpdate(BaseModel):
    claim_id: UUID
    requested_amount: Decimal | None = None
    status: str | None = None
    remarks: str | None = None