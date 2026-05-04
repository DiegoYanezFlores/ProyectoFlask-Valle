# modelos/libro.py

class Libro:
    def __init__(self, titulo, autor, isbn):
        """
        Cosntructor de la clase Libro: Aqui definimos que tipo de datos vamos 
        a almacenar y a que objeto pertenecen.
        'self' es la referencia al objeto que estamos creando en memoria.
        """  
        self.titulo = titulo
        self.autor = autor
        self.isbn = isbn

    # 1. Informacion desde Angular
    @classmethod
    def desde_json_angular(cls, datos_json_angular):
        """ Toma el Json de Angular y creo un objeto Libro"""

        return cls(
            titulo=datos_json_angular.get('titulo'),
            autor=datos_json_angular.get('autor'),
            isbn=datos_json_angular.get('isbn')
        )
    
    #2 . De Python a Angular 
    def a_diccionario(self):
        """ Converte el objeto a un diccionario para que flask pueda enviarlo"""
        return {
            'titulo': self.titulo,
            'autor': self.autor,
            'isbn': self.isbn
        }



 