from werkzeug.security import generate_password_hash, check_password_hash

from app.models.base import Base
from sqlalchemy import Column,Integer,ForeignKey,String,Boolean,Float
from sqlalchemy.orm import relationship




class user(Base):
    id = Column(Integer, primary_key=True)
    nickname = Column(String(24), nullable=False)
    phone_number = Column(String(18), unique=True)
    _password = Column('password', String(128))
    email = Column(String(50), unique=True, nullable=False)
    confirmed = Column(Boolean, default=False)
    beans = Column(Float, default=0)
    send_counter = Column(Integer, default=0)
    receive_counter = Column(Integer, default=0)
    gifts = relationship('Gift')

    @property
    def password(self):
        return self._password


    @password.setter
    def password(self,raw):
        self._password = generate_password_hash(raw)


    def check_password(self,raw):
        return check_password_hash(self._password,raw)

    def get_id(self):
        return self.id



