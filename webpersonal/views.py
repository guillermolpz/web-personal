from ast import Return
#from webpersonal import app
from flask import render_template, Blueprint

base = Blueprint('base', __name__)

@base.route('/')
@base.route('/home')
def home():
    return render_template('inicio.html')

@base.route('/portafolio')
def portafolio():
    return render_template('portafolio.html')

@base.route('/contacto')
def contacto():
    return render_template('contacto.html')

"""
@app.route('/')
@app.route('/home')
def home():
    return render_template('inicio.html')

@app.route('/portafolio')
def portafolio():
    return render_template('portafolio.html')

@app.route('/contacto')
def contacto():
    return render_template('contacto.html')
"""