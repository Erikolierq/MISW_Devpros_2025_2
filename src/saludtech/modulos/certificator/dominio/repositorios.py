""" Interfaces para los repositorios del dominio de certificación """

from abc import ABC
from saludtech.seedwork.dominio.repositorios import Repositorio

class RepositorioCertificacion(Repositorio, ABC):
    """ Interfaz del repositorio para la validación de roles y permisos """
    ...
