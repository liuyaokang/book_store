from book.modles.base import db
from sqlalchemy import Column,Integer,String,Boolean

class Gift(db.Model):
    id = Column(Integer,primary_key=True)
    launched = Column(Boolean,default=False)