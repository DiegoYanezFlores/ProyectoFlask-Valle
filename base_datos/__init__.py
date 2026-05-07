#__init__.py
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def init_db(app):
    db.init_app(app)

    with app.app_context():
        print("Inicializando BD...")  # DEBUG

        from .models import Usuario, Cliente, Libro, Categoria, Prestamo
        # Elimina toda la base de datos 
        # db.drop_all()
        # Crea todas las tablas nuevas
        db.create_all()

        print("Tablas creadas con éxito") # DEBUG