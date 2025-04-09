from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_wtf.csrf import CSRFProtect
from flask_sitemap import Sitemap
from flask_migrate import Migrate

# App
app = Flask(__name__)
ext = Sitemap(app=app)


# Secret_Key
app.secret_key = '194d1746a5ce02a18vcab2a4269235cd'

# Db
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:''@localhost:3306/doc_persian'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
migrate = Migrate(app, db)


from models import User


# Password-Hash
bcrypt = Bcrypt(app)

# Flask-Login
login_manager = LoginManager(app)
login_manager.login_view = 'users.login'
login_manager.login_message = 'برای وارد شدن اطلاعات خود را وارد کنید'
login_manager.login_message_category = 'info'


# Flask_Login
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)

# CSRF
csrf = CSRFProtect(app)

