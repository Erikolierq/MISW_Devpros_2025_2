from __future__ import annotations
from dataclasses import dataclass
from saludtech.seedwork.dominio.eventos import EventoDominio
from datetime import datetime
import uuid

@dataclass
class PermisoValidado(EventoDominio):
    id_usuario: uuid.UUID = None
    role: int = None
    fecha_validacion: datetime = None

@dataclass
class PermisoDenegado(EventoDominio):
    id_usuario: uuid.UUID = None
    role: int = None
    fecha_validacion: datetime = None
