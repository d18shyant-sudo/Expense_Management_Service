from pydantic import BaseModel,EmailStr
from uuid import UUID
from datetime import datetime
from typing import Optional



class LoginRequest(BaseModel):
    username: str
    password: str


class LoginResponse(BaseModel):
    token: str
    expires_at: datetime
    authentication_type: str = "Bearer"
    employee_id: UUID

class LoginRegister(BaseModel):
    username:str
    password:str
    email:EmailStr





from pydantic import BaseModel, EmailStr


class ForgotPasswordRequest(BaseModel):
    email: str
    

class VerifyOtpRequest(BaseModel):
    email: EmailStr
    otp: str


class ResetPasswordRequest(BaseModel):
    email: EmailStr
    otp: str
    new_password: str





class MessageResponse(BaseModel):
    message: str