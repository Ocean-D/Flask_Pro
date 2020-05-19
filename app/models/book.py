
from app.models.base import Base
from sqlalchemy import Column,Integer,String
#sqlalchemy
#Flsk_SQLAlchemy
#wtform
#Flask_WTFORM



class Book(Base):
    id = Column(Integer,primary_key=True,autoincrement=True)
    title = Column(String(20),nullable=False)
    author = Column(String(30),default='未名')
    binding = Column(String(20))
    publisher = Column(String(50))
    price = Column(String(20))
    pages = Column(Integer)
    pubdate = Column(String(15))
    isbn = Column(String(15),nullable=False,unique=True)
    summary = Column(String(1000))
    image = Column(String(50))
    # id =Column(Integer,primary_key=True,autoincrement=True)
    # title = Column(String(35),nullable=False)
    # author = Column(String(30),default='未名')#作者没有显示为未名
    # publisher = Column(String(20))
    # binding = Column(String(20))
    # price = Column(String(20))
    # pages =Column(Integer)
    # image = Column(String(50))
    # summary = Column(String(1000))
    # isbn = Column(String(15),nullable=False,unique=True)




