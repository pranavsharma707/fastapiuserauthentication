from calendar import c
from fastapi import APIRouter,Depends,status,HTTPException
from sqlalchemy.orm import Session
from api import databases
from api import model
from api import schema
from api.hashing import Hash
from fastapi.security import OAuth2PasswordRequestForm
from api.routers import token
router=APIRouter(
    prefix='/login',
    tags=['authentication']
)

@router.post('/')
def login(request:OAuth2PasswordRequestForm=Depends(),db:Session=Depends(databases.get_db)):
    user=db.query(model.User).filter(model.User.email==request.username).first()

    
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f'invalid username please try with corrcet username')
    if not  Hash.verify(user.password,request.password):#here user.password means the hashpassword and request.password the plain passweord
                raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f'invalid password please try with correct password')
    data=new(request,db)
    print(data)
    access_token = token.create_access_token(data={"sub": user.email})
    # return {"access_token": access_token, "token_type": "bearer"}
    return user.email

def new(request:OAuth2PasswordRequestForm=Depends(),db:Session=Depends(databases.get_db)):
    user=db.query(model.User).filter(model.User.email==request.username).first()
    return user.email

