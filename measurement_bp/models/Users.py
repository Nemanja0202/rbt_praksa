import os
from app import db
from sqlalchemy import Column,Integer,Float,String
from datetime import datetime

class Users(db.Model):
    __tablename__ = 'users'

    id = Column(Integer, primary_key = True)
    username = Column(String(50), nullable=False)
    password = Column(String(50), nullable=False)
    date_created = Column(db.DateTime, nullable=False,default=datetime.utcnow)
 