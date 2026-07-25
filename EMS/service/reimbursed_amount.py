from datetime import datetime

from models.reimbursed_amount import (
    Reimbursed_amount
)

from repository.reimbursed_amount import (
    ReimbursementRepository
)


class ReimbursementService:

    @staticmethod
    def create_reimbursement(
        payload,
        db
    ):

        claim = (
            ReimbursementRepository
            .get_claim_by_id(
                payload.claim_id,
                db
            )
        )

        if not claim:
            return "CLAIM_NOT_FOUND"

        reimbursement = Reimbursed_amount(
            claim_id=payload.claim_id,
            paid_amount=payload.paid_amount,
            payment_date=payload.payment_date,
            payment_mode=payload.payment_mode,
            transaction_reference=
            payload.transaction_reference,
            created_at=datetime.utcnow()
        )

        created = (
            ReimbursementRepository
            .create(
                reimbursement,
                db
            )
        )

        return {
            "message":
            "Reimbursement created",
            "id":
            str(created.id),
            "claim_id":
            str(created.claim_id)
        }

    @staticmethod
    def update_reimbursement(
        reimbursement_id,
        payload,
        db
    ):

        reimbursement = (
            ReimbursementRepository
            .get_reimbursement_by_id(
                reimbursement_id,
                db
            )
        )

        if not reimbursement:
            return "REIMBURSEMENT_NOT_FOUND"

        claim = (
            ReimbursementRepository
            .get_claim_by_id(
                payload.claim_id,
                db
            )
        )

        if not claim:
            return "CLAIM_NOT_FOUND"

        reimbursement.claim_id = claim.id

        if payload.paid_amount is not None:
            reimbursement.paid_amount = (
                payload.paid_amount
            )

        if payload.payment_date is not None:
            reimbursement.payment_date = (
                payload.payment_date
            )

        if payload.payment_mode is not None:
            reimbursement.payment_mode = (
                payload.payment_mode
            )

        if (
            payload.transaction_reference
            is not None
        ):
            reimbursement.transaction_reference = (
                payload.transaction_reference
            )

        reimbursement.updated_at = (
            datetime.utcnow()
        )

        ReimbursementRepository.save(
            reimbursement,
            db
        )

        return {
            "message":
            "Reimbursement updated",
            "id":
            str(reimbursement.id),
            "claim_id":
            str(reimbursement.claim_id),
            "paid_amount":
            float(
                reimbursement.paid_amount
            ),
            "payment_date":
            str(
                reimbursement.payment_date
            )
        }
    @staticmethod
    def get_reimbursement(
        claim_id,
        db
    ):

        return (
            ReimbursementRepository.get_reimbursement(
                claim_id,
                db
            )
        )