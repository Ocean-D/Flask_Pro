


from flask_login import login_required
from . import web


@web.route('/my/gifts')

def my_gifts():
    pass


@web.route('/gifts/book/<isbn>')
@login_required
def save_to_gifts(isbn):
    pass


@web.route('/gifts/<gid>/redraw')
def redraw_from_gifts(gid):
    pass



