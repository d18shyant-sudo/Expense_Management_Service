from datetime import datetime

from models.status_history import (
    Status_history
)

from repository.status_history import (
    StatusHistoryRepository
)

class StatusHistoryService:

    @staticmethod
    def create_status_history(
        payload,
        db
    ):

        claim = (
            StatusHistoryRepository
            .get_claim_by_id(
                payload.claim_id,
                db
            )
        )

        if not claim:
            return "CLAIM_NOT_FOUND"

        employee = claim.employee
        department = employee.department
        manager_id = department.manager_id

        history = Status_history(
            claim_id=claim.id,
            approver_id=manager_id,
            requested_amount=
            claim.requested_amount,

            approved_amount=
            payload.approved_amount,

            remaining_amount=(
                claim.requested_amount
                - payload.approved_amount
            ),

            status=payload.status,
            remarks=payload.remarks,

            action_time=
            datetime.utcnow(),

            created_at=
            datetime.utcnow()
        )

        created_history = (
            StatusHistoryRepository
            .create(
                history,
                db
            )
        )

        return {
            "message":
            "Status history created",
            "id":
            str(created_history.id)
        }

    @staticmethod
    def update_status_claim(
        history_id,
        payload,
        db
    ):

        history = (
            StatusHistoryRepository
            .get_history_by_id(
                history_id,
                db
            )
        )

        if not history:
            return "HISTORY_NOT_FOUND"

        claim = (
            StatusHistoryRepository
            .get_claim_by_id(
                payload.claim_id,
                db
            )
        )

        if not claim:
            return "CLAIM_NOT_FOUND"

        manager_id = (
            claim.employee
            .department
            .manager_id
        )

        history.claim_id = claim.id
        history.approver_id = manager_id

        history.requested_amount = (
            claim.requested_amount
        )

        history.updated_at = (
            datetime.utcnow()
        )

        StatusHistoryRepository.save(
            history,
            db
        )

        return {
            "message":
            "Status history updated"
        }

    @staticmethod
    def update_status(
        history_id,
        payload,
        db
    ):

        history = (
            StatusHistoryRepository
            .get_history_by_id(
                history_id,
                db
            )
        )

        if not history:
            return "HISTORY_NOT_FOUND"

        history.status = payload.status
        history.remarks = payload.remarks

        history.approved_amount = (
            payload.approved_amount
        )

        history.remaining_amount = (
            history.requested_amount
            - payload.approved_amount
        )

        history.action_time = (
            datetime.utcnow()
        )

        history.updated_at = (
            datetime.utcnow()
        )

        StatusHistoryRepository.save(
            history,
            db
        )

        return {
            "message":
            "Status updated"
        }