from app.pages import Pages
from app import app
from flask import render_template
from flask import redirect
from flask import url_for
from colorama import Fore
from json import loads, load, dump

try:
    name = str(input(f"{Fore.LIGHTBLACK_EX}username > "))
    password = str(input(f"{Fore.LIGHTBLACK_EX}password > "))
    with open('data.json', 'w') as data:
        data = data.write('{ "username": "%s", "password": "%s" }'%(name, password))
except KeyboardInterrupt as e:
    print(f"{Fore.LIGHTRED_EX}Error {e}")


config = Pages(name, password)


@app.route('/')
def home():
    return config.homep()
