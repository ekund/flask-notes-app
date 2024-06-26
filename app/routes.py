from flask import render_template
from app import app
from app.forms import LoginForm
from app import db
from app.forms import RegistrationForm
from app.models import Users
from flask_login import login_required, current_user, login_user, logout_user
import sqlalchemy as sa
from flask import flash, redirect, render_template, url_for, request
from urllib.parse import urlsplit

@app.route('/')
@app.route('/index')
@login_required
def index():
    # TODO: read notes from DB
    notes=[{"text": "note1", "date": "20240201", "text": "note2"}, {"text": "note2", "date": "20240301"}]
    return render_template('index.html', title='Home', notes=notes)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
        user = db.session.scalar(
            sa.select(Users).where(Users.username == form.username.data))
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password')
            return render_template('login.html', title='Sign In', form=form)
        login_user(user, remember=form.remember_me.data)
        next_page = request.args.get('next')
        if not next_page or urlsplit(next_page).netloc != '':
            return redirect(url_for('index'))
    return render_template('login.html', title='Sign In', form=form)

@app.route('/logout')
def logout():
    logout_user()
    request.args
    return redirect(url_for('login'), code=302)

@app.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = RegistrationForm()
    if form.validate_on_submit():
        user = Users(username=form.username.data, email=form.email.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Congratulations, you are now a registered user!')
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)

