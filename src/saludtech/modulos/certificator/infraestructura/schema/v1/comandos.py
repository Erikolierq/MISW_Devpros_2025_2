from pulsar.schema import *
from saludtech.seedwork.infraestructura.schema.v1.comandos import ComandoIntegracion

class ComandoValidarPermisoPayload(Record):
    id_usuario = String()

class ComandoValidarPermiso(ComandoIntegracion):
    data = ComandoValidarPermisoPayload()
