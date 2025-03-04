""" Interfaces para los repositorios del dominio de usuarios """

from abc import ABC
from saludtech.seedwork.dominio.repositorios import Repositorio

class RepositorioUsuarios(Repositorio, ABC):
    """ Interfaz del repositorio para la gestión de usuarios """
    ...
