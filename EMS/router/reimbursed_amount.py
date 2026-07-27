from fastapi import (
    APIRouter,
    Depends
)

from fastapi.responses import (
    JSONResponse
)

from sqlalchemy.orm import Session

from engine import get_db

from schema.reimbursement import (
    ReimbursementCreate,
    ReimbursementUpdate
)

from service.reimbursed_amount import (
    ReimbursementService
)

router = APIRouter(
    prefix="/api/v1",
    tags=["Reimbursement"]
)
@router.post("/reimbursements")
def create_reimbursement(
    payment: ReimbursementCreate,
    db: Session = Depends(get_db)
):
    try:

        result = (
            ReimbursementService
            .create_reimbursement(
                payment,
                db
            )
        )

        if result == "CLAIM_NOT_FOUND":
            return JSONResponse(
                status_code=404,
                content={
                    "error":
                    "Claim not found"
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
@router.put(
    "/reimbursements/{reimbursement_id}"
)
def update_reimbursement(
    reimbursement_id: str,
    payment: ReimbursementUpdate,
    db: Session = Depends(get_db)
):
    try:

        result = (
            ReimbursementService
            .update_reimbursement(
                reimbursement_id,
                payment,
                db
            )
        )

        if (
            result
            == "REIMBURSEMENT_NOT_FOUND"
        ):
            return JSONResponse(
                status_code=404,
                content={
                    "error":
                    "Reimbursement not found"
                }
            )

        if result == "CLAIM_NOT_FOUND":
            return JSONResponse(
                status_code=404,
                content={
                    "error":
                    "Claim not found"
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