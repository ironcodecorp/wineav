
import os
from flask import Flask, session, render_template, request, session
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from flask import Blueprint
from .import *
app = Flask(__name__)

juegos_admin = Blueprint('juegos_admin',__name__)
cat_juegos_admin = Blueprint('cat_juegos_admin',__name__)

from models.juegos import Juegos

@juegos_admin.route('/')
def index_admin():
    return render_template('admin/index.html')



@juegos_admin.route('/nuevo')
def login_admin():
    return render_template('admin/login.html')   


@juegos_admin.route('/nuevo/alta', methods=['POST'])
def nuevo_juego_admin():
    with app.app_context():
        nuevo_juego = Juegos('titulo', request.form['titulo'])
        print(request.form['titulo'])
        db.session.add(nuevo_juego)
        db.session.commit()
        #return jsonify({'status': "alta ok"})   
        #return render_template('web/index.html')
        return redirect('/')
        return jsonify({'status': "alta ok"})   
    return render_template('admin/login.html')   

@cat_juegos_admin.route('/')
def cat_index_juegos_admin():
    return render_template('admin/index.html')

  