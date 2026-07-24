from pydantic import BaseModel
from uuid import UUID

class Claim_Create(BaseModel):
    employee_id: UUID
    purpose: str
    requested_amount: float


class Claim_Resubmit(BaseModel):
    purpose: str
    requested_amount: float