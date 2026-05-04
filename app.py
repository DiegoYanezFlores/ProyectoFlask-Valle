# app.py
from flask import Flask, request, jsonify
from modelos.libro import Libro
from base_datos.gestor_json import GestorDB

app = Flask(__name__)

# Instanciamos nuestra "Base de Datos" temporal
db = GestorDB()

@app.route('/api/libros', methods=['GET'])
def get_libros():
    """Angular pedirá esto para mostrar la lista de libros"""
    lista_libros = db.obtener_todos()
    return jsonify(lista_libros), 200

@app.route('/api/libros', methods=['POST'])
def add_libro():
    """Angular enviará un JSON aquí para registrar un libro"""
    datos_recibidos = request.get_json()
    
    # 1. Usamos POO para procesar los datos
    nuevo_libro = Libro.desde_angular(datos_recibidos)
    
    # 2. Guardamos usando nuestro Gestor
    db.guardar_libro(nuevo_libro.para_json())
    
    return jsonify({"message": "Libro creado con éxito"}), 201

if __name__ == "__main__":
    app.run(debug=True, port=5000)