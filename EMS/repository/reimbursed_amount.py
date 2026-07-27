from sqlalchemy.orm import Session

from models.expense_claim import Expense_claim
from models.reimbursed_amount import Reimbursed_amount


class ReimbursementRepository:

    @staticmethod
    def get_claim_by_id(
        claim_id,
        db: Session
    ):
        return (
            db.query(Expense_claim)
            .filter(
                Expense_claim.id == claim_id
            )
            .first()
        )

    @staticmethod
    def get_reimbursement_by_id(
        reimbursement_id,
        db: Session
    ):
        return (
            db.query(Reimbursed_amount)
            .filter(
                Reimbursed_amount.id == reimbursement_id
            )
            .first()
        )

    @staticmethod
    def create(
        reimbursement,
        db: Session
    ):
        db.add(reimbursement)
        db.commit()
        db.refresh(reimbursement)
        return reimbursement

    @staticmethod
    def save(
        reimbursement,
        db: Session
    ):
        db.commit()
        db.refresh(reimbursement)
        return reimbursement