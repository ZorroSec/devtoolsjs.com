from flask import render_template
from flask import request
from flask import redirect
from flask import url_for
from app import app

class Pages:
    def __init__(self, name, password):
        self.name = name
        self.password = password
    
    def homep(self):
        return render_template('iindx.html')