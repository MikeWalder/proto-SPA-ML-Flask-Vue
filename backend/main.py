from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
import json
import requests

from flask_cors import CORS

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
    mail = db.Column(db.String(100), nullable=False)
    password = db.Column(db.String(16), nullable=False) 
    ##Create a function to return a string when we add 
    def __repr__(self):
        return '<Mail %r>' % self.mail

app.config.from_object(__name__)

# Enables CORS (Cross-Origin Resource Sharing)
#CORS(app, resources={r'/*':{'origins':'*', "allow_headers":"Access-Control-Allow-Origin"}})
CORS(app, resources={r"/*":{'origins':"*"}})

GAMES = [12]

# a simple route
@app.route('/', methods=['GET', 'POST'])
def testing():
    response_object = {'status': 'success'} # default response when an HTTP request is successfull 
    response = requests.get('https://db.ygoprodeck.com/api/v7/cardinfo.php?name=Survie%20du%20Plus%20Fort&language=fr')
    content = json.loads(response.content.decode('utf-8'))
    response_object['log'] = 'Log successfully'
    response_object['cardDatas'] = content
    return jsonify(response_object)

@app.route('/projet1', methods=['GET', 'POST'])
def log():
    dictionnaire = {
        'type': 'Prévision de température',
        'valeurs': [24, 24, 25, 26, 27, 28],
        'unite': "degrés Celcius"
    }
    return jsonify(dictionnaire)

@app.route('/dashboard', methods=['GET', 'POST'])
def dash():
    response_object = {'status': 'success'} # default response when an HTTP request is successfull 

    response_object['log'] = 'Log successfully'
    return jsonify(response_object)



if __name__ == "__main__":
    app.run(debug=True)