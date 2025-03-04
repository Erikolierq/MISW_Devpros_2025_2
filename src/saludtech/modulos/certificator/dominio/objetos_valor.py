"""Objetos valor del dominio de certificación

En este archivo encontrará los objetos valor del dominio de certificación
"""

from __future__ import annotations
from dataclasses import dataclass
from enum import Enum
from saludtech.seedwork.dominio.objetos_valor import ObjetoValor

@dataclass(frozen=True)
class Certificado(ObjetoValor):
    """Objeto valor que representa un certificado de autorización"""
    id_certificado: str
    usuario_id: str
    rol: int

class TipoPermiso(Enum):
    """Define los tipos de permisos disponibles"""
    RESTRINGIDO = "Restringido"
    PERMITIDO = "Permitido"
