from flask import Flask, json , jsonify, render_template, request, redirect, url_for, flash
import pymysql
from flaskext.mysql import MySQL
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from flask_bcrypt import generate_password_hash
from flask_login import UserMixin


# initializations
app = Flask(__name__)
cors = CORS(app, resources={r"/*": {"origins": "*"}})

mysql = MySQL()
 
# MySQL configurations
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://pro-bit:37124796@158.69.195.94:3306/pro-bit'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Catjuegos(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    titulo = db.Column(db.String(200))