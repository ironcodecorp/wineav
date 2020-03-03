
import os
from flask import Flask, session, render_template
from flask import Blueprint
from .import *
app = Flask(__name__)

cat_juegos_admin = Blueprint('cat_juegos_admin',__name__)

@cat_juegos_admin.route('/')
def cat_juegos_admin():
    return render_template('admin/index.html')

@cat_admin.route('/nuevo')
def login_admin():
    return render_template('admin/login.html')  