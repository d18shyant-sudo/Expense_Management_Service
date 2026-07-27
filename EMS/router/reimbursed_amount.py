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
from auth import require_role
router = APIRouter(
    prefix="/api/v1",
    tags=["Reimbursement"]
)
@router.post("/reimbursements")
def create_reimbursement(
    payment: ReimbursementCreate,
    db: Session = Depends(get_db),user = Depends(require_role("Finance_admin"))
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
    "/reimbursements"
)
def update_reimbursement(
    reimbursement_id: str,
    payment: ReimbursementUpdate,
    db: Session = Depends(get_db),user = Depends(require_role("Finance_admin"))
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
@router.get("/reimbursements")
def get_reimbursed_amount(
    claim_id: str,
    db: Session = Depends(get_db),user = Depends(require_role("Finance_Head","Finance_admin"))
):
    try:

        result = (
            ReimbursementService.get_reimbursement(
                claim_id,
                db
            )
        )

        if result is None:

            return JSONResponse(
                status_code=404,
                content={
                    "error": "Reimbursement not found"
                }
            )

        return JSONResponse(
            status_code=200,
            content={
                "id": str(result.id),
                "claim_id": str(result.claim_id),
                "paid_amount": float(result.paid_amount),
                "payment_date": (
                    str(result.payment_date)
                    if result.payment_date
                    else None
                ),
                "payment_mode": result.payment_mode,
                "transaction_reference": result.transaction_reference
            }
        )

    except Exception as e:

        return JSONResponse(
            status_code=500,
            content={
                "error": str(e)
            }
        )