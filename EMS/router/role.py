from schema.role import Role_name,Update_Role
from engine import get_db
from fastapi import APIRouter,Depends
from sqlalchemy.orm import Session
from fastapi.responses import JSONResponse
from service.role import role_service
from auth import require_role
router = APIRouter(prefix="/api/v1",tags=["Roles"])
@router.get("/get-role-name",response_model=list[Role_name])
def get_roles(db:Session = Depends(get_db)):
    try:
        results = role_service.get_roles(db)
        if results:
            return JSONResponse(status_code=200,content=[result for result in results])
        if not results:
            return JSONResponse(status_code=404,content={"Error":"No roles are there"})
    except Exception as e:
        return JSONResponse(status_code=500,content={"Error":str(e)})
@router.post("/post-role-name",response_model=Role_name)
def post_role(new_role:Role_name,db:Session = Depends(get_db)):
    try:
        results = role_service.post_role(db,new_role)
        if results:
            return JSONResponse(status_code=200,content={"role_name":results.role_name})
        if not results:
            return JSONResponse(status_code=400,content={"Error":"Role alrady exists"})
    except Exception as e:
         return JSONResponse(status_code=500,content={"Error":str(e)})
@router.put("/update-role-name",response_model=Role_name)
def update_role(update_role:Update_Role,db:Session = Depends(get_db)):
    try:
        results = role_service.update_role(db,update_role)
        if results:
            return JSONResponse(status_code=200,content={"updated_role_name":results.role_name})
        if not results:
            return JSONResponse(status_code=400,content={"Error":"Updating the already exists one"})
    except Exception as e:
        return JSONResponse(status_code=500,content={"Error":str(e)})