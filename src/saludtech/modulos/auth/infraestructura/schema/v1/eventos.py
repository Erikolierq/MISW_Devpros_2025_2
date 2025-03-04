from pulsar.schema import *
from saludtech.seedwork.infraestructura.schema.v1.eventos import EventoIntegracion

class LoginExitosoPayload(Record):
    id_usuario = String()
    username = String()
    role = Integer()
    token = String()
    fecha_login = Long()

class EventoLoginExitoso(EventoIntegracion):
    data = LoginExitosoPayload()
