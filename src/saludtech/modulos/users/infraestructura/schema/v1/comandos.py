from pulsar.schema import *
from dataclasses import dataclass, field
from saludtech.seedwork.infraestructura.schema.v1.comandos import ComandoIntegracion

class ComandoCrearUsuarioPayload(Record):
    username = String()
    password = String()
    role = Integer()

class ComandoCrearUsuario(ComandoIntegracion):
    data = ComandoCrearUsuarioPayload()
