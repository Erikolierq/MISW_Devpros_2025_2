""" Excepciones del dominio de usuarios """

from saludtech.seedwork.dominio.excepciones import ExcepcionFabrica

class UsuarioNoExisteExcepcion(ExcepcionFabrica):
    def __init__(self, mensaje='El usuario solicitado no existe en la base de datos'):
        self.__mensaje = mensaje
    def __str__(self):
        return str(self.__mensaje)
