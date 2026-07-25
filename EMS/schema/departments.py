from pydantic import BaseModel,EmailStr
from typing import Optional
class Department_name(BaseModel):
    department_name:str
class DepartmentCreate(BaseModel):
    name: str
    manager_name: str
    manager_email: EmailStr
    finance_admin_name: str
    finance_admin_email:EmailStr
class DepartmentUpdate(BaseModel):
    name: Optional[str] = None
    manager_name: Optional[str] = None
    finance_admin_name: Optional[str] = None
