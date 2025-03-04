import pulsar, _pulsar
from pulsar.schema import AvroSchema
import logging
import traceback

from saludtech.modulos.auth.infraestructura.schema.v1.eventos import EventoLoginExitoso
from saludtech.modulos.auth.infraestructura.schema.v1.comandos import ComandoAutenticarUsuario
from saludtech.seedwork.infraestructura import utils

def suscribirse_a_eventos():
    cliente = None
    try:
        cliente = pulsar.Client("pulsar://broker:6650")

        consumidor = cliente.subscribe(
            'eventos-auth',
            consumer_type=_pulsar.ConsumerType.Shared,
            subscription_name='saludtech-auth-sub-eventos',
            schema=AvroSchema(EventoLoginExitoso)
        )

        while True:
            mensaje = consumidor.receive()
            print(f'Evento recibido (Login Exitoso): {mensaje.value().data}')
            consumidor.acknowledge(mensaje)

        cliente.close()
    except:
        logging.error('ERROR: Suscribiéndose al tópico de eventos de autenticación!')
        traceback.print_exc()
        if cliente:
            cliente.close()

def suscribirse_a_comandos():
    cliente = None
    try:
        cliente = pulsar.Client("pulsar://broker:6650")

        consumidor = cliente.subscribe(
            'comandos-auth',
            consumer_type=_pulsar.ConsumerType.Shared,
            subscription_name='saludtech-auth-sub-comandos',
            schema=AvroSchema(ComandoAutenticarUsuario)
        )

        while True:
            mensaje = consumidor.receive()
            print(f'Comando recibido (Autenticar Usuario): {mensaje.value().data}')
            consumidor.acknowledge(mensaje)

        cliente.close()
    except:
        logging.error('ERROR: Suscribiéndose al tópico de comandos de autenticación!')
        traceback.print_exc()
        if cliente:
            cliente.close()
