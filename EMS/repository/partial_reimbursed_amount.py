from sqlalchemy.orm import Session

from models.expense_claim import Expense_claim
from models.partial_reimbursed_amount import (
    Partial_reimbursed_amount
)

class PartialReimbursementRepository:

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
    def get_partial_by_id(
        partial_id,
        db: Session
    ):
        return (
            db.query(
                Partial_reimbursed_amount
            )
            .filter(
                Partial_reimbursed_amount.id
                == partial_id
            )
            .first()
        )

    @staticmethod
    def create(
        partial,
        db: Session
    ):
        db.add(partial)
        db.commit()
        db.refresh(partial)
        return partial

    @staticmethod
    def save(
        partial,
        db: Session
    ):
        db.commit()
        db.refresh(partial)
        return partial