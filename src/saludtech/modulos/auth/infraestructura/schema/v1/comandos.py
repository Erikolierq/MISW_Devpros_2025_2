from pulsar.schema import *
from saludtech.seedwork.infraestructura.schema.v1.comandos import ComandoIntegracion

class ComandoAutenticarUsuarioPayload(Record):
    username = String()
    password = String()

class ComandoAutenticarUsuario(ComandoIntegracion):
    data = ComandoAutenticarUsuarioPayload()
