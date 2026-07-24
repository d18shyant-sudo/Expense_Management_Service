from datetime import datetime
from repository.expense_claim import ExpenseClaimRepository
from models.expense_claim import Expense_claim

class ExpenseClaimService:

    @staticmethod
    def create_claim(
        claim_data,
        db
    ):

        existing_claim = (
            ExpenseClaimRepository
            .get_latest_claim_by_employee(
                db,
                claim_data.employee_id
            )
        )

        revision_count = 0
        last_resubmitted_at = None

        if existing_claim:
            revision_count = (
                existing_claim.revision_count + 1
            )
            last_resubmitted_at = datetime.utcnow()

        claim = Expense_claim(
            employees_id=claim_data.employee_id,
            purpose=claim_data.purpose,
            requested_amount=claim_data.requested_amount,
            status="Submitted",
            revision_count=revision_count,
            submitted_at=datetime.utcnow(),
            last_resubmitted_at=last_resubmitted_at,
            created_at=datetime.utcnow()
        )

        return ExpenseClaimRepository.create_claim(
            db,
            claim
        )

    @staticmethod
    def resubmit_claim(
        claim_id,
        claim_data,
        db
    ):

        claim = (
            ExpenseClaimRepository
            .get_claim_by_id(
                db,
                claim_id
            )
        )

        if not claim:
            return None

        claim.purpose = claim_data.purpose
        claim.requested_amount = (
            claim_data.requested_amount
        )

        claim.revision_count += 1
        claim.last_resubmitted_at = datetime.utcnow()
        claim.status = "Submitted"
        claim.updated_at = datetime.utcnow()

        return ExpenseClaimRepository.save(
            db,
            claim
        )

    @staticmethod
    def approve_claim(
        claim_id,
        db
    ):

        claim = (
            ExpenseClaimRepository
            .get_claim_by_id(
                db,
                claim_id
            )
        )

        if not claim:
            return None

        claim.approved_at = datetime.utcnow()
        claim.updated_at = datetime.utcnow()
        claim.status = "Approved"

        return ExpenseClaimRepository.save(
            db,
            claim
        )

    @staticmethod
    def reimburse_claim(
        claim_id,
        db
    ):

        claim = (
            ExpenseClaimRepository
            .get_claim_by_id(
                db,
                claim_id
            )
        )

        if not claim:
            return None

        claim.reimbursed_at = datetime.utcnow()
        claim.updated_at = datetime.utcnow()
        claim.status = "Reimbursed"

        return ExpenseClaimRepository.save(
            db,
            claim
        )
    @staticmethod
    def get_claims(
        employee_id,
        db
    ):

        employee = (
            ExpenseClaimRepository
            .get_employee(
                employee_id,
                db
            )
        )


        if not employee:
            return None


        role = employee.role.role_name


        if role == "Employee":

            return (
                ExpenseClaimRepository
                .get_employee_claims(
                    employee.id,
                    db
                )
            )


        elif role in [
            "Manager",
            "Finance_admin"
        ]:

            return (
                ExpenseClaimRepository
                .get_department_claims(
                    employee.department_id,
                    db
                )
            )


        elif role == "Finance_head":

            return (
                ExpenseClaimRepository
                .get_all_claims(
                    db
                )
            )


        return []