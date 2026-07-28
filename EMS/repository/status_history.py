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

        print(">>> add_status_history called:", status)

        history = Status_history(
            claim_id=claim_id,
            approver_id=approver_id,
            requested_amount=requested_amount,
            approved_amount=approved_amount,
            remaining_amount=remaining_amount,
            status=status,
            remarks=remarks
        )

        db.add(history)
        db.commit()
        db.refresh(history)

        return history