from flask import Blueprint, render_template, request, redirect
from database.database import conn_db

userView = Blueprint("user_routs", __name__, render_template = './../templates')
connDb = conn_db()

@userView.route('/login', methods = ['GET','POST'])
def login():
    data = request.form
    #a faire ....

@userView.route('/signin', methods = ['GET', 'POST'])
def signin():
    data = request.form

@userView.route('/profile', methods= ['GET'])
def profile():
    #a faire 
    pass

@userView.route('/edit', methods = ['POST'])
def edit():
    data = request.form

@userView.route('/logout', methods = ['GET'])
def logout():
    pass
