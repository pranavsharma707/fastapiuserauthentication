from fastapi import FastAPI
import api
from api.databases import engine
from api.routers import blog,user,authentication


app=FastAPI()

api.model.Base.metadata.create_all(engine)


app.include_router(authentication.router)
app.include_router(blog.router)
app.include_router(user.router)








