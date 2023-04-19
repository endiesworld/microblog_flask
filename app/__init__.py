from flask import Flask
from app.core import global_config

app = Flask(__name__)
app.config.from_object(global_config.GlobalConfig)
    

from app.routes import index, login
