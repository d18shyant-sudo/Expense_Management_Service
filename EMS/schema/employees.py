from pydantic import BaseModel
from uuid import UUID
from typing import Optional
# request
class Employee_name(BaseModel):
    name:str
class Employee_role(BaseModel):
    role:str
class Employee_department(BaseModel):
    department:str
class EmployeeCreate(BaseModel):
    name: str
    email: str
    role_name: str
    department_name: str
class EmployeeUpdate(BaseModel):
    name: Optional[str] = None
    email: Optional[str] = None
    role_name: Optional[str] = None
    department_name: Optional[str] = None
    is_active: Optional[bool] = None
# response
class Get_Employees(BaseModel):
    name:str
    id:UUID
    role:str
    department:str
class Get_Employees_department(BaseModel):
    name:str
    id:UUID
    role:str