from flask import render_template, flash, redirect, url_for, request
from flask_login import current_user, login_user
from werkzeug.urls import url_parse

from app import app, database as db
from app.forms.signup_form import SignUpForm
from app.models import User


@app.route('/signup', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    
    form = SignUpForm()
    
    if form.validate_on_submit():
        user = User(username=form.username.data, email=form.email.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Congratualtions, you are now a registered user')
        return redirect(url_for('login'))
    
    return render_template('signup.html', title="Sign up", form=form)
     