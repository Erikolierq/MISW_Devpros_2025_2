"""
Módulo base para Objetos de Valor del Dominio.
"""

class ObjetoValorBase:
    """
    Clase base para objetos de valor en DDD.
    """
    def __eq__(self, other):
        return self.__dict__ == other.__dict__
