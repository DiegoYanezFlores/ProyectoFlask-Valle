from base_datos import db
from base_datos.models import Libro


def guardar_libro(libro):
    db.session.add(libro)
    db.session.commit()
    return libro