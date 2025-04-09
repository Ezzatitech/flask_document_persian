from sqlalchemy import Column, Integer, String, Boolean
from config import db
from flask_login import UserMixin
import datetime

class User(db.Model, UserMixin):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    email = Column(String(100), unique=True, nullable=False)
    password = Column(String(100), nullable=False)
    is_admin = Column(Boolean, default=False)
    mobile_number = Column(String(20), nullable=True)

    def __repr__(self):
        return f"User(id={self.id}, name={self.name}, email={self.email}, is_admin={self.is_admin})"


class Category(db.Model):
    __tablename__ = 'categorys'

    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    name_lotin = Column(String(50), nullable=False)
    link = Column(String(128), unique=True, nullable=False)
    date = db.Column(db.DateTime, nullable=False, default=datetime.datetime.now)
    update = db.Column(db.DateTime, nullable=False, default=datetime.datetime.now, onupdate=datetime.datetime.now)
    price = db.Column(db.Integer, nullable=False, default=0)
    students = db.Column(db.Integer, db.ForeignKey(User.id), nullable=True)
    content = db.Column(db.Text, nullable=True)
    url = Column(String(320), nullable=True)

    def __repr__(self):
        return f"Category(id={self.id}, name={self.name}, name_lotin={self.name_lotin}, link={self.link})"


class Post(db.Model):
    __tablename__ = 'posts'

    cat_id = db.Column(db.Integer, db.ForeignKey(Category.id), nullable=False)
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(120), nullable=False)
    date = db.Column(db.DateTime, nullable=False, default=datetime.datetime.now)
    update = db.Column(db.DateTime, nullable=False, default=datetime.datetime.now, onupdate=datetime.datetime.now)
    link = db.Column(db.String(120), unique=True, nullable=False)
    content = db.Column(db.Text, nullable=False)

    def __repr__(self):
        return f"Category(id={self.id}, name={self.name}, name_lotin={self.name_lotin}, link={self.link})"







