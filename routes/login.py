from config import app, bcrypt, db
from flask import render_template, request, redirect, url_for, flash, Blueprint
from forms import Register, Login
from flask_login import current_user, login_user, logout_user, login_required
from models import User
from config import ext


users_bp = Blueprint('users', __name__)


@users_bp.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('home.home'))

    form = Login(request.form)

    if request.method == 'POST' and form.validate():
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user)
            next_page = request.args.get('next')
            flash('شما با موفقیت وارد شدید', 'success')
            return redirect(next_page if next_page else url_for('home.home'))
        else:
            flash('ایمیل یا گذرواژه اشتباه است', 'danger')
            return redirect(url_for('users.login'))

    return render_template('login.html', form=form)


@users_bp.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('home.home'))

    form = Register(request.form)

    if request.method == 'POST' and form.validate():
        hashed = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        email = User.query.filter_by(email=form.email.data).first()
        if not email:
            user = User(name=form.name.data, email=form.email.data, password=hashed, mobile_number=form.phone.data)
            db.session.add(user)
            db.session.commit()
            flash('شما با موفقیت ثبت نام کردید', 'info')
            return redirect(url_for('users.login'))
        else:
            flash('ایمیل وارد شده قبلا در سیستم ثبت شده است', 'danger')
            return redirect(url_for('users.register'))

    return render_template('register.html', form=form)


@users_bp.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('users.login'))


@users_bp.route('/profile', methods=['POST', 'GET'])
@login_required
def profile():
    form = Register(request.form)
    user = User.query.get_or_404(current_user.id)

    if request.method == 'POST' and form.validate():
        user.name = form.name.data
        user.mobile_number = form.phone.data
        db.session.commit(user)
        flash('اطلاعات با موفقیت تغییر کرد', 'info')
        return redirect(url_for('users.profile'))

    return render_template('profile.html', form=form)


@ext.register_generator
def logine():
    yield 'users.login', {}

@ext.register_generator
def regi():
    yield 'users.register', {}