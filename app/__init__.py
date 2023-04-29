from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager

from global_config import GlobalConfig

# app = Flask(__name__)
# app.config.from_object(global_config.GlobalConfig)
# database = SQLAlchemy(app)
# migrate = Migrate(app, database)
# login = LoginManager(app)
# login.login_view = 'login'

database = SQLAlchemy()
migrate = Migrate()
login = LoginManager()
login.login_view = 'auth.login'

# from app import  models
# from app.routes.login import login
# from app.routes.index import index
# from app.routes.signup import signup
# from app.routes.logout import logout

def create_app(config_class=GlobalConfig):
    app = Flask(__name__)
    app.config.from_object(config_class)

    database.init_app(app)
    migrate.init_app(app, database)
    login.init_app(app)
    
    from app.auth import bp as auth_bp
    app.register_blueprint(auth_bp, url_prefix='/auth')
    
    from app.main import bp as main_bp
    app.register_blueprint(main_bp)
    
    return app

from app import models