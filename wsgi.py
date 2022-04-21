#!/usr/bin/env python3

from flask import Flask, render_template, request, redirect, flash
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from werkzeug.security import generate_password_hash, check_password_hash
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired
from time import sleep

app = Flask(__name__)
app.config.from_object(Config)

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Sign In')

@app.route("/")
def root():
    return redirect("/login")

@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
#    if form.validate_on_submit():
    flash('Login requested for user {}, remember_me={}'.format(form.username.data, form.remember_me.data))
    return redirect('/login-results')
    #elif not form.validate_on_submit():
    #    return redirect('/login')
    #    pass
    return render_template("login.html", form=form)

@app.route("/login-results")
def login_results():
    return render_template("login-results.html")

@app.route("/register")
def register():
    return render_template("registration.html")

@app.route("/registration-error")
def regerror():
    return render_template("registration-failure.html")

@app.route("/registration-success")
def regsuccess():
    return render_template("registration-success.html")
