from fastapi import (
    APIRouter,
    Depends
)
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session
from engine import get_db
from service.budget_requests import (
    BudgetRequestService
)
from schema.budget_requests import (
    BudgetRequestCreate,
    BudgetRequestUpdate
)

from auth import require_role


router = APIRouter(
    prefix="/api/v1",
    tags=["Budget_Request"]
)


# =====================================================
# Manager creates budget request
# =====================================================

@router.post(
    "/budget-requests",
    dependencies=[
        Depends(require_role("MANAGER"))
    ]
)
def create_budget_request(
    request: BudgetRequestCreate,
    db: Session = Depends(get_db)
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
                    "error": "Claim not found"
                }
            )


        if result == "EMPLOYEE_NOT_FOUND":

            return JSONResponse(
                status_code=404,
                content={
                    "error": "Employee not found"
                }
            )


        return JSONResponse(
            status_code=201,
            content=result
        )


    except Exception as e:

        return JSONResponse(
            status_code=500,
            content={
                "error": str(e)
            }
        )



# =====================================================
# Update Budget Request
#
# Manager:
#       update before approval
#
# Finance Admin:
#       APPROVED / REJECTED
#
# Finance Head:
#       ALLOCATED
#
# =====================================================

@router.put(
    "/budget-requests/{budget_request_id}"
)
def update_budget_request(
    budget_request_id: str,
    request: BudgetRequestUpdate,
    db: Session = Depends(get_db)
):

    try:

        result = (
            BudgetRequestService
            .update_budget_request(
                budget_request_id,
                request,
                db
            )
        )


        if result == "BUDGET_REQUEST_NOT_FOUND":

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


        if result == "EMPLOYEE_NOT_FOUND":

            return JSONResponse(
                status_code=404,
                content={
                    "error":
                    "Employee not found"
                }
            )


        if result == "NOT_AUTHORIZED":

            return JSONResponse(
                status_code=403,
                content={
                    "error":
                    "User not allowed to perform this action"
                }
            )


        if result == "INVALID_STATUS":

            return JSONResponse(
                status_code=400,
                content={
                    "error":
                    "Invalid status change"
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



# =====================================================
# Get Budget Requests by Claim
# =====================================================

@router.get(
    "/budget-requests/{claim_id}"
)
def get_budget_requests(
    claim_id: str,
    db: Session = Depends(get_db)
):

    try:

        result = (
            BudgetRequestService
            .get_budget_requests(
                claim_id,
                db
            )
        )


        if result is None:

            return JSONResponse(
                status_code=404,
                content={
                    "error":
                    "Expense claim not found"
                }
            )


        return JSONResponse(
            status_code=200,
            content=[
                {

                    "id":
                    str(request.id),


                    "department":
                    request.department.name,


                    "requested_by":
                    request.requester.name,


                    "requested_amount":
                    float(
                        request.requested_amount
                    ),


                    "status":
                    request.status,


                    "approved_by":
                    (
                        request.approver.name
                        if request.approver
                        else None
                    ),


                    "approved_at":
                    (
                        str(request.approved_at)
                        if request.approved_at
                        else None
                    ),


                    "remarks":
                    request.remarks

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