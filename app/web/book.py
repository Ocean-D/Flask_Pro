from flask import jsonify,request,render_template,flash
import json
from app.forms.book import SearchForm
from app.libs.helper import is_isbn_or_key
from app.spider.yushu_book import YuShuBook
from app.viwe_models.book import  BookCollection,BookViewModel

from . import web

@web.route('/book/search')
def search():
    '''
    q:普通子搜索 isbn
    page
    isbn13 与  isbn10  是有短横线_
     '''

    form = SearchForm(request.args)
    books = BookCollection()
    if form.validate():
        q = form.q.data.strip()
        page = form.page.data
        isbn_or_key = is_isbn_or_key(q)
        yushu_book = YuShuBook()
        if isbn_or_key == 'isbn':
            yushu_book.search_by_isbn(q)
        else:
            yushu_book.search_by_keyword(q,page)
        books.fill(yushu_book,q)


        # return json.dumps(books.__dict__, default=lambda o: o.__dict__)
    else:
        flash('搜索的关键字不符合要求，请重新输入关键字')
        # return jsonify(form.errors)
    return render_template('search_result.html', books=books)


@web.route('/book/<isbn>/detail')
def book_detail(isbn):
    yushu_book=YuShuBook()
    
    book = BookViewModel(yushu_book.books[0])


    pass









@web.route('/test')
def test():
    r={
        "name":'',
        "age": 15,
    }
    return render_template('test.html',r=r)


