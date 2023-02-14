
from flask import jsonify, request, current_app, url_for, render_template, flash
from book.forms.book import SearchForm
import json


from book.spider.search import Yushubook

from . import web


from ..libs.search_style import is_isbn_or_key
from ..view_modlels.book import BookCollection,BookViewModel




@web.route('/book/search')
def search():
    """
        q :普通关键字 isbn
        page
        ?q=金庸&page=1
    """

    form = SearchForm(request.args)
    books = BookCollection()

    if form.validate():
        q = form.q.data.strip()
        page = form.page.data
        isbn_or_key = is_isbn_or_key(q)
        yushu_book = Yushubook()

        if isbn_or_key == 'isbn':
            yushu_book.search_by_isbn(q)
        else:
            yushu_book.search_by_keyword(q, page)

        books.fill(yushu_book, q)
    else:
        flash('搜索的关键字不符合要求，请重新输入关键字')
        # return jsonify(form.errors)
    # current_app.logger.info("user: " + q + " Login")
    return render_template('search_result.html', books=books)


@web.route('/book/<isbn>/detail')
def book_detail(isbn):
    yushu_book =Yushubook()
    yushu_book.search_by_isbn(isbn)
    book = BookViewModel(yushu_book.first)
    return render_template("book_detail.html",book=book,wishes=[],gifts=[])





