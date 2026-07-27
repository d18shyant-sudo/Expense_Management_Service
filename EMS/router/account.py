from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from fastapi.responses import JSONResponse

from engine import get_db

from service.account import (
    AccountService
)

from schema.account import (
    LoginRequest,
    LoginResponse
)

router = APIRouter(
    prefix="/api/v1",
    tags=["Authentication"]
)


@router.post(
    "/login",
    response_model=LoginResponse
)
def login(
    login_detail: LoginRequest,
    db: Session = Depends(get_db)
):
    try:

        result = (
            AccountService.login(
                login_detail.username,
                login_detail.password,
                db
            )
        )

        if not result:
            return JSONResponse(
                status_code=404,
                content={
                    "error":
                    "Invalid Credential"
                }
            )

        return JSONResponse(
            status_code=200,
            content=result
        )

    except Exception as e:

        return JSONResponse(
            status_code=500,
            content={
                "error": str(e)
            }
        )