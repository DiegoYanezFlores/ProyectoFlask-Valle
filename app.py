# app.py
import os
from flask import Flask, jsonify, request
from dotenv import load_dotenv

from base_datos import init_db, db   # IMPORTANTE: aquí traes db
from base_datos.models import Usuario

# 1. Cargar variables de entorno
load_dotenv()

# 2. Crear app
app = Flask(__name__)

# 3. Obtener variables del .env
DB_USER = os.getenv('DB_USERNAME')
DB_PASS = os.getenv('DB_PASSWORD')
DB_HOST = os.getenv('DB_HOST')
DB_PORT = os.getenv('DB_PORT')
DB_NAME = os.getenv('DB_NAME')

# Debug (puedes quitar luego)
print("DB_USER:", DB_USER)
print("DB_HOST:", DB_HOST)
print("DB_NAME:", DB_NAME)

# 4. Construir URI
DATABASE_URI = f"postgresql://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
print("DATABASE_URI:", DATABASE_URI)

# 5. Configuración de SQLAlchemy
app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE_URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# 6. Inicializar base de datos
init_db(app)

# ------------------ RUTAS ------------------

# Ruta de prueba
@app.route('/')
def home():
    return jsonify({
        "mensaje": "Servidor activo",
        "db": DB_NAME
    })

# ------------------ RUN ------------------

if __name__ == "__main__":
    app.run(debug=True)