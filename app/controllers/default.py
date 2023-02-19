from app import app
from flask import render_template
from flask import redirect
from flask import url_for
from flask import request
from colorama import Fore
from json import loads, load, dump

@app.route('/', methods=['GET', 'POST'])
def home():
    return render_template('iindx.html', user='zorro')

@app.route('/login', methods=['GET', 'POST'])
def login():
    name = request.form.get('name')
    password = request.form.get('password')
    return render_template('login.html', user=name)