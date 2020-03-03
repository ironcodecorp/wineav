from flask import Flask, json , jsonify, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from flask_bcrypt import generate_password_hash
from flask_login import UserMixin
from slugify import slugify


# initializations
app = Flask(__name__)
cors = CORS(app, resources={r"/*": {"origins": "*"}})

 
# MySQL configurations
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://pro-bit:37124796@158.69.195.94:3306/pro-bit'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Juegos(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    codigo = db.Column(db.String(8))
    titulo = db.Column(db.String(200))
    slug = db.Column(db.String(200))
    contexto = db.Column(db.Text())
    jugado = db.Column(db.Integer, default=0)
    pregunta = db.Column(db.String(255))

class Respuestas(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    juego_id = db.Column(db.Integer)
    pregunta = db.Column(db.String(255))
    resp1 = db.Column(db.String(255))
    resp2 = db.Column(db.String(255))
    resp3 = db.Column(db.String(255))
    correcta = db.Column(db.String(1))

class Catjuegos(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    titulo = db.Column(db.String(200))
    slug = db.Column(db.String(200))
    descripcion = db.Column(db.Text())

    def __repr__(self):
        return "<id(id='%s', titulo='%s')>" % (self.id, self.titulo)    
