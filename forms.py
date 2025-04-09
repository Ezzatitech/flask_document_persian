from wtforms import Form
from wtforms import (StringField, TextAreaField, IntegerField, BooleanField,
                     RadioField, PasswordField, EmailField, URLField, FileField)
from wtforms.validators import InputRequired, Length, EqualTo, Email, URL


class MyBaseForm(Form):
    class Meta:
        csrf = True  # Enable CSRF


class Register(Form):
    name = StringField('نام و نام خانوادگی', [InputRequired('فیلد نام و نام خانوادگی خالی است')])
    email = StringField('ایمیل', [InputRequired('فیلد ایمیل خالی است'), Email('ایمیل اشتباه است')])
    phone = StringField('شماره موبایل', [Length(min=11,max=11, message='شماره موبایل اشتباه است'),
                                         InputRequired('شماره موبایل را وارد کنید')] )
    password = PasswordField('گذرواژه',
                             [InputRequired('فیلد گذرواژه خالی است'), EqualTo('confirm', message='گذرواژه هماهنگ نیست'),
                              Length(min=8, message='گذرواژه باید 8 نویسه باشد')])
    confirm = PasswordField('تکرار گذرواژه')


class Edit_user(Form):
    name = StringField('نام و نام خانوادگی', [InputRequired('فیلد نام و نام خانوادگی خالی است')])
    email = StringField('ایمیل', [InputRequired('فیلد ایمیل خالی است'), Email('ایمیل اشتباه است')])
    admin = BooleanField('کاربر ادمین')


class Upload_avatar(Form):
    img = FileField(IntegerField('upload'))


class Edit_pass(Form):
    password = PasswordField('گذرواژه',
                             [InputRequired('فیلد گذرواژه خالی است'), EqualTo('confirm', message='گذرواژه هماهنگ نیست'),
                              Length(min=8, message='گذرواژه باید 8 نویسه باشد')])
    confirm = PasswordField('تکرار گذرواژه')


class Login(Form):
    email = StringField('ایمیل', [InputRequired('فیلد ایمیل خالی است'), Email('ایمیل اشتباه است')])
    password = PasswordField('گذرواژه', [InputRequired('فیلد گذرواژه خالی است')])


class Cpassword(Form):
    password = StringField('گذرواژه فعلی', [InputRequired('فیلد گذرواژه فعلی خالی است')])
    password_copy = StringField('گذرواژه جدید', [InputRequired('فیلد گذرواژه جدید خالی است'),
                                                 Length(min=8, message='گذرواژه باید 8 کاراکتر باشد')])


class Create_post(Form):
    title = StringField('عنوان', [InputRequired('عنوان را وارد کنید')])
    content = TextAreaField('توضیحات', validators=[InputRequired('فیلد توضیحات خالی است')])
    link = StringField('آدرس پست', [InputRequired('آدرس پست را وارد کنید')])


class Create_category(Form):
    title = StringField('عنوان دسته بندی', [InputRequired('عنوان دسته بندی را وارد کنید')])
    title_lotin = StringField('عنوان لاتین', [InputRequired('عنوان لاتین را وارد کنید')])
    slug = StringField('آدرس دسته بندی', [InputRequired('آدرس دسته بندی را وارد کنید')])
    price = IntegerField('قیمت آموزش به تومان', [InputRequired('قیمت را وارد کنید')])


