
from app.models.base import Base, db
from sqlalchemy import Column,Integer,Boolean,ForeignKey,String,func,desc
from sqlalchemy.orm import relationship


from app.spider.yushu_book import YuShuBook


class Wish(Base):

    id = Column(Integer, primary_key=True)
    launched = Column(Boolean, default=False)
    user = relationship('User')
    uid = Column(Integer, ForeignKey('user.id'), nullable=False)
    isbn = Column(String(13))

    @classmethod
    def get_user_wishes(cls, uid):
        wishes = Wish.query.filter_by(uid=uid, launched=False).order_by(
            desc(Wish.create_time)).all()
        return wishes

    @classmethod
    def   get_gifts_counts(cls, isbn_list):
        # 根据传入一组isbn，到wish表中计算出某个礼物的
        # wish心愿数
        # db.sessions
        # filter是传入表达式
        from app.models.gift import Gift
        count_list = db.session.query(func(Gift.id), Gift.isbn).filter(Gift.launched == False,
                                                                       Gift.isbn.in_(isbn_list),
                                                                       Gift.status == 1).group_by(Gift.isbn).all()
        count_list = [{'count': w(0), 'isbn': w(1)} for w in count_list]
        return count_list

    @property
    def book(self):
        yushu_book = YuShuBook()
        yushu_book.search_by_isbn(self.isbn)
        return yushu_book.first


