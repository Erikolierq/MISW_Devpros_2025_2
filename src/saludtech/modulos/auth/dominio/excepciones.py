""" Excepciones del dominio de autenticación """

from saludtech.seedwork.dominio.excepciones import ExcepcionFabrica

class CredencialesInvalidasExcepcion(ExcepcionFabrica):
    def __init__(self, mensaje='Las credenciales proporcionadas no son válidas'):
        self.__mensaje = mensaje
    def __str__(self):
        return str(self.__mensaje)
