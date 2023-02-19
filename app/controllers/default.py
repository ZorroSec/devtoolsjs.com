from app.pages import Pages
from app import app
from flask import render_template
from flask import redirect
from flask import url_for
from colorama import Fore
from json import loads, load, dump

name = input(f"{Fore.LIGHTBLACK_EX} username > ")
passw = input(f"{Fore.LIGHTBLACK_EX} password > ")
with open("data.json", 'w') as file:
    dump({ "username": f"{name}", "password": f"{passw}" }, file)

@app.route('/')
def home():
    return config.homep()
