# -*- encoding:utf-8 -*-
from flask_sqlalchemy import SQLAlchemy
from flask import Flask
import config
from datetime import datetime

app = Flask(__name__)
app.config.from_object(config.config_dict['config'])
db = SQLAlchemy(app)

class Base(object):
    create_time = db.Column(db.DATETIME,default=datetime.now())
    update_time = db.Column(db.DATETIME,default=datetime.now())

class Admin(Base,db.Model):
    __tablename__ = 'admin'
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(20),nullable=False)
    pass_hash = db.Column(db.String(200),nullable=False)

class User(Base,db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    nick_name = db.Column(db.String(20),index=True)
    password_has = db.Column(db.String(200), nullable=False)
    mobile = db.Column(db.String(200), nullable=False)
    avatar_url = db.Column(db.String(256))
    last_login = db.Column(db.DATETIME)
    signature = db.Column(db.String(512))
    gender = db.Column(db.String(10),default='Man',nullable=False)

class Category(Base,db.Model):
    __tablename__ = 'category'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30))

class News(Base,db.Model):
    __tablename__ = 'news'
    id = db.Column(db.Integer,primary_key=True)
    title = db.Column(db.String(30))
    source = db.Column(db.String(30))
    index_image_url = db.Column(db.String(100))
    digest = db.Column(db.String(255))
    clicks = db.Column(db.Integer)
    content = db.Column(db.TEXT)
    category_id = db.Column(db.Integer,db.ForeignKey('category.id'))
    user_id = db.Column(db.Integer,db.ForeignKey('user.id'))
    status = db.Column(db.Integer)
    reason = db.Column(db.String(100))

class User_collection(db.Model):
    __tablename__ = 'user_collection'
    id = db.Column(db.Integer,primary_key=True)
    user_id = db.Column(db.Integer)
    news_id = db.Column(db.Integer)

class Comment(db.Model):
    __tablename__ = 'comment'
    id = db.Column(db.Integer,primary_key=True)
    news_id = db.Column(db.Integer)
    user_id = db.Column(db.Integer)
    content = db.Column(db.String(255))

if __name__ == '__main__':
    # db.create_all()
    app.run()