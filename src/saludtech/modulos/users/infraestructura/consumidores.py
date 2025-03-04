import pulsar, _pulsar
from pulsar.schema import AvroSchema
import logging
import traceback

from saludtech.modulos.users.infraestructura.schema.v1.eventos import EventoUsuarioCreado
from saludtech.modulos.users.infraestructura.schema.v1.comandos import ComandoCrearUsuario
from saludtech.seedwork.infraestructura import utils

def suscribirse_a_eventos():
    cliente = None
    try:
        cliente = pulsar.Client("pulsar://broker:6650")

        consumidor = cliente.subscribe(
            'eventos-usuarios',
            consumer_type=_pulsar.ConsumerType.Shared,
            subscription_name='saludtech-sub-eventos',
            schema=AvroSchema(EventoUsuarioCreado)
        )

        while True:
            mensaje = consumidor.receive()
            print(f'Evento recibido (Usuario Creado): {mensaje.value().data}')
            consumidor.acknowledge(mensaje)

        cliente.close()
    except:
        logging.error('ERROR: Suscribiéndose al tópico de eventos de usuarios!')
        traceback.print_exc()
        if cliente:
            cliente.close()

def suscribirse_a_comandos():
    cliente = None
    try:
        cliente = pulsar.Client("pulsar://broker:6650")

        consumidor = cliente.subscribe(
            'comandos-usuarios',
            consumer_type=_pulsar.ConsumerType.Shared,
            subscription_name='saludtech-sub-comandos',
            schema=AvroSchema(ComandoCrearUsuario)
        )

        while True:
            mensaje = consumidor.receive()
            print(f'Comando recibido (Crear Usuario): {mensaje.value().data}')
            consumidor.acknowledge(mensaje)

        cliente.close()
    except:
        logging.error('ERROR: Suscribiéndose al tópico de comandos de usuarios!')
        traceback.print_exc()
        if cliente:
            cliente.close()
