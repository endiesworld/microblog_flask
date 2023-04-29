import os

basedir = os.path.abspath(os.path.dirname(__file__))
sub_dir = os.path.join(basedir, 'app')
sqlite_db = 'sqlite:///' + os.path.join(sub_dir, 'db','app.db')

class GlobalConfig(object):
    """Global configurations."""
    
    SECRET_KEY =  os.environ.get('SECRET_KEY', 'Super-dupper-secret')
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL', sqlite_db)
    SQLALCHEMY_TRACK_MODIFICATIONS = False