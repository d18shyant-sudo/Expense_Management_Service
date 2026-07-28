from fastapi import (
    APIRouter,
    Depends
)

from fastapi.responses import (
    JSONResponse
)

from sqlalchemy.orm import Session

from engine import get_db

from service.budget_requests import (
    BudgetRequestService
)

from schema.budget_requests import (
    BudgetRequestCreate,
    BudgetRequestUpdate
)

router = APIRouter(
    prefix="/api/v1",
    tags=["Budget_Request"]
)
from auth import require_role
@router.post("/budget-requests")
def create_budget_request(
    request: BudgetRequestCreate,
    db: Session = Depends(get_db),user = Depends(require_role("Manager"))
):
    try:

        result = (
            BudgetRequestService
            .create_budget_request(
                request,
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
    "/budget-requests"
)
def update_budget_request(
    budget_request_id: str,
    request: BudgetRequestUpdate,
    db: Session = Depends(get_db),user = Depends(require_role("Manager","Finance_admin","Finance_Head"))
):
    try:

        result = (
            BudgetRequestService
            .update_budget_request(user,
                budget_request_id,
                request,
                db
            )
        )

        if result == (
            "BUDGET_REQUEST_NOT_FOUND"
        ):
            return JSONResponse(
                status_code=404,
                content={
                    "error":
                    "Budget request not found"
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
@router.get("/budget-requests")
def get_budget_requests(
    claim_id: str,
    db: Session = Depends(get_db),user = Depends(require_role("Finance_Head","Finance_admin","Manager"))
):
    try:

        result = (
            BudgetRequestService.get_budget_requests(
                claim_id,
                db
            )
        )

        if result is None:

            return JSONResponse(
                status_code=404,
                content={
                    "error": "Expense claim not found"
                }
            )

        return JSONResponse(
            status_code=200,
            content=[
                {
                    "id": str(request.id),
                    "department": request.department.name,
                    "requested_by": request.requester.name,
                    "requested_amount": float(request.requested_amount),
                    "status": request.status,
                    "approved_by": (
                        request.approver.name
                        if request.approver
                        else None
                    ),
                    "approved_at": (
                        str(request.approved_at)
                        if request.approved_at
                        else None
                    ),
                    "remarks": request.remarks
                }
                for request in result
            ]
        )

    except Exception as e:

        return JSONResponse(
            status_code=500,
            content={
                "error": str(e)
            }
        )
