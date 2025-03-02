import time

def suscribirse_a_eventos():
    """
    Consumidor de eventos para 'auth'.
    """
    while True:
        # Lógica de lectura de eventos desde Pulsar, Kafka, etc.
        time.sleep(5)

def suscribirse_a_comandos():
    """
    Consumidor de comandos para 'auth'.
    """
    while True:
        # Lógica para escuchar y procesar comandos de autenticación
        time.sleep(5)
