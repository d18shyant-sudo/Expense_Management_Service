from pydantic import BaseModel
from uuid import UUID
# request
class Employee_name(BaseModel):
    name:str
class Employee_role(BaseModel):
    role:str
class Employee_department(BaseModel):
    department:str
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