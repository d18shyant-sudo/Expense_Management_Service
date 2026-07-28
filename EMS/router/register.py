from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from fastapi.responses import JSONResponse

from engine import get_db

from schema.account import (
    LoginRegister

)
from service.register import Register_service
router = APIRouter(
    prefix="/api/v1",
    tags=["Registeration"]
)
@router.post("/register")
def register_account(detail:LoginRegister,db:Session=Depends(get_db)):
    try:
         result = Register_service.add_account(detail,db)
         if result:
              return JSONResponse(status_code=200,content={"Message":"The Account is created successfulyy"})
         elif not result:
              return JSONResponse(status_code=400,content={"message":"Account already exists"})
    except Exception as e:
         return JSONResponse(status_code=500,content={"message":str(e)})
