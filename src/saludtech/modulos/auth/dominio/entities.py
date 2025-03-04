from __future__ import annotations
from dataclasses import dataclass, field
import uuid

from saludtech.modulos.auth.dominio.events import UsuarioAutenticado, IntentoFallido
from saludtech.seedwork.dominio.entidades import AgregacionRaiz

@dataclass
class Autenticacion(AgregacionRaiz):
    username: str
    password: str

    def autenticar(self, usuario_validado: bool):
        if usuario_validado:
            self.agregar_evento(UsuarioAutenticado(username=self.username))
        else:
            self.agregar_evento(IntentoFallido(username=self.username))
