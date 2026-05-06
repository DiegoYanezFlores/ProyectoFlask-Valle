#__init__.py
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def init_db(app):
    db.init_app(app)

    with app.app_context():
        print("Inicializando BD...")  # DEBUG

        from .models import Usuario, Categoria, Tarea

        db.create_all()

        print("Tablas creadas con éxito") # DEBUG