import os

class GlobalConfig(object):
    """Global configurations."""
    SECRET_KEY =  os.environ.get('SECRET_KEY', "Super-dupper-secret")