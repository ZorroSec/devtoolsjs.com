from app import app
from flask import render_template
from flask import redirect
from flask import url_for
from flask import request
from colorama import Fore
from json import loads, load, dump

@app.route('/', methods=['GET', 'POST'])
def home():
    with open('data.json', 'r') as f:
        data = load(f)
    return render_template('iindx.html', user=data['username'])



@app.route('/login', methods=['GET','POST'])
def login():
    if request.method == 'POST':
        name = request.form.get('name')
        password = request.form.get('pass')
        with open('data.json', 'w') as f:
            dump(
                {
                    "username": f"{name}",
                    "password": f"{password}"
                },
                f
            )
        return render_template('login.html', user=name)
    
    return render_template('login.html')