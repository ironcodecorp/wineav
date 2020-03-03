
import os
import random
from flask import Flask, session, render_template, request, jsonify, session, redirect
from flask import Blueprint
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from slugify import slugify
from .import *
app = Flask(__name__)

from models.juegos import Juegos, Respuestas
from models.juegos import Catjuegos

admin_index = Blueprint('admin_index',__name__)
juegos_admin = Blueprint('juegos_admin',__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://pro-bit:37124796@158.69.195.94:3306/pro-bit'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
engine = create_engine('mysql+pymysql://pro-bit:37124796@158.69.195.94:3306/pro-bit', echo=True)
db = SQLAlchemy(app)
#index_admin = Blueprint('index_admin',__name__)

@admin_index.route('/login')
def login_admin():
    return render_template('admin/login.html')

@admin_index.route('/registro')
def registro_admin():
    return render_template('admin/registro.html')      

@admin_index.route('/nuevo-juego')
def nuevo_juego_admin():
    Session = sessionmaker(bind=engine)
    s = Session()
    querys = s.query(Catjuegos.titulo, Catjuegos.id).all()
    if querys:
        return render_template('admin/nuevo_juego.html', categorias = querys)    

@admin_index.route('/juegos', methods=['GET'])
def juegos_admin():
    Session = sessionmaker(bind=engine)
    s = Session()
    juegos = s.query(Juegos.titulo, Juegos.id,Juegos.contexto, Juegos.slug, Juegos.codigo).order_by(Juegos.id.desc()).all()
    if juegos:
        return render_template('admin/juegos.html', juegos = juegos)
    return "mal"

@admin_index.route('/nuevo/alta', methods=['POST'])
def grabo_nuevo_juego_admin():
    with app.app_context():
        id = random.randint(1,101)
        cod = random.randint(1,101)
        jgo = "jgo-" + str(cod)
        txt = slugify(request.form['titulo'])
        txt = txt + '-' + str(id)
        #self.assertEqual(r, "this-is-a-test")
        nuevo_juego = Juegos(titulo =  request.form['titulo'], 
        contexto =  request.form['contexto'], 
        slug =  txt, codigo = jgo)
        db.session.add(nuevo_juego) 
        db.session.commit()
        #return redirect('/admin/juegos')
        #return add_pregunta_admin(jgo)
        return redirect('/admin/add-pregunta/'+jgo)
        return render_template('admin/add-pregunta.html', codigo = jgo) 
        #for resp in request.form:
        #    nueva_respuesta = Respuestas(juego_id = 0, 
        #    respuesta =  request.form['respuesta1'], correcta = request.form['correcta'])
        #    print(nueva_respuesta.respuesta)
        #    db.session.add(nueva_respuesta) 
        #    db.session.commit()
        #return jsonify({'status': "alta ok"})   
        #return render_template('web/index.html')
        #return render_template('admin/juegos.html') 
        return redirect('/admin/juegos')
        return jsonify({'status': "alta ok"})      


@admin_index.route('/add-pregunta/<jgo>', methods=['GET'])
def add_pregunta_admin(jgo):
    #return(jgo)
    #print(jgo)
    Session = sessionmaker(bind=engine)
    s = Session()
    query = s.query(Juegos).filter(Juegos.codigo.in_([jgo]))
    result = query.first()
    #print (result)
    if result:
        return render_template('admin/add-pregunta.html', juego = result) #, categorias = querys
    return "error"    

@admin_index.route('/add-pregunta/preguntas/guardar', methods=['POST'])
def grabo_respuesta_juego_admin():
    with app.app_context():
        if request.form['correcta'] != 0:
            print(request.form)
            jgo=request.form['codigo']
            txt = slugify(request.form['respuesta'])
            #self.assertEqual(r, "this-is-a-test")
            nueva_respuesta = Respuestas(juego_id =  request.form['id'], 
            resp1 =  request.form['respuesta'],
            resp2 =  request.form['respuesta1'],
            resp3 =  request.form['respuesta2'],
            correcta =  request.form['correcta'],  
            pregunta =  request.form['pregunta'])
            db.session.add(nueva_respuesta) 
            db.session.commit()
            #return redirect('/admin/juegos')
            #return add_pregunta_admin(jgo)
            return redirect('/admin/add-pregunta/'+jgo)
        return jsonify({'status': "falto ingresar una respuesta correcta"})      


@admin_index.route('/')
def index_admin():
    return render_template('admin/index.html')        