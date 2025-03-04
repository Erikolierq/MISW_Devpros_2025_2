import pulsar
from pulsar.schema import *
from saludtech.modulos.certificator.infraestructura.schema.v1.eventos import EventoPermisoValidado, PermisoValidadoPayload
from saludtech.modulos.certificator.infraestructura.schema.v1.comandos import ComandoValidarPermiso, ComandoValidarPermisoPayload
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
        payload = PermisoValidadoPayload(
            id_usuario=str(evento.id_usuario),
            role=int(evento.role),
            permitido=bool(evento.permitido),
            fecha_validacion=unix_time_millis(evento.fecha_validacion)
        )
        evento_integracion = EventoPermisoValidado(data=payload)
        self._publicar_mensaje(evento_integracion, topico, AvroSchema(EventoPermisoValidado))

    def publicar_comando(self, comando, topico):
        payload = ComandoValidarPermisoPayload(
            id_usuario=str(comando.id_usuario)
        )
        comando_integracion = ComandoValidarPermiso(data=payload)
        self._publicar_mensaje(comando_integracion, topico, AvroSchema(ComandoValidarPermiso))
