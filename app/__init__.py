from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager

from app.core import global_config

app = Flask(__name__)
app.config.from_object(global_config.GlobalConfig)
database = SQLAlchemy(app)
migrate = Migrate(app, database)
login = LoginManager(app)
login.login_view = 'login'

from app import  routes, models
