from config import app, ext
from routes.login import users_bp
from routes.home import home_bq
from routes.admin import admin_bq


app.register_blueprint(home_bq)
app.register_blueprint(users_bp, url_prefix='/users')
app.register_blueprint(admin_bq, url_prefix='/admin')


if __name__ == '__main__':
    app.run(debug=True)
