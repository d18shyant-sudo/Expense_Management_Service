from schema.expense_claim import Claim_Create,Claim_Resubmit
from engine import get_db
from fastapi import APIRouter,Depends
from sqlalchemy.orm import Session
from fastapi.responses import JSONResponse
from service.expense_claim import ExpenseClaimService
from auth import require_role
router = APIRouter(prefix="/api/v1",tags=["Expense_Claim"])

@router.post("/expense-claims")
def create_claim(
    claim: Claim_Create,
    db: Session = Depends(get_db),user = Depends(require_role("Employee","Manager"))
):
    try:
        result = ExpenseClaimService.create_claim(
            claim,
            db
        )

        return JSONResponse(
            status_code=200,
            content={
                "message": "Claim created",
                "claim_id": str(result.id),
                "revision_count": result.revision_count
            }
        )

    except Exception as e:
        return JSONResponse(
            status_code=500,
            content={
                "error": str(e)
            }
        )
@router.put(
    "/expense-claims/resubmit"
)
def resubmit_claim(
    claim_id: str,
    claim: Claim_Resubmit,
    db: Session = Depends(get_db),user = Depends(require_role("Employee","Manager"))
):
    try:

        result = ExpenseClaimService.resubmit_claim(
            claim_id,
            claim,
            db
        )

        if not result:
            return JSONResponse(
                status_code=404,
                content={
                    "error": "Claim not found"
                }
            )

        return JSONResponse(
            status_code=200,
            content={
                "message":
                "Claim resubmitted successfully",
                "claim_id": str(result.id),
                "revision_count":
                result.revision_count
            }
        )

    except Exception as e:
        return JSONResponse(
            status_code=500,
            content={
                "error": str(e)
            }
        )
@router.put("/expense-claims/approve")
def approve_claim(
    claim_id: str,
    db: Session = Depends(get_db),
    user=Depends(require_role("Manager", "Finance_admin"))
):
    try:

        result = ExpenseClaimService.approve_claim(
            claim_id,
            user["employee_id"],
            db
        )

        if result is None:
             return JSONResponse(
                 status_code=404,
                 content={"error": "Claim not found"}
             )

        if isinstance(result, str):
             return JSONResponse(
                 status_code=400,
                 content={"error": result}
             )

        return JSONResponse(
            status_code=200,
            content={
                "message": "Claim approved successfully",
                "claim_id": str(result.id),
                "approved_at": str(result.approved_at)
            }
        )

    except Exception as e:
        return JSONResponse(
            status_code=500,
            content={"error": str(e)}
        )
@router.put("/expense-claims/reimburse")
def reimburse_claim(
    claim_id: str,
    db: Session = Depends(get_db),
    user=Depends(require_role("Finance_Head", "Finance_admin"))
):
    try:

        result = ExpenseClaimService.reimburse_claim(
            claim_id,
            user["employee_id"],
            db
        )

        if result is None:
           return JSONResponse(
               status_code=404,
               content={"error": "Claim not found"}
           )

        if isinstance(result, str):
           return JSONResponse(
               status_code=400,
               content={"error": result}
           )

        return JSONResponse(
            status_code=200,
            content={
                "message": "Claim reimbursed successfully",
                "claim_id": str(result.id),
                "reimbursed_at": str(result.reimbursed_at)
            }
        )

    except Exception as e:
        return JSONResponse(
            status_code=500,
            content={"error": str(e)}
        )
@router.get("/expense-claims")
def get_claims(
    employee_id: str,
    db: Session = Depends(get_db),user = Depends(require_role("Finance_Head","Finance_admin","Manager","Employee"))
):
    try:

        result = ExpenseClaimService.get_claims(
            employee_id,
            db
        )

        if result is None:
            return JSONResponse(
                status_code=404,
                content={
                    "error": "Employee not found"
                }
            )

        return JSONResponse(
            status_code=200,
            content=[
                {
                    "id": str(claim.id),
                    "employee_id": str(claim.employees_id),
                    "purpose": claim.purpose,
                    "requested_amount": float(claim.requested_amount),
                    "status": claim.status,
                    "revision_count": claim.revision_count,
                    "submitted_at": str(claim.submitted_at)
                }
                for claim in result
            ]
        )

    except Exception as e:

        return JSONResponse(
            status_code=500,
            content={
                "error": str(e)
            }
        )