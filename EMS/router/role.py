from schema.role import Role_name
from engine import get_db
from fastapi import APIRouter,Depends
from sqlalchemy.orm import Session
from fastapi.responses import JSONResponse
from service.role import role_service
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