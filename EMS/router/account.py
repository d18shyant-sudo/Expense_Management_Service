from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from fastapi.responses import JSONResponse

from engine import get_db

from schema.account import (
    LoginRequest,
    LoginResponse,
    ForgotPasswordRequest,
    VerifyOtpRequest,
    ResetPasswordRequest
)

from service.account import AccountService


router = APIRouter(
    prefix="/api/v1",
    tags=["Authentication"]
)


@router.post(
    "/login",
    response_model=LoginResponse
)
def login(
    payload: LoginRequest,
    db: Session = Depends(get_db)
):

    result = AccountService.login(
        payload.username,
        payload.password,
        db
    )

    if not result:
        return JSONResponse(
            status_code=404,
            content={
                "error": "Invalid Credential"
            }
        )

    return JSONResponse(
        status_code=200,
        content=result
    )


@router.post("/forgot-password")
def forgot_password(
    payload: ForgotPasswordRequest,
    db: Session = Depends(get_db)
):
    return AccountService.forgot_password(
        payload,
        db
    )

@router.post("/verify-otp")
def verify_otp(
    payload: VerifyOtpRequest,
    db: Session = Depends(get_db)
):
    return AccountService.verify_otp(payload)

@router.post("/reset-password")
def reset_password(
    payload: ResetPasswordRequest,
    db: Session = Depends(get_db)
):
    return AccountService.reset_password(payload, db)
