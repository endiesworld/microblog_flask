from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

from app.core import global_config

app = Flask(__name__)
app.config.from_object(global_config.GlobalConfig)
db = SQLAlchemy(app)
migrate = Migrate(app, db)
    

from app import routes, models
