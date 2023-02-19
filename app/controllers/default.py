from app import app
from flask import render_template
from flask import redirect
from flask import url_for
from colorama import Fore
from json import loads, load, dump

@app.route('/', methods=['GET', 'POST'])
def home():
    return render_template('iindx.html')
