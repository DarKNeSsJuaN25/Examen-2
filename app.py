from crypt import methods
from html import entities
from turtle import back
from flask import Flask, render_template, request, jsonify, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
import sys
from sqlalchemy import sql

def suma(x,y):
    return x + y
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:Softjuandius_25@localhost:5432/software3'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Usuario(db.Model):
    __tablename__ = 'usuario'
    id = db.Column(db.Integer,primary_key=True)
    nombre = db.Column(db.String(80), nullable=False)
    contraseña = db.Column(db.String(80), nullable=False)
    tipo = db.Column(db.String(80),nullable=False)



class Mensaje(db.Model):
    __tablename__ = 'mensajes'
    id = db.Column(db.Integer,primary_key = True)
    texto = db.Column(db.String(100),nullable = False)
    topico = db.Column(db.String(80),nullable = False)


db.create_all()

@app.route('/subscriber')
def subs():
    return render_template("subscriber.html")

@app.route('/publisher')
def pub():
    return render_template("publisher.html")

#LOGEAR USUARIOS
@app.route('/authenticate', methods=['POST'])
def authenticate_user():
    tipo = request.get_json()['tipo']
    return render_template("index.html")

@app.route('/set_informacion',methods = ['POST'])
def set_info():
    try:
        texto = request.get_json()['informacion']
        topico = request.get_json()['topico']
        mensaje = Mensaje(texto = texto, topico = topico)
        db.session.add(mensaje)
        db.session.commit()
    except:
        db.session.rollback()

    return render_template("index.html")

'''
@app.route('/test',methods=['GET'])
def probar_test():
    db_session = db.getSession()
    user = entities.Usuario(
        username = "dion",
        password = "0"
    )
'''





@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(port=5003, debug=True)
else:
    print('using global variables from FLASK')