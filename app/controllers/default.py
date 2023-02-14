from app.pages import Pages
from app import app
from flask import render_template
from flask import redirect
from flask import url_for
from colorama import Fore
from json import loads, load, dump
config = Pages(name, password)


@app.route('/')
def home():
    return config.homep()
