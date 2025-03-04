from pulsar.schema import *
from saludtech.seedwork.infraestructura.schema.v1.comandos import ComandoIntegracion

class ComandoCrearResultadoClinicoPayload(Record):
    patient = String()
    result = String()

class ComandoCrearResultadoClinico(ComandoIntegracion):
    data = ComandoCrearResultadoClinicoPayload()
