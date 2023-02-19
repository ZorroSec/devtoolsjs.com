from app import app
from flask import render_template
from flask import redirect
from flask import url_for
from colorama import Fore
from json import loads, load, dump

if __name__ == "__main__":
    app.run(
        debug=True,
        host='localhost',
        port=3000
    )