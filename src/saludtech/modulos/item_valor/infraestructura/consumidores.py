import pulsar, _pulsar
from pulsar.schema import AvroSchema
import logging
import traceback

from saludtech.modulos.item_valor.infraestructura.schema.v1.eventos import EventoResultadoClinicoCreado
from saludtech.modulos.item_valor.infraestructura.schema.v1.comandos import ComandoCrearResultadoClinico
from saludtech.seedwork.infraestructura import utils

def suscribirse_a_eventos():
    cliente = None
    try:
        cliente = pulsar.Client("pulsar://broker:6650")

        consumidor = cliente.subscribe(
            'eventos-resultados',
            consumer_type=_pulsar.ConsumerType.Shared,
            subscription_name='saludtech-resultados-sub-eventos',
            schema=AvroSchema(EventoResultadoClinicoCreado)
        )

        while True:
            mensaje = consumidor.receive()
            print(f'Evento recibido (Resultado Clínico Creado): {mensaje.value().data}')
            consumidor.acknowledge(mensaje)

        cliente.close()
    except:
        logging.error('ERROR: Suscribiéndose al tópico de eventos de resultados clínicos!')
        traceback.print_exc()
        if cliente:
            cliente.close()

def suscribirse_a_comandos():
    cliente = None
    try:
        cliente = pulsar.Client("pulsar://broker:6650")

        consumidor = cliente.subscribe(
            'comandos-resultados',
            consumer_type=_pulsar.ConsumerType.Shared,
            subscription_name='saludtech-resultados-sub-comandos',
            schema=AvroSchema(ComandoCrearResultadoClinico)
        )

        while True:
            mensaje = consumidor.receive()
            print(f'Comando recibido (Crear Resultado Clínico): {mensaje.value().data}')
            consumidor.acknowledge(mensaje)

        cliente.close()
    except:
        logging.error('ERROR: Suscribiéndose al tópico de comandos de resultados clínicos!')
        traceback.print_exc()
        if cliente:
            cliente.close()
