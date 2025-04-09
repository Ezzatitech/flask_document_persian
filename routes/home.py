from config import app, bcrypt, db
from flask import render_template, request, redirect, url_for, flash, Blueprint
from forms import Register, Login
from flask_login import current_user, login_user
from models import Post, Category
from flask_paginate import Pagination, get_page_parameter
from config import ext

home_bq = Blueprint('home', __name__)



@home_bq.route('/')
def home():
    category_all = Category.query.all()
    category = Category.query.order_by(Category.date.desc()).limit(4).all()
    post = Post.query.order_by(Post.date.desc()).limit(4).all()
    return render_template('index.html', post=post, category=category, category_all=category_all)


@home_bq.route('/post/<string:post_link>')
def post_get(post_link):
    post = Post.query.filter_by(link = post_link).first_or_404()
    category = Category.query.get_or_404(post.cat_id)
    category_all = Category.query.all()
    post_all = Post.query.filter_by(cat_id=category.id).all()
    return render_template('single_post.html', category=category, post=post, post_all=post_all)


@home_bq.route('/documents')
def documents():
    per_page = 10
    page = request.args.get(get_page_parameter(), type=int, default=1)
    start = (page - 1) * per_page
    end = start + per_page
    category = Category.query.offset(start).limit(per_page).all()
    total = Category.query.count()
    pagination = Pagination(page=page, total=total, per_page=per_page)

    return render_template('category_all.html', category=category, pagination=pagination)



@ext.register_generator
def home():
    yield 'home.home', {}


@ext.register_generator
def post():
    post = Post.query.all()
    for item in post:

        yield 'home.post_get', {'post_link': item.link}


@ext.register_generator
def doc():
    yield 'home.documents', {}

