#!/usr/bin/python3
from flask import Flask, jsonify, render_template

from blueprints.usuario import usuario

app = Flask(__name__)
app.register_blueprint(usuario)

@app.route('/')
def home():
    return render_template('index.html', title='Home')

if __name__ == '__main__':
    app.run(debug=True)

