# libro_service.py

from repositories import libro_repository
from base_datos.models import Libro

#CREAR EL LIBRO

def crear_libro(data):
    
    # TRY/EXCEPT - Captura errores para que flask no de errores 500 gigantes
    try:
        if data.get('stock', 0) < 0:

            return {
                "exito" : False,
                "error" : "El Stock no puede ser igual o menor a cero"
            } 
        nuevo_libro = Libro(

            titulo=data['titulo'],
            autor=data['autor'],
            editorial=data['editorial'],
            anio=data['anio'],
            isbn=data['isbn'],
            stock=data['stock'],
            categoria_id=data['categoria_id'],
            usuario_id=data['usuario_id']
        )

        libro_repository.guardar_libro(nuevo_libro)

        return{
            "exito": True,

            "libro": nuevo_libro
        }
    
    #Manejo de Errores

    except Exception as e:

        return {
            "exito": False,

            "error": str(e)
        }