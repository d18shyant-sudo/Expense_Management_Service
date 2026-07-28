from datetime import datetime

from repository.expense_claim import ExpenseClaimRepository
from repository.status_history import StatusHistoryRepository

from models.expense_claim import Expense_claim


class ExpenseClaimService:

    @staticmethod
    def create_claim(claim_data, db):

        claim = Expense_claim(
            employees_id=claim_data.employee_id,
            purpose=claim_data.purpose,
            requested_amount=claim_data.requested_amount,
            status="Submitted",
            revision_count=0,
            submitted_at=datetime.utcnow(),
            created_at=datetime.utcnow()
        )

        claim = ExpenseClaimRepository.create_claim(
            db,
            claim
        )

        # Automatically create status history
        StatusHistoryRepository.add_status_history(
            db=db,
            claim_id=claim.id,
            approver_id=claim.employees_id,
            requested_amount=claim.requested_amount,
            approved_amount=0,
            remaining_amount=claim.requested_amount,
            status="Submitted",
            remarks="Expense claim submitted"
        )

        return claim

    @staticmethod
    def resubmit_claim(
        claim_id,
        claim_data,
        db
    ):

        claim = ExpenseClaimRepository.get_claim_by_id(
            db,
            claim_id
        )

        if not claim:
            return None

        claim.purpose = claim_data.purpose
        claim.requested_amount = claim_data.requested_amount
        claim.revision_count += 1
        claim.last_resubmitted_at = datetime.utcnow()
        claim.status = "Submitted"
        claim.updated_at = datetime.utcnow()

        claim = ExpenseClaimRepository.save(
            db,
            claim
        )

        StatusHistoryRepository.add_status_history(
            db=db,
            claim_id=claim.id,
            approver_id=claim.employees_id,
            requested_amount=claim.requested_amount,
            approved_amount=0,
            remaining_amount=claim.requested_amount,
            status="Submitted",
            remarks="Expense claim resubmitted"
        )

        return claim

    @staticmethod
    def approve_claim(
        claim_id,
        approver_id,
        db
    ):

        claim = ExpenseClaimRepository.get_claim_by_id(
            db,
            claim_id
        )

        if not claim:
            return None
        
        if claim.status == "Approved":
          return "Already Approved"

        if claim.status == "Reimbursed":
          return "Already Reimbursed"

        if claim.status != "Submitted":
          return "Claim must be in 'Submitted' status to approve"

        claim.approved_at = datetime.utcnow()
        claim.updated_at = datetime.utcnow()
        claim.status = "Approved"

        claim = ExpenseClaimRepository.save(
            db,
            claim
        )

        StatusHistoryRepository.add_status_history(
            db=db,
            claim_id=claim.id,
            approver_id=approver_id,
            requested_amount=claim.requested_amount,
            approved_amount=claim.requested_amount,
            remaining_amount=0,
            status="Approved",
            remarks="Expense claim approved"
        )

        return claim

    @staticmethod
    def reimburse_claim(
        claim_id,
        approver_id,
        db
    ):

        claim = ExpenseClaimRepository.get_claim_by_id(
            db,
            claim_id
        )

        if not claim:
            return None
        
        if claim.status == "Reimbursed":
            return "Already Reimbursed"
        

        if claim.status != "Approved":
            return "Claim must be approved before reimbursement"

        
        claim.reimbursed_at = datetime.utcnow()
        claim.updated_at = datetime.utcnow()
        claim.status = "Reimbursed"

        claim = ExpenseClaimRepository.save(
            db,
            claim
        )

        StatusHistoryRepository.add_status_history(
            db=db,
            claim_id=claim.id,
            approver_id=approver_id,
            requested_amount=claim.requested_amount,
            approved_amount=claim.requested_amount,
            remaining_amount=0,
            status="Reimbursed",
            remarks="Amount reimbursed"
        )

        return claim

    @staticmethod
    def get_claims(
        employee_id,
        db
    ):

        employee = ExpenseClaimRepository.get_employee(
            employee_id,
            db
        )

        if not employee:
            return None

        role = employee.role.role_name

        if role == "Employee":

            return ExpenseClaimRepository.get_employee_claims(
                employee.id,
                db
            )

        elif role in [
            "Manager",
            "Finance_admin"
        ]:

            return ExpenseClaimRepository.get_department_claims(
                employee.department_id,
                db
            )

        elif role == "Finance_Head":

            return ExpenseClaimRepository.get_all_claims(
                db
            )

        return []