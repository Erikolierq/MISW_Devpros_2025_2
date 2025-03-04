from pulsar.schema import *
from saludtech.seedwork.infraestructura.schema.v1.eventos import EventoIntegracion

class UsuarioCreadoPayload(Record):
    id_usuario = String()
    username = String()
    role = Integer()
    fecha_creacion = Long()

class EventoUsuarioCreado(EventoIntegracion):
    data = UsuarioCreadoPayload()
