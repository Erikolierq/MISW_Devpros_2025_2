"""Objetos valor del dominio de usuarios

En este archivo encontrará los objetos valor del dominio de usuarios
"""

from __future__ import annotations
from dataclasses import dataclass, field
from enum import Enum
from saludtech.seedwork.dominio.objetos_valor import ObjetoValor

@dataclass(frozen=True)
class NombreUsuario(ObjetoValor):
    """Objeto valor para representar el nombre de usuario"""
    valor: str

@dataclass(frozen=True)
class Contrasena(ObjetoValor):
    """Objeto valor para representar la contraseña de un usuario"""
    valor: str

class RolUsuario(Enum):
    """Roles posibles en el sistema"""
    ADMIN = 1
    USUARIO = 2
