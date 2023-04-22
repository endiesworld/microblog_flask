from flask import render_template
from flask_login import login_required
from app import app

@app.route('/')
@app.route('/index')
@login_required
def index():
    user = {"username": "Emmanuel"}
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
    return render_template('index.html', title="Home", user=user, posts=posts)
        
