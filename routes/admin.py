from config import app, bcrypt, db
from flask import render_template, request, redirect, url_for, flash, Blueprint
from forms import Create_category, Create_post
from flask_login import current_user, login_user, login_required
from models import Category, User, Post
from flask_paginate import Pagination, get_page_parameter

admin_bq = Blueprint('admin', __name__)


@admin_bq.before_request
@login_required
def before_request():
    if current_user.is_admin == 0:
        return redirect(url_for('home.home'))


@admin_bq.route('/')
def admin():
    return render_template('admin/admin.html')


@admin_bq.route('/create_category', methods=['POST', 'GET'])
def admin_category():
    form = Create_category(request.form)
    if request.method == 'POST' and form.validate():
        category = Category(name=form.title.data, name_lotin=form.title_lotin.data, link=form.slug.data,
                            price=form.price.data)
        db.session.add(category)
        db.session.commit()
        flash('دسته بندی با موفقیت ایجاد شد', 'Success')
        return redirect(url_for('admin.admin_category'))

    return render_template('admin/create_category.html', form=form)


@admin_bq.route('/edit_category/<int:cat_id>', methods=['POST', 'GET'])
def admin_category_edit(cat_id):
    form = Create_category(request.form)
    category = Category.query.get_or_404(cat_id)
    if request.method == 'POST' and form.validate():
        category.name = form.title.data
        category.content = request.form.get('text_cat')
        category.name_lotin = form.title_lotin.data
        category.link = form.slug.data
        category.url = request.form.get('url_cat')
        category.price = form.price.data
        db.session.commit()
        flash('دسته بندی با موفقیت بروزرسانی شد', 'info')
        return redirect(url_for('admin.admin_category_edit', cat_id=category.id))

    return render_template('admin/edit_category.html', form=form, category=category)


@admin_bq.route('/all_category')
def admin_all_category():
    category = Category.query.all()
    return render_template('admin/all_category.html', category=category)


@admin_bq.route('/category_delete/<int:cat_id>')
def admin_category_delete(cat_id):
    category = Category.query.get_or_404(cat_id)
    db.session.delete(category)
    db.session.commit()
    flash('دسته بندی حذف شد', 'danger')
    return redirect(url_for('admin.admin_all_category'))


@admin_bq.route('/create_post', methods=['POST', 'GET'])
def admin_create_post():
    form = Create_post(request.form)
    category = Category.query.all()
    if request.method == 'POST' and form.validate():
        category = request.form.get('category_id')
        post_filter = Post.query.filter_by(link=form.link.data).first()
        if category.isdigit():

            post = Post(cat_id=category, title=form.title.data, link=form.link.data, content=form.content.data)
            if not post_filter:
                db.session.add(post)
                db.session.commit()
                flash('پست با موفقیت ایجاد شد', 'info')
                return redirect(url_for('admin.admin_create_post'))
            else:
                flash('لینک قبلا وارد شده!', 'danger')
        else:
            flash('دسته بندی را انتخاب کنید', 'danger')
            return redirect(url_for('admin.admin_create_post'))

    return render_template('admin/create_post.html', form=form, category=category)


@admin_bq.route('/edit_post/<int:post_id>', methods=['POST', 'GET'])
def admin_edit_post(post_id):
    form = Create_post(request.form)
    category_all = Category.query.all()
    post = Post.query.get_or_404(post_id)
    content = request.form.get('content')

    if request.method == 'POST' and form.validate():
        post.cat_id = request.form.get('category_id')
        post.title = form.title.data
        post.link = form.link.data
        post.content = content
        db.session.commit()
        flash('پست بروزرسانی شد', 'info')
        return redirect(url_for('admin.admin_edit_post', post_id=post.id))

    return render_template('admin/edit_post.html', form=form, post=post, category_all=category_all)


@admin_bq.route('/posts')
def admin_posts():
    page = request.args.get(get_page_parameter(), type=int, default=1)
    per_page = 10  # تعداد آیتم‌ها در هر صفحه
    post = Post.query.paginate(page=page, per_page=per_page)
    pagination = Pagination(page=page, total=post.total, per_page=per_page)
    return render_template('admin/posts.html', post=post, pagination=pagination)


@admin_bq.route('/delete_post/<int:id_post>')
def admin_delete_post(id_post):
    post = Post.query.get_or_404(id_post)
    db.session.delete(post)
    db.session.commit()
    flash('پست با موفقیت حذف شد', 'danger')
    return redirect(url_for('admin.admin_posts'))



































