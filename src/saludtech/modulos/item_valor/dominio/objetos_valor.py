"""Objetos valor del dominio de resultados clínicos

En este archivo encontrará los objetos valor del dominio de resultados clínicos
"""

from __future__ import annotations
from dataclasses import dataclass, field
from datetime import datetime
from saludtech.seedwork.dominio.objetos_valor import ObjetoValor

@dataclass(frozen=True)
class Paciente(ObjetoValor):
    """Representa la información básica del paciente"""
    id_paciente: str
    nombre: str

@dataclass(frozen=True)
class ResultadoClinico(ObjetoValor):
    """Representa un resultado clínico"""
    id_resultado: str
    paciente: Paciente
    resultado: str
    fecha: datetime
