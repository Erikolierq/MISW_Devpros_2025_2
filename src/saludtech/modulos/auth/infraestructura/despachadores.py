import pulsar
from pulsar.schema import *
from saludtech.modulos.auth.infraestructura.schema.v1.eventos import EventoLoginExitoso, LoginExitosoPayload
from saludtech.modulos.auth.infraestructura.schema.v1.comandos import ComandoAutenticarUsuario, ComandoAutenticarUsuarioPayload
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
        payload = LoginExitosoPayload(
            id_usuario=str(evento.id_usuario),
            username=str(evento.username),
            role=int(evento.role),
            token=str(evento.token),
            fecha_login=unix_time_millis(evento.fecha_login)
        )
        evento_integracion = EventoLoginExitoso(data=payload)
        self._publicar_mensaje(evento_integracion, topico, AvroSchema(EventoLoginExitoso))

    def publicar_comando(self, comando, topico):
        payload = ComandoAutenticarUsuarioPayload(
            username=str(comando.username),
            password=str(comando.password)
        )
        comando_integracion = ComandoAutenticarUsuario(data=payload)
        self._publicar_mensaje(comando_integracion, topico, AvroSchema(ComandoAutenticarUsuario))
