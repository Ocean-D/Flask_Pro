from flask import current_app
from werkzeug.security import generate_password_hash, check_password_hash

from app.libs.enums import PendingStatus
from app.libs.helper import is_isbn_or_key
from app.models.base import Base, db
from sqlalchemy import Column,Integer,ForeignKey,String,Boolean,Float
from sqlalchemy.orm import relationship
from flask_login import UserMixin
from app import login_manager
from app.models.gift import Gift
from app.models.wish import Wish
from app.spider.yushu_book import YuShuBook
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
from app.models.drift import Drift
from math import floor



class User(UserMixin,Base):
    id = Column(Integer, primary_key=True)
    nickname = Column(String(24), nullable=False)
    phone_number = Column(String(18), unique=True)
    _password = Column('password', String(128),nullable=False)
    email = Column(String(50), nullable=False,unique=True)
    confirmed = Column(Boolean, default=False)
    beans = Column(Float, default=0)
    send_counter = Column(Integer, default=0)
    receive_counter = Column(Integer, default=0)


    def can_send_drift(self):
        if self.beans < 1:
            return False
        success_gift_count = User.query.filter_by(
            uid=self.id,launched=True).count()
        success_receive_count = Drift.query.filter_by(
            request_id=self.id,pending=PendingStatus.Success).count()
        return True \
            if floor(success_receive_count/2) <= floor(success_gift_count) \
            else  False


    @property
    def password(self):
        return self._password
    @password.setter
    def password(self,raw):
        self._password = generate_password_hash(raw)


    # @property
    # def password(self):
    #     return self._password
    #
    #
    # @password.setter
    # def password(self,raw):
    #     self._password = generate_password_hash(raw)

    def check_password(self,raw):
       return check_password_hash(self._password,raw)

    # def check_password(self,raw):
    #     return check_password_hash(self._password,raw)
    # #判断isbn是否是属于合法 再判断是否在YuShuBook中的
    # def get_id(self):
    #     return self.id
    def can_save_to_list(self,isbn):
        if is_isbn_or_key(isbn) != 'isbn':
            return False
        yushu_book = YuShuBook()
        yushu_book.search_by_isbn(isbn)
        if not yushu_book.first:
            return False
        # 一个用户不能同时赠送多本相同的书
        #一个用户不能同时是赠送者和索要这
        #一本书既不在赠送清单，也不在心愿清单才能添加
        gifting = Gift.query.filter_by(uid=self.id,isbn=isbn,launched=False).first()
        wishing = Wish.query.filter_by(uid=self.id,isbn=isbn,launched=False).first()
        if not gifting and not wishing:
            return True
    #     if is_isbn_or_key(isbn) != 'isbn':
    #         return False
    #     yushu_book = YuShuBook()
    #     yushu_book.search_by_isbn(isbn)
    #     if not yushu_book.books.first:
    #         return False
    #     gifting = Gift.query.filter_by(uid=self.id,isbn=isbn,launched=False).first()
    #     wishing = Wish.query.filter_by(uid=self.id,isbn=isbn,launched=False).first()
    #     if not gifting and not wishing:
    #         return True
    #     else:
    #         return False
    def generate_token(self,expiration=600):
        s = Serializer(current_app.config['SECRET_KEY'],expiration)
        return s.dumps({'id':self.id}).decode('utf-8')

    @staticmethod
    def reset_password(token,new_password):
        s = Serializer(current_app.congig['SECRET_KEY'])
        try:
            data = s.loads(token.encode('utf-8'))
        except:
            return
        uid = data.get('id')
        with db.auto_commit():
            user = User.query.get(uid)
            user.password = new_password
        return True

    @property
    def summary(self):
        return dict(
            nickname = self.nickname,
            beans = self.beans,
            email = self.email,
            send_receive = str(self.send_counter) + '/' + str(self.receive_counter)
        )







@login_manager.user_loader
def get_user(uid):
    return User.query.get(int(uid))


