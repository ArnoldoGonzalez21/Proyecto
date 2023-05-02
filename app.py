from flask import Flask, request, jsonify
from flask_cors import CORS
from Cliente import Cliente
import os

app = Flask(__name__)
CORS(app)

clientes = []
administrador = {
    "nombre":"Arnoldo",
    "apellido":"Gonzalez",
    "nombre_usuario":"admin",
    "password":"1234"   
} 

@app.route('/', methods=['GET'])
def principal():
    return 'Arnoldo Luis Antonio González Camey'

#---------------------------Cliente----------------------------------

@app.route('/registro_cliente', methods=['POST'])
def registro_cliente():
    contenido = request.get_json()
    nombre = contenido['nombre']
    apellido = contenido['apellido']
    nombre_usuario = contenido['nombre_usuario']
    global clientes
    if (existe_usuario(nombre_usuario, clientes)):
        return jsonify({'agregado':0,'mensaje':'El Usuario que desea Agregar Ya Existe'})
    password = contenido['password']
    telefono = contenido['telefono']
    cliente_nuevo = Cliente(nombre,apellido,nombre_usuario,password,telefono)
    clientes.append(cliente_nuevo)
    return jsonify({'agregado':1,'mensaje':'Registro Exitoso'})

def existe_usuario(nombre_usuario, clientes):
    if nombre_usuario == administrador['nombre_usuario']:
        return True
    for client in clientes:
        if client.nombre_usuario == nombre_usuario:
            return True
    return False    

def verificar_contrasena(nombre_usuario, password):
    if nombre_usuario == administrador['nombre_usuario'] and password == administrador['password']:
        return True
    global clientes
    for client in clientes:
        if client.nombre_usuario == nombre_usuario and client.password == password:
            return True
    return False


if __name__ == '__main__':
    puerto = int(os.environ.get('PORT',3000))
    app.run(host= '0.0.0.0', port = puerto)
    