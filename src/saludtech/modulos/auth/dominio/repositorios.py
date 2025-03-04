""" Interfaces para los repositorios del dominio de autenticación """

from abc import ABC
from saludtech.seedwork.dominio.repositorios import Repositorio

class RepositorioAuth(Repositorio, ABC):
    """ Interfaz del repositorio para autenticación de usuarios """
    ...
