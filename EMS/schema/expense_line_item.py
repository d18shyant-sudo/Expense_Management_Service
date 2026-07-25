from pydantic import BaseModel
from uuid import UUID

class ExpenseLineItemCreate(BaseModel):
    claim_id: UUID
    category_name: str
    amount: float
    description: str
    receipt_url: str


class ExpenseLineItemUpdate(BaseModel):
    category_name: str
    amount: float
    description: str
    receipt_url: str