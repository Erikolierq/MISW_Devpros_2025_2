""" Interfaces para los repositorios del dominio de resultados clínicos """

from abc import ABC
from saludtech.seedwork.dominio.repositorios import Repositorio

class RepositorioResultadosClinicos(Repositorio, ABC):
    """ Interfaz del repositorio para almacenar y recuperar resultados clínicos """
    ...
