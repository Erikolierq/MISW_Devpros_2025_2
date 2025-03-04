from pulsar.schema import *
from saludtech.seedwork.infraestructura.schema.v1.eventos import EventoIntegracion

class PermisoValidadoPayload(Record):
    id_usuario = String()
    role = Integer()
    permitido = Boolean()
    fecha_validacion = Long()

class EventoPermisoValidado(EventoIntegracion):
    data = PermisoValidadoPayload()
