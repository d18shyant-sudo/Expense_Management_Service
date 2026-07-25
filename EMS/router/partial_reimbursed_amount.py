from fastapi import (
    APIRouter,
    Depends
)

from fastapi.responses import (
    JSONResponse
)

from sqlalchemy.orm import Session

from engine import get_db

from schema.partial_reimbursement import (
    PartialReimbursementCreate,
    PartialReimbursementUpdate
)

from service.partial_reimbursed_amount import (
    PartialReimbursementService
)
from auth import require_role
router = APIRouter(
    prefix="/api/v1",
    tags=["Partial_Reimbursement"]
)
@router.post(
    "/partial-reimbursements"
)
def create_partial_reimbursement(
    payment: PartialReimbursementCreate,
    db: Session = Depends(get_db)
):
    try:

        result = (
            PartialReimbursementService
            .create_partial_reimbursement(
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

        if result == "EMPLOYEE_NOT_FOUND":
            return JSONResponse(
                status_code=404,
                content={
                    "error":
                    "Employee not found"
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
    "/partial-reimbursements/{partial_id}"
)
def update_partial_reimbursement(
    partial_id: str,
    payment: PartialReimbursementUpdate,
    db: Session = Depends(get_db)
):
    try:

        result = (
            PartialReimbursementService
            .update_partial_reimbursement(
                partial_id,
                payment,
                db
            )
        )

        if (
            result
            ==
            "PARTIAL_REIMBURSEMENT_NOT_FOUND"
        ):
            return JSONResponse(
                status_code=404,
                content={
                    "error":
                    "Partial reimbursement not found"
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
@router.get("/partial-reimbursement/{claim_id}")
def get_partial_reimbursement(
    claim_id: str,
    db: Session = Depends(get_db)
):
    try:

        result = (
            PartialReimbursementService
            .get_partial_reimbursement(
                claim_id,
                db
            )
        )

        if result is None:

            return JSONResponse(
                status_code=404,
                content={
                    "error": "Partial reimbursement not found"
                }
            )

        return JSONResponse(
            status_code=200,
            content={
                "id": str(result.id),
                "claim_id": str(result.claim_id),
                "paid_amount": float(result.approved_amount),
                "payment_date": (
                    str(result.responded_at)
                    if result.responded_at
                    else None
                )

            }
        )

    except Exception as e:

        return JSONResponse(
            status_code=500,
            content={
                "error": str(e)
            }
        )