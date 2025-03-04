from __future__ import annotations
from dataclasses import dataclass
from saludtech.seedwork.dominio.eventos import EventoDominio
from datetime import datetime
import uuid

@dataclass
class UsuarioAutenticado(EventoDominio):
    id_usuario: uuid.UUID = None
    username: str = None
    fecha_autenticacion: datetime = None

@dataclass
class IntentoFallido(EventoDominio):
    username: str = None
    ip: str = None
    fecha_intento: datetime = None
