from __future__ import annotations
from dataclasses import dataclass, field
import uuid

from saludtech.modulos.certificator.dominio.events import PermisoValidado
from saludtech.seedwork.dominio.entidades import AgregacionRaiz

@dataclass
class Permiso(AgregacionRaiz):
    
    role: int
    user_id: uuid.UUID 

    def validar_permiso(self):
        permitido = self.role == 2
        self.agregar_evento(PermisoValidado(user_id=self.user_id, permitido=permitido))
