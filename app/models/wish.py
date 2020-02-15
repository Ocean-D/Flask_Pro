
from app.models.base import Base
from sqlalchemy import Column,Integer,Boolean,ForeignKey,String
from sqlalchemy.orm import relationship


class Wish(Base):

    id = Column(Integer, primary_key=True)
    launched = Column(Boolean, default=False)
    uid = Column(Integer, ForeignKey('user.id'), nullable=False)
    user = relationship('User')
    isbn = Column(String(13))