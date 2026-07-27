from sqlalchemy.orm import Session

from models.expense_claim import Expense_claim
from models.status_history import Status_history

class StatusHistoryRepository:

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
    def get_history_by_id(
        history_id,
        db: Session
    ):
        return (
            db.query(Status_history)
            .filter(
                Status_history.id == history_id
            )
            .first()
        )

    @staticmethod
    def create(
        history,
        db: Session
    ):
        db.add(history)
        db.commit()
        db.refresh(history)
        return history

    @staticmethod
    def save(
        history,
        db: Session
    ):
        db.commit()
        db.refresh(history)
        return history