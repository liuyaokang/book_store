from sqlalchemy import Column,Integer,String
from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()

class Book(db.Model):
    id = Column(Integer,primary_key=True,autoincrement=True)#将id设置为主键
    title = Column(String(50),nullable=False) #标题不能为空
    author = Column(String(20),default="未名")
    binding = Column(String(20))
    publisher = Column(String(50))
    price = Column(String(20))
    page = Column(Integer)
    pubdate = Column(String(20))
    isbn = Column(String(15),nullable=False,unique=True)
    summary = Column(String(1000))
    image = Column(String(50))

    def sample(self):
        pass