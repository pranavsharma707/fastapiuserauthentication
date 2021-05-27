import re
from fastapi import APIRouter,Depends,status,HTTPException,Request
from sqlalchemy.orm import Session, query
from typing import List

from starlette.routing import request_response
from api import databases
from api import schema
from api import oauth2
from api import model
from fastapi import Request, status
from fastapi.encoders import jsonable_encoder
from fastapi.exceptions import RequestValidationError
import codecs


router=APIRouter(
    prefix='/blog',
    tags=['blogs']
)




@router.get('/',response_model=List[schema.ShowBlog])
def all(db:Session=Depends(databases.get_db)):
    blog=db.query(model.Blog).all()
    return blog

@router.get('/{id}',status_code=200,response_model=schema.ShowBlog)
def show(id,db:Session=Depends(databases.get_db),get_current_user:schema.User=Depends(oauth2.get_current_user)):
    blog=db.query(model.Blog).filter(model.Blog.id==id).first()
    if not blog:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f'Blog with id {id} is not available')
    return blog

@router.post('/',status_code=status.HTTP_201_CREATED)
def create_data(request:schema.Blog,get_current_user:schema.User=Depends(oauth2.get_current_user),db:Session=Depends(databases.get_db)):
    new_blog=model.Blog(title=request.title,body=request.body,user_id=1)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog



    

@router.delete('/{id}',status_code=status.HTTP_204_NO_CONTENT)
def delete(id,db:Session=Depends(databases.get_db),get_current_user:schema.User=Depends(oauth2.get_current_user)):
    blog=db.query(model.Blog).filter(model.Blog.id==id)
    if not blog.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f'Blog with id {id} is not available')
    blog.delete(synchronize_session=False)

    db.commit()
    return 'done'

    

@router.put('/{id}',status_code=status.HTTP_202_ACCEPTED)
def update(id,request:schema.Blog,db:Session=Depends(databases.get_db),get_current_user:schema.User=Depends(oauth2.get_current_user)):
    blog=db.query(model.Blog).filter(model.Blog.id==id)
    if not blog.first():
         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f'Blog with id {id} is not available')
    blog.update({'title':request.title,'body':request.body})
    db.commit()
    return 'updated'




# @router.get('/user/{id}',status_code=status.HTTP_302_FOUND)
# def get_user(id,db:Session=Depends(databases.get_db)):
#     user=db.query(model.NewUser).filter(model.NewUser.id==id).first()
#     if not user:
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f'Blog with id {id} is not available')
#     return user



    





