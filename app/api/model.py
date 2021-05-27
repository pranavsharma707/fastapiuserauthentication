
from api.databases import Base
from sqlalchemy import Column, Integer, String,ForeignKey
from sqlalchemy.orm import relationship

class Blog(Base):
    __tablename__='Blog'

    id=Column(Integer,primary_key=True,index=True)
    title=Column(String(100))
    body=Column(String(100))
    user_id=Column(Integer,ForeignKey('User.id'))
    creator=relationship('User',back_populates='blogs')

class User(Base):
    __tablename__='User'
    id=Column(Integer,primary_key=True,index=True) # it is auto increment show it will not be show at the time of inserting data
    name=Column(String(100))
    email=Column(String(100))
    password=Column(String(100))
    blogs=relationship('Blog',back_populates='creator')

class NewUser(Base):
    __tablename__='newuser'
    id=Column(Integer,primary_key=True,index=True)
    email=Column(String(100))
 


class CreateUser(Base):
    __tablename__='createuser'
    id=Column(Integer,primary_key=True,index=True)
    first_name=Column(String(50))
    last_name=Column(String(50))
    address=Column(String(50))

    
