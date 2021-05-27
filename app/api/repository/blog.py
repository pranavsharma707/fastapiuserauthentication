from sqlalchemy.orm import Session
from fastapi import Depends,HTTPException,status
from api import databases
from api import model
from api import schema

def get_all(db:Session=Depends(databases.get_db)):
    blog=db.query(model.Blog).all()
    return blog

def single(id,db:Session=Depends(databases.get_db)):
    blog=db.query(model.Blog).filter(model.Blog.id==id).first()
    if not blog:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f'Blog with id {id} is not available')
    return blog

def data_created(request:schema.User,db:Session=Depends(databases.get_db)):
    new_blog=model.Blog(title=request.title,body=request.body,user_id=1)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog

def  data_delete(id,db:Session=Depends(databases.get_db)):
    blog=db.query(model.Blog).filter(model.Blog.id==id)
    if not blog.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f'Blog with id {id} is not available')
    blog.delete(synchronize_session=False)
    db.commit()
    return 'done'

def update_data(id,request:schema.Blog,db:Session=Depends(databases.get_db)):
    blog=db.query(model.Blog).filter(model.Blog.id==id)
    if not blog.first():
         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f'Blog with id {id} is not available')
    blog.update({'title':request.title,'body':request.body})
    db.commit()
    return 'updated'