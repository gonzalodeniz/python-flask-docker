#-*- coding: utf-8 -*-
"""
Aplicación web con el framework Flask
"""
from flask import Flask
from flask.json import jsonify
from users import users

app = Flask(__name__)

# RUTAS
# Para la ruta inicial utiliza el método GET. Devuelve un json de un objeto
@app.route('/', methods=['GET'])
def ping():
    return jsonify({"response": "hello world"})

# User
@app.route('/users')
def usersHandler():
    return jsonify({"users": users})


if __name__== '__main__':
    # Para que se ejecute desde cualquier dirección, se incluye por parámetro la dirección 0.0.0.0
    # y el puerto que va a estar en escucha
    # debug=True actualiza el servidor con cada cambio ques e realice
    app.run(host="0.0.0.0", port=4000, debug=True)