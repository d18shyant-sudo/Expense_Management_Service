from database import Base, engine
from sqlalchemy.orm import configure_mappers
from models.role import Role
from models.employees import Employee
from models.departments import Department
from models.category import Category
from models.account import Account
from models.expense_claim import Expense_claim
from models.expense_line_items import Expense_line_item
from models.status_history import Status_history
from models.budget_requests import Budget_requests
from  models.reimbursed_amount import Reimbursed_amount
from models.partial_reimbursed_amount import Partial_reimbursed_amount
Base.metadata.create_all(engine)
configure_mappers()
print("All tables are fine and perfect")