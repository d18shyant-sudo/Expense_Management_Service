from datetime import datetime

from models.expense_claim import Expense_claim
from models.status_history import Status_history

class StatusHistoryRepository:

    @staticmethod
    def add_status_history(
        db,
        claim_id,
        approver_id,
        requested_amount,
        approved_amount,
        remaining_amount,
        status,
        remarks
    ):

        history = Status_history(
            claim_id=claim_id,
            approver_id=approver_id,
            requested_amount=requested_amount,
            approved_amount=approved_amount,
            remaining_amount=remaining_amount,
            status=status,
            remarks=remarks,
            action_time=datetime.utcnow()
        )

        db.add(history)
        db.commit()
        db.refresh(history)

        return history

    @staticmethod
    def get_status_history(claim_id, db):
        claim = (
            db.query(Expense_claim)
            .filter(Expense_claim.id == claim_id)
            .first()
        )

        if not claim:
            return None

        return claim.status_histories