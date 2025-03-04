""" Excepciones del dominio de resultados clínicos """

from saludtech.seedwork.dominio.excepciones import ExcepcionFabrica

class ResultadoClinicoNoExisteExcepcion(ExcepcionFabrica):
    def __init__(self, mensaje='El resultado clínico solicitado no existe en la base de datos'):
        self.__mensaje = mensaje
    def __str__(self):
        return str(self.__mensaje)
