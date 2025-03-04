import pulsar, _pulsar
from pulsar.schema import AvroSchema
import logging
import traceback

from saludtech.modulos.certificator.infraestructura.schema.v1.eventos import EventoPermisoValidado
from saludtech.modulos.certificator.infraestructura.schema.v1.comandos import ComandoValidarPermiso
from saludtech.seedwork.infraestructura import utils

def suscribirse_a_eventos():
    cliente = None
    try:
        cliente = pulsar.Client("pulsar://broker:6650")

        consumidor = cliente.subscribe(
            'eventos-certificator',
            consumer_type=_pulsar.ConsumerType.Shared,
            subscription_name='saludtech-certificator-sub-eventos',
            schema=AvroSchema(EventoPermisoValidado)
        )

        while True:
            mensaje = consumidor.receive()
            print(f'Evento recibido (Permiso Validado): {mensaje.value().data}')
            consumidor.acknowledge(mensaje)

        cliente.close()
    except:
        logging.error('ERROR: Suscribiéndose al tópico de eventos de certificación!')
        traceback.print_exc()
        if cliente:
            cliente.close()

def suscribirse_a_comandos():
    cliente = None
    try:
        cliente = pulsar.Client("pulsar://broker:6650")

        consumidor = cliente.subscribe(
            'comandos-certificator',
            consumer_type=_pulsar.ConsumerType.Shared,
            subscription_name='saludtech-certificator-sub-comandos',
            schema=AvroSchema(ComandoValidarPermiso)
        )

        while True:
            mensaje = consumidor.receive()
            print(f'Comando recibido (Validar Permiso): {mensaje.value().data}')
            consumidor.acknowledge(mensaje)

        cliente.close()
    except:
        logging.error('ERROR: Suscribiéndose al tópico de comandos de certificación!')
        traceback.print_exc()
        if cliente:
            cliente.close()
