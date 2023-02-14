'''应用级别的初始化__init__文件'''
import logging
from logging.handlers import TimedRotatingFileHandler

from flask import Flask
from book.web.book import web
from book.modles.book import db

def create_app():
    app = Flask(__name__)
    app.config.from_object('book.secure')
    app.config.from_object('book.setting')
    register_blueprint(app)
    db.init_app(app)
    db.create_all(app=app)
    formatter = logging.Formatter(

        "[%(asctime)s][%(filename)s:%(lineno)d][%(levelname)s][%(thread)d] - %(message)s")

    handler = TimedRotatingFileHandler(

        "flask.log", when="D", interval=1, backupCount=15,

        encoding="UTF-8", delay=False, utc=True)

    app.logger.addHandler(handler)

    handler.setFormatter(formatter)
    return app
# '''创建flaskapp'''

def register_blueprint(app):
    app.register_blueprint(web)


