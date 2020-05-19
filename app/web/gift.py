from werkzeug.local import Local

from app.libs.enums import PendingStatus
from app.models.drift import Drift
from app.viwe_models.gift import MyGifts
from . import web
from flask_login import login_required,current_user
from app.models.gift import Gift
from app.models.base import db
from flask import current_app, render_template, flash, url_for, redirect


Local()
@web.route('/my/gifts')
@login_required
def my_gifts():
    uid = current_user.id
    gift_of_mine = Gift.get_user_gifts(uid)
    isbn_list = [gift.isbn for gift in gift_of_mine]
    wish_count_list = Gift.get_wish_counts(isbn_list)
    view_model = MyGifts(gift_of_mine,wish_count_list)
    return render_template('my_gifts.html',gifts=view_model.gifts)





@web.route('/gifts/book/<isbn>')
@login_required
def save_to_gifts(isbn):
    #验证isbn是否符合规矩
    if current_user.can_save_to_list(isbn):
        with db.auto_commit():
            gift = Gift()
            gift.isbn = isbn
            gift.uid = current_user.id
            current_user.beans += current_app.config['BEANS_UPLODE_ONE_BOOK']
            db.session.add(gift)
    else:
        flash('这本书已添加到你的赠送清单或者已存在你的心愿清单,请不要重复添加')
    return redirect(url_for('web.book_detail',isbn=isbn))

    # if current_user.can_save_to_list(isbn):
    #     #事务回滚 rollback
    #     try:
    #         gift = Gift()
    #         gift.isbn = isbn
    #         gift.uid = current_user.id
    #         gift.beans += current_app.config['BEANS_UPLODE_ONE_BOOK']
    #         db.session.add(gift)
    #         db.session.commit()
    #     except Exception as e:
    #         db.session.rollback()
    #         raise e
    #
    # else:
    #     flash('这本书已添加到你的赠送清单或者已存在你的心愿清单，请不要重复添加')
    #
    # return redirect(url_for('web.book_detail',isbn=isbn))




@web.route('/gifts/<gid>/redraw')
@login_required
def redraw_from_gifts(gid):
    gift = Gift.query.filter_by(id=gid,lauched=False,uid=current_user.id).first_or_404()
    drift = Drift.query.filter_by(gift_id=gid,pending=PendingStatus.Waiting).firt()
    if drift:
        flash('这个礼物正处于交易状态，请先前往鱼漂完成该交易')
    else:
        with db.auto_commit():
            gift.delete()
            current_user.beans -=current_app.config['BEANS_UPLOAD_ONE_BOOK']

    return redirect(url_for('web.my_gifts'))















    # gift = Gift.query.filter_by(id=gid, launched=False).first_or_404()
    # drift = Drift.query.filter_by(gift_id=gid, pending=PendingStatus.waiting).first()
    # if drift:
    #     flash('这个礼物正处于交易状态，请先前往鱼漂完成该交易')
    # else:
    #     with db.auto_commit():
    #         current_user.beans -= current_app.config['BEANS_UPLOAD_ONE_BOOK']
    #         gift.delete()
    # return redirect(url_for('web.my_gifts'))




