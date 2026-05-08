#libro_routes.py 

from flask import Blueprint, jsonify, request
from services import libro_service

# =========================================================
# BLUEPRINT
# =========================================================
# Un Blueprint permite separar rutas por módulos.
#
# En vez de tener TODAS las rutas en app.py,
# organizamos el proyecto por funcionalidades.
#
# Este Blueprint manejará todas las rutas de libros.
# =========================================================

libros_bp = Blueprint('libros', __name__)

# =========================================================
# CREAR LIBRO
# =========================================================

"""
ENDPOINT: POST /libros
CREA un nuevo libro en la base de datos.

Este endpoint va a recibir un JSON con los datos del libro, 
desde el cliente (FrontEnd - Angular | Insomnia para pruebas de API )

"""

@libros_bp.route('/libros', methods=['POST'])


def crear_libro():
    """
    request.get_json()

    Captura el Json enviado por el cliente. 

    Ejemplo de Json : 
    {
        "titulo": "Clean Code",
        "autor": "Robert C. Martin"
    }
    """
    data = request.get_json()

    libro_creado = libro_service.crear_libro(data)

    if libro_creado['exito']:
        return jsonify({
            "exito": True,
            "mensaje": "Libro creado exitosamente",

            
            #Convertir esto a JSON
            "libro": libro_creado['libro'].to_dict()
        }), 201
    
    return jsonify({
        "exito": False,
        "mensaje": "Error al crear el libro"
    }), 400



    