from pydantic import BaseModel
from uuid import UUID
from datetime import datetime


class LoginRequest(BaseModel):
    username: str
    password: str


class LoginResponse(BaseModel):
    token: str
    expires_at: datetime
    authentication_type: str = "Bearer"
    employee_id: UUID