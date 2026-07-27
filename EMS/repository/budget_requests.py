from sqlalchemy.orm import Session
from models.expense_claim import Expense_claim
from models.budget_requests import Budget_requests

class BudgetRequestRepository:

    @staticmethod
    def get_claim_by_id(claim_id, db: Session):
        return (
            db.query(Expense_claim)
            .filter(
                Expense_claim.id == claim_id
            )
            .first()
        )

    @staticmethod
    def get_budget_request_by_id(
        budget_request_id,
        db: Session
    ):
        return (
            db.query(Budget_requests)
            .filter(
                Budget_requests.id == budget_request_id
            )
            .first()
        )

    @staticmethod
    def create(
        budget_request,
        db: Session
    ):
        db.add(budget_request)
        db.commit()
        db.refresh(budget_request)
        return budget_request

    @staticmethod
    def save(
        budget_request,
        db: Session
    ):
        db.commit()
        db.refresh(budget_request)
        return budget_request