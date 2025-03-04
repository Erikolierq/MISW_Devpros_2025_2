from __future__ import annotations
from dataclasses import dataclass
from saludtech.seedwork.dominio.eventos import EventoDominio
from datetime import datetime
import uuid

@dataclass
class ResultadoClinicoCreado(EventoDominio):
    id_resultado: uuid.UUID = None
    patient: str = None
    result_text: str = None
    fecha_creacion: datetime = None

@dataclass
class ResultadoConsultado(EventoDominio):
    id_resultado: uuid.UUID = None
    id_usuario: uuid.UUID = None
    fecha_consulta: datetime = None
