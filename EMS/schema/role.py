from pydantic import BaseModel
from uuid import UUID
class Role_name(BaseModel):
    role_name:str
class Update_Role(BaseModel):
    role_name:str
    role_id:UUID