from flask import Flask, request, jsonify
from flask_cors import CORS
from Cliente import Cliente
from Producto import Producto
import os

app = Flask(__name__)
CORS(app)

clientes = []
productos = []

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
    if (existe_usuario(nombre_usuario)):
        return jsonify({'agregado':0,'mensaje':'El Usuario que desea Agregar Ya Existe'})
    password = contenido['password']
    telefono = contenido['telefono']
    cliente_nuevo = Cliente(nombre,apellido,nombre_usuario,password,telefono)
    clientes.append(cliente_nuevo)
    return jsonify({'agregado':1,'mensaje':'Registro Exitoso'})

@app.route('/obtener_cliente', methods=['GET'])
def obtener_cliente():
    json_clientes = []
    json_clientes.append(administrador)
    global clientes
    for cliente in clientes:
        json_clientes.append(cliente.get_json())
    return jsonify(json_clientes)

def existe_usuario(nombre_usuario):    
    global clientes
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

@app.route('/registro_producto', methods=['POST'])
def registro_producto():
    contenido = request.get_json()
    nombre = contenido['nombre']
    precio = contenido['precio']
    descripcion = contenido['descripcion']
    cantidad = contenido['cantidad']
    imagen = contenido['imagen']
    producto_nuevo = Producto(nombre, precio, descripcion, cantidad, 0, -1, 0, imagen)
    global productos
    productos.append(producto_nuevo)
    return jsonify({'agregado':3,'mensaje':'Registro Exitoso'})

@app.route('/obtener_producto', methods=['GET'])
def obtener_producto():
    json_producto = []
    global productos
    for prod in productos:
        json_producto.append(prod.get_json())
    return jsonify(json_producto)

@app.route('/agregar_venta_producto', methods=['POST'])
def agregar_venta_producto():
    cuerpo = request.get_json()
    posicion = cuerpo['posicion']
    venta = cuerpo['venta']
    cliente = cuerpo['cliente']
    compra = cuerpo['compra']
    i = int(posicion)
    global productos
    agregar_venta = int(productos[i].venta) + int(venta)
    productos[i].agregar_venta(agregar_venta, cliente, compra)
    return jsonify(productos[i].get_json())

@app.route('/login', methods=['GET'])
def login():
    nombre_usuario = request.args.get("nombre_usuario")
    password = request.args.get("password")
    if nombre_usuario == administrador['nombre_usuario'] and password == administrador['password']:
        return jsonify({'estado':2,'mensaje':'Login Exitoso Administrador'})
    if (not existe_usuario(nombre_usuario)):
        return jsonify({'estado':0,'mensaje':'El Usuario No Existe'})
    if verificar_contrasena(nombre_usuario, password):
        return jsonify({'estado':1,'mensaje':'Login Existoso Cliente'})
    return jsonify({'estado':0,'mensaje':'La Contraseña o Usuario es Incorrecta'})

if __name__ == '__main__':
    puerto = int(os.environ.get('PORT', 3000))
    app.run(host= '0.0.0.0', port = puerto)
    