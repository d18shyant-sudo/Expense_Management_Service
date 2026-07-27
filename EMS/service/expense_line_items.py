from datetime import datetime

from repository.expense_line_items import (
    ExpenseLineItemRepository
)

from models.expense_line_items import (
    Expense_line_item
)

class ExpenseLineItemService:

    @staticmethod
    def create_line_item(
        payload,
        db
    ):

        category = (
            ExpenseLineItemRepository
            .get_category_by_name(
                payload.category_name,
                db
            )
        )

        if not category:
            return None

        line_item = Expense_line_item(
            claim_id=payload.claim_id,
            category_id=category.id,
            amount=payload.amount,
            description=payload.description,
            receipt_url=payload.receipt_url,
            created_at=datetime.utcnow()
        )

        created_item = (
            ExpenseLineItemRepository
            .create(
                line_item,
                db
            )
        )

        return {
            "message":
            "Expense line item created",
            "id":
            str(created_item.id),
            "category":
            category.name
        }

    @staticmethod
    def update_line_item(
        line_item_id,
        payload,
        db
    ):

        line_item = (
            ExpenseLineItemRepository
            .get_line_item_by_id(
                line_item_id,
                db
            )
        )

        if not line_item:
            return "LINE_ITEM_NOT_FOUND"

        category = (
            ExpenseLineItemRepository
            .get_category_by_name(
                payload.category_name,
                db
            )
        )

        if not category:
            return "CATEGORY_NOT_FOUND"

        line_item.category_id = category.id
        line_item.amount = payload.amount
        line_item.description = payload.description
        line_item.receipt_url = payload.receipt_url
        line_item.updated_at = datetime.utcnow()

        ExpenseLineItemRepository.save(
            line_item,
            db
        )

        return {
            "message":
            "Expense line item updated",
            "id":
            str(line_item.id),
            "category":
            category.name
        }
    @staticmethod
    def get_expense_line_items(
        claim_id,
        db
    ):

        return (
            ExpenseLineItemRepository
            .get_expense_line_items(
                claim_id,
                db
            )
        )