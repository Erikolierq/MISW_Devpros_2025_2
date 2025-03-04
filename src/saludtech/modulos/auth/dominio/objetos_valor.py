"""Objetos valor del dominio de autenticación

En este archivo encontrará los objetos valor del dominio de autenticación
"""

from __future__ import annotations
from dataclasses import dataclass, field
from datetime import datetime
from saludtech.seedwork.dominio.objetos_valor import ObjetoValor

@dataclass(frozen=True)
class TokenJWT(ObjetoValor):
    """Representa un token JWT generado para autenticación"""
    valor: str
    expiracion: datetime

@dataclass(frozen=True)
class Credenciales(ObjetoValor):
    """Representa las credenciales de autenticación"""
    username: str
    password: str
