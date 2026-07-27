from sqlalchemy.orm import Session
from models.category import Category
from models.expense_line_items import Expense_line_item
from models.employees import Employee
from models.expense_claim import Expense_claim
class ExpenseLineItemRepository:

    @staticmethod
    def get_category_by_name(
        category_name: str,
        db: Session
    ):
        return (
            db.query(Category)
            .filter(
                Category.name == category_name
            )
            .first()
        )

    @staticmethod
    def get_line_item_by_id(
        line_item_id,
        db: Session
    ):
        return (
            db.query(Expense_line_item)
            .filter(
                Expense_line_item.id == line_item_id
            )
            .first()
        )

    @staticmethod
    def create(
        line_item,
        db: Session
    ):
        db.add(line_item)
        db.commit()
        db.refresh(line_item)
        return line_item

    @staticmethod
    def save(
        line_item,
        db: Session
    ):
        db.commit()
        db.refresh(line_item)
        return line_item
    @staticmethod
    def get_expense_line_items(
        claim_id,
        db
    ):

        expense_claim = (
            db.query(Expense_claim)
            .filter(
                Expense_claim.id == claim_id
            )
            .first()
        )

        if not expense_claim:
            return None

        return expense_claim.line_items