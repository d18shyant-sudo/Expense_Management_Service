from datetime import datetime
from decimal import Decimal
from pydantic import BaseModel


class StatusHistoryResponse(BaseModel):
    id: str
    claim_id: str
    approver_id: str
    approver_name: str
    requested_amount: Decimal
    approved_amount: Decimal
    remaining_amount: Decimal
    status: str
    remarks: str
    action_time: datetime

    class Config:
        from_attributes = True