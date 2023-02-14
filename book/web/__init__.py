
from flask import Blueprint

web = Blueprint('web', __name__)

from book.web import book
from book.web import drift
from book.web import gift
from book.web import main
from book.web import wish
from book.web import auth
