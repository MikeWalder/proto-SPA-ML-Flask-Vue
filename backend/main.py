from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
import json
import requests
from flask_cors import CORS
from input import *

# configuration
DEBUG = True

# instantiate the app
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///login.db'
# Initialize the database
db = SQLAlchemy(app)
# Create db model
class Login(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    mail = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(16), unique=True, nullable=False) 
    def get_dict(self):
        return {
            'id': self.id,
            'mail': self.mail,
            'password': self.password,
        }
    
    # __init__ method 
    def __init__(self, mail, password):
        self.mail = mail
        self.password = password

    ##Create a function to return a string when we add 
    #def __repr__(self):
    #   return '<Mail %r>' % self.mail

app.config.from_object(__name__)

# Enables CORS (Cross-Origin Resource Sharing)
#CORS(app, resources={r'/*':{'origins':'*', "allow_headers":"Access-Control-Allow-Origin"}})
CORS(app)
# app.config['CORS_HEADERS'] = 'Content-Type'

GAMES = [12]

# a simple route
@app.route('/', methods=['POST'])
def tableLogin_get():
    logins = Login.query.order_by(Login.id.desc()).all()
    return jsonify(logins=[login.get_dict() for login in logins])

@app.route('/log', methods=['POST'])
def logAccount():
    response_object = {'status': 'success'}
    mail = request.form['mail']
    password = request.form['password']
    response_object['mail'] = mail
    response_object['password'] = password
    return response_object

@app.route('/log', methods=['GET'])
def logger():
    logins = Login.query.order_by(Login.id.desc()).all()
    return jsonify(logins=[login.get_dict() for login in logins])

@app.route('/projet1', methods=['GET', 'POST'])
def log():
    dictionnaire = {
        'type': 'Prévision de température',
        'valeurs': [24, 24, 25, 26, 27, 28],
        'unite': "degrés Celcius"
    }
    return jsonify(dictionnaire)

@app.route('/projet1/add', methods=['GET', 'POST'])
def getDatas():
    response_object = {'status': 'success'}
    response_object['log'] = 'Log successfully'
    if request.method == 'POST':
        json_data = request.get_json()
        ville = json_data.get('ville')
        url_ville = requests.get('https://geo.api.gouv.fr/communes?nom='+ville+'&fields=nom,code,codesPostaux,codeDepartement,codeRegion,population&format=json&geometry=centre')
        #meteo_code = request.get(url_ville) # => pour voir le code d'erreur
        ville_json = url_ville.json()
        #meteo_data_json = meteo_data.json()
        #content = json.loads(meteo_data.content.decode('utf-8'))
        #response_object['meteo'] = meteo_data
        #response_object['url_ville'] = url_ville
        # response_object['meteo_data'] = meteo_data_json
        response_object['ville'] = ville
        response_object['url_ville'] = url_ville
        response_object['ville_json'] = ville_json
        #response_object['code'] = meteo_data
    return jsonify(response_object)

@app.route('/dashboard/new', methods=['GET', 'POST'])
def dash():
    response_object = {'status': 'success'} # default response when an HTTP request is successfull 

    response_object['log'] = 'Log successfully'
    if request.method == "POST":
        json_data = request.get_json()
        response_object['mail'] = json_data.get('mail')
        response_object['password'] = json_data.get('pass')
        addData = Login(mail=json_data.get('mail'), password=json_data.get('pass'))
        db.session.add(addData)
        db.session.commit()
    return jsonify(response_object)

@app.route('/dashboard/get', methods=['GET'])
def get_all():
    logins = Login.query.order_by(Login.mail.asc()).all()
    return jsonify(logins=[login.get_dict() for login in logins])

@app.route('/image', methods=['GET', 'POST'])
def getImg():
    response_object = {'status': 'success'}
    response_object['log'] = 'Log successfully'
    if request.method == 'POST':
        json_data = request.get_json()
        response_object['imageName'] = json_data.get('imageName')
        response_object['imageSize'] = json_data.get('imageSize')
    return jsonify(response_object)

@app.route('/recover', methods=['GET', 'POST'])
def recover():
    response_object = {'status': 'success'}
    response_object['log'] = 'Log successfully'
    return response_object

@app.route('/image/url', methods=['GET', 'POST'])
def imgUrl():
    response_object = {'status': 'success'}
    response_object['log'] = 'Log successfully'
    if request.method == 'POST':
        json_data = request.get_json()
        image_url = json_data.get('imageURL') # URL de l'image
        url = "https://api.imagga.com/v2/categories/personal_photos"
        querystring = {"image_url":image_url}
        headers = {
            'accept': "application/json",
            'authorization': SECRET_ACCOUNT_KEY
        }
        response = requests.request("GET", url, headers=headers, params=querystring)
        response_object['response_text'] = response.text
    return response_object


if __name__ == "__main__":
    app.run(debug=True)