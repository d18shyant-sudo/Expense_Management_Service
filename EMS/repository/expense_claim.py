from models.expense_claim import Expense_claim
from sqlalchemy.orm import Session

class ExpenseClaimRepository:

    @staticmethod
    def get_latest_claim_by_employee(db: Session,employee_id):
        return (
            db.query(Expense_claim)
            .filter(
                Expense_claim.employees_id == employee_id
            )
            .order_by(
                Expense_claim.created_at.desc()
            )
            .first()
        )

    @staticmethod
    def get_claim_by_id(db: Session,claim_id):
        return (
            db.query(Expense_claim)
            .filter(
                Expense_claim.id == claim_id
            )
            .first()
        )

    @staticmethod
    def create_claim(db: Session,claim: Expense_claim):
        db.add(claim)
        db.commit()
        db.refresh(claim)
        return claim

    @staticmethod
    def save(db: Session,claim: Expense_claim):
        db.commit()
        db.refresh(claim)
        return claim