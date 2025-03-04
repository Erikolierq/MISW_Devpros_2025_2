import pulsar
from pulsar.schema import *
from saludtech.modulos.users.infraestructura.schema.v1.eventos import EventoUsuarioCreado, UsuarioCreadoPayload
from saludtech.modulos.users.infraestructura.schema.v1.comandos import ComandoCrearUsuario, ComandoCrearUsuarioPayload
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
        payload = UsuarioCreadoPayload(
            id_usuario=str(evento.id_usuario),
            username=str(evento.username),
            role=int(evento.role),
            fecha_creacion=unix_time_millis(evento.fecha_creacion)
        )
        evento_integracion = EventoUsuarioCreado(data=payload)
        self._publicar_mensaje(evento_integracion, topico, AvroSchema(EventoUsuarioCreado))

    def publicar_comando(self, comando, topico):
        payload = ComandoCrearUsuarioPayload(
            username=str(comando.username),
            password=str(comando.password),
            role=int(comando.role)
        )
        comando_integracion = ComandoCrearUsuario(data=payload)
        self._publicar_mensaje(comando_integracion, topico, AvroSchema(ComandoCrearUsuario))
