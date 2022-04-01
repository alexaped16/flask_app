from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from config import Config 
from flask_login import LoginManager

app = Flask(__name__)
app.config.from_object(Config)


db = SQLAlchemy(app)
migrate = Migrate(app, db, render_as_batch=True)

login = LoginManager(app)
login.login_view = 'login'
login.login_message_category = 'danger'

from app.blueprints.auth import auth
app.register_blueprint(auth)

from app.blueprints.site import site
app.register_blueprint(site)

from app import routes, models
