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
            department_id=
            employee.department_id,
            # Manager who raised request
            requested_by=
            employee.manager_id,
            requested_amount=
            payload.requested_amount,
            # Default status
            status="PENDING",
            remarks=
            payload.remarks,
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
            "requested_amount":
            float(
                created_budget.requested_amount
            ),
            "status":
            created_budget.status
        }

    @staticmethod
    def update_budget_request(
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
        action_employee = (
            BudgetRequestRepository
            .get_employee_by_id(
                payload.approved_by,
                db
            )
        )
        if not action_employee:
            return "EMPLOYEE_NOT_FOUND"
        role = action_employee.role.nam

        # =====================================
        # MANAGER
        # =====================================
        if role == "MANAGER":
            if budget.status != "PENDING":
                return "REQUEST_ALREADY_PROCESSED"
            if payload.requested_amount is not None:
                budget.requested_amount = (
                    payload.requested_amount
                )
            if payload.remarks is not None:
                budget.remarks = (
                    payload.remarks
                )

        # =====================================
        # FINANCE ADMIN
        # APPROVE / REJECT
        # =====================================

        elif role == "FINANCE_ADMIN":
            if budget.status != "PENDING":
                return "REQUEST_ALREADY_PROCESSED"
            if payload.status not in [
                "APPROVED",
                "REJECTED"
            ]:
                return "INVALID_STATUS"
            budget.status = (
                payload.status
            )
            budget.approved_by = (
                action_employee.id
            )
            budget.approved_at = (
                datetime.utcnow()
            )
            if payload.remarks is not None:
                budget.remarks = (
                    payload.remarks
                )

        # =====================================
        # FINANCE HEAD
        # =====================================

        elif role == "FINANCE_HEAD":
            if budget.status != "APPROVED":
                return "REQUEST_NOT_APPROVED"
            if payload.status != "ALLOCATED":
                return "INVALID_STATUS"
            budget.status = "ALLOCATED"
            budget.approved_by = (
                action_employee.id
            )
            budget.approved_at = (
                datetime.utcnow()
            )
            if payload.remarks is not None:

                budget.remarks = (
                    payload.remarks
                )
        else:
            return "NOT_AUTHORIZED"
        budget.updated_at = (
            datetime.utcnow()
        )
        BudgetRequestRepository.save(budget,db)
        return {
            "message":
            "Budget request updated",
            "id":
            str(budget.id),
            "status":
            budget.status,
            "approved_by":
            (
                str(budget.approved_by)
                if budget.approved_by
                else None
            ),
            "approved_at":
            (
                str(budget.approved_at)
                if budget.approved_at
                else None
            ),
            "remarks":
            budget.remarks
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