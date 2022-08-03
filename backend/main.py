from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)

app.config.from_object(__name__)

# a simple route
@app.route('/', methods=['GET'])
def testing():
    return "Hello world this is Mike"

if __name__ == "__main__":
    app.run(debug=True)