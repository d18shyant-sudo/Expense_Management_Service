from schema.category import Category_name
from engine import get_db
from fastapi import APIRouter,Depends
from sqlalchemy.orm import Session
from fastapi.responses import JSONResponse
from service.category import category_service
router = APIRouter(prefix="/api/v1",tags=["Categories"])
@router.get("/get-category-name",response_model=list[Category_name])
def get_category(db:Session = Depends(get_db)):
    try:
        results = category_service.get_category(db)
        if results:
            return JSONResponse(status_code=200,content=[result for result in results])
        if not results:
            return JSONResponse(status_code=404,content={"Error":"No Categories found"})
    except Exception as e:
        return JSONResponse(status_code=500,content={"Error":str(e)})
