from datetime import datetime

from models.partial_reimbursed_amount import (
    Partial_reimbursed_amount
)

from repository.partial_reimbursed_amount import (
    PartialReimbursementRepository
)

class PartialReimbursementService:

    @staticmethod
    def create_partial_reimbursement(
        payload,
        db
    ):

        claim = (
            PartialReimbursementRepository
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

        approver_id = (
            employee.department.manager_id
        )

        partial = (
            Partial_reimbursed_amount(
                claim_id=claim.id,

                approved_by=
                approver_id,

                approved_amount=
                payload.approved_amount,

                status=
                payload.status,

                reason=
                payload.reason,

                responded_at=
                datetime.utcnow(),

                created_at=
                datetime.utcnow()
            )
        )

        created = (
            PartialReimbursementRepository
            .create(
                partial,
                db
            )
        )

        return {
            "message":
            "Partial reimbursement created",

            "id":
            str(created.id),

            "claim_id":
            str(created.claim_id),

            "approved_by":
            str(created.approved_by)
        }

    @staticmethod
    def update_partial_reimbursement(
        partial_id,
        payload,
        db
    ):

        partial = (
            PartialReimbursementRepository
            .get_partial_by_id(
                partial_id,
                db
            )
        )

        if not partial:
            return (
                "PARTIAL_REIMBURSEMENT_NOT_FOUND"
            )

        claim = (
            PartialReimbursementRepository
            .get_claim_by_id(
                payload.claim_id,
                db
            )
        )

        if not claim:
            return "CLAIM_NOT_FOUND"

        employee = claim.employee

        partial.claim_id = claim.id

        partial.approved_by = (
            employee.department.manager_id
        )

        if (
            payload.approved_amount
            is not None
        ):
            partial.approved_amount = (
                payload.approved_amount
            )

        if payload.status is not None:
            partial.status = (
                payload.status
            )

        if payload.reason is not None:
            partial.reason = (
                payload.reason
            )

        partial.responded_at = (
            datetime.utcnow()
        )

        partial.updated_at = (
            datetime.utcnow()
        )

        PartialReimbursementRepository.save(
            partial,
            db
        )

        return {
            "message":
            "Partial reimbursement updated",

            "claim_id":
            str(partial.claim_id),

            "approved_by":
            str(partial.approved_by),

            "approved_amount":
            float(
                partial.approved_amount
            ),

            "status":
            partial.status
        }