from fastapi import APIRouter
from router.employees import router as employee_router
from router.category import router as category_router
from router.departments import router as department_router
from router.role import router as role_router
from router.expense_claim import router as expense_router
from router.expense_line_items import router as expense_line_router
from router.status_history import router as status_history_router
from router.budget_requests import router as budget_requests_router
from router.reimbursed_amount import router as reimbursed_amount_router
from router.partial_reimbursed_amount import router as partial_reimbursed_router
from router.account import router as account_router
api_router = APIRouter()
api_router.include_router(employee_router)
api_router.include_router(category_router)
api_router.include_router(department_router)
api_router.include_router(role_router)
api_router.include_router(expense_router)
api_router.include_router(expense_line_router)
api_router.include_router(status_history_router)
api_router.include_router(budget_requests_router)
api_router.include_router(reimbursed_amount_router)
api_router.include_router(partial_reimbursed_router)
api_router.include_router(account_router)
