from __future__ import annotations
from dataclasses import dataclass
from saludtech.seedwork.dominio.eventos import EventoDominio
from datetime import datetime
import uuid

@dataclass
class UsuarioCreado(EventoDominio):
    id_usuario: uuid.UUID = None
    username: str = None
    fecha_creacion: datetime = None
