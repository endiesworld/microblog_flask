from app import app, database 
from app.models import  *

@app.shell_context_processor
def make_shell_context():
    return {"db": database,
            "User": User,
            "Post": Post
            }