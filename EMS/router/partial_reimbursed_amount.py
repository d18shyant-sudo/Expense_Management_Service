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