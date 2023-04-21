import os

basedir = os.path.abspath(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
sqlite_db = 'sqlite:///' + os.path.join(basedir, 'db','app.db')

class GlobalConfig(object):
    """Global configurations."""
    
    SECRET_KEY =  os.environ.get('SECRET_KEY', 'Super-dupper-secret')
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL', sqlite_db)
    SQLALCHEMY_TRACK_MODIFICATIONS = False