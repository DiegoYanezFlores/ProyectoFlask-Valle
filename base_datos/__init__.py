from flask_sqlalchemy import SQLAlchemy

# Creamos el objeto de la hase de datos. Todavia no se sabe a que app pertenece. 
# Se identifica en el app.py con el metodo init_app()
db = SQLAlchemy()