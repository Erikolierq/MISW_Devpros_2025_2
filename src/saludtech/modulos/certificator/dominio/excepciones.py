""" Excepciones del dominio de certificación """

from saludtech.seedwork.dominio.excepciones import ExcepcionFabrica

class PermisoDenegadoExcepcion(ExcepcionFabrica):
    def __init__(self, mensaje='El usuario no tiene los permisos necesarios para realizar esta acción'):
        self.__mensaje = mensaje
    def __str__(self):
        return str(self.__mensaje)
