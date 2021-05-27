from fastapi import APIRouter,Depends,status,HTTPException
from sqlalchemy.orm import Session
from api import schema
from api import databases
from api import model
from api.hashing import Hash
from api.repository.user import *

router=APIRouter(
    prefix='/user',
    tags=['user']
)



@router.post('/',response_model=schema.ShowUser)
def create_user(request:schema.User,db:Session=Depends(databases.get_db)):
    return create(request,db)



@router.get('/{id}',response_model=schema.ShowUser)
def get_user(id:int,db:Session=Depends(databases.get_db)):
    return single_user(id,db)

