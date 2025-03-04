from pulsar.schema import *
from saludtech.seedwork.infraestructura.schema.v1.eventos import EventoIntegracion

class ResultadoClinicoCreadoPayload(Record):
    id_resultado = String()
    patient = String()
    result = String()
    fecha_creacion = Long()

class EventoResultadoClinicoCreado(EventoIntegracion):
    data = ResultadoClinicoCreadoPayload()
