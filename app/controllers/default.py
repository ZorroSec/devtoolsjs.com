# from app.pages import Pages
# from app import app
# from flask import render_template
# from flask import redirect
# from flask import url_for
from colorama import Fore

try:
    name = str(input(f"{Fore.LIGHTBLACK_EX}username > "))
    password = str(input(f"{Fore.LIGHTBLACK_EX}password > "))
    with open('data.json', 'w') as data:
        data = data.write('{ "username": "%s", "password": "%s" }'%(name, password))
except:
    pass
