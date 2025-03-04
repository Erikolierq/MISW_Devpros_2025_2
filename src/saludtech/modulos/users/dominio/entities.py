from __future__ import annotations
from dataclasses import dataclass, field
import uuid

from saludtech.modulos.users.dominio.events import UsuarioCreado
from saludtech.seedwork.dominio.entidades import AgregacionRaiz

@dataclass
class Usuario(AgregacionRaiz):
    username: str
    password: str
    role: int

    def crear_usuario(self, usuario: Usuario):
        self.username = usuario.username
        self.password = usuario.password
        self.role = usuario.role

        self.agregar_evento(UsuarioCreado(id_usuario=self.id, username=self.username, role=self.role))
