#!/usr/bin/python3
from flask import Flask, jsonify

from blueprints.usuario import usuario

app = Flask(__name__)
app.register_blueprint(usuario)

@app.route('/')
def home():
    return jsonify({'status' : 'Running'})

if __name__ == '__main__':
    app.run(debug=True)

