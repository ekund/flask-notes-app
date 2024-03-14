from flask import render_template
from app import app
from app.forms import LoginForm
from app import db
from app.models import Users

@app.route('/')
@app.route('/index')
def index():
    user = {'username': Users.query.all()[0].name}
    return render_template('index.html', title='Home', user=user)

@app.route('/login')
def login():
    form = LoginForm()
    return render_template('login.html', title='Sign In', form=form)
