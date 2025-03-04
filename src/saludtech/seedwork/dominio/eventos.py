"""Entidades reusables parte del seedwork del proyecto

En este archivo usted encontrará las clases para eventos reusables parte del seedwork del proyecto

"""

from dataclasses import dataclass, field
from .reglas import IdEntidadEsInmutable
from .excepciones import IdDebeSerInmutableExcepcion
from datetime import datetime
import uuid
from abc import ABC
from dataclasses import dataclass

@dataclass
class EventoDominio(ABC):
    id: uuid.UUID = field(hash=True)
    _id: uuid.UUID = field(init=False, repr=False, hash=True)
    fecha_evento: datetime =  field(default=datetime.now())
    
    def __post_init__(self):
        if not self.fecha_evento:
            self.fecha_evento = datetime.utcnow()
    @classmethod
    def siguiente_id(self) -> uuid.UUID:
        return uuid.uuid4()

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, id: uuid.UUID) -> None:
        if not IdEntidadEsInmutable(self).es_valido():
            raise IdDebeSerInmutableExcepcion()
        self._id = self.siguiente_id()