from schema.departments import Department_name
from engine import get_db
from fastapi import APIRouter,Depends
from sqlalchemy.orm import Session
from fastapi.responses import JSONResponse
from service.departments import department_service
router = APIRouter(prefix="/api/v1",tags=["Departments"])
@router.get("/get-department-name",response_model=list[Department_name])
def get_departments(db:Session = Depends(get_db)):
    try:
        results = department_service.get_departments(db)
        if results:
            return JSONResponse(status_code=200,content=[result for result in results])
        if not results:
            return JSONResponse(status_code=404,content={"Error":"No Departments found"})
    except Exception as e:
        return JSONResponse(status_code=500,content={"Error":str(e)})