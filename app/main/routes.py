from flask import render_template
from flask_login import login_required
from app.main import bp

@bp.route('/')
@bp.route('/index')
@login_required
def index():
    posts = [
        {
            'author': {"username": "Adaobi"},
            'body': "Home made cake"
        },
        {
            'author': {"username": "Chidubem"},
            'body': "How to build a game with scratch"
        }
    ]
    return render_template('index.html', title="Home Page", posts=posts)
        
