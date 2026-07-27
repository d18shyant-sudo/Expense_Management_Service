from datetime import datetime

from models.budget_requests import (
    Budget_requests
)

from repository.budget_requests import (
    BudgetRequestRepository
)

class BudgetRequestService:

    @staticmethod
    def create_budget_request(
        payload,
        db
    ):

        claim = (
            BudgetRequestRepository
            .get_claim_by_id(
                payload.claim_id,
                db
            )
        )

        if not claim:
            return "CLAIM_NOT_FOUND"

        employee = claim.employee

        if not employee:
            return "EMPLOYEE_NOT_FOUND"

        budget_request = Budget_requests(

            claim_id=claim.id,

            requested_by=employee.id,

            department_id=
            employee.department_id,

            requested_amount=
            payload.requested_amount,

            status=payload.status,

            remarks=payload.remarks,

            created_at=
            datetime.utcnow()
        )

        created_budget = (
            BudgetRequestRepository
            .create(
                budget_request,
                db
            )
        )

        return {
            "message":
            "Budget request created",
            "id":
            str(created_budget.id),
            "department_id":
            str(created_budget.department_id),
            "requested_by":
            str(created_budget.requested_by)
        }

    @staticmethod
    def update_budget_request(
    user,
    budget_request_id,
    payload,
    db
):

     budget = (
        BudgetRequestRepository
        .get_budget_request_by_id(
            budget_request_id,
            db
        )
    )

     if not budget:
        return "BUDGET_REQUEST_NOT_FOUND"


     claim = (
        BudgetRequestRepository
        .get_claim_by_id(
            payload.claim_id,
            db
        )
    )

     if not claim:
        return "CLAIM_NOT_FOUND"


     employee = claim.employee


     budget.claim_id = claim.id
     budget.requested_by = employee.id
     budget.department_id = employee.department_id


     role = user["role"]


    # Manager can only create/update request
    # status should remain Pending
     if role == "Manager":

        budget.status = "Pending"


    # Finance Admin can change status if provided
     elif role == "Finance_admin":

        if payload.status is not None:
            budget.status = payload.status


    # Finance Head has full control
     elif role == "Finance_Head":

        if payload.status is not None:
            budget.status = payload.status


     if payload.requested_amount is not None:
        budget.requested_amount = (
            payload.requested_amount
        )


     if payload.remarks is not None:
        budget.remarks = payload.remarks


     budget.updated_at = datetime.utcnow()


     BudgetRequestRepository.save(
        budget,
        db
    )


     return {
        "message": "Budget request updated",
        "claim_id": str(budget.claim_id),
        "department_id": str(budget.department_id),
        "requested_by": str(budget.requested_by),
        "requested_amount": float(budget.requested_amount),
        "status": budget.status,
        "remarks": budget.remarks
    }
    @staticmethod
    def get_budget_requests(
        claim_id,
        db
    ):

        return (
            BudgetRequestRepository
            .get_budget_requests(
                claim_id,
                db
            )
        )