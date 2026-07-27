from fastapi import (
    APIRouter,
    Depends
)

from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session

from engine import get_db

from schema.expense_line_item import (
    ExpenseLineItemCreate,
    ExpenseLineItemUpdate
)

from service.expense_line_items import (
    ExpenseLineItemService
)

router = APIRouter(
    prefix="/api/v1",
    tags=["Expense_Line_Items"]
)
from auth import require_role

@router.post("/expense-line-items")
def create_line_item(
    line_item: ExpenseLineItemCreate,
    db: Session = Depends(get_db),user = Depends(require_role("Employee","Manager"))
):
    try:

        result = (
            ExpenseLineItemService
            .create_line_item(
                line_item,
                db
            )
        )

        if not result:
            return JSONResponse(
                status_code=404,
                content={
                    "error":
                    "Category not found"
                }
            )

        return JSONResponse(
            status_code=200,
            content=result
        )

    except Exception as e:
        return JSONResponse(
            status_code=500,
            content={
                "error": str(e)
            }
        )


@router.put(
    "/expense-line-items"
)
def update_line_item(
    line_item_id: str,
    line_item: ExpenseLineItemUpdate,
    db: Session = Depends(get_db),user = Depends(require_role("Employee","Manager"))
):
    try:

        result = (
            ExpenseLineItemService
            .update_line_item(
                line_item_id,
                line_item,
                db
            )
        )

        if result == "LINE_ITEM_NOT_FOUND":
            return JSONResponse(
                status_code=404,
                content={
                    "error":
                    "Line item not found"
                }
            )

        if result == "CATEGORY_NOT_FOUND":
            return JSONResponse(
                status_code=404,
                content={
                    "error":
                    "Category not found"
                }
            )

        return JSONResponse(
            status_code=200,
            content=result
        )

    except Exception as e:
        return JSONResponse(
            status_code=500,
            content={
                "error": str(e)
            }
        )
@router.get("/expense-line-items/{claim_id}")
def get_expense_line_items(
    claim_id: str,
    db: Session = Depends(get_db),user = Depends(require_role("Finance_Head","Finance_admin","Manager","Employee"))
):
    try:

        result = (
            ExpenseLineItemService
            .get_expense_line_items(
                claim_id,
                db
            )
        )

        if result is None:

            return JSONResponse(
                status_code=404,
                content={
                    "error": "Expense claim not found"
                }
            )

        return JSONResponse(
            status_code=200,
            content=[
                {
                    "id": str(item.id),
                    "category": item.category.name,
                    "amount": float(item.amount),
                    "description": item.description,
                    "receipt_url": item.receipt_url
                }
                for item in result
            ]
        )

    except Exception as e:

        return JSONResponse(
            status_code=500,
            content={
                "error": str(e)
            }
        )