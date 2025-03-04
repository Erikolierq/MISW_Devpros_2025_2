import pulsar
from pulsar.schema import *
from saludtech.modulos.item_valor.infraestructura.schema.v1.eventos import EventoResultadoClinicoCreado, ResultadoClinicoCreadoPayload
from saludtech.modulos.item_valor.infraestructura.schema.v1.comandos import ComandoCrearResultadoClinico, ComandoCrearResultadoClinicoPayload
from saludtech.seedwork.infraestructura import utils
import datetime

epoch = datetime.datetime.utcfromtimestamp(0)

def unix_time_millis(dt):
    return int((dt - epoch).total_seconds() * 1000.0)

class Despachador:
    def _publicar_mensaje(self, mensaje, topico, schema):
        cliente = pulsar.Client(f'pulsar://{utils.broker_host()}:6650')
        publicador = cliente.create_producer(topico, schema=schema)
        publicador.send(mensaje)
        cliente.close()

    def publicar_evento(self, evento, topico):
        payload = ResultadoClinicoCreadoPayload(
            id_resultado=str(evento.id_resultado),
            patient=str(evento.patient),
            result=str(evento.result),
            fecha_creacion=unix_time_millis(evento.fecha_creacion)
        )
        evento_integracion = EventoResultadoClinicoCreado(data=payload)
        self._publicar_mensaje(evento_integracion, topico, AvroSchema(EventoResultadoClinicoCreado))

    def publicar_comando(self, comando, topico):
        payload = ComandoCrearResultadoClinicoPayload(
            patient=str(comando.patient),
            result=str(comando.result)
        )
        comando_integracion = ComandoCrearResultadoClinico(data=payload)
        self._publicar_mensaje(comando_integracion, topico, AvroSchema(ComandoCrearResultadoClinico))
